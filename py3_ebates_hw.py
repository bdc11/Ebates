import requests, json

more = True 
i = 1 # initialize at page 1
hd_true = 0
hd_false = 0

while (more == True):
	print(i) 
	new_url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=100&page=' + str(i) #changed per_page to 100 for faster page increment 
	ebates = requests.get(new_url, headers={'User-Agent': 'Mozilla/5.0'}) #connect to ebates server
	result = json.loads(ebates.content) #parse JSON object into an python object with attributes corresponding to dict keys
	more = result['more'] #check if more = true then continue
	for keys in result['response']: #loop iterates keys in response dictionary
		flags = keys['flags'] #finds flag key values where hd is nested
		hd = flags['hd'] #checks hd key value 
		if hd == True: #loop checks if hd value is true 
			hd_true += 1 
		else:
			hd_false += 1 

	i += 1 # it will increment i and modify url page number 


print('The number of hd keys true: %s' %hd_true) 
print('The number of hd keys false: %s' %hd_false)
print(new_url)
