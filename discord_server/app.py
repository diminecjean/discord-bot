from fastapi import FastAPI
from discord_server.webhooks.http.endpoints import router as webhook_router
from discord_server.webhooks_example.http.endpoints import router as webhook_test_router

app = FastAPI()


app.include_router(webhook_router)
app.include_router(webhook_test_router)
