from pathlib import Path


def naive_summarize(txt_path: str, out_md: str, title: str, date: str):
    text = Path(txt_path).read_text(encoding="utf-8")
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    head = lines[:20]
    bullets = "\n".join([f"- {l[:120]}" for l in head])

    md = f"""# {title}
- 収録日: {date}

## 概要（暫定）
{bullets}

## 今後の予定
- 話者分離（埋め込み＋クラスタリング）導入
- セクションごとの要旨生成
- タイムスタンプ目次の自動生成
"""
    Path(out_md).write_text(md, encoding="utf-8")
