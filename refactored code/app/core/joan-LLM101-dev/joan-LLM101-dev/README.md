# LLM 101 Learning

[![Build Status](https://img.shields.io/badge/version-1.0.0-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green)](https://fastapi.tiangolo.com/)

## Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Environment Configuration](#environment-configuration)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Key Practices](#key-practices)

## Project Overview
- In this lab, you will explore the evolution, architecture, applications, and challenges of LLMs, focusing on their impact in the field of Natural Language Processing (NLP).
- Objectives:
  - Understand what LLM is.
  - Understand the LLM process, why it is important and its application.
  - Learn how to use LLM

## Getting Started

### Prerequisites
- Python 3.10+
- Docker 20.10+

### Installation
```bash
# Clone repository
git clone https://github.com/AI-Security-Academy-Web/joan-LLM101.git

#create a virtualenv 
python -m venv venv

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

python main.py


```

## Environment Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `LLM 101 Learning` | name of the application |
| `DEBUG` | False | setting this to true during developement will help in reloading the uvicorn server whenever there is a change to the code.  |
| `LOG_LEVEL` | `INFO` | set the level of logging |
| `VERSION` | `1.0.0` | the version of the lab |
| `API_KEY` | `` | get this key from the assets of the database. |
| `PORT` | 8000 | API listening port |
| `HOST` | `0.0.0.0`| API HOST |

## API Documentation
### Base URL
`https://<domain or ip>`

### Endpoints
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `"/"` | GET | Read root | No |
| `/chatbot/` | POST | Generate a conversational response using ChatterBot based on the user's message | No |
| `/generate-text` | POST | Generate text using GPT-2 model based on a prompt | No |
| `/translate` | POST | Translate the given text to a specified target language using Google Translator | No |
| `/summarize` | POST | Generate a summary of the input text using a BART model | No |
| `/analyze` | POST | Perform sentiment analysis on the input text using a transformer-based model | No |

## Deployment
### Docker Build

```bash
docker build -t llm_101 .
```
## Key Practices
- All endpoints must include authentication
- Logs must not contain sensitive data

