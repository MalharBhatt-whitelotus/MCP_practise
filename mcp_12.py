import httpx
import asyncio
from random import randint
from httpx import AsyncClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 12")

async def get_post(
        client: AsyncClient, 
        post_id: int, 
        attempts: int = 1, 
        delay: int = 0,
) -> dict:
    
    random_trigger = randint(1,2)

    url = (
        "https://httpbin.org/delay/2" 
        if random_trigger == 2 
        else f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    try:
        await asyncio.sleep(delay)

        response = await client.get(url)

        if response.status_code != 200:
            raise httpx.HTTPStatusError(
                f"HTTP error: {response.status_code}",
                request=response.request,
                response=response,
            )

        return response.json()
    
    except Exception as exc:

        if attempts < 3:
            retry_delay = 1

            print(f"Post {post_id} failed on attempt {attempts}: {exc}")
            print(f"Retrying in {retry_delay} seconds...")
            
            return await get_post(client, post_id, attempts + 1, retry_delay)
        
        return {
            "success": False,
            "error": f"Failed to fetch post {post_id}: {str(exc)}",
        }

@mcp.tool()
async def get_concurrent_posts(post_ids: list[int]) -> list[dict]:

    async with httpx.AsyncClient(timeout=1.0) as client:

        tasks = [get_post(client, post_id) for post_id in post_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    return results

if __name__ == "__main__":
    mcp.run()