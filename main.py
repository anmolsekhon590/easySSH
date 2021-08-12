import json
import os

f = open('C:\ssh\server.config',)
data = json.load(f)

os.system("ssh " + data['hostname'] + "@" + data['ip'])
