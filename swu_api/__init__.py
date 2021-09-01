import requests, bs4

stops_url = "https://echtzeit.swu.de/haltestelle/abfahrtsmonitor"
departure_url = "https://echtzeit.swu.de/api/TDI/StopPassage?StopNumber={stop_id}&View=DepartureMonitor&Count={count}"

stops = {}
shortcuts = {"hbf": 1008}

get_stop_name = stops.get

def get_stop_id(search_str):
    # make sure that we get a string
    if not type(search_str) == str:
        raise TypeError("please provide a string")
    
    stop_id = None
    search_str = search_str.lower()
    
    # check if the search term is listed as a shortcut like 'hbf'
    if search_str in shortcuts:
        return shortcuts[search_str]
    
    # check if the stop can be found by comapring the exact string
    for s_id, s_name in stops.items():
        if search_str == s_name.lower():
            stop_id = s_id
            break
    
    # check if the search term is a part of a station name
    if not stop_id:
        for s_id, s_name in stops.items():
            if search_str in s_name.lower():
                stop_id = s_id
                break
        
    if not stop_id:
        raise ValueError("stop not found")
    else:
        return stop_id
    
def get_departures(stop_id, count = 15, ignore_local_stop_list = False):
    # make sure that we get an integer
    if not type(stop_id) == int:
        try:
            stop_id = int(stop_id)
        except:
            raise ValueError("please provide an integer")
    
    # withe the defaults, we first check wether the stop is in our local list of stops
    if not ignore_local_stop_list:
        if not stop_id in stops:
            raise ValueError("stop not found in local stop list")
        
    # try to handle some api states
    response = requests.get(departure_url.format(stop_id=stop_id, count=count)).json()["StopPassage"]
    if response["State"] == "ok":
        return response["Data"]["Passage"]
    elif response["State"] == "No data":
        return []
    else:
        raise ValueError("unknown api state: {}".format(response["State"]))
    
def update_stop_list():
    # there seems to be no api for searching stops, so we will just donwload a list with all of them
    raw_html = requests.get(stops_url).content
    soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    stops_html = None
    
    # find the <datalist> conaing the stops
    for x in soup.find_all("datalist"):
        if x.has_attr("id"):
            if x.attrs["id"] == "Haltestellenliste":
                stops_html = x
    if not stops_html:
        raise ValueError("could not retrive stop list")
    
    # convert the <datalist> to a python dict
    for x in stops_html.find_all("option"):
        stop_id = int(x.attrs["value"].split(" - ")[0])
        stop_name = x.attrs["value"].split(" - ")[1]
        stops[stop_id] = stop_name

# update the station list when this file is imported, it is needed for other functions             
update_stop_list()
