import xml.etree.ElementTree as ET
import os

tree = ET.parse("note.xml")
root = tree.getroot()

os.makedirs("docs/posts", exist_ok=True)

index_list = []

for i, item in enumerate(root.iter("item")):
    title = item.findtext("title") or f"post{i}"
    content = item.findtext("content") or ""

    filename = f"docs/posts/{i}.html"

    html = f"""
<html>
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
<h1>{title}</h1>
<div>{content}</div>
</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    index_list.append((title, f"posts/{i}.html"))

index_html = "<h1>Archive</h1><ul>"
for title, link in index_list:
    index_html += f'<li><a href="{link}">{title}</a></li>'
index_html += "</ul>"

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
