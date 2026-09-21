from tryagent.checks import check_tool_poisoning, check_unauthenticated, check_broad_permissions, check_dangerous_inputs

def test_tool_poisoning():
    tools = [{"name": "safe_tool", "description": "Does nothing"}, {"name": "run_shell", "description": "Execute arbitrary shell commands"}]
    findings = check_tool_poisoning(tools)
    assert any(f["tool"] == "run_shell" for f in findings)

def test_unauthenticated():
    findings = check_unauthenticated(None)
    assert len(findings) == 1
    assert findings[0]["type"] == "unauthenticated_access"

def test_broad_permissions():
    tools = [{"name": "admin_tool", "permissions": ["*"]}, {"name": "limited_tool", "permissions": ["read"]}]
    findings = check_broad_permissions(tools)
    assert len(findings) == 1

def test_dangerous_inputs():
    tools = [{"name": "read_file", "inputSchema": {"type": "object", "properties": {"path": {"type": "string", "description": "File path to read"}}}}]
    findings = check_dangerous_inputs(tools)
    assert len(findings) == 1
