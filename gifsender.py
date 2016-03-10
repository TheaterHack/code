import requests

def gif(animal):
	endpoint = "http://api.giphy.com/v1/gifs/search"
	payload = {"q": animal, "limit":1, "api_key": "dc6zaTOxFJmzC"}
	response = requests.get(endpoint, params=payload)
	data=response.json()
	link=data['data'][0]['images']['fixed_width']['url']
	print link

	return u"{}".format(link)
