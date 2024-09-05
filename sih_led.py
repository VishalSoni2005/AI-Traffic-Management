import time

total_time_max = 400
total_time_min = 120
time_min = 5
time_max = 100
time_lap = 60
car1 = 10
car2 = 20
car3 = 5
car4 = 15
while True:
    lane1 = "green"
    lane2 = lane3 = lane4 = "red"
    total_car = car1+car2+car3+car4
    if total_car >= 60:
        time_lap = total_time_max/total_car
    else:
        time_lap = total_time_min/total_car
    lane1_time = time_lap*car1
    lane2_time = time_lap*car2
    lane3_time = time_lap*car3
    lane4_time = time_lap*car4
    while lane1=="green":
        print("Lane 1: ",lane1)
        print("Lane 2: ",lane2)
        print("Lane 3: ",lane3)
        print("Lane 4: ",lane4)
        time.sleep(2)
        lane1 = "red"
        lane2 = "green"
    while lane2=="green":
        print("Lane 1: ",lane1)
        print("Lane 2: ",lane2)
        print("Lane 3: ",lane3)
        print("Lane 4: ",lane4)
        time.sleep(2)
        lane2 = "red"
        lane3 = "green"
    while lane3=="green":
        print("Lane 1: ",lane1)
        print("Lane 2: ",lane2)
        print("Lane 3: ",lane3)
        print("Lane 4: ",lane4)
        time.sleep(2)
        lane3 = "red"
        lane4 = "green"
    while lane4=="green":
        print("Lane 1: ",lane1)
        print("Lane 2: ",lane2)
        print("Lane 3: ",lane3)
        print("Lane 4: ",lane4)
        time.sleep(2)
        lane4 = "red"
        lane1 = "green"
        
