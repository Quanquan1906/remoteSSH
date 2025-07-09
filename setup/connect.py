from kaggle_secrets import UserSecretsClient
from .ssh import start_ssh
from .ngrok import start_ngrok

def connect_vscode(cfg={}):
    user_secrets = UserSecretsClient()
    kaggle_cfg = {}
    for name in ['NGROK_TOKEN_1', 'ID_RSA_PUB', 'SSH_PASS']:
        try:
            kaggle_cfg[name] = user_secrets.get_secret(name)
        except:
            pass
    kaggle_cfg.update(cfg)

    start_ssh(
        id_rsa_pub=kaggle_cfg.get("ID_RSA_PUB", ""),
        install_ssh=True,
        config_ssh=True,
        password=kaggle_cfg.get("SSH_PASS", "12345")
    )

    start_ngrok([kaggle_cfg.get("NGROK_TOKEN_1", "")])

def clone_project_from_github(giturl, folder, branch="main"):
    from IPython import get_ipython
    get_ipython().system(f"git clone --branch {branch} {giturl} {folder}")
