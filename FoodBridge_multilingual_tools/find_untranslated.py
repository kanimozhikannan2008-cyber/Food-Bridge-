# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.untranslated = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        has_i18n = "data-i18n" in attr_dict or "data-i18n-ph" in attr_dict
        parent_has_i18n = any(item[1] for item in self.stack)
        self.stack.append((tag, has_i18n or parent_has_i18n, attr_dict))

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        text = data.strip()
        if not text or len(text) <= 2:
            return
        if self.stack:
            tag, has_i18n, attrs = self.stack[-1]
            if tag in ["script", "style", "title"]:
                return
            if not has_i18n:
                cleaned = re.sub(
                    r'[\\d\\s\\:\\,\\.\\-\\+\\(\\)\\#\\%\\$\\₹\\/\\•\\—\\▼\\▾\\✓\\✗\\⚠️\\⚡\\💡\\🔒\\🛡️\\🚨\\🧭\\🛵\\🚗\\🚲\\🍞\\🍲\\🥛\\🍎\\📦\\📍\\📜\\🔄\\🌐\\🎙️\\🔊\\➤\\🤖\\✕\\×\\👤\\🏢\\🏠\\⏱️\\🔑\\📋\\🛡]+',
                    '',
                    text,
                )
                if len(cleaned) > 2:
                    cls = attrs.get("class", "")
                    self.untranslated.append((tag, cls, text))

parser = MyHTMLParser()
with open("index.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())

with open("untranslated_output.txt", "w", encoding="utf-8") as out:
    out.write(f"Total untranslated snippets: {len(parser.untranslated)}\\n")
    for tag, cls, text in parser.untranslated:
        out.write(f"<{tag} class='{cls}'>: {text}\\n")

print("Saved untranslated to untranslated_output.txt")
