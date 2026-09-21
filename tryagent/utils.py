import re

SUSPICIOUS_PATTERNS = [
    r"shell", r"exec", r"eval", r"system", r"cmd", r"command",
    r"file", r"read", r"write", r"delete", r"upload", r"download",
    r"http", r"https", r"curl", r"wget", r"fetch", r"request",
    r"base64", r"decode", r"encode", r"obfuscate",
    r"token", r"secret", r"password", r"key", r"credential",
    r"sql", r"query", r"database",
    r"email", r"sms", r"slack", r"discord", r"webhook",
    r"admin", r"root", r"sudo",
]

def is_suspicious(text: str) -> bool:
    if not text:
        return False
    text = text.lower()
    return any(re.search(p, text) for p in SUSPICIOUS_PATTERNS)

def matched_keywords(text: str) -> list:
    if not text:
        return []
    text = text.lower()
    return [p for p in SUSPICIOUS_PATTERNS if re.search(p, text)]
