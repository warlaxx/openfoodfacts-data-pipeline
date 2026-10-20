"""Download the first N rows of the Open Food Facts CSV export.

The full export is several GB compressed; streaming the gzip and stopping after N lines lets you
work locally on a realistic sample in a few seconds.

Usage: python scripts/download_sample.py --rows 50000
"""

import argparse
import gzip
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from off_pipeline import config  # noqa: E402

URL = "https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=50_000, help="data rows to keep")
    parser.add_argument("--out", type=Path, default=config.SAMPLE_CSV)
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(URL, headers={"User-Agent": "off-pipeline (learning project)"})
    with urllib.request.urlopen(req) as resp, gzip.open(resp, "rt", encoding="utf-8") as src:
        with args.out.open("w", encoding="utf-8") as dst:
            for i, line in enumerate(src):
                if i > args.rows:  # line 0 is the header
                    break
                dst.write(line)
    print(f"Wrote {min(i, args.rows)} rows (+ header) to {args.out}")


if __name__ == "__main__":
    main()
