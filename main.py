from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool : Add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

# Tool : Generate a random number
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    return random.randint(min_val, max_val)

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    info = {
        "name": "Simple Calculator",
        "version" : "1.0.0",
        "description" : "A basic MCP server with the math tool",
        "tools": ["add", "random_number"],
        "author": "Rahul"
    }
    return json.dumps(info, indent=2)

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)