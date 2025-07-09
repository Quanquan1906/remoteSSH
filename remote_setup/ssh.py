from IPython import get_ipython

def start_ssh(id_rsa_pub="", password="", install_ssh=False, config_ssh=False):
    print(f'{"*" * 10} SETUP SSH SERVICE {"*"*10}')

    if install_ssh:
        get_ipython().system('apt-get install ssh -y > /dev/null')

    if id_rsa_pub:
        get_ipython().system('mkdir -p ~/.ssh')
        get_ipython().system(f'echo {id_rsa_pub} > ~/.ssh/authorized_keys')

    if config_ssh:
        cfgs = [
            "Port 22", "PasswordAuthentication yes",
            "ListenAddress 0.0.0.0", "PermitRootLogin yes",
            "PubkeyAuthentication yes", "AllowAgentForwarding yes",
            "AllowTcpForwarding yes", "PermitTTY yes", "GatewayPorts yes"
        ]
        for line in cfgs:
            key = line.split()[0]
            get_ipython().system(f"sed -i 's/^#*{key}.*/{line}/' /etc/ssh/sshd_config")

    if password:
        get_ipython().system(f'echo -e "{password}\n{password}" | passwd root > /dev/null')

    get_ipython().system('service ssh restart')

    get_ipython().system('grep -qx "^PS1=.*$" ~/.bashrc || echo "PS1=" >> ~/.bashrc')
    get_ipython().system('echo "TERM=xterm-256color" >> ~/.bashrc')
    
    print(f'{"-" * 10} Finished {"-"*10}')
