import httpx
import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 8")

async def get_post(post_id: int) -> dict:
    """Fetch single post from json placeholder asynchronously."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch the post: {response.status_code}")

    return response.json()

@mcp.tool()
async def get_concurrent_posts(post_ids: list[int]) -> list[dict]:
    tasks = [get_post(post_id) for post_id in post_ids]
    result = await asyncio.gather(*tasks)
    return result


if __name__ == "__main__":
    mcp.run()