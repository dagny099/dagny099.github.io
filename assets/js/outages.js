---
layout: null
sitemap: false
# Generated from _data/outages.yml. Loaded synchronously in <head> so page
# scripts (e.g. /projects/) can call isDownLink() while rendering.
---
(function () {
  var DOWN = {{ site.data.outages.down | default: empty | jsonify }};

  function norm(url) {
    return String(url || "").replace(/^https?:\/\//i, "").replace(/^www\./i, "");
  }

  window.isDownLink = function (url) {
    var u = norm(url);
    for (var i = 0; i < DOWN.length; i++) {
      if (u.indexOf(DOWN[i]) === 0) return true;
    }
    return false;
  };

  if (!DOWN.length) return;

  // Catch-all for links outside the data-driven buttons (case-study prose,
  // hero actions, footer nav): hide button-styled links, mark the rest offline.
  function sweep() {
    var links = document.querySelectorAll("a[href]");
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (!window.isDownLink(a.getAttribute("href"))) continue;
      if (/(^|\s)(btn|btn--cta)(\s|$|-)/.test(a.className)) {
        a.hidden = true;
        a.style.display = "none";
        continue;
      }
      a.setAttribute("data-offline-href", a.getAttribute("href"));
      a.removeAttribute("href");
      a.removeAttribute("target");
      a.classList.add("link--offline");
      a.setAttribute("aria-disabled", "true");
      a.title = "Temporarily offline — back soon";
    }
  }

  var style = document.createElement("style");
  style.textContent =
    ".link--offline{color:inherit;opacity:.6;text-decoration:none;cursor:default}" +
    ".link--offline::after{content:\" (temporarily offline)\";font-size:.85em;font-style:italic}";
  document.head.appendChild(style);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", sweep);
  } else {
    sweep();
  }
})();
