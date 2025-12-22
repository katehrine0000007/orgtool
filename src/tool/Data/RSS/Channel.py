from App.Objects.Object import Object
from Data.RSS.ChannelImage import ChannelImage
from Data.RSS.ChannelItem import ChannelItem
from pydantic import Field
from typing import Optional
from dateutil import parser, tz
import xml

class Channel(Object):
    title: str = Field(default = None)
    description: str = Field(default = None)
    url: str = Field(default = None)
    channel_link: str = Field(default = None, alias='link')
    generator: str = Field(default = None)
    copyright: str = Field(default = None)
    language: str = Field(default = None)
    ttl: int = Field(default = None)
    image: Optional[ChannelImage] = Field(default = None)

    def update_data(self, channel: dict):
        self.title = channel.get('title')
        self.description = channel.get('description')
        self.channel_link = channel.get('link')
        self.generator = channel.get('generator')
        self.copyright = channel.get('copyright')
        self.language = channel.get('language')

    async def download(self):
        import aiohttp, xmltodict

        response_xml = None
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                response_xml = await response.text()

        rss_response = xmltodict.parse(response_xml)
        rss = rss_response.get('rss')

        return rss.get('channel')

    def addItem(self, item: dict):
        return ChannelItem.model_validate(item, by_alias = True)
