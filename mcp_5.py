from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp practise 5")

users = {
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

user_id = 3

# =================================
# MCP TOOLS
# =================================
@mcp.tool()
def creat_user(name: str, email: str, active: bool = False) -> dict:
    """Create new User"""
    global user_id
    id = user_id
    if id < 1:
        id = 1
    users[id] = {
        "id": id,
        "name": name,
        "email": email,
        "active": active,
    }
    user_id += 1
    return {
        "success": True,
        "user_details": users.get(id, None),
    }

@mcp.tool()
def get_user(user_id: int) -> dict:
    """Fetch user details from user_id"""
    return users.get(user_id, None)

@mcp.tool()
def delete_user(user_id: int) -> dict:
    """Delete the user by user_id"""
    user_detail = users.pop(user_id) if users.get(user_id, None) is not None else None
    return user_detail if user_detail else None


# =================================
# MCP RESOURCES
# =================================
@mcp.resource("info://application")
def application_info() -> str:
    """Return the information about application."""
    return """
    Application: User Management System
    Version: 1.1.0.10
    URL: https://student_management_system.example
    """

@mcp.resource("info://{user_id}")
def user_info(user_id: int) -> dict:
    """Return the information about the user from user_id"""
    return users.get(user_id) if users.get(user_id, None) is not None else None


# =================================
# MCP RESOURCES
# =================================
@mcp.prompt()
def generate_user_report(user_id: int) -> str:
    """Generate the user report prompt/template."""
    return f"""
    Generate a detailed report about user ID 1.

    The report should include:

    1. User identity
    2. Email
    3. Account status
    4. Observations
    5. Recommendations

    User ID: {user_id}
    User Details: {users.get(user_id)}
    """ if users.get(user_id, None) is not None else None


if __name__ == "__main__":
    mcp.run()