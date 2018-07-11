def city_country(city,country):
    belong=city.title()+','+country.title()
    return belong

city=city_country('beijing','china')
city1=city_country("los angeles","america")

print(city)
print(city1)
