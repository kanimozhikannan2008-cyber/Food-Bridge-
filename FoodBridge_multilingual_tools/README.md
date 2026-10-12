# FoodBridge Multilingual Tools

This folder contains the Python scripts created from the code shared in chat.

## Files
- `verify_coverage.py` — checks HTML translation keys against the 10 language dictionaries.
- `find_untranslated.py` — scans `index.html` for visible text that may not have i18n attributes.
- `add_i18n_attributes.py` — applies the replacement patterns shared for history labels and headers; writes `index_i18n_updated.html`.
- `compile_multilingual_engine.py` — loads the base dictionaries, adds the supplied new translations, and generates `app.js`.
- `history_i18n_example.html` — cleaned example of the history search and Export CSV markup.

## How to use
1. Copy these scripts into the project folder that contains `index.html` and the dictionary modules.
2. Make sure the following modules are available beside the scripts (or importable by Python):
   `make_all_languages.py`, `build_full_languages.py`, `dict_hi.py`, `dict_ta.py`, `dict_te_bn.py`, `dict_fr_de.py`, `dict_zh_ar.py`.
3. Run the desired script from that project directory, for example:
   `python verify_coverage.py`

The HTML and dictionary files from your full project were not uploaded in this chat, so this bundle contains the tools and the HTML example only. Review generated outputs before replacing any production files.
