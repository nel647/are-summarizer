from pathlib import Path

from faster_whisper import WhisperModel


def transcribe_whisper(
    wav_path,
    srt_out,
    txt_out,
    model_size="base",
    language="ja",
    beam_size=5,
):
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(wav_path, language=language, beam_size=beam_size)

    with open(txt_out, "w", encoding="utf-8") as f:
        for seg in segments:
            f.write(seg.text.strip() + "\n")

    def srt_time(t):
        from math import floor

        h = floor(t / 3600)
        m = floor((t % 3600) / 60)
        s = floor(t % 60)
        ms = int((t - floor(t)) * 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    segments, _ = model.transcribe(wav_path, language=language, beam_size=beam_size)
    with open(srt_out, "w", encoding="utf-8") as f:
        idx = 1
        for seg in segments:
            f.write(f"{idx}\n")
            f.write(f"{srt_time(seg.start)} --> {srt_time(seg.end)}\n")
            f.write(seg.text.strip() + "\n\n")
            idx += 1
