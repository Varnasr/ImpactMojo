#!/usr/bin/env python3
"""
Extract full text from a PDF for book-companion authoring.

Two-stage: (1) PyMuPDF native text extraction (fast, exact for text PDFs, which
read_file_content truncates); (2) Tesseract OCR fallback for pages that come back
near-empty (image-only scans). Writes plain text to the output path.

Usage:
    python3 scripts/extract-pdf-text.py in.pdf out.txt [--ocr-threshold 40] [--dpi 200] [--max-ocr-pages 400]

Requires: pymupdf, pytesseract, Pillow, and the tesseract binary.
"""
import argparse
import sys


def extract(pdf_path, out_path, ocr_threshold=40, dpi=200, max_ocr_pages=400):
    import fitz  # PyMuPDF
    doc = fitz.open(pdf_path)
    pages_text = []
    ocr_pages = []
    for i, page in enumerate(doc):
        t = page.get_text("text")
        if len(t.strip()) < ocr_threshold:
            ocr_pages.append(i)
            pages_text.append(None)  # placeholder, fill by OCR
        else:
            pages_text.append(t)

    native_pages = sum(1 for t in pages_text if t is not None)
    print(f"{doc.page_count} pages; {native_pages} had native text; "
          f"{len(ocr_pages)} need OCR", file=sys.stderr)

    if ocr_pages:
        try:
            import pytesseract
            from PIL import Image
            import io
        except Exception as e:
            print(f"OCR libs unavailable ({e}); leaving {len(ocr_pages)} pages blank",
                  file=sys.stderr)
        else:
            todo = ocr_pages[:max_ocr_pages]
            if len(ocr_pages) > max_ocr_pages:
                print(f"NOTE: capping OCR at {max_ocr_pages} pages "
                      f"({len(ocr_pages) - max_ocr_pages} skipped)", file=sys.stderr)
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            for n, i in enumerate(todo):
                pix = doc[i].get_pixmap(matrix=mat)
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                pages_text[i] = pytesseract.image_to_string(img)
                if (n + 1) % 10 == 0:
                    print(f"  OCR {n + 1}/{len(todo)}", file=sys.stderr)

    text = "\n\n".join(t or "" for t in pages_text)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path}: {len(text):,} chars", file=sys.stderr)
    return len(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("--ocr-threshold", type=int, default=40)
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--max-ocr-pages", type=int, default=400)
    a = ap.parse_args()
    extract(a.pdf, a.out, a.ocr_threshold, a.dpi, a.max_ocr_pages)


if __name__ == "__main__":
    main()
