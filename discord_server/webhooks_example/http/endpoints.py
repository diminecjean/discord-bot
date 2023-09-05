from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from discord_webhook import DiscordWebhook

router = APIRouter()
discord_webhook_url = "https://discord.com/api/webhooks/1146008058904973373/DjGT_m3DKWYFBxLEsOt6tfcvuSEgn4lnDj2U2padIO0VMJWJW4qNii5AUVwrhCsShP3L"


@router.post("/test-message")
async def test_message():
    content = "This is a sample message for webhooks"
    webhook = DiscordWebhook(
        discord_webhook_url,
        content=content,
    )
    webhook.execute()
    return JSONResponse({"Status": "OK"})


@router.post("/test-ping")
async def test_ping():
    # Spam for Loves by Jason
    content = "You look so handsome Suai Ge <@453715456466092032>"
    allowed_mentions = {"users": ["453715456466092032"]}
    webhook = DiscordWebhook(
        discord_webhook_url,
        content=content,
        allowed_mentions=allowed_mentions,
    )
    webhook.execute()
    return JSONResponse({"Status": "OK"})


@router.post("/test-ping-role")
async def test_ping_role():
    # Enslave Moderators
    content = "Cannot Slack <@&885355018943877130>, keep working hard"
    allowed_mentions = {"roles": ["885355018943877130"]}
    webhook = DiscordWebhook(
        discord_webhook_url,
        content=content,
        allowed_mentions=allowed_mentions,
    )
    webhook.execute()
    return JSONResponse({"Status": "OK"})
