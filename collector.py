#u9QEe02oYi9WonmL2dcufjr6dykCG8dt9maS89Qk

import requests
import json

headers = {
	"X-API-Key" : "u9QEe02oYi9WonmL2dcufjr6dykCG8dt9maS89Qk"
}

for i in range(80,81):
	# Make a get request 
	response = requests.get("https://api.propublica.org/congress/v1/" + str (i) + "/senate/votes/party.json", headers = headers)

	print(response.status_code) 

	if (response.status_code == 200):
		data = response.json()
		with open('congress' + str(i) + '.json', 'w') as outfile:
		    json.dump(data, outfile)

