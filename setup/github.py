import os
from IPython import get_ipython

def setup_github_config(private_key_path):
    key_name = os.path.basename(private_key_path)
    key_path = f'~/.ssh/{key_name}'
    get_ipython().system("mkdir -p ~/.ssh")
    get_ipython().system(f"cp '{private_key_path}' ~/.ssh/{key_name}")
    get_ipython().system(f"chmod 600 {key_path}")

    ssh_config_path = os.path.expanduser('~/.ssh/config')
    ssh_config_content = f"""
Host github.com
    HostName ssh.github.com
    User git
    Port 443
    StrictHostKeyChecking no
    IdentityFile ~/.ssh/{key_name}
"""
    with open(ssh_config_path, 'w') as f:
        f.write(ssh_config_content)

    print("setup github_config finished")
