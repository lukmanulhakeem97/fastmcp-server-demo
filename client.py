import asyncio
from fastmcp import Client, FastMCP
from fastmcp.client import StreamableHttpTransport

async def main():
    #transport = StreamableHttpTransport("https://philosophical-crawdad.fastmcp.app/mcp")
    transport = StreamableHttpTransport("http://127.0.0.1:8000/mcp")
    async with Client(transport=transport, timeout=10.0) as client:
        print(f"Connected: {client.is_connected()}")
        # Basic server interaction
        if await client.ping():
            print("Server is reachable.")
        else:
            print("Server is not reachable or did not respond to ping.")
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        print("-------Available tools are------")
        for tool in tools:
            print(f"Tool: {tool.name}")
            #print(f"Description: {tool.description}")

        print("-------Available resources are------")
        for resource in resources:
            #print(f"Resource URI: {resource.uri}")
            print(f"Name: {resource.name}")
            #print(f"Description: {resource.description}")

        print("-------Available prompts are------")
        for prompt in prompts:
            print(f"Prompt: {prompt.name}")
            #print(f"Description: {prompt.description}")

        print("---Tool action----")
        result = await client.call_tool("add", {"a": 5, "b": 3}, timeout=20)
        print(result.data)

    print(f"Connected: {client.is_connected()}")

asyncio.run(main())