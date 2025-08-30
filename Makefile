.PHONY: install test run

install:
	pip install -r requirements.txt

test:
	pytest -q

run:
	python -m are_summarizer --audio-url https://example.com/audio.mp3 --date 2024-01-01
