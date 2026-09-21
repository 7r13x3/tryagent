from flask import Flask, request, jsonify
app = Flask(__name__)

TOOLS = [
    {"name": "echo", "description": "Echo back the input.", "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}}, "permissions": ["read"]},
    {"name": "run_shell", "description": "Execute arbitrary shell commands.", "inputSchema": {"type": "object", "properties": {"command": {"type": "string", "description": "The shell command"}}}, "permissions": ["*"]},
    {"name": "read_file", "description": "Read any file.", "inputSchema": {"type": "object", "properties": {"path": {"type": "string", "description": "Path or URL"}}}, "permissions": ["read", "all"]},
    {"name": "send_webhook", "description": "Send data to any URL.", "inputSchema": {"type": "object", "properties": {"url": {"type": "string", "description": "HTTP endpoint"}, "token": {"type": "string", "description": "API token"}}}},
]

@app.route("/rpc", methods=["POST"])
def rpc():
    data = request.get_json(force=True)
    method = data.get("method")
    if method == "tools/list":
        return jsonify({"jsonrpc": "2.0", "id": data.get("id"), "result": {"tools": TOOLS}})
    return jsonify({"jsonrpc": "2.0", "id": data.get("id"), "error": {"code": -32601, "message": "Method not found"}})

if __name__ == "__main__":
    print("[!] Mock vulnerable MCP server on http://localhost:8000")
    app.run(host="127.0.0.1", port=8000)
