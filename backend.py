import requests

# API Key
API_KEY = "93a420769bf9a2934b7b064370c8aede"
limit = 5


def get_data(place, state=None, forecast_days=None):
    states = False
    if states == "":
        url0 = "http://api.openweathermap.org/geo/1.0/direct?q=" \
               f"{place}," \
               f"{state}" \
               "&limit=" \
               f"{limit}&appid={API_KEY}"
        response = requests.get(url0)
        data = response.json()
        english_city_name = data[0]["name"]
    else:
        url0 = "http://api.openweathermap.org/geo/1.0/direct?q=" \
               f"{place}" \
               "&limit=" \
               f"{limit}&appid={API_KEY}"
        response = requests.get(url0)
        data = response.json()
        english_city_name = data[0]["name"]

    url1 = "https://api.openweathermap.org/data/2.5/forecast?q=" \
           f"{english_city_name}&appid=" \
           f"{API_KEY}"
    response2 = requests.get(url1)
    final_data = response2.json()
    # 3 hour interval so 8 obs for every 24 hours
    filtered_data = final_data["list"]
    # filtered data based on number of observation
    num_obs = 8 * forecast_days
    filtered_data = filtered_data[:num_obs]

    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo", forecast_days=3)

