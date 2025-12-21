from App.Objects.Test import Test
from Data.RSS.GetFeed import GetFeed

class RSSTest(Test):
    async def implementation(self, i):
        _rss = GetFeed()
        res = await _rss.execute({
            'url': 'https://feeds.bbci.co.uk/news/world/rss.xml'
        })

        return res
