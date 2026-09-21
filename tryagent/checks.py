from typing import Dict, List
from .utils import matched_keywords

def check_tool_poisoning(tools: List[Dict]) -> List[Dict]:
    findings = []
    for tool in tools:
        name = tool.get("name", "")
        desc = tool.get("description", "")
        hits = matched_keywords(name) + matched_keywords(desc)
        if hits:
            findings.append({
                "type": "tool_poisoning", "severity": "medium", "tool": name,
                "message": f"Tool '{name}' has suspicious keywords: {sorted(set(hits))}",
            })
    return findings

def check_unauthenticated(api_key: str = None) -> List[Dict]:
    if not api_key:
        return [{
            "type": "unauthenticated_access", "severity": "high", "tool": "-",
            "message": "No API key provided. Server may allow unauthenticated access.",
        }]
    return []

def check_broad_permissions(tools: List[Dict]) -> List[Dict]:
    findings = []
    for tool in tools:
        perms = tool.get("permissions", []) or []
        if "*" in perms or "all" in perms:
            findings.append({
                "type": "broad_permissions", "severity": "high", "tool": tool.get("name", "-"),
                "message": f"Tool '{tool.get('name')}' claims broad permissions: {perms}",
            })
    return findings

def check_dangerous_inputs(tools: List[Dict]) -> List[Dict]:
    findings = []
    for tool in tools:
        schema = tool.get("inputSchema", {}) or {}
        props = schema.get("properties", {}) or {}
        for prop_name, prop in props.items():
            desc = (prop.get("description") or "").lower()
            if any(k in desc for k in ["command", "shell", "path", "url", "file", "query"]):
                findings.append({
                    "type": "dangerous_input", "severity": "medium", "tool": tool.get("name", "-"),
                    "message": f"Tool '{tool.get('name')}' input '{prop_name}' looks dangerous: {desc[:80]}",
                })
    return findings

def run_all_checks(tools: List[Dict], api_key: str = None) -> List[Dict]:
    findings = []
    findings.extend(check_unauthenticated(api_key))
    findings.extend(check_tool_poisoning(tools))
    findings.extend(check_broad_permissions(tools))
    findings.extend(check_dangerous_inputs(tools))
    return findings
