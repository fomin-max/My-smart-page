import datetime
import requests
from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render
from ipware.ip import get_ip


def launding(request):
    # ip = get_ip(request)
    # ip = '81.26.80.18' krasnoyarsk
    # ip = '46.72.224.18' vrn
    # ip = '31.42.43.28' mendeleyevo
    ip = '82.179.78.1'
    #ip = '193.0.166.20' nn
    # ip = '94.100.205.20' murmansk
    # ip = '62.106.126.20' smr
    # ip = '80.76.235.18'
    # ip = '95.84.0.12' saratov
    # ip = '94.198.2.18' dd
    if ip is not None:
        try:
            g = GeoIP2()
            city = g.city(ip)
            code = city['country_code']
            city = city['city']
        except:
            city = {'Локация': 'нет данных'}

    s_city = str(city) + ',' + str(code)
    city_id = 0
    city_html = city
    city_html = city_html.replace(" ", "_");
    appid = "dc963d586e747302682e9144d2ec250c"
    mylink = "https://news.yandex.ru/" + str(city_html) + "/index.rss"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
    except Exception as e:
        temp = "Not found ;<"
        pass

    try:
        res1 = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})
        data = res1.json()
        conditions = str(data['weather'][0]['description'])
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
    except Exception as e:
        # print("Exception (weather):", e)
        pass

    now_time = datetime.datetime.now()
    now_date = datetime.date.today()
    num_week = now_date.isoweekday()
    day = now_date.day
    month = now_date.month
    hour = now_time.hour
    freeday = ""
    if (month == 1) and (day < 9):
        freeday = "Now the New Year holidays!"
    elif (month == 2) and (day == 23):
        freeday = "Today the Fatherland Defender's Day!"
    elif (month == 3) and (day == 8):
        freeday = "Today is International Women's Day!"
    elif (month == 5) and (day == 1):
        freeday = "Today is a holiday of Spring and Work!"
    elif (month == 5) and (day == 9):
        freeday = "Today Victory Day!"
    elif (month == 11) and (day == 4):
        freeday = "Today the Day of National Unity"
    if (num_week < 6):
        if (hour < 9):
            work_time = "To work remained " + str(9 - hour) + " hour"
        elif (hour >= 9) and (hour <= 18):
            work_time = "To the end work left " + str(18 - hour) + " hour"
        elif (hour > 18):
            work_time = "To work remained " + str(24 - hour + 9) + " hour"
    else:
        work_time = "Today free day!"

    if num_week == 1:
        num_week = "Monday"
    elif num_week == 2:
        num_week = "Tuesday"
    elif num_week == 3:
        num_week = "Wednesday"
    elif num_week == 4:
        num_week = "Thursday"
    elif num_week == 5:
        num_week = "Friday"
    elif num_week == 6:
        num_week = "Saturday (day off, enjoy!)"
    elif num_week == 7:
        num_week = "Sunday (day off, enjoy!)"
    day = now_time.day
    if (hour >= 0) and (hour < 6):
        hi = "Good night!"
    elif (hour >= 6) and (hour < 12):
        hi = "Good morning!"
    elif (hour >= 12) and (hour < 18):
        hi = "Good day!"
    elif hour >= 18:
        hi = "Good evening!"

    return render(request, 'launding/launding.html', locals())
