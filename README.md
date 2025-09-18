# FastMCP Server Demo

This is a simple FastMCP client-server implemenation demo. Server can be also hosted in any remote server. [FastMCP Cloud](https://fastmcp.cloud/) provide free, fast and easy server deployemnt service.

## Set up
Pre-requisites are `python<=3.13` and `uv` package manger, instructions to set up can be found [here](https://docs.astral.sh/uv/getting-started/).
1. **Clone this repository**
   
   Either by download as zip option or by `git clone https://github.com/lukmanulhakeem97/fastmcp-server-demo.git` command in CLI tool.
2. **Create an python environment and install dependencies**

   create environment: `uv venv [name]`, name is optional.
   
   install dependency given in `pyproject.toml` file: `uv sync`.
3. Activate `venv` by `.\.venv\Scripts\activate`

## Run the MCP Server
Run mcp server in a teminal. FastMCP `server.py` can be run,
- either locally at `127.0.0.1` local host by `uv run server.py` or,
- at any remote server. Can set up server at [FastMCP Cloud](https://fastmcp.cloud/) using intruction given it their [website](https://gofastmcp.com/deployment/fastmcp-cloud).





