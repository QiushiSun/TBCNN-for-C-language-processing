"""Constants for the algorithm scraper."""

import os

CRAWLER_DIR = 'code2ast'

# Where to store the cached HTTP requests
CACHE_DIR = os.path.join(CRAWLER_DIR, 'codesource', 'cache')
# File for storing cached HTTP requests
REQUESTS_CACHE = os.path.join(CACHE_DIR, 'requests')
