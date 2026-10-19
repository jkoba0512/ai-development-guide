"""Check MkDocs navigation and relative file links offline."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import yaml
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
errors = []


def nav_paths(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from nav_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from nav_paths(child)
    elif isinstance(value, str):
        yield value


pages = list(DOCS.rglob("*.md"))
for path in nav_paths(config["nav"]):
    if not (DOCS / path).is_file():
        errors.append(f"nav: missing {path}")
for page in pages:
    text = page.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in re.findall(r"!?(?:\[[^\]]*\])\(([^\s)]+)\)", text):
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        destination = (page.parent / unquote(url.path)).resolve() if url.path else page
        if not destination.is_relative_to(DOCS.resolve()):
            errors.append(f"{page.relative_to(DOCS)}: outside docs: {target}")
        elif not destination.is_file():
            errors.append(f"{page.relative_to(DOCS)}: missing: {target}")
        elif url.fragment and destination.suffix == ".md":
            headings = re.findall(r"^#{1,6}\s+(.+)$", destination.read_text(encoding="utf-8"), re.M)
            anchors = {slugify_unicode(heading, "-") for heading in headings}
            if unquote(url.fragment) not in anchors:
                errors.append(f"{page.relative_to(DOCS)}: missing anchor: {target}")
for name in ("SPEC", "ENVIRONMENT", "VERIFICATION", "HANDOFF", "WORKING_RULES"):
    if not (DOCS / "assets" / "templates" / f"{name}.md.txt").is_file():
        errors.append(f"missing template: {name}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"OK: {len(pages)} pages, navigation, relative links, 4 core templates + 1 optional verification template")
