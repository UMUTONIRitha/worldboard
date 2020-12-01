import urllib.request,json
from .models import Country

base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['COUNTRY_API_BASE_URL']

def get_countries():
    '''
    Function that gets the json response to our url request
    '''
    get_countries_url = base_url

    with urllib.request.urlopen(get_countries_url) as url:
        get_countries_data = url.read()
        get_countries_response = json.loads(get_countries_data)

        country_results = None
        country_results_list = get_countries_response
        country_results = process_results(country_results_list)


    return country_results

def process_results(country_list):
    '''
    Function  that processes the country result and transform them to a list of Objects

    Args:
        country_list: A list of dictionaries that contain country details

    Returns :
        country_results: A list of country objects
    '''
    country_results = []
    for country_item in country_list:
        name = country_item.get('name')
        capital = country_item.get('capital')
        flag = country_item.get('flag')

        if flag:
            country_object = Country(name,capital,flag)
            country_results.append(country_object)

    return country_results