import pyowm
import requests,time
import csv

def prepare_data():

    with open("D:\\STUDY_WORK_SANJIT\\PYTHON_WEATHER_APP\\us-cities-top-20.csv") as file:
        reader = csv.reader(file)
        print (type(reader))
        list_of_cities = {}
        counter  = 1
        for row in reader:
            list_of_cities[counter] = row[0]
            counter += 1



    city_temp_list = fetch_weather_data(list_of_cities)

    for key in city_temp_list:
        print (key,city_temp_list[key])



def fetch_weather_data(list_of_cities):
    my_own_api_key = "PUT_YOUR_OWN_KEY"
    owm = pyowm.OWM(my_own_api_key)
    city_temp_list = {}


    for key in list_of_cities:
        city_name = list_of_cities[key]
        root_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},USA&appid={my_own_api_key}"

        r= requests.get(root_url)

        print (r.json())

        data = r.json()

        if(data['cod'] ==200 ):
            main_data = data['main']
            city_temp_list[city_name] = round(main_data['temp']-273.15)
        else:
            pass

    return city_temp_list




prepare_data()