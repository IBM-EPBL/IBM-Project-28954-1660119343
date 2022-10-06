def hotwater():
    sense = SenseHat()
    sense.clear()
    celcius = round(sense.get_temperature(), 1)
    return celcius

celcius= hotwater()
result = 'temp. C' + str(celcius)
print(result)
result_list = [(datetime.datetime.now(), celcius)]