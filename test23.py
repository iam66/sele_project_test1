cities={'beijing':{'country':'china','population':999999999,'fact':'is powful!'},
        'new york':{'country':'america','population':1000000,'fact':'is open.'},
        'paris':{'cpuntry':'france','population':2000000,'fact':" is fashion."}
        }

for city_name,country_info in cities.items():
    for country, info in country_info.items():
        country_info[country]=info
    print(city_name,country_info)
