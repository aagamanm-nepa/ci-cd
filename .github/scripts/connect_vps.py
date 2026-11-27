import os
import subprocess
from pathlib import Path

host = os.environ["SERVER_HOST"]
user = os.environ["SERVER_USER"]
private_key = os.environ["SERVER_SSH_KEY"]

ssh_dir = Path.home() / ".ssh"
ssh_dir.mkdir(mode=0o700, exist_ok=True)
key_file = ssh_dir / "id_ed2551"
key_file.write_text(private_key)
key_file.chmod(0o600)

ssh_command = [
    "ssh",
    "-i", str(key_file),
    f"{user}@{host}",
]

subprocess.run(ssh_command, check=True)