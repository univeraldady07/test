class AutomaticSprinkler: 
    def __init__(self): 
        self.soil_moisture = 0  # Soil moisture level (0 - dry, 100 - saturated) 
        self.weather_condition = "sunny"  # weather condition (sunny, cloudy, rainy) 
        self.time_of_day = "day"  # time of day (day or night) 
 
    def set_soil_moisture(self, moisture_level): 
        """Sets the current soil moisture level.""" 
        self.soil_moisture = moisture_level 
 
    def set_weather_condition(self, condition): 
        """Sets the current weather condition.""" 
        self.weather_condition = condition 
 
    def set_time_of_day(self, time_of_day): 
        """Sets the current time of day.""" 
        self.time_of_day = time_of_day 
 
    def decide_sprinkler_action(self): 
        """Decides whether to activate the sprinkler based on RBS rules.""" 
        if self.weather_condition == "rainy": 
            print("It's raining. No need to water the plants.") 
            return "No action" 
         
        if self.weather_condition == "cloudy": 
            if self.soil_moisture < 50: 
                print("It's cloudy, but soil is dry. Sprinkler activated.") 
                return "Sprinkler on" 
            else: 
                print("It's cloudy, and soil moisture is sufficient. No need to water.") 
                return "No action" 
 
        if self.weather_condition == "sunny": 
            if self.soil_moisture < 30 and self.time_of_day == "day": 
                print("It's sunny, and soil is dry. Sprinkler activated.") 
                return "Sprinkler on" 
            elif self.soil_moisture >= 30 and self.time_of_day == "day": 
                print("It's sunny, but soil moisture is sufficient. No need to water.") 
                return "No action" 
            elif self.time_of_day == "night": 
                print("It's night, no watering needed.") 
                return "No action" 
 
        return "No action" 
 
# Example usage 
sprinkler = AutomaticSprinkler() 
 
# Set conditions 
sprinkler.set_soil_moisture(100)  # Soil moisture level 
sprinkler.set_weather_condition("sunny")  # Weather condition 
sprinkler.set_time_of_day("day")  # Time of day 
 
# Check if the sprinkler needs to be activated 
sprinkler_action = sprinkler.decide_sprinkler_action() 
print(f"Sprinkler action: {sprinkler_action}")
