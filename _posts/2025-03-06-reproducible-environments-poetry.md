---
layout: post
title: "The Data Scientist's Toolkit: Poetry + direnv for Project Isolation"
subtitle: "A clean, reproducible Python environment for every project, switched on automatically when you cd in"
date: 2025-03-06
last_modified_at: 2026-10-19
permalink: /blog/poetry-of-python/
header:
  overlay_image: /assets/images/coding-workspace-top-view.png
  overlay_filter: 0.5
  teaser: /assets/diagrams/poetry-direnv-layers-v1.svg
excerpt: "Poetry keeps each project's dependencies isolated and pinned. direnv turns the right environment on when you cd into a project and off when you leave. Tested end to end on Poetry 2.4, with Jupyter kernels and .env secrets included."
excerpt_display: true
tags: [poetry, direnv, python, reproducibility, jupyter, tutorial]
stack: [Poetry, direnv, Python, Jupyter]
classes: wide
categories: [tutorial]
pagination:
  enabled: true
---

*Updated October 2026 for Poetry 2.x. The first version of this post had a few recipes that no longer work, and one that never did. Every command below was re-run end to end on Poetry 2.4 and direnv 2.32.*

My favorite part of this setup is the part I never think about. When I `cd` into a project folder, its environment is simply on: the right Python, the right packages, the project's own environment variables. When I leave, it's off again. No `source .venv/bin/activate`, and no pausing to wonder which Python I'm about to run.

Here's what that looks like with two projects that need different versions of pandas:

{% include figure image_path="/assets/videos/poetry-direnv-terminal.svg" alt="Terminal recording. Outside any project, which python3 shows /usr/bin/python3. After cd new-data-project, direnv loads the project's .envrc and pandas reports version 3.0.6. After cd ../another-project, direnv loads that project's environment and pandas reports 2.2.3. After cd .., direnv unloads and python3 is the global one again." caption="A real session: two projects, two pandas versions, and no activate command anywhere. (Paths shortened to `~/projects`.)" %}

Two tools make that happen:

- **Poetry** gives each project its own isolated environment and records exactly what's installed in it, so you (or a collaborator, or you a year from now) can rebuild it.
- **direnv** notices which folder you're in and turns that folder's environment on and off for you.

## Your toolkit, in layers

{% include figure image_path="/assets/diagrams/poetry-direnv-layers-v1.svg" alt="Diagram of two layers. Your machine, installed once: Homebrew, Poetry, direnv, Git, JupyterLab, and the direnv hook in ~/.zshrc. Below it, two project folders, each with its own .venv, pyproject.toml, poetry.lock, .envrc and .env, a different pandas version, and a Jupyter kernel pointing at its own .venv. Along the bottom, your shell moves from ~/projects (global python3) into new-data-project and then another-project, picking up each one's environment." %}

It helps to picture two layers. Tools you use across every project (Homebrew, Poetry, direnv, Git, JupyterLab) are installed once, on your machine. Everything a single project needs (its packages, its lockfile, its secrets) lives inside that project's folder. direnv is the bridge between the two.

## One-time setup: install the tools and hook up your shell

```bash
brew install poetry direnv
```

(If you'd rather not use Homebrew for Poetry, its docs recommend `pipx install poetry`.)

Next, let direnv check for instructions every time you change directories. For zsh, the macOS default, add this line to the end of `~/.zshrc`:

```bash
eval "$(direnv hook zsh)"
```

For bash, put `eval "$(direnv hook bash)"` in `~/.bashrc` instead. Then open a new terminal window. My first version of this post skipped this step, and without it direnv never runs.

## Step 1: Create the project, with its environment inside it

```bash
mkdir new-data-project && cd new-data-project
poetry init
poetry config virtualenvs.in-project true --local
```

`poetry init` walks you through creating `pyproject.toml`, the file that lists what your project depends on. You can skip adding dependencies when it asks; we'll add them in Step 3.

The third command tells Poetry to put this project's virtual environment in a `.venv/` folder inside the project, instead of a cache directory somewhere else on your machine. I like that for three reasons: I can see it, I can delete and rebuild it without hunting for it, and editors like VS Code find it on their own. The `--local` flag saves the setting in a small `poetry.toml` file in the project, so it travels with the repo.

## Step 2: Tell Poetry this is a project, not a package

Poetry was built for publishing Python packages, so by default it assumes your project is one. Run `poetry install` on a plain data project and you'll get this:

```text
Error: The current project could not be installed: No file/folder found for package new-data-project
If you do not want to install the current project use --no-root.
If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
```

Most data projects are that second case. Add this to the bottom of `pyproject.toml`:

```toml
[tool.poetry]
package-mode = false
```

## Step 3: Add your dependencies

```bash
poetry add pandas requests matplotlib
```

This installs the packages into `.venv/` and records them in two files: `pyproject.toml` (what you asked for) and `poetry.lock` (the exact versions you got). Commit both. The lockfile is what makes the environment reproducible on another machine, or on this one next year.

Starting from an existing `requirements.txt`? You can add everything in one go:

```bash
grep -Ev '^\s*(#|$)' requirements.txt | xargs poetry add
```

The `grep` skips comments and blank lines, and handing everything to a single `poetry add` lets Poetry work out compatible versions for the whole set at once. (My earlier version looped over the file and called `poetry add` once per package, which repeats that work for every line.)

One rule worth keeping: once a project uses Poetry, don't `pip install` into it. Pip will happily put the package in `.venv/`, but `pyproject.toml` and `poetry.lock` never hear about it, so the next rebuild quietly leaves it out.

## Step 4: Teach direnv what to do when you walk in

Create a file named `.envrc` in the project folder with two lines:

```bash
source .venv/bin/activate
dotenv_if_exists
```

The first line activates the project's environment. The second loads variables from a `.env` file, if the project has one (that's Step 5). Then approve it:

