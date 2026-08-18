/* =========================================================
   AI 方法论技能库 — 前端逻辑
   数据源：data/skills.json（由 scripts/seed.py 从数据库导出）
   路由：hash 路由
     #/           技能列表（支持搜索 + 分类筛选）
     #/skill/<id> 技能详情
     #/terms      名词表
   ========================================================= */

(function () {
  "use strict";

  const APP = document.getElementById("app");
  let DATA = null; // { categories, skills, terms }
  let state = { query: "", category: "all" };

  /* ---------- 初始化 ---------- */
  function init() {
    fetch("data/skills.json")
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        DATA = data;
        document.getElementById("statSkills").textContent = data.skills.length;
        document.getElementById("statTerms").textContent = data.terms.length;
        window.addEventListener("hashchange", render);
        render();
      })
      .catch(function (e) {
        APP.innerHTML =
          '<div class="empty">数据加载失败：' + escapeHtml(String(e)) +
          "<br><br>请确认是通过 http 服务访问（如 http://127.0.0.1:8765），" +
          "而不是双击打开 file:// 页面。</div>";
      });
  }

  /* ---------- 工具 ---------- */
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function nl2br(s) {
    return String(s || "").replace(/\n/g, "<br>");
  }
  function skillById(id) {
    return DATA.skills.find(function (s) { return s.id === id; });
  }
  function catById(id) {
    return DATA.categories.find(function (c) { return c.id === id; });
  }
  function catCount(id) {
    return DATA.skills.filter(function (s) { return s.category === id; }).length;
  }

  /* ---------- 视图：列表 ---------- */
  function viewList() {
    const q = state.query.trim().toLowerCase();
    const cat = state.category;
    const matched = DATA.skills.filter(function (s) {
      if (cat !== "all" && s.category !== cat) return false;
      if (!q) return true;
      return (
        (s.id + " " + s.name_cn + " " + s.short_desc + " " + s.plain).toLowerCase().indexOf(q) !== -1
      );
    });

    const chips =
      '<div class="chips">' +
      chip("all", "全部", DATA.skills.length) +
      DATA.categories.map(function (c) { return chip(c.id, c.icon + " " + c.name, catCount(c.id)); }).join("") +
      "</div>";

    const cards = matched.map(function (s) {
      const cat = catById(s.category);
      return (
        '<a class="skill-card" href="#/skill/' + encodeURIComponent(s.id) + '">' +
        '<div class="card-head">' +
        '<span class="card-name">' + escapeHtml(s.name_cn || s.id) + "</span>" +
        '<span class="card-cn">' + escapeHtml(s.id) + "</span>" +
        '<span class="card-cat">' + (cat ? cat.icon + " " + cat.name : "") + "</span>" +
        "</div>" +
        '<div class="card-desc">' + escapeHtml(s.short_desc || s.plain.slice(0, 80)) + "</div>" +
        '<div class="card-foot"><span>' + escapeHtml(s.source) + "</span></div>" +
        "</a>"
      );
    }).join("");

    return (
      '<div class="searchbar">' +
      '<input class="search-input" id="searchInput" type="search" placeholder="搜索技能：如 数据、可行性、训练…" value="' +
      escapeHtml(state.query) + '">' +
      "</div>" +
      chips +
      (cards || '<div class="empty">没有找到匹配的技能 😢</div>')
    );
  }

  function chip(id, label, count) {
    return (
      '<button class="chip' + (state.category === id ? " active" : "") + '" data-cat="' + id + '">' +
      escapeHtml(label) + '<span class="count">' + count + "</span></button>"
    );
  }

  /* ---------- 视图：详情 ---------- */
  function viewDetail(id) {
    const s = skillById(id);
    if (!s) return '<div class="empty">未找到该技能</div>';
    const cat = catById(s.category);

    const list = function (arr, cls) {
      if (!arr || !arr.length) return "";
      return (
        "<ul>" +
        arr.map(function (x) { return '<li class="' + cls + '">' + nl2br(escapeHtml(x)) + "</li>"; }).join("") +
        "</ul>"
      );
    };
    const related = (s.related || []).map(function (r) {
      return (
        '<a class="related-chip" href="#/skill/' + encodeURIComponent(r.id) + '">' +
        escapeHtml(r.id) + " <small>" + escapeHtml(r.relation) + "</small></a>"
      );
    }).join("");
    const relatedTerms = DATA.terms.filter(function (t) {
      return t.skills.indexOf(s.id) !== -1;
    }).map(function (t) {
      return '<a class="related-chip" href="#/terms">' + escapeHtml(t.term) + "</a>";
    }).join("");

    return (
      '<a class="back-link" href="#/">← 返回列表</a>' +
      '<div class="detail-head">' +
      '<div class="detail-title">' + escapeHtml(s.name_cn || s.id) +
      '<span class="detail-cn">' + escapeHtml(s.id) + "</span></div>" +
      '<div class="detail-meta">' +
      '<span class="badge">' + (cat ? cat.icon + " " + cat.name : "") + "</span>" +
      '<span class="badge source">📚 ' + escapeHtml(s.source) + "</span>" +
      "</div></div>" +

      section("💬 大白话 · 一句话懂它", '<div class="plain-box">' + nl2br(escapeHtml(s.plain)) + "</div>") +
      section("🎯 什么时候用得上", list(s.use_cases, "case-item")) +
      section("🏠 生活化例子", '<div class="example-box">' + nl2br(escapeHtml(s.example)) + "</div>") +
      section("📜 原文金句", '<div class="quote-box">' + escapeHtml(s.quote) + "</div>") +
      section("🧱 方法论骨架", nl2br(escapeHtml(s.core))) +
      section("📖 书里的案例", list(s.cases, "case-item")) +
      section("🛠️ 怎么做（步骤）", list(s.steps, "step-item")) +
      section("⚠️ 边界 · 什么时候别用它", list(s.boundary, "boundary-item")) +
      (related ? section("🔗 相关技能", '<div class="related-chips">' + related + "</div>") : "") +
      (relatedTerms ? section("📇 涉及名词", '<div class="related-chips">' + relatedTerms + "</div>") : "")
    );
  }

  function section(title, inner) {
    return '<section class="section"><h3>' + title + "</h3>" + inner + "</section>";
  }

  /* ---------- 视图：术语表 ---------- */
  function viewTerms() {
    const groups = {};
    DATA.terms.forEach(function (t) {
      const first = t.term.charAt(0);
      const key = /[a-zA-Z]/.test(first) ? "A–Z" : "中文";
      (groups[key] = groups[key] || []).push(t);
    });
    const order = ["A–Z", "中文"];
    return order.map(function (key) {
      if (!groups[key]) return "";
      return (
        '<div class="term-group"><h2>' + key + "</h2>" +
        groups[key].map(function (t) {
          return (
            '<div class="term-card">' +
            '<div class="term-name">' + escapeHtml(t.term) + "</div>" +
            '<div class="term-plain">' + escapeHtml(t.plain) + "</div>" +
            '<div class="term-skills">出现在：' +
            t.skills.map(function (sid) {
              const s = skillById(sid);
              return '<a href="#/skill/' + encodeURIComponent(sid) + '">' +
                escapeHtml(s ? s.name_cn : sid) + "</a>";
            }).join("、") +
            "</div></div>"
          );
        }).join("") +
        "</div>"
      );
    }).join("");
  }

  /* ---------- 渲染 ---------- */
  function render() {
    const hash = location.hash || "#/";
    let html = "";
    if (hash.indexOf("#/skill/") === 0) {
      const id = decodeURIComponent(hash.slice("#/skill/".length));
      html = viewDetail(id);
    } else if (hash === "#/terms") {
      html = viewTerms();
    } else {
      html = viewList();
    }
    APP.innerHTML = html;

    // 导航高亮
    document.querySelectorAll(".nav-link").forEach(function (a) {
      a.classList.toggle("active", a.getAttribute("data-nav") === (hash.indexOf("#/skill/") === 0 ? "list" : a.getAttribute("data-nav")));
    });

    // 列表页事件绑定
    const search = document.getElementById("searchInput");
    if (search) {
      search.addEventListener("input", function () {
        state.query = search.value;
        render();
      });
    }
    document.querySelectorAll(".chip[data-cat]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.category = b.getAttribute("data-cat");
        render();
      });
    });
    // 滚动到顶部
    window.scrollTo({ top: 0 });
  }

  document.getElementById("brandBtn").addEventListener("click", function () {
    state.query = ""; state.category = "all";
    location.hash = "#/";
  });

  init();
})();
