# CV maintenance

The PDF uses a two-page, black-and-white academic layout with embedded Liberation
Serif fonts. Identity, dates, publications, and submission statuses come from the
shared website data. Concise CV-specific research text lives in `_data/cv.json`.

With Python, `reportlab`, `pypdf`, `pdfplumber`, and Liberation Serif installed:

```sh
python3 tools/build_cv.py
python3 tools/check_cv.py
```

Set `CV_FONT_DIR` to the directory containing the four `LiberationSerif-*.ttf`
files if they are not in a detected font location. After edits, render both PDF
pages with Poppler and inspect spacing, heading hierarchy, and page breaks.
Commit `cv/Yukai_Wang_CV.pdf` with its source edits; Pages serves this built PDF.
