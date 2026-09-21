import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

console = Console()

def print_report(findings: List[Dict]):
    if not findings:
        console.print("[green]No issues found.[/green]")
        return
    table = Table(title="TryAgent Findings")
    table.add_column("Severity", style="bold")
    table.add_column("Type")
    table.add_column("Tool")
    table.add_column("Message")
    for f in findings:
        sev = f.get("severity", "info")
        color = {"high": "red", "medium": "yellow", "low": "blue"}.get(sev, "white")
        table.add_row(f"[{color}]{sev}[/{color}]", f.get("type", ""), f.get("tool", "-"), f.get("message", ""))
    console.print(table)

def save_json_report(findings: List[Dict], path: str):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(findings, fh, indent=2)
