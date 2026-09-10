import httpx
import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 9")

async def get_post(post_id: int) -> dict:
    """Fetch post from the jsonplaceholder by post_id."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch post: {response.status_code}")
    return response.json()

@mcp.tool()
async def get_concurrect_post(post_ids: list[int]) -> list[dict]:
    tasks = [get_post(post_id) for post_id in post_ids]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    processed_results = []
    for result in results:
        if isinstance(result, Exception):
            processed_results.append({
                "success": False,
                "error": str(result)
            }) 
        else:
            processed_results.append({
                "success": True,
                "data": result
            })
    return processed_results

if __name__ == "__main__":
    mcp.run()