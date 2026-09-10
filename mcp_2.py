from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-practise-2")

user_details = {
    1: {
        "id": 1,
        "name": "Malhar",
        "email": "malhar@example.com",
        "active": True,
    },
    2: {
        "id": 2,
        "name": "John",
        "email": "john@example.com",
        "active": False,
    },
}

@mcp.tool()
def get_user(user_id: int) -> dict:
    """Fetch user details from user id"""
    return user_details.get(user_id, "None")

if __name__ == "__main__":
    mcp.run()