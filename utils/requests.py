import asyncio

from httpx import AsyncClient

from settings import HOMEPAGE_URL


async def get_homepage_html(client: AsyncClient) -> str:
    response = await client.get(url=HOMEPAGE_URL)

    if response.status_code not in [200, 301]:
        raise Exception("Resource unavailable")

    return response.text


async def get_ad_pages_html_list(client: AsyncClient, urls: list[str]) -> list[str]:
    tasks = [asyncio.create_task(client.get(url=url)) for url in urls]
    responses_list = await asyncio.gather(*tasks)

    if any(response.status_code not in [200, 301] for response in responses_list):
        raise Exception("Resource unavailable")

    return [response.text for response in responses_list]
