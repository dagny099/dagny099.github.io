---
layout: single
title: "Poolula Platform: RAG-Powered Business Intelligence"
permalink: /projects/poolula-platform/
classes: [project]
author_profile: false
read_time: false
toc: true
toc_sticky: true
toc_label: "Contents"
toc_icon: "database"
order: 3
tags: [RAG, NLP, FastAPI, SQLModel, ChromaDB, Claude, Evaluation, Data Lineage, Python]
categories: ["AI Systems & MLOps (Pragmatic)"]
stack: [Python 3.13, FastAPI, SQLModel, SQLite, ChromaDB (ONNX), Anthropic Claude, Alembic, pytest, MkDocs]
status: WIP
header:
  teaser: assets/images/portfolio/poolula-platform-teaser.png
  overlay_image: assets/images/portfolio/poolula-platform-architecture.png
  overlay_filter: 0.3
  caption: "Natural language queries with verifiable, source-cited answers"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/poolula-platform
      class: "btn--primary"
excerpt: "Business questions live in spreadsheets, PDFs, and memory—but answers require digging. This platform turns natural language queries into verifiable responses by combining structured data (transactions, properties) with unstructured documents (contracts, policies). The differentiator: an evaluation harness that measures AI accuracy before you trust it."
url: /projects/poolula-platform/
btn_label: "Project"
---

Most RAG systems ship without knowing how often they're wrong. This one measures accuracy against a golden question set before deployment—**because "it sounds right" isn't a reliability standard.** The platform combines SQL queries over structured financial data with semantic search over business documents, then validates responses through a multi-dimensional evaluation harness targeting ≥90% accuracy.

{% include page__taxonomy.html %}

---

## Why This Matters

**The gap between "data exists" and "answers are accessible."** Small businesses accumulate transaction records, contracts, tax documents, and compliance obligations across disconnected systems. When a question arises—"What was my rental income last quarter?" or "When does the insurance policy renew?"—the answer requires manual lookup across multiple sources.

**RAG can help, but RAG can also hallucinate.** The standard approach (embed documents → retrieve chunks → generate answer) produces fluent responses that may or may not be accurate. For financial and compliance questions, "mostly right" isn't acceptable.

**Verification-first design.** This platform inverts the typical RAG workflow: instead of shipping and hoping, it runs every query type through an evaluation harness with known correct answers. The AI doesn't go live until it passes.

---

## How It Works

```
User Query: "What was my rental income in August 2025?"
    ↓
AI determines tools needed → query_database
    ↓
Execute: query_database(query_type="aggregate_transactions",
                        filters={category: "RENTAL_INCOME",
                                start_date: "2025-08-01",
                                end_date: "2025-08-31"})
    ↓
Returns: {"success": true, "count": 12, "total_amount": "16144.12"}
    ↓
AI synthesizes: "Your rental income in August 2025 was $16,144.12
                from 12 transactions."
    ↓
Audit log records: query, response, sources, timestamp
```

### Two-Tool Architecture

The chatbot has access to two specialized tools:

| Tool | Purpose | Safety |
|------|---------|--------|
| **Database Query** | SQL over structured transaction/property data | SELECT-only, parameterized queries |
| **Document Search** | Semantic search over embedded documents | ChromaDB vector similarity |

The AI decides which tool(s) to invoke based on the question. Financial questions hit the database; policy questions search documents; mixed questions use both.

<details>
<summary><strong>Example: Document search query</strong></summary>

```
User Query: "What are the LLC's registered agent requirements?"
    ↓
AI determines tools needed → search_documents
    ↓
Execute: search_documents(query="registered agent requirements",
                          doc_types=["formation", "operating_agreement"])
    ↓
Returns: [
  {
    "content": "The LLC shall maintain a registered agent...",
    "source": "Operating Agreement Section 2.3",
    "similarity": 0.89
  }
]
    ↓
AI synthesizes answer with source citation
```

</details>

---

## Architecture

### Five Core Tables

The data model tracks properties, financial transactions, documents, compliance obligations, and data lineage:

| Table | Purpose | Key Fields |
|-------|---------|------------|
| **Property** | Rental properties with basis calculations | address, purchase_price, land_basis, building_basis, depreciation |
| **Transaction** | Financial events (30+ categories) | amount, category, transaction_type, source_account |
| **Document** | Business documents with embeddings | doc_type, effective_date, storage_path, vector_id |
| **Obligation** | Compliance deadlines with recurrence | due_date, status, recurrence (RRULE), is_overdue |
| **Provenance** | Data lineage for every record | source_type, source_id, confidence, verification_status |

<details>
<summary><strong>Transaction categories (30+ types)</strong></summary>

