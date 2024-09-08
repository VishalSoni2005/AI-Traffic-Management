import time
import led_class
import cam_class
import timer

def change_cam(a):
    a[0],a[1],a[2],a[3]=a[1],a[2],a[3],a[0]
    return a
def change_cam(a):
    a[0],a[1],a[2],a[3]=a[1],a[2],a[3],a[0]
    return a
lane1 = led_class.LEDController(2,3,4,17)
lane2 = led_class.LEDController(27,22,23,24)
lane3 = led_class.LEDController(25,5,6,13)
lane4 = led_class.LEDController(19,26,16,20)
lanes = [lane1,lane2,lane3,lane4]
cam1 = cam_class.cam_class(0)
cam2 = cam_class.cam_class(1)
cam3 = cam_class.cam_class(2)
cam4 = cam_class.cam_class(3)
cam_lst = [cam1,cam2,cam3,cam4]
time_max = 400
time_min = 200
time1 = time2 = time3 = time4 = 5
time_lane2 = 5
while True:
    lanes[0].on()
    time.sleep(time_lane2-3)
    #car1 = cam_lst[0].count_car()
    car2 = cam_lst[1].count_car()
    car3 = cam_lst[2].count_car()
    car4 = cam_lst[3].count_car()
    total_car = car2 + car3 + car4
    if total_car>30:
        time_per_lane = time_max//total_car
    else:
        time_per_lane = time_min//total_car
    #time_lane1 = time_per_lane*car1
    time_lane2 = time_per_lane*car2
    time_lane3 = time_per_lane*car3
    time_lane4 = time_per_lane*car4