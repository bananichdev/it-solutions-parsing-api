from sqlalchemy import delete, select
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import async_sessionmaker

from database.models import AdModel
from schemas.v1.ad import Ad
from schemas.v1.errors import AdNotFoundError, DBAPICallError


async def get_ad_by_id(
    db_sessionmaker: async_sessionmaker,
    ad_id: int,
) -> Ad:
    try:
        async with db_sessionmaker.begin() as session:
            if (
                ad_entity := await session.scalar(select(AdModel).where(AdModel.ad_id == ad_id))
            ) is None:
                raise AdNotFoundError(ad_id=ad_id)
    except DBAPIError as e:
        raise DBAPICallError(msg=f"can not get ad with id={ad_id}") from e

    return Ad(**ad_entity.as_dict())


async def get_ads_list(
    db_sessionmaker: async_sessionmaker,
) -> list[Ad]:
    try:
        async with db_sessionmaker.begin() as session:
            ads_entity_list = await session.scalars(select(AdModel))
    except DBAPIError as e:
        raise DBAPICallError(msg="can not get ads list") from e

    return [Ad(**ad_entity.as_dict()) for ad_entity in ads_entity_list]


async def create_ads_from_list(
    db_sessionmaker: async_sessionmaker,
    ads_list: list[dict[str, int | str]],
) -> None:
    try:
        async with db_sessionmaker.begin() as session:
            for ad in ads_list:
                ad_entity = AdModel(**ad)
                session.add(ad_entity)
    except DBAPIError as e:
        await session.rollback()
        raise Exception("can not create ads list") from e


async def delete_all_ads(db_sessionmaker: async_sessionmaker) -> None:
    ads_list = await get_ads_list(db_sessionmaker=db_sessionmaker)

    try:
        async with db_sessionmaker.begin() as session:
            for ad in ads_list:
                await session.execute(delete(AdModel).where(AdModel.ad_id == ad.ad_id))
    except DBAPIError as e:
        await session.rollback()
        raise DBAPICallError(msg="can not get ads list") from e
