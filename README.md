# HuggingChat API Examples

## Installation

Create a `.env` file at the top level with this content:

```{dotenv}
HUGGING_FACE_EMAIL=<Your email on HuggingFace>
HUGGING_FACE_PASSWORD=<Your password on HuggingFace>
```

For example (not a real account):

```{dotenv}
HUGGING_FACE_EMAIL=nobody@email.com
HUGGING_FACE_PASSWORD=12345678
```

### Windows

```{bash}
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

### Linux

```{bash}
python -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

## Usage

### CLI

```{bash}
python cli.py
```

### Translator

```{bash}
python translator.py
```
