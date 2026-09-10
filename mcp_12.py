import httpx
import asyncio
from random import randint
from httpx import AsyncClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 12")


async def get_post(client: AsyncClient, post_id: int) -> dict:
    """Fetch a post with retry and exponential backoff."""

    timeout_trigger = randint(1, 2)
    if timeout_trigger == 1:
        url = "https://httpbin.org/delay/10"
    else:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Post {post_id}: attempt {attempt}")
            response = await client.get(url)
            if response.status_code != 200:
                raise ValueError(
                    f"Failed to fetch post {post_id}: "
                    f"{response.status_code}"
                )
            return response.json()
        except (httpx.TimeoutException, httpx.RequestError) as error:
            print(
                f"Post {post_id}: attempt {attempt} failed: {error}"
            )
            if attempt == max_attempts:
                raise
            delay = 2 ** (attempt - 1)
            print(
                f"Post {post_id}: retrying in {delay} seconds..."
            )
            await asyncio.sleep(delay)

@mcp.tool()
async def get_concurrent_posts(post_ids: list[int]) -> list[dict]:
    """Fetch multiple posts concurrently with retry handling."""

    timeout = httpx.Timeout(2.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [
            get_post(client, post_id)
            for post_id in post_ids
        ]
        results = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )
    processed_tasks = []
    for result in results:
        if isinstance(result, Exception):
            processed_tasks.append({
                "success": False,
                "error": str(result),
            })
        else:
            processed_tasks.append({
                "success": True,
                "data": result,
            })
    return processed_tasks

if __name__ == "__main__":
    mcp.run()