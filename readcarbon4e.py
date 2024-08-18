from helper import load_env
load_env()

# Create a dictionary with the coordinates
coordinates = {
    "lat":34.00906474557528,
    "lon": -118.4984580927553
}

# Build the url
url= f"https://api.electricitymap.org/v3/carbon-intensity/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"

# Print the endpoint
print("Endpoint: " + str(url))

import requests
import helper

request = requests.get(
    url,
    headers={"auth-token": helper.load_emaps_api_key()})

# This byte format is more compact
request.content
type(request.content)

import json

json.loads(request.content)

# Build the url
url = f"https://api.electricitymap.org/v3/power-breakdown/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"
print(url)

request = requests.get(
    url,
    headers={"api_key": helper.load_emaps_api_key()})

power_breakdown = json.loads(request.content)

# Print the content
print(power_breakdown)
power_breakdown['renewablePercentage']
power_breakdown['fossilFreePercentage']
# Power Consumption Breakdown in MegaWatts
power_breakdown['powerConsumptionBreakdown']

import numpy as np

total_consumption = power_breakdown['powerConsumptionTotal']
print(total_consumption)

consumption_percent = {
    k: np.round((v/total_consumption) * 100)
    for k,v
    in power_breakdown['powerConsumptionBreakdown'].items()}
print(consumption_percent)
