import requests
import matplotlib.pyplot as plt


villes = ["Azilal", "Rabat", "Marakech", "casablanca"]

temperatures = []
humidites = []


for ville in villes:
    url = "https://wttr.in/" + ville + "?format=j1"
    response = requests.get(url)
    data = response.json()

    temp = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]

    temperatures.append(int(temp))
    humidites.append(int(humidity))

plt.subplot(1, 2, 1)
plt.bar(villes, temperatures)
plt.title("Temperature des villes")
plt.xlabel("Villes")
plt.ylabel("Temperature °C")



plt.subplot(1, 2, 2)
plt.pie(humidites, labels=villes)
plt.title("Humidite")
plt.tight_layout()  
plt.show()