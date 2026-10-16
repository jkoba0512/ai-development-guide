"""Optional browser smoke check. Run using uv run --with playwright python scripts/check_preview.py."""
from pathlib import Path
import os
from playwright.sync_api import sync_playwright
import json
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
BASE = os.environ.get("GUIDE_PREVIEW_URL", "http://127.0.0.1:8000").rstrip("/")
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)
routes = [
    "/", "/plans/", "/setup/", "/tools/antigravity/", "/tools/grok-build/",
    "/tools/copilot/", "/tools/codex/", "/tools/claude-code/",
    "/workflow/specification/", "/workflow/implementation/",
    "/workflow/permissions/", "/workflow/handoff/", "/practice/",
    "/templates/", "/troubleshooting/", "/maintenance/", "/sources/",
    "/assets/templates/SPEC.md.txt", "/assets/templates/ENVIRONMENT.md.txt",
    "/assets/templates/VERIFICATION.md.txt", "/assets/templates/HANDOFF.md.txt",
    "/assets/templates/DECISIONS.md.txt", "/assets/templates/WORKING_RULES.md.txt",
    "/assets/example/study_stats.py", "/assets/example/test_study_stats.py",
    "/assets/stylesheets/extra.css",
]
for route in routes:
    with urlopen(BASE + route, timeout=10) as response:
        assert response.status == 200, route
with urlopen(BASE + "/search/search_index.json", timeout=10) as response:
    index = json.load(response)
    assert len(index["docs"]) >= 17
    assert any("handoff" in item.get("text", "").lower() for item in index["docs"])
errors = []
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        headless=True,
    )
    page = browser.new_page(viewport={"width": 1440, "height": 1000}, locale="en-US")
    page.on("pageerror", lambda error: errors.append(str(error)))
    for route in ("/", "/plans/", "/practice/", "/templates/"):
        page.goto(BASE + route, wait_until="load")
        assert page.locator("h1").is_visible(), route
        assert page.locator("html").get_attribute("lang") == "en", route
    page.goto(BASE + "/", wait_until="load")
    page.screenshot(path=str(ARTIFACTS / "preview-desktop.png"), full_page=True)
    search = page.locator('input[data-md-component="search-query"]')
    page.wait_for_timeout(1500)
    search.fill("handoff")
    page.locator(".md-search-result__link").first.wait_for(state="visible", timeout=10000)
    assert page.locator(".md-search-result__link").count() > 0, "English search results missing"
    page.keyboard.press("Escape")
    toggle = page.locator('label[for="__palette_1"]')
    toggle.click()
    assert page.locator("body").get_attribute("data-md-color-scheme") == "slate"
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(BASE + "/practice/", wait_until="load")
    assert page.locator("h1").is_visible()
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"), "Mobile page overflow"
    page.screenshot(path=str(ARTIFACTS / "preview-mobile.png"), full_page=True)
    assert not errors, errors
    browser.close()
print("OK: 17 pages, 9 static assets, search index, English search, dark mode, mobile layout; no page errors")
