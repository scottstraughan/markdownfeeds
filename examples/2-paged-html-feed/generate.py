#!/usr/bin/python python3
import logging

from markdownfeeds.Generators import GeneratorSettings
from markdownfeeds.Generators.Html.HtmlFeedGenerator import HtmlFeedGenerator
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed

logging.basicConfig(level=logging.INFO)

HtmlFeedGenerator(
    feed=JsonFeed(title='Captain\'s Log', ),
    generator_settings=GeneratorSettings(
        source_directory='../1-simple-json-feed/logs',
        feed_items_per_export=20
    )
).run_standalone()
