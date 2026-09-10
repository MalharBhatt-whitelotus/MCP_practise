import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(("MCP Practise 6"))


# =========================
# MCP TOOLS
# =========================
@mcp.tool()
def get_post(post_id: int) -> dict:
    """Fetch a post from external JSONPlaceholder API."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = httpx.get(url)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch post: {response.status_code}")
    
    return response.json()

if __name__ == "__main__":
    mcp.run()