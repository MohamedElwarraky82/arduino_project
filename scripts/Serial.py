import serial, json

test_data = {}
arduino = serial.Serial(port='COM8', baudrate=115200, timeout=0.1)

def write(data):
    print(f"Write {data}")
    arduino.write(bytes(data, 'utf-8'))
    arduino.flush()

def read():
    while not arduino.in_waiting > 0:
        pass
    
    while True:
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(f"Read: {data}")
            return data

try:
    while not arduino.is_open:
        pass
    
    write("S")
    value = read()
    if value == "1":
        pass
    while True:
        value = read()
        if value != "End":
            data = value.split(":")
            test_name = data[0]
            test_res = data[1]
            if test_res == "1":
                test_data[test_name] = "Passed"
            else:
                raise Exception(f"{test_name} is failed!")
        else:
            break

except KeyboardInterrupt:
    print("Exiting...")

finally:
    arduino.close()

test_data = {"Tests": test_data}

json_obj = json.dumps(test_data)

with open("build/results.json", "w") as f:
    f.write(json_obj)
