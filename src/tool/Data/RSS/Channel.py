from App.Objects.Object import Object
from Data.RSS.ChannelImage import ChannelImage
from pydantic import Field
from typing import Optional

class Channel(Object):
    title: str = Field(default = None)
    description: str = Field(default = None)
    channel_link: str = Field(default = None, alias='link')
    generator: str = Field(default = None)
    copyright: str = Field(default = None)
    language: str = Field(default = None)
    ttl: int = Field(default = None)
    image: Optional[ChannelImage] = Field(default = None)
