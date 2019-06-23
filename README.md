# flask-admin-interface
This is a simple interface panel created by means of Flask Framework and Bootstrap 4.
The goal of this project is providing an administrative panel for FlatBox microclimate system.
 
**To use this project you need to install:**
1. python 3.7;
2. MySQL 5.5+.

All All libs listed in requirements.txt file.

You also need to create config directory ( put here config json). config.json structure:

`{
  "database": {
    "host": "",
    "user": "",
    "password": "",
    "database": "",
    "port": 
  },
  "secret_key": ""
}`