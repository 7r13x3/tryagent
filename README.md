# TryAgent 🕵️
> Break AI agents before attackers do.

TryAgent is a lightweight security scanner for **MCP (Model Context Protocol)** servers and AI agents.
It connects to an MCP server, enumerates tools, and flags dangerous capabilities such as shell execution, file access, network calls, credential handling, and overly broad permissions.

## Features
- Connect to MCP servers (HTTP JSON-RPC)
- Detect tool poisoning via keyword analysis
- Detect missing authentication
- Detect overly broad permissions (`*`, `all`)
- Console + JSON reporting
- Built-in vulnerable mock server for safe local testing

## Legal
For **authorized testing and education only**. Do not scan systems you do not own or have written permission to test.

## Install
```bash
pip install -r requirements.txt
Usage
You need two terminals to run this.

Terminal 1 — Start the mock vulnerable server:
python -m tryagent.mock_server
Terminal 2 — Scan it:
python -m tryagent.cli scan --url http://localhost:8000
Save JSON report:
python -m tryagent.cli scan --url http://localhost:8000 --json report.json
Run tests
pytest -v
