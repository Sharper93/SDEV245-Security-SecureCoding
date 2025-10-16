import re

# Common regex patterns for secrets
# This dictionary maps a descriptive name to a compiled regex pattern.

PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "AWS Secret Key": re.compile(r"(?i)aws_secret_access_key\s*=\s*[A-Za-z0-9/+=]{40}"),
    "Generic API Key": re.compile(r"(?i)(api[-_]?key\s*[:=]\s*[\'\"]?[A-Za-z0-9_\-]{16,45}[\'\"]?)"),
    "Bearer Token": re.compile(r"(?i)bearer\s+[A-Za-z0-9\-\._~\+\/]+=*"),
    "Private Key": re.compile(r"-----BEGIN (?:RSA|DSA|EC|PGP|OPENSSH)? ?PRIVATE KEY-----"),
    "Password": re.compile(r"(?i)(password\s*[:=]\s*[\'\"]?.+[\'\"]?)"),
}