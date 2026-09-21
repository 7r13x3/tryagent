import requests
from typing import Dict, List, Optional

class MCPClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def _rpc(self, method: str, params: Optional[Dict] = None) -> Dict:
        payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
        resp = self.session.post(f"{self.base_url}/rpc", json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"RPC error: {data['error']}")
        return data.get("result", {})

    def list_tools(self) -> List[Dict]:
        return self._rpc("tools/list").get("tools", [])
