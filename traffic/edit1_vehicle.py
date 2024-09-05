import cv2
import time
haar_cascade = 'cars.xml'
video = 'video.avi'
count = 0
detect = []
offset = 6 
cap = cv2.VideoCapture(1)
car_cascade = cv2.CascadeClassifier(haar_cascade)
frame_count = 0
def center_handle(x, y, w, h):
    cx = x + int(w / 2)
    cy = y + int(h / 2)
    return cx, cy

# loop runs if capturing has been initialized.
start = int(time.perf_counter())

while True:
    # reads frames from a video
    ret, frames = cap.read()
    if not ret:
        break
    '''
    end = int(time.perf_count())
    
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
  
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
      
    # To draw a rectangle in each cars
    if (end-start)%3==0:
      for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        count+=1
        # Display frames in a window 
      cv2.imshow('video', frames)
    
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
    '''
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    cv2.line(frames, (25, 550), (1200, 550), (255, 127, 0), 2)

    if frame_count%30==0:
        for (x,y,w,h) in cars:
            validate_count = (w >= 80) and (h >= 80)
            if not validate_count:
                continue

            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)

            center = center_handle(x, y, w, h)
            detect.append(center)
            cv2.circle(frames, center, 4, (0, 0, 255), -1)

            for (x, y) in detect:
                count += 1
                cv2.line(frames, (25, 550), (1200, 550), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle count: " + str(count))

    cv2.putText(frames, "VEHICLE count: " + str(count), (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow('Original Video', frames)
    frame_count +=1

    if cv2.waitKey(1) == 13:
        break
# De-allocate any associated memory usage
end_time = time.perf_counter()
print(count)
cv2.destroyAllWindows()
