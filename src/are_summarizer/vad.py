import numpy as np
import soundfile as sf
import webrtcvad
from pydub import AudioSegment


def _to_wav_mono16k(src_path: str) -> AudioSegment:
    seg = AudioSegment.from_file(src_path)
    seg = seg.set_channels(1).set_frame_rate(16000).set_sample_width(2)
    return seg


def apply_vad_and_save_wav(
    src_audio: str, dst_wav: str, frame_ms: int = 30, aggressiveness: int = 2
):
    seg = _to_wav_mono16k(src_audio)
    samples = np.array(seg.get_array_of_samples())
    vad = webrtcvad.Vad(aggressiveness)
    frame_len = int(16000 * frame_ms / 1000)
    voiced = []

    for i in range(0, len(samples), frame_len):
        frame = samples[i : i + frame_len]
        if len(frame) < frame_len:
            break
        ok = vad.is_speech(frame.tobytes(), sample_rate=16000)
        if ok:
            voiced.append(frame)

    if voiced:
        out = np.concatenate(voiced).astype(np.int16)
    else:
        out = np.zeros(16000, dtype=np.int16)

    sf.write(dst_wav, out, 16000)
    return dst_wav
