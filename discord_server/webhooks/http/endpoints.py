from discord_webhook import DiscordWebhook
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from typing import Dict
from pydantic import BaseModel


class Payload(BaseModel):
    subscriptionId: str
    notificationId: int
    id: str
    eventType: str
    publisherId: str
    message: dict
    detailedMessage: dict
    resource: dict
    resourceVersion: str
    resourceContainers: dict
    createdDate: str

discord_webhook_url_1 = "https://discord.com/api/webhooks/1148429405870366720/Bdcm6cxXFtoyzqnXgf9C536FuSGhuXcKEBBdFNC9GFwPzFPxjlZclZJ5aXe6TyeojlF2"

discord_webhook_url_2 = "https://discord.com/api/webhooks/1147023038961942559/9Ho5acOW-aAqcz-QmsYPkVC3tI0_YMDk1h8L_iKqwu5Qjrz2vlrVme_yMaKkPEoiro3w"

router = APIRouter()


@router.get("/")
async def index():
    return JSONResponse({"Status": "OK", "Message": "Server is OK"})


@router.post("/get-payload")
async def get_payload(item: Payload):
    content = f"Got new PR bois, {item.resource['_links']['web']['href']}"  
    print ({item.resource['repository']['name']})
    print (f"{item.resource['repository']['name']}" == 'TodoApp')
    if (f"{item.resource['repository']['name']}" == "Discord-Bot"): 
        discord_webhook_url = discord_webhook_url_1
    else:
        discord_webhook_url = discord_webhook_url_2

    webhook = DiscordWebhook(
        discord_webhook_url,
        content=content,
    )
    webhook.execute()
    return JSONResponse({"Status": "OK"})
