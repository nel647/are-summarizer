"""Placeholder audio transcription and summarization pipeline."""
from __future__ import annotations

from pathlib import Path


def download_audio(url: str) -> Path:
    """Pretend to download audio from the given URL.

    Args:
        url: Location of the audio file.

    Returns:
        Path to a dummy audio file.
    """
    return Path("dummy_audio.wav")


def remove_silence(path: Path) -> Path:
    """Placeholder for voice activity detection."""
    return path


def transcribe(path: Path) -> str:
    """Fake transcription step."""
    return "dummy transcription"


def summarize(text: str) -> str:
    """Produce a dummy summary."""
    return "dummy summary"


def run_pipeline(audio_url: str, date: str, output: str | Path | None = None) -> str:
    """Execute the placeholder pipeline."""
    audio = download_audio(audio_url)
    cleaned = remove_silence(audio)
    text = transcribe(cleaned)
    summary = summarize(text)
    if output is not None:
        Path(output).write_text(summary, encoding="utf-8")
    return summary
