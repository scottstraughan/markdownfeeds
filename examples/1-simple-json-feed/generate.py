#!/usr/bin/python python3
import logging

from markdownfeeds.Generators import GeneratorSettings
from markdownfeeds.Generators.Json.JsonFeedGenerator import JsonFeedGenerator
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed

logging.basicConfig(level=logging.INFO)

JsonFeedGenerator(
    feed=JsonFeed(
        title='Captain\'s Log'
    ),
    generator_settings=GeneratorSettings(
        source_directory='logs',
        feed_items_per_export=20
    )
).run_standalone()
