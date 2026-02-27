---
title: KN3AUX-CODE.CLOUD
emoji: 💻
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
short_description: Acode — A powerful code editor for Android, served on the web
---

# KN3AUX-CODE.CLOUD

**Acode** is a powerful, open-source code editor originally built for Android — now running on the web via this Hugging Face Docker Space.

## Features

- Edit and preview HTML, CSS, JavaScript, and more
- Multi-language support (Python, Java, Kotlin, TypeScript, and more)
- Built-in JavaScript console
- Community plugin support
- LSP (Language Server Protocol) integration for IDE-grade completions

## Running Locally

```bash
git clone https://huggingface.co/spaces/krisshattanicole/KN3AUX-CODE.CLOUD
cd KN3AUX-CODE.CLOUD
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
```

## Tech Stack

- **Frontend**: Acode web app (JavaScript/HTML)
- **Backend**: FastAPI + Uvicorn
- **Container**: Docker (Python 3.9)

## Links

- [GitHub Repository](https://github.com/krisshattanicole/Acode)
- [Original Acode App](https://acode.app)
