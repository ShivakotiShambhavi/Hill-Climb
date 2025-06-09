import cv2
import mediapipe as mp
import time
from pynput.keyboard import Key, Controller

# Keyboard controller for key press/release
keyboard = Controller()
time.sleep(2.0)
current_key_pressed = None

# MediaPipe setup
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]

# Start webcam
video = cv2.VideoCapture(0)

# Setup OpenCV window and keep it always on top
cv2.namedWindow("Automation Gestures", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Automation Gestures", cv2.WND_PROP_TOPMOST, 1)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5,
                   max_num_hands=2) as hands:

    while True:
        ret, image = video.read()
        if not ret:
            break

        # Flip and convert image
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

        key_to_press = None
        hand_states = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lmList = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hand.HAND_CONNECTIONS)

                # Detect fingers (ignore thumb for robustness)
                fingers = []
                for i in range(1, 5):  # index to pinky
                    if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = fingers.count(1)

                if total_fingers == 4:
                    hand_states.append("open")
                elif total_fingers == 0:
                    hand_states.append("closed")

        # Decide gesture
        if "open" in hand_states:
            key_to_press = Key.right
            cv2.putText(image, "GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 255, 0), 5)
        elif "closed" in hand_states:
            key_to_press = Key.left
            cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)

        # Handle key press
        if key_to_press:
            if current_key_pressed != key_to_press:
                if current_key_pressed:
                    keyboard.release(current_key_pressed)
                keyboard.press(key_to_press)
                current_key_pressed = key_to_press
        else:
            if current_key_pressed:
                keyboard.release(current_key_pressed)
                current_key_pressed = None

        # Show image window
        cv2.imshow("Automation Gestures", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Cleanup
video.release()
cv2.destroyAllWindows()
if current_key_pressed:
    keyboard.release(current_key_pressed)
