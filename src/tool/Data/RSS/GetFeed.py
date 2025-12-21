from App.Objects.Extractor import Extractor
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Types.String import String
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.RSS.Channel import Channel
from Data.RSS.ChannelItem import ChannelItem

class GetFeed(Extractor):
    # Should it be in Web category or in Data? dont know

    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            String(
                name = 'url',
                assertions = [NotNoneAssertion()]
            )
        ])

    async def implementation(self, i):
        import aiohttp, xmltodict

        url = i.get('url')
        response_xml = None

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_xml = await response.text()

        self.log(f"url: {url}")
        rss_response = xmltodict.parse(response_xml)
        rss = rss_response.get('rss')
        _channel = rss.get('channel')
        channel = Channel(
            title = _channel.get('title'),
            description = _channel.get('description'),
            channel_link = _channel.get('link'),
            generator = _channel.get('generator'),
            copyright = _channel.get('copyright'),
            language = _channel.get('language'),
        )

        for item in _channel.get('item'):
            _item = ChannelItem.model_validate(item, by_alias = True)
            channel.link(_item)

        self.append(channel)
