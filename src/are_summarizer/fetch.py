import pathlib
import urllib.request


def download_audio(url: str, dst: str):
    pathlib.Path(dst).parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dst)
    return dst
