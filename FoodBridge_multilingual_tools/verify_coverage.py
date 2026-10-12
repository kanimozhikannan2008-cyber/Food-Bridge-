# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html_i18n = set(re.findall(r'data-i18n="([^"]+)"', html))
html_ph = set(re.findall(r'data-i18n-ph="([^"]+)"', html))
all_html = html_i18n.union(html_ph)

from make_all_languages import en_dict
from build_full_languages import es_dict
import dict_hi, dict_ta, dict_te_bn, dict_fr_de, dict_zh_ar

dicts = {
    "en": en_dict,
    "es": es_dict,
    "hi": dict_hi.hi_dict,
    "ta": dict_ta.ta_dict,
    "te": dict_te_bn.te_dict,
    "bn": dict_te_bn.bn_dict,
    "fr": dict_fr_de.fr_dict,
    "de": dict_fr_de.de_dict,
    "zh": dict_zh_ar.zh_dict,
    "ar": dict_zh_ar.ar_dict,
}

print(f"Total HTML keys detected: {len(all_html)}")

for lang, d in dicts.items():
    missing = all_html - set(d.keys())
    print(f"{lang}: total keys in dict={len(d)}, missing from HTML={len(missing)}")
    if missing:
        print(f"  missing in {lang}: {sorted(missing)}")
