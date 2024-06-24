#!/usr/bin/python python3
import logging

from markdownfeeds.Gatherer import Gatherer
from markdownfeeds.Generators import GeneratorSettings
from markdownfeeds.Generators.Html.HtmlFeedGenerator import HtmlFeedGenerator
from markdownfeeds.Generators.Json.JsonFeedGenerator import JsonFeedGenerator
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed

logging.basicConfig(level=logging.INFO)

Gatherer([
    JsonFeedGenerator(
        feed=JsonFeed(title='Captain\'s Log 1'),
        generator_settings=GeneratorSettings(
            source_directory='../1-simple-json-feed/logs',
            target_directory='json/log1',
            feed_items_per_export=20
        )
    ),

    JsonFeedGenerator(
         feed=JsonFeed(
             title='Captain\'s Log 2'),
         generator_settings=GeneratorSettings(
             source_directory='../1-simple-json-feed/logs',
             target_directory='json/log2',
             feed_items_per_export=20
         )
    ),

    HtmlFeedGenerator(
         feed=JsonFeed(title='Captain\'s Log'),
         generator_settings=GeneratorSettings(
             source_directory='../1-simple-json-feed/logs',
             target_directory='html',
             feed_items_per_export=20
         )
    ),
]).generate()