```bash
direnv allow
```

direnv won't run an `.envrc` it hasn't seen before, or one that changed since you last approved it. That's a safety feature: cloning someone's repo shouldn't silently run their code. Whenever you edit `.envrc`, run `direnv allow` again.

> **About other `.envrc` recipes for Poetry.** Two show up a lot, including in the first version of this post.
> - `use poetry` doesn't work. direnv has built-in layouts for pipenv, pyenv, and plain virtualenvs, but none for Poetry, so that line fails with `use_poetry: command not found`.
> - `source "$(poetry env info -p)/bin/activate"` works, but it starts Poetry every time you enter the folder just to ask where the environment lives. On my M1 Mac that added about 0.3 seconds to every `cd`, versus 0.01 seconds for sourcing `.venv/bin/activate` directly. Small, but you pay it every time you enter the folder. Since Step 1 put the environment at `.venv/`, there's no need to ask.

## Step 5: Keep secrets in `.env`, out of Git

Tell Git to ignore the file first, then create it:

```bash
echo ".env" >> .gitignore
touch .env
```

Open `.env` in your editor and add one variable per line, like `OPENAI_API_KEY=...`. Run `direnv reload` (or `cd` out and back in) and those variables are set in your shell, ready for `os.environ["OPENAI_API_KEY"]` in Python. The `.envrc` is safe to commit because it holds no secrets. The `.env` never is.

## Step 6: Take it for a walk

```bash
cd ..
cd new-data-project
```

On the way out you'll see `direnv: unloading`. On the way back in you'll see `direnv: loading .../.envrc`, followed by the variables it set. `which python` should now point inside the project's `.venv/`.

That's the whole setup. Everything after this is just using it.

## Using Jupyter with the project's environment

Jupyter can run code with any Python it knows about, which makes notebooks an easy place for environments to get crossed. The fix is to register the project's environment as its own named kernel:

```bash
poetry add --group dev ipykernel
python -m ipykernel install --user --name new-data-project --display-name "Python (new-data-project)"
```

The first line adds `ipykernel` as a development-only dependency. The second registers the kernel. Because direnv has already activated the environment, `python` here is the project's Python; no `poetry run` needed.

The registration writes a small `kernel.json` that points straight at the project's interpreter:

```json
"argv": [
  "/Users/you/projects/new-data-project/.venv/bin/python",
  "-m", "ipykernel_launcher", ...
]
```

That's why it works from any Jupyter you launch: a global JupyterLab, VS Code's notebook editor, whatever you prefer. Open a notebook, pick **Python (new-data-project)** from the kernel list, and it runs with exactly this project's packages. To remove the kernel later, run `jupyter kernelspec uninstall new-data-project`.

## Starting from someone else's Poetry project

```bash
git clone <repo-url>
cd <repo>
poetry config virtualenvs.in-project true --local   # skip if the repo already has a poetry.toml
poetry install
```

`poetry install` reads `poetry.lock` and rebuilds the same environment the author had. If the repo includes an `.envrc`, direnv will tell you it's blocked when you `cd` in. Read it, and once `poetry install` has created `.venv/`, run `direnv allow`. If there's no `.envrc`, add the two-line one from Step 4.

## A few gotchas

- **`poetry shell` is gone.** Poetry 2.0 moved it into a separate plugin, so older tutorials that use it now fail with "Looks like you're trying to use a Poetry command that is not available." `poetry env activate` prints the activation command instead. With direnv, you need neither.
- **Copying or moving a project quietly breaks its `.venv/`.** A virtual environment remembers the absolute path where it was created. In a test, a copied project kept running Python and pip from the *original* folder's environment, with no error at all. After a move, run `rm -rf .venv && poetry install` in the new location.
- **Keep tools global and packages local.** Tools like Docker, the GitHub CLI, and Poetry itself belong on your machine, managed by Homebrew. Project dependencies like pandas, scikit-learn, openai, and streamlit belong in the project's Poetry environment. Mixing the two is how a clean environment slowly stops being clean.

## Why I bother

The payoff shows up later. When I come back to a project after months away, `cd` puts me back in the environment I left, with the same packages at the same versions. Picking a project back up costs nothing, which makes me much more likely to actually do it.

Next in the Data Scientist's Toolkit: [launching an RDS database with the AWS CLI](/blog/aws-cli-tutorial-launch-rds-for-ec2-access/).

## Resources

- [Poetry documentation](https://python-poetry.org/docs/), especially [managing environments](https://python-poetry.org/docs/managing-environments/)
- [direnv](https://direnv.net/) and its [standard library](https://direnv.net/man/direnv-stdlib.1.html) of `.envrc` commands
