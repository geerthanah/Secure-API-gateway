import redis.asyncio as redis
from fastapi import HTTPException
from datetime import datetime

r = redis.from_url("redis://redis:6379")

RATE_LIMIT = 100
WINDOW_SIZE = 60

async def rate_limiter(api_key: str):
    now = int(datetime.utcnow().timestamp())
    key = f"ratelimit:{api_key}:{now // WINDOW_SIZE}"
    count = await r.incr(key)
    if count == 1:
        await r.expire(key, WINDOW_SIZE)
    if count > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
