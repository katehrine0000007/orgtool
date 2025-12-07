from App.Tests.Test import Test
from Data.XML import XML
from Data.JSON import JSON

class ConverterTest(Test):
    async def implementation(self, i):
        _xml_str = """<?xml version="1.0" encoding="utf-8"?>
<example>
    <example_item id="itm1">
    </example_item>
    <example_item id="itm2">
    </example_item>
</example>
        """
        _xml = XML(xml=_xml_str)
        print(await _xml.convertTo(JSON))
