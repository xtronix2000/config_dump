import os
import json
import paramiko
from datetime import datetime


def get_config(host, login, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=22, username=login, password=password, timeout=3)
    (stdin, stdout, stderr) = client.exec_command(command)
    config = stdout.read().strip().decode('ASCII')
    client.close()
    return config


with open('commands.json', 'r') as f1, open('devices.json', 'r') as f2:
    commands = json.load(f1)
    devices = json.load(f2)


curr_date = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
os.makedirs(f'results/config_dump_{curr_date}', 0o774)

for k, v in devices.items():
    try:
        tmp = get_config(k, v[0], v[1], commands[v[2]]).strip().replace('\n', '')
    except paramiko.SSHException as e:
        tmp = str(e)
    with open(f'results/config_dump_{curr_date}/{k}.txt', 'w') as f:
        f.write(tmp)
