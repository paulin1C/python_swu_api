from swu_api import *

print("found {} stops".format(len(stops)))

stop_id = get_stop_id("Hauptbahnhof")
print("id for Hauptbahnhof: " + str(stop_id))

print("next departure for Hauptbahnhof:")
print(get_departures(stop_id, count = 1))

while True:
    search_term = input("station name: ")
    
    try:
        stop_id = get_stop_id(search_term)
    except:
        print("stop not found")
    else:
        print("{} ({})".format(stops[stop_id], stop_id))
        departures = get_departures(stop_id, count=5)
        for departure in departures:
            print("in {}s  {} {}".format(departure["DepartureCountdown"], departure["Route"], departure["DepartureDirection"]))
