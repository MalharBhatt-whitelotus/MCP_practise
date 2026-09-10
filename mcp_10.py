import httpx
import asyncio
from httpx import AsyncClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 10")

async def get_post(client: AsyncClient, post_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = await client.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch post: {response.status_code}")
    return response.json()


@mcp.tool()
async def get_concurrent_posts(post_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [get_post(client, post_id) for post_id in post_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    processed_result = []
    for result in results:
        if isinstance(result, Exception):
                processed_result.append({
                "success": False,
                "error": str(result),
            })
        else:
            processed_result.append({
                "success": True,
                "data": result
            })
    return processed_result


if __name__ == "__main__":
    mcp.run()