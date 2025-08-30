.PHONY: setup run
setup:
	pip install -r requirements.txt

run:
	python -m src.are_summarizer.cli --config config/settings.example.yaml
