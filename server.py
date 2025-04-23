# server.py
from mcp.server.fastmcp import FastMCP
from PIL import Image as PILImage, ImageDraw
# Create an MCP server
mcp = FastMCP("StableDiffusionMCP")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# @mcp.tool()
# def generate_image(text: str = "MCP!") -> PILImage:
#     """產生一張帶有文字的圖片"""

#     img = PILImage.new("RGB", (256, 256), color=(255, 255, 255))
#     d = ImageDraw.Draw(img)
#     d.text((10, 100), text, fill=(0, 0, 0))

#     return img

@mcp.tool()
def generate_image(text: str = "MCP!") -> Image:
    """產生一張帶有文字的圖片，並以 MCP Image 格式回傳"""

    img = PILImage.new("RGB", (256, 256), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10, 100), text, fill=(0, 0, 0))
    img.show()
    return img  # ✅ 回傳 MCP-compatible 的格式
