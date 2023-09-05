# Discord Webhook and Azure Devops Integration

This app works as a middleware for Azure Devops and Discord Webhooks.
It can send messages to discord servers when the API is triggered.

## Getting Started

1. Create Virtual Environment

```zsh
python -m venv env
```

2. Access Virtual Environment

```zsh
.\env\Scripts\activate
```

3. Install dependencies

```zsh
pip install -r requirements.txt
```

4. Start FastAPI process

```zsh
uvicorn discord_server.app:app --reload
```

5. Execute ngrok.exe (Optional)

```zsh
Double click ngork.exe from project
```

6. Expose your localhost to public (Optional)

```zsh
ngrok http 8000
```
