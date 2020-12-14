# import required modules
import requests

# function to request for data
def weather_data(query):
   api_key = "a0a0e15a1a637278b01fef743314c833"
   # base_url variable to store url
   base_url = "http://api.openweathermap.org/data/2.5/weather?"
   complete_url = base_url + "appid=" + api_key + "&" + query
   # response object
   res=requests.get(complete_url);
   return res.json();

# function to display results
def display_results(weathers,city):
   print("{}'s temperature: {}°C ".format(city,weathers['main']['temp']))
   print("Wind speed: {} m/s".format(weathers['wind']['speed']))
   print("Description: {}".format(weathers['weather'][0]['description']))
   print("Weather: {}".format(weathers['weather'][0]['main']))

# main function
def main():
   city=input('Enter the city name or zip code:')
   print()
   try:
      query='q='+city;
      w_data=weather_data(query);
      display_results(w_data, city)
      print()
   except:
      print('City name not found')

if __name__=='__main__':
   main()
