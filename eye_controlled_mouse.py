import cv2
import mediapipe as mp
#import pyautogui

face_mesh= mp.solutions.face_mesh.FaceMesh()

cam =cv2.VideoCapture(0)
while True:
	_, frame = cam.read()
	rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	output= face_mesh.process(rgb_frame)
	landmark_points=output.multi_face_landmarks
	frame_h,frame_w,_=frame.shape
	if landmark_points:
		landmarks=landmark_points[0].landmark
		for landmark in landmarks:
			x=int(landmark.x*frame_w)
			y=int(landmark.y*frame_h)
			cv2.circle(frame,(x,y),3,(0,255,0))#parameter(where ,location,radius,color)
			print(x,y)
	print(landmark_points)
	cv2.imshow("eye_controlled_mouse",frame)

	key = cv2.waitKey(100)
	if key == 27:
		break