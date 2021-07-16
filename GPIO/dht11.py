import time
import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {:.1f} C    Humidity: {}% ".format(temperature, humidity))
 
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
