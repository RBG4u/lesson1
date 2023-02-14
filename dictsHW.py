from pprint import pprint

weather = {"city": "Москва", "temperature": "20"}
pprint(weather)
print(weather["city"])
weather["temperature"] = int(weather["temperature"]) - 5
weather["temperature"] = str(weather["temperature"])
pprint(weather)
print(type(weather["temperature"]))

print(weather.get("country"))

weather["date"] = "27.05.2019"
pprint(weather)

