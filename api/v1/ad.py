from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import async_sessionmaker

from database.connection import get_db_sessionmaker
from database.controllers.ad import get_ad_by_id, get_ads_list
from schemas.v1.ad import Ad
from utils.auth import check_token

router = APIRouter()


@router.get("/{ad_id}", status_code=status.HTTP_200_OK)
async def get_ad_handler(
    db_sessionmaker: Annotated[async_sessionmaker, Depends(get_db_sessionmaker)],
    _: Annotated[None, Depends(check_token)],
    ad_id: int,
) -> Ad:
    return await get_ad_by_id(db_sessionmaker=db_sessionmaker, ad_id=ad_id)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_ads_list_handler(
    db_sessionmaker: Annotated[async_sessionmaker, Depends(get_db_sessionmaker)],
    _: Annotated[None, Depends(check_token)],
) -> list[Ad]:
    return await get_ads_list(db_sessionmaker=db_sessionmaker)
