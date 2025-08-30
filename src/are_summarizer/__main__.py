"""Command line interface for are_summarizer."""
from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the placeholder pipeline")
    parser.add_argument("--audio-url", required=True, help="URL to the audio file")
    parser.add_argument("--date", required=True, help="Recording date")
    parser.add_argument("--output", default="summary.txt", help="Where to write the summary")
    args = parser.parse_args()
    summary = run_pipeline(args.audio_url, args.date, args.output)
    print(summary)


if __name__ == "__main__":
    main()
