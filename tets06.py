sandwich_orders=['pastrami','fruit','egg','pastrami','pastrami','chees']
finished_sandwiches=[]

print("pastrami sandwich is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
        sandwich=sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
