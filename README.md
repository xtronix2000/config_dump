# config_dump
A simple tool for collecting network device configurations

## Installation

1. Clone this repo

    `git clone https://github.com/xtronix2000/config_dump.git`

2. Navigate to the directory

    `cd config_dump`

3. Create a virtual environment for this project

    `python3 -m venv venv`

4. Load the virtual environment

    `source venv/bin/activate`
  
5. Run `pip install -r requirements.txt`

6. Open the `commands.json` file and add a new dictionary element with the device vendor string as the key and command as the value.

7.Open the `devices.json` file and enter the device information in the format `"ip_address": ["type", "login", "password"]`. Pay attention to the `"type"` field, it must be at least one key from the `commands.json` file.

7. Run the main.py script

    `python3 main.py`
8. The result of the program execution will appear in the folder `results/config_dump_YYYY-MM-DD_HH.MM.SS/host address`

P.S. https://github.com/paramiko/paramiko
