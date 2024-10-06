from fastapi import APIRouter, Depends
import os
from dotenv import load_dotenv

load_dotenv(".env")

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def get_health():
    return {"health": "OK", "version": os.getenv("VERSION")}
