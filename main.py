import paramiko
import os
from datetime import datetime

device_info = []  # device info list
device_list = ['cisco', 'huawei', 'paloalto']
cisco = ['show run']
huawei = ['display current-configuration']
paloalto = ['configure']

commands = {'cisco': 'show running configutation',
            'huawei': 'display current configuration',
            'paloalto': 'configure'
            }


def ssh_audit(_host, _login, _password, _commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(_host, port=22, username=_login,
                password=_password, timeout=3)
    data_ssh = []
    for k in _commands:
        (stdin, stdout, stderr) = ssh.exec_command(k)
        data_ssh.append(stdout.read().strip().decode('ASCII'))
    ssh.close()
    return data_ssh


curr_date = str(datetime.now())[:19].replace(' ', '_').replace(':', '.')

# getting information about devices
file_reader = open('C:/Users/AinurK/Desktop/devices.txt', 'r')
while True:
    line = file_reader.readline()
    if not line:
        break
    device_info.append(line.split(','))
file_reader.close()

for i in device_info[1:]:  # remove '\n' from last list element in a row
    i[3] = i[3].strip()

#  creating a current folder
os.makedirs(f'C:/Users/AinurK/Desktop/config_dump_{curr_date}', 0o774)

#  dump configs
for i in device_info[1:]:
    if i[0] in device_list:
        # if i[0] == 'huawei':
        #    command = huawei
        # if i[0] == 'cisco':
        #    command = cisco
        command = locals()[i[0]]
        try:
            tmp = ssh_audit(i[1], i[2], i[3], command)
        except paramiko.SSHException as e:  # ConnectionRefusedError
            tmp = str(e)
    else:
        #  print('Unsupported device')
        #  sys.exit(0)
        tmp = f'Unsupported decice {i[0]}'
    with open(f'C:/Users/AinurK/Desktop/config_dump_{curr_date}/{i[1]}.txt', 'w') as file_writer:
        for j in tmp:
            file_writer.write(j)
