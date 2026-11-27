import os
import subprocess
from pathlib import Path

host = os.environ["SERVER_HOST"]
user = os.environ["SERVER_USER"]
private_key = os.environ["SERVER_SSH_KEY"]
port = os.environ.get("SERVER_PORT", "").strip() or "22"
# Optional: output of `ssh-keyscan <host>` stored as a secret, to pin the host key.
pinned_known_hosts = os.environ.get("SERVER_KNOWN_HOSTS", "").strip()

ssh_dir = Path.home() / ".ssh"
ssh_dir.mkdir(mode=0o700, exist_ok=True)

key_file = ssh_dir / "id_ed2551"
# OpenSSH requires the private key to end with a newline.
key_file.write_text(private_key.strip() + "\n")
key_file.chmod(0o600)

known_hosts = ssh_dir / "known_hosts"
if pinned_known_hosts:
    known_hosts.write_text(pinned_known_hosts + "\n")
else:
    # Fallback: trust the host key presented right now (trust-on-first-use).
    scan = subprocess.run(
        ["ssh-keyscan", "-H", "-T", "10", "-p", port, host],
        check=True,
        capture_output=True,
        text=True,
    )
    if not scan.stdout.strip():
        raise SystemExit(f"ssh-keyscan returned no host keys for {host}")
    known_hosts.write_text(scan.stdout)
known_hosts.chmod(0o600)

ssh_command = [
    "ssh",
    "-T",
    "-p", port,
    "-i", str(key_file),
    "-o", "IdentitiesOnly=yes",
    "-o", "StrictHostKeyChecking=yes",
    "-o", f"UserKnownHostsFile={known_hosts}",
    f"{user}@{host}",
]

subprocess.run(ssh_command, check=True)
