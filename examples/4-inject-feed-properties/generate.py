#!/usr/bin/python python3
import logging

from markdownfeeds.Generators import GeneratorSettings
from markdownfeeds.Generators.Json.JsonFeedGenerator import JsonFeedGenerator
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

logging.basicConfig(level=logging.INFO)


class CustomFeedGenerator(JsonFeedGenerator):
    def _inject_feed_item_details(
        self,
        feed_item_details: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        feed_item_details.set('warp_factor', '9')
        return feed_item_details


CustomFeedGenerator(
    feed=JsonFeed(title='Captain\'s Log 1'),
    generator_settings=GeneratorSettings(
        source_directory='../1-simple-json-feed/logs',
        target_directory='json/log1',
        feed_items_per_export=20
    )
).run_standalone()
