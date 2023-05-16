import os
import json
import paramiko
from datetime import datetime


def get_config(host, login, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username=login, password=password, timeout=3)
    config = []
    for comm in command:
        (stdin, stdout, stderr) = ssh.exec_command(comm)
        config.append(stdout.read().strip().decode('ASCII'))
        ssh.close()
    return config


with open('commands.json', 'r') as f:
    commands = json.load(f)


file_reader = open('devices', 'r')
lines = file_reader.readlines()
device_info = [line.split(';') for line in lines]
file_reader.close()


print(*device_info)
curr_date = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
os.makedirs(f'results/config_dump_{curr_date}', 0o774)
