import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 7")


@mcp.tool()
async def get_post(post_id: int) -> dict:
    """Asynchronously fetch the post by post if from the placeholde."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise ValueError(f"Failed to fetch post: {response.status_code}")

        return response.json()


if __name__ == "__main__":
    mcp.run()