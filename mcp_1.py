from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Practise Server 1")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def reverse(text: str) -> str:
    """Reverse the text"""
    return text[::-1]

@mcp.tool()
def calculate(a: int, b: int, operation: str) -> int:
    """Calculate basic arthimatic operations"""
    operations = {
        "+": a + b,
        "-": a - b if a > b else b - a,
        "*": a * b,
        "/": a / b if b != 0 else 0,
    }
    return operations.get(operation, 0)

@mcp.tool()
def greet(name: str, greetings = "Hello", puncuation = "!") -> str:
    """Greetings method with default greetings to Good Morning."""
    return f"{greetings}, {name} {puncuation}"

if __name__ == "__main__":
    mcp.run()