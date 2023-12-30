
# Christmas card factory

This is an example of how to programatically generate a pdf file from a libreoffice document.

## Requirements

pip and python3 and unoserver are required. Tested with python 3.11

Unoserver is sometimes installed with libreoffice.

## Installation

```
python -m venv .venv
source .venv/bin/env
pip -Ur requirements.txt
```

## Usage

```
source .venv/bin/env
python christmas-card-factory.py  --action pdf "Tim Cook" assets/Tim-Cook-Circle.png > tim_cook_christmas_card.pdf
```

For help do:

```
python christmas-card-factory.py --help
```
