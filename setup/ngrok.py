from IPython import get_ipython

def start_ngrok(ngrok_tokens=[], ngrok_binds=None):
    if ngrok_binds is None:
        ngrok_binds = {
            'ssh': {'port': 22, 'type': 'tcp'},
            'vscode': {'port': 9000, 'type': 'http'}
        }

    try:
        from pyngrok import ngrok, conf
    except:
        get_ipython().system('pip install -qq pyngrok')
        from pyngrok import ngrok, conf

    get_ipython().system('kill -9 "$(pgrep ngrok)" || true')
    
    print(f'{"*" * 10} SETUP NGROK {"*"*10}')
    ngrok_info = {}
    for token in ngrok_tokens:
        for region in ["us", "en", "au", "vn"]:
            try:
                conf.get_default().region = region
                ngrok.set_auth_token(token)
                for name, cfg in ngrok_binds.items():
                    ngrok_info[name] = ngrok.connect(cfg['port'], cfg['type'])
                print("> Registry success!")
                for key in ngrok_info:
                    print(f"{key}: {ngrok_info[key]}")
                return
            except Exception as e:
                print(e)
    print(f'{"-" * 10} Finished {"-"*10}')
