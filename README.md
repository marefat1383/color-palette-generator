# Color Palette Generator

A small educational AI project that reduces a collection of colors to a compact palette using K-Means clustering.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python palette_generator.py "#ff0000,#f01010,#0000ff,#1010ee,#00aa00,#10bb10" --colors 3
```

## Test

```bash
python -m unittest test_palette_generator.py
```

This project works on a short list of hex colors and demonstrates an interpretable clustering workflow.
