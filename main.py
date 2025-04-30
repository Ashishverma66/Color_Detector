import cv2

clicked = False                                                          #Setting up global variables
b = g = r = x_pos = y_pos = 0

def show_color(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        x_pos= x
        y_pos= y
        b,g,r = frame[y,x]

cap=cv2.VideoCapture(0)
cv2.namedWindow("Color Detector")
cv2.setMouseCallback("Color Detector", show_color)

while True:
    ret, frame= cap.read()
    if not ret:
        break

    if clicked:
        cv2.rectangle(frame,(20,20),(220,60), (int(b), int(g), int(r)), -1)
        text = f"B: {b} G : {g} R: {r}"
        brightness = int(b) + int(g) + int(r)
        text_color=(0,0,0) if brightness > 400 else (255,255,255)
        cv2.putText(frame, text,(30,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,text_color,2)

    cv2.imshow("Color Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



