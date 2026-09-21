import argparse
import sys
from .scanner import MCPClient
from .checks import run_all_checks
from .report import print_report, save_json_report
from . import __version__

def main():
    parser = argparse.ArgumentParser(prog="tryagent", description="TryAgent - MCP / AI agent security scanner")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="Scan an MCP server")
    scan.add_argument("--url", required=True, help="Base URL, e.g. http://localhost:8000")
    scan.add_argument("--api-key", help="Bearer token (optional)")
    scan.add_argument("--json", help="Save JSON report to this path")
    args = parser.parse_args()

    if args.command == "scan":
        client = MCPClient(args.url, args.api_key)
        try:
            tools = client.list_tools()
        except Exception as e:
            print(f"[!] Error connecting: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"[+] Retrieved {len(tools)} tool(s) from {args.url}")
        findings = run_all_checks(tools, args.api_key)
        print_report(findings)
        if args.json:
            save_json_report(findings, args.json)
            print(f"[+] JSON report saved to {args.json}")

if __name__ == "__main__":
    main()
