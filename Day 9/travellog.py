travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def addToLog(country, times, places):
    newCountry = {
        "country": country,
        "visits": times,
        "cities": places
    }
    travel_log.append(newCountry)

addToLog("UK", 5, ["London", "Manchester"])
print(travel_log)
