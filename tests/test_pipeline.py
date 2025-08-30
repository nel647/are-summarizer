from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from are_summarizer import run_pipeline


def test_run_pipeline(tmp_path: Path) -> None:
    out = tmp_path / "out.txt"
    summary = run_pipeline("https://example.com/audio.mp3", "2024-01-01", out)
    assert "dummy summary" in summary
    assert out.read_text(encoding="utf-8") == summary
