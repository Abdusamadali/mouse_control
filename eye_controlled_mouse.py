import cv2
import mediapipe
import pyautogui

cam =cv2.VideoCapture(0)
while True:
	_, frame = cam.read()
	cv2.imshow("eye_controlled_mouse",frame)
	key = cv2.waitKey(100)
	if key == 27:
		break