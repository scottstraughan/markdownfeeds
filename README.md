# Markdown Feeds

A fast and efficient tool that can generate paged "feeds" based on Markdown files.

A example use case of this tool is to generate a JSON or HTML feed for some news that you may have.

**Core Features:**

* Generate [complaint JSON Feed v1.0](https://www.jsonfeed.org/version/1/_) feeds
* Generate HTML feeds
* Supports pagination, with user defined "items per page"
* Fast and efficient, uses async based work groups
* Reads Markdown files in [YAML Front-Matter Jekyll Format](https://jekyllrb.com/docs/collections/#add-content)
* Markdown files can provide yaml based "front-matter" allowing extra details to be provided to feed

## Simple JSON Feed Example

This tool can be used to take the below files:

### Example Code

```python
from markdownfeeds.Generators.Json.JsonFeedGenerator import JsonFeedGenerator
from markdownfeeds.Generators.Json.JsonFeedGeneratorSettings import JsonFeedGeneratorSettings
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed

JsonFeedGenerator(
    feed=JsonFeed(title='Captain\'s Log 1'),
    generator_settings=JsonFeedGeneratorSettings(
        source_directory='../1-simple-json-feed/logs',
        target_directory='json/log1',
    )
).run_standalone()
```

### Input

**File 1: 2024-02-02-hello-world.md:**
```markdown
---
title: "Hello World!"
author: "Jean-Luc Picard"
---

Make it so!
```

**File 2: 2024-02-06-another-test-file.md:**
```markdown
---
title: "Another Test File"
author: "Kathryn Janeway"
location: "Delta Quadrant"
---

Tom, warp 6.
```

### Output

If you run the above files via the tool using `JsonFeedGenerator` generator, the output would be similar to:

```json
{
  "version": "https://jsonfeed.org/version/1",
  "title": "News Feed",
  "items": [
    {
      "id": "11581cc76bfff77669ebd94621959b016416e48d",
      "title": "Another Test File",
      "summary": "Tom, warp 6.",
      "date_published": "2024-02-06T00:00:00",
      "author": "Kathryn Janeway",
      "_location": "Delta Quadrant"
    },
    {
      "id": "de9d22cb5f4a20a3aeb00d156e086122148cd141",
      "title": "Hello World!",
      "summary": "Make it so!",
      "date_published": "2024-02-02T00:00:00",
      "author": "Jean-Luc Picard"
    }
  ],
  "_total_items": 2,
  "_total_pages": 1
}
```

## More Examples

There are a few additional examples available below:

* [Example 1 - Generate an HTML Feed](examples/1-simple-json-feed/)
* [Example 2 - Generate a JSON Feed with pagination](examples/2-paged-html-feed)
* [Example 3 - Generate multiple different feeds in parallel using the `Gatherer`](examples/3-multiple-parallel-feeds)
* [Example 4 - Inject Feed Properties](examples/4-inject-feed-properties)

### Extending

You can extend the functionality of this tool by adding support for new feed types. To do this, please create a new
feed class and extend the "BaseFeed" class.

