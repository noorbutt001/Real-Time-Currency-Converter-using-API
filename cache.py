from cachetools import TTLCache

weather_cache = TTLCache(
    maxsize=100,
    ttl=300
)