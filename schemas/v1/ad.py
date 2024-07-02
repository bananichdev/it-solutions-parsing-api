from pydantic import BaseModel


class Ad(BaseModel):
    ad_id: int
    title: str
    author: str
    views: int
    position: int
