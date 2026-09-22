# CV maintenance

The PDF uses a two-page, black-and-white academic layout with embedded Liberation
Serif fonts. Identity, dates, publications, and submission statuses come from the
shared website data. Concise CV-specific research text lives in `_data/cv.json`.
The additional Chinese edition uses `_data/cv_zh.json`; English paper titles,
authors, publication venues, and manuscript statuses remain unchanged.

With Python, `reportlab`, `pypdf`, `pdfplumber`, and Liberation Serif installed:

```sh
python3 tools/build_cv.py
python3 tools/check_cv.py
python3 tools/build_cv.py --lang zh
python3 tools/check_cv.py --lang zh
```

Set `CV_FONT_DIR` to the directory containing the four `LiberationSerif-*.ttf`
files if they are not in a detected font location. After edits, render both PDF
pages with Poppler and inspect spacing, heading hierarchy, and page breaks.
Commit `cv/Yukai_Wang_CV.pdf` with its source edits; Pages serves this built PDF.
For Chinese builds, Songti SC Regular and Bold are embedded from the macOS
Songti.ttc collection (indices 6 and 1). Set `CV_CJK_FONT` if this collection is
elsewhere. Commit `cv/Yukai_Wang_CV_CN.pdf` for the separate Chinese download.
