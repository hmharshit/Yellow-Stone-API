import requests


def get_station(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?&key=AIzaSyA4nYjRo6Pye_jaYqZufE6xx473MzK-HqY"
    params = {'query':query}
    r = requests.get(url, params=params)
    response = r.json()
    # results = {'results':response['results']}
    # return results
    return response['results'][0]['formatted_address']
    # return response['results'][0]['name']

print(get_station('new delhi railway station'))