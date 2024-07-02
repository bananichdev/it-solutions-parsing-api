from contextlib import asynccontextmanager

from fastapi import FastAPI
from httpx import AsyncClient

from database.connection import get_db_sessionmaker
from database.controllers.ad import create_ads_from_list, delete_all_ads
from settings import HEADERS
from utils.parse import get_ad_dict, get_sub_urls_list, get_views_list
from utils.requests import get_ad_pages_html_list, get_homepage_html


@asynccontextmanager
async def lifespan(_: FastAPI):
    db_sessionmaker = get_db_sessionmaker()

    async with AsyncClient(headers=HEADERS) as client:
        homepage_html = await get_homepage_html(client=client)
        ad_page_urls_list = get_sub_urls_list(homepage_html=homepage_html)
        ads_html_list = await get_ad_pages_html_list(client=client, urls=ad_page_urls_list)

    ads_list: list[dict[str, int | str]] = []
    views_list = get_views_list(homepage_html=homepage_html)

    for index, ad_html in enumerate(ads_html_list):
        ad_info = get_ad_dict(ad_html=ad_html)
        ad_info |= {"views": views_list[index], "position": index + 1}
        ads_list.append(ad_info)

    await create_ads_from_list(db_sessionmaker=db_sessionmaker, ads_list=ads_list)

    yield

    await delete_all_ads(db_sessionmaker=db_sessionmaker)
