# python_swu_api
a python library to fetch live departure data for public transport in ulm

## usage example
```python
>>> from swu_api import *
>>> get_stop_id("Hauptbahnhof")
1008
>>> get_departures(stop_id = 1008, count = 1)
[{
  'PlatformNumber': 1,
  'PlatformName': '1',
  'ArrivalDirection': 'Kuhberg',
  'ArrivalTimeScheduled': '2021-09-01 13:51:00',
  'ArrivalTimeActual': '2021-09-01 13:51:57',
  'ArrivalCountdown': -19,
  'ArrivalDeviation': 57,
  'DepartureDirection': 'Sc. Park II (als Bus)',
  'DepartureTimeScheduled': '2021-09-01 13:51:00',
  'DepartureTimeActual': '2021-09-01 13:51:57',
  'DepartureCountdown': -19,
  'DepartureDeviation': 57,
  'VehicleNumber': 175,
  'VehicleCategory': 5,
  'Route': '2',
  'RouteNumber': 102,
  'Status': 3,
  'PassengerAlertRoute': 'false',
  'PassengerAlertTrip': 'false'
}]
```