```python
class TransactionCategory(str, Enum):
    # Revenue
    RENTAL_INCOME = "RENTAL_INCOME"
    CLEANING_FEE = "CLEANING_FEE"

    # Operating expenses
    UTILITIES_GAS = "UTILITIES_GAS"
    UTILITIES_ELECTRIC = "UTILITIES_ELECTRIC"
    REPAIRS_MAINTENANCE = "REPAIRS_MAINTENANCE"
    PROPERTY_MANAGEMENT = "PROPERTY_MANAGEMENT"
    INSURANCE = "INSURANCE"

    # Capital
    CAPITAL_IMPROVEMENT = "CAPITAL_IMPROVEMENT"
    FURNITURE_EQUIPMENT = "FURNITURE_EQUIPMENT"

    # ... 20+ more categories
```

</details>

### Design Decisions

- **Provenance tracking** on every record—know where data came from (CSV import, manual entry, bank statement) and its confidence level
- **Soft deletes** (set `deleted_at`, never hard DELETE)—preserves audit trail
- **UUID primary keys**—portable across systems
- **SQLite for development**, PostgreSQL-ready via SQLModel/Alembic

---

## Governance & Reliability

### Evaluation Harness

The platform includes a rigorous testing system with a golden question set:

```bash
uv run python apps/evaluator/evaluation_harness.py
# Outputs: docs/evaluation/evaluation_report_YYYYMMDD_HHMMSS.json
```

**Five scoring dimensions:**

| Dimension | What It Measures |
|-----------|------------------|
| **Tool Usage** | Did the AI invoke the correct tools? |
| **Content Relevance** | Does the answer address the actual question? |
| **Semantic Similarity** | Does the answer match expected content (embedding comparison)? |
| **Numerical Accuracy** | Do financial figures match expected values? |
| **Citation Accuracy** | Are sources correct and relevant? |

**Target:** ≥90% composite score before production deployment.

### Audit Logging

Every chatbot interaction is logged:
- Query text and timestamp
- AI response and reasoning
- Tools invoked and their outputs
- Sources cited

This creates an immutable record for debugging, compliance review, and evaluation refinement.

### Provenance Tracking

Every piece of data carries its lineage:

```json
{
  "source_type": "csv_import",
  "source_id": "airbnb_export_2025-08.csv",
  "confidence": 0.95,
  "verification_status": "unverified",
  "imported_at": "2025-08-15T10:30:00Z"
}
```

When the AI cites a transaction, you can trace it back to the original source file.

---

## What's Shipped vs. In Progress

### ✅ Shipped

- **Database schema** with 5 tables and full provenance tracking
- **FastAPI REST API** with CRUD endpoints for all entities
- **RAG system** combining database queries + document search
- **Chatbot CLI** with source citations and multi-turn conversations
- **Airbnb CSV import** with accrual accounting logic
- **Evaluation harness** with 15 golden questions
- **Test suite** with 31/37 tests passing, ≥80% coverage
- **Audit logging** for all chatbot interactions

### 🔧 In Progress

- **Document re-ingestion** — ChromaDB document search bug being fixed
- **Vanilla JS frontend** — 4 persona-based help sections (New LLC Owner, Bookkeeper, Property Manager, Compliance Officer)
- **Expanded evaluation set** — 15 → 40 golden questions
- **Numerical accuracy scoring** — Improved tolerance for financial comparisons

---

## What's Next

1. **Expand golden question set** from 15 to 40 questions covering edge cases
2. **Improve numerical accuracy scoring** with configurable tolerance thresholds
3. **Build evaluation dashboard** for tracking accuracy trends over time
4. **Document search improvements** — better chunking strategy for multi-page contracts
5. **Automated transaction import** from additional sources (bank statements, expense receipts)

---

## Implementation Notes

**Tech choices and rationale:**

| Choice | Why |
|--------|-----|
| **SQLite** | Perfect for single-user; Alembic migrations allow PostgreSQL upgrade path |
| **ChromaDB with ONNX** | Avoids PyTorch dependency headaches on macOS; still fast enough for small corpus |
| **No repository pattern** | Direct SQLModel usage is simpler and more transparent at this scale |
| **Claude Sonnet 4.5** | Best tool-use performance in testing; cost-effective for low query volume |

**Key patterns:**
- Lazy loading of ML models via `@st.cache_resource`
- Graceful degradation when optional dependencies unavailable
- Multi-environment API key management (env vars for prod, secrets for dev)

---

## Links

[View Repository](https://github.com/dagny099/poolula-platform){: .btn .btn--primary}

**Documentation:**
- Architecture: `docs/architecture/business-objects.md`
- Workflows: `docs/workflows/data-import.md`, `docs/workflows/api-usage.md`
- API Reference: `http://localhost:8082/docs` (Swagger UI when running)

**Related reading:**
- [Evaluation-Driven Development for RAG Systems](https://www.anthropic.com/research) — the methodology behind the evaluation harness
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/) — the ORM powering the data layer

---

*Note: This platform was built for a specific business use case (rental property LLC management). The patterns—RAG with evaluation, provenance tracking, audit logging—are transferable to other domains where AI-generated answers need verification.*
