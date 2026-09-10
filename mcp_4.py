from mcp.server.fastmcp import FastMCP

mcp = FastMCP("practise match 4")

@mcp.prompt()
def explain_code(code: str) -> str:
    """Create a prompt for explaining Python code."""
    return f"""
    Explain the following Python code step by step.

    Code:
    {code}

    Please explain:
    1. What the code does
    2. How it works
    3. Important Python concepts used
    4. Any potential problems or improvements
    """

@mcp.prompt()
def review_code(code: str) -> str:
    """ Create a prompt for reviewing Python code."""
    return f"""
    Review the following Python code.

    Code:
    {code}

    Check for:
    1. Bugs
    2. Code quality
    3. Error handling
    4. Type hints
    5. Performance
    6. Security issues
    7. Possible improvements

    Provide practical recommendations.
    """

@mcp.prompt()
def generate_docstring(code: str) -> str:
    """Generate a docsting for Python code."""
    return f"""
    Generate a clear Python docstring for this function.

    Include:
    - Description
    - Parameters
    - Return value
    - Possible exceptions
    - Example usage

    Code:
    {code}
    """

if __name__ == "__main__":
    mcp.run()