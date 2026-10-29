import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen


def download_file(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with urlopen(url, timeout=120) as response:
        output_path.write_bytes(response.read())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)
    parser.add_argument("--url", required=True)

    args = parser.parse_args()

    month_text = f"{args.month:02d}"

    output_directory = Path(
        "data",
        "bronze",
        "yellow_taxi",
        f"year={args.year}",
        f"month={month_text}",
    )

    output_file = output_directory / "source.parquet"
    metadata_file = output_directory / "metadata.json"

    if output_file.exists():
        print(f"File already exists: {output_file}")
        return

    print(f"Downloading source file from: {args.url}")

    download_file(args.url, output_file)

    metadata = {
        "source_url": args.url,
        "source_year": args.year,
        "source_month": args.month,
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "output_file": str(output_file),
        "file_size_bytes": output_file.stat().st_size,
    }

    metadata_file.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(f"Downloaded file to: {output_file}")
    print(f"Created metadata file: {metadata_file}")


if __name__ == "__main__":
    main()