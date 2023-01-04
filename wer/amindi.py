from pyowm import OWM

owm = OWM('5dfdd607d0c33f12e428ca24dce76755')


mgr = owm.weather_manager()

city = input('enter city: ')

obs = mgr.weather_at_place(city)

w = obs.weather

print(w.detailed_status)
print(w.wind())
print(w.humidity)
print(w.temperature('celsius'))

