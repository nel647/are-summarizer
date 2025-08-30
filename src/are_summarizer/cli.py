import argparse
import os
import yaml

from .fetch import download_audio
from .vad import apply_vad_and_save_wav
from .transcribe import transcribe_whisper
from .summarize import naive_summarize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/settings.example.yaml")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    outdir = cfg["output"]["dir"]
    os.makedirs(outdir, exist_ok=True)
    base = cfg["output"]["basename"]

    # 1) ダウンロード
    audio_path = os.path.join("data", "input", f"{base}.mp3")
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    download_audio(cfg["episode"]["audio_url"], audio_path)

    # 2) VAD
    wav_path = os.path.join("data", "intermediate", f"{base}_vad.wav")
    os.makedirs(os.path.dirname(wav_path), exist_ok=True)
    apply_vad_and_save_wav(
        audio_path,
        wav_path,
        frame_ms=cfg["transcribe"]["vad_frame_ms"],
        aggressiveness=cfg["transcribe"]["vad_aggressiveness"],
    )

    # 3) 文字起こし
    srt_path = os.path.join(outdir, f"{base}.srt")
    txt_path = os.path.join(outdir, f"{base}.txt")
    transcribe_whisper(
        wav_path,
        srt_out=srt_path,
        txt_out=txt_path,
        model_size=cfg["transcribe"]["model_size"],
        language=cfg["transcribe"]["language"],
        beam_size=cfg["transcribe"]["beam_size"],
    )

    # 4) 要約
    summary_md = os.path.join(outdir, f"{base}_summary.md")
    naive_summarize(
        txt_path,
        summary_md,
        title=cfg["episode"]["title"],
        date=cfg["episode"]["date"],
    )

    print("DONE:", {"srt": srt_path, "txt": txt_path, "summary": summary_md})


if __name__ == "__main__":
    main()
