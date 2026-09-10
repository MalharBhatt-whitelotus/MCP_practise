from mcp.server.fastmcp import FastMCP

mcp = FastMCP("practise mcp 3")

@mcp.resource("info://application")
def application_info() -> str:
    """Return information about this application"""
    return """
    Application: MCP Practice Server
    Version: 1.0.0
    Environment: Development
    Author: Malhar
    """

@mcp.resource("info://server")
def server_info() -> str:
    """Return information about mcp server"""
    return """
    Server: mcp-practise-2
    Protocol: MCP
    Transport: STDIO
    Status: Running
    """

@mcp.resource("info://database")
def database_info() -> str:
    """Return information about database"""
    return """
Database: MCP_server
Database_type: Local
URL: local:8080
"""

@mcp.resource("info://environment")
def environment_info() -> str:
    """Return information about environment"""
    return """
Env: .env
Access: local
URL: local:8080/env
"""

@mcp.resource("info://company")
def company_info() -> str:
    """Return information about Company"""
    return """
Company name: MB
Company type: international
Company assets: 4.5
"""

if __name__ == "__main__":
    mcp.run()