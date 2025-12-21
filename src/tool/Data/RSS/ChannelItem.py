from App.Objects.Object import Object
from pydantic import Field
import datetime
from typing import Optional

class ChannelItem(Object):
    title: str = Field(default = None)
    description: str = Field(default = None)
    channel_link: str = Field(default = None, alias = 'link')
    guid: Optional[dict | str] = Field(default = None)
    pubDate: datetime.datetime | str = Field(default = None)
    media_thumbnail: Optional[dict] = Field(alias="media:thumbnail", default = None)
