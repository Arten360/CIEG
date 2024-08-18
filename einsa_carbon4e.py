import helper, requests, json, numpy as np
def power_stats(lat,lon, api_key=helper.load_emaps_api_key()):
    coordinates = { "lat": lat, "lon": lon }

    url_intensity = f"https://api.electricitymap.org/v3/carbon-intensity/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"
    request_intensity = requests.get(url_intensity, headers={"auth-token": api_key})
    intensity = json.loads(request_intensity.content)

    url_breakdown = f"https://api.electricitymap.org/v3/power-breakdown/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"
    request_breakdown = requests.get(url_breakdown, headers={"auth-token": api_key})
    breakdown = json.loads(request_breakdown.content)

    breakdown_abridged = {
        'renewablePercentage': breakdown['renewablePercentage'],
        'fossilFreePercentage': breakdown['fossilFreePercentage'],
        'powerConsumptionBreakdown': breakdown['powerConsumptionBreakdown'],
        'consumption_percent': {
            k: np.round((v/breakdown['powerConsumptionTotal']) * 100) 
            for k, v 
            in breakdown['powerConsumptionBreakdown'].items()
        },
    }
    
    return intensity, breakdown_abridged

# Coordinates from Dülmen, 
intensity, breakdown = power_stats(
    lat=51.82891701116644,
    lon=7.278057219988674
    )

print(intensity, breakdown)
