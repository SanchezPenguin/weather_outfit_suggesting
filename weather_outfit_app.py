from flask import Flask,render_template
import requests
from datetime import datetime 

app = Flask(__name__)

clothing_dict = {
    "headwear": ["cap", "beanie","No hat needed"],
    "shirt": ["T-shirt", "long sleeve shirt", "short sleeve button-up shirt","graphic tee"],
    "pants": ["baggy jeans", "western pants", "straignt jeans"," Loose Jean"],
    "jacket": ["leather jacket", "denim jacket", "no jacket needed","Puffer jacket"],
    "shoes": ["Nike sneakers", "New balance 550", "Dr. martens"],
    "other": ["scarf", "gloves", "sunglasses","none"]
}

@app.route('/')
def home():
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=El%20Paso&appid=4f2ee15d79620a89d16f3b10d8711c1f&units=metric")
    weather_data = weather.json()
    #tempeture details
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]


    #time 
    current_time = str(datetime.now())[:16] 

    # getting huminity levels
    humidity = weather_data["main"]["humidity"] 
    if humidity < 30:
        humidityLevel = "Low humidity"
    elif humidity < 60:
        humidityLevel = "Moderate humidity"
    else:
        humidityLevel = "High humidity"
     # Weather condition
    weather_condition = weather_data["weather"][0]["description"].lower()


    return render_template('index.html', 
                           temp=temp, 
                           feels_like=feels_like, 
                           temp_min=temp_min, 
                           temp_max=temp_max, 
                          humidity=humidity, 
                          humidity_level=humidityLevel, 
                           current_time=current_time, 
                          weather_condition=weather_condition)

@app.route('/outfit')
def outfit_suggestion():
    

    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=El%20Paso&appid=4f2ee15d79620a89d16f3b10d8711c1f&units=metric")
    weather_data = weather.json()
    #tempeture details
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]


    # getting huminity levels
    humidity = weather_data["main"]["humidity"] 
    if humidity < 30:
        humidityLevel = "Low humidity"
    elif humidity < 60:
        humidityLevel = "Moderate humidity"
    else:
        humidityLevel = "High humidity"
    # Weather condition
    weather_condition = weather_data["weather"][0]["description"].lower()

    outfit = {
        "headwear": "none",
        "shirt": "none",
        "pants": "none",
        "jacket": "none",
        "shoes": "noen",
        "other": "none"
    }

    # Suggest outfits based on temperature
    if temp >= 30:  # Hot weather
        outfit["headwear"] = "cap"
        outfit["shirt"] = "T-shirt"
        outfit["pants"] = "Loose Jean"
        outfit["jacket"] = "no jacket needed"
        outfit["shoes"] = "Nike sneakers"
        outfit["other"] = "sunglasses"
    elif temp >= 20:  # Mild weather
        outfit["headwear"] = "No hat needed"
        outfit["shirt"] = "long sleeve shirt"
        outfit["pants"] = "western pants"
        outfit["jacket"] = "denim jacket"
        outfit["shoes"] = "New balance 550"
        outfit["other"] = "none"
    elif temp >= 10:  # Cool weather
        outfit["headwear"] = "beanie"
        outfit["shirt"] = "long sleeve shirt"
        outfit["pants"] = "straight jeans"
        outfit["jacket"] = "leather jacket"
        outfit["shoes"] = "Dr. Martens"
        outfit["other"] = "scarf"
    else:  # Extremely cold weather
        outfit["headwear"] = "beanie"
        outfit["shirt"] = "graphic tee"
        outfit["pants"] = "baggy jeans"
        outfit["jacket"] = "Puffer jacket"
        outfit["shoes"] = "boots"
        outfit["other"] = "gloves"

    # Return the outfit page
    return render_template('outfit.html', outfit=outfit, weather_condition=weather_condition)


if __name__ == '__main__':
    app.run(debug=True)    





app.run()


