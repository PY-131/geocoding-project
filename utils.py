import requests as rqs
import os 

def get_coordinates(address, URL, PRIVATE_TOKEN):
    """
    Queries Location API and get's coordinates
    """

    data = {
      'key': PRIVATE_TOKEN,
      'q': address,
      'format': 'json'
      }
    try:
       response = rqs.get(URL, params=data)
    except Exception as e:
       raise e

    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']

    return lat, lon


def get_iss_location(ISS_URL, endpoint="iss-now.json"):
    
    res = {}
    response = __run_request(ISS_URL, endpoint)

    if response['message'] == 'success':
      iss_pos = response['iss_position']
      res['lat'] = iss_pos['latitude']
      res['lon'] = iss_pos['longitude']
      # possibly reverse geocode for address
      #res['location']
    else:
      res['location'] = 'over water'
    return res 

def get_iss_people(ISS_URL, endpoint="astros.json"): 

    people = []
    response = __run_request(ISS_URL, endpoint) 

    if response['message'] == 'success': 
      people = [person["name"] for person in response["people"]] 
    
    return people



def __run_request(url, endpoint):

    URL = os.path.join(url, endpoint)

    res = {}
    try:
       response = rqs.get(URL).json()

    except Exception as e:
       raise e

    return response




