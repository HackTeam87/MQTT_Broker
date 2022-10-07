import paho.mqtt.subscribe as subscribe
from geopy import distance

#Локація Університету Телекомунікацій
BASE_LOC = (50.42887501136511, 30.47598202502631)
TOPIC = "heat"

def CALCULATE_LOC(INPUT_LOC):
    My_DISTANCE = round(distance.distance(BASE_LOC, INPUT_LOC).meters)
    
    if My_DISTANCE > 500:
        return('OFF')
    else:
        return('ON')

    # if My_DISTANCE > 500:
    #     return(f'Ви знаходитесь за {My_DISTANCE} метрів від Університету Power OFF')
    # else:
    #     return(f'Ви знаходитесь за {My_DISTANCE} метрів від Університету Power ON')    
    


def ON_MESSAGE(client, userdata, message):
    print(CALCULATE_LOC(message.payload.decode('utf8')))
    # print("%s %s" % (message.topic, message.payload.decode('utf8')))

try:
    print('\nBroker Start')
    subscribe.callback(ON_MESSAGE, TOPIC , hostname="localhost")
except:
    print('\nBroker Stop')
    pass    
