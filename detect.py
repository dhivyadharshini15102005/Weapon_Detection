from ultralytics import YOLO
import cv2
import pygame
import time
import numpy as np
import os

# Initialize Pygame mixer safely
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Load alarm sound with correct absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder where this script is located
alarm_path = os.path.join(script_dir, "alarm.wav")

if not os.path.exists(alarm_path):
    raise FileNotFoundError(f"alarm.wav not found at {alarm_path}")

alarm_sound = pygame.mixer.Sound(alarm_path)
alarm_sound.set_volume(1.0)  # Max volume

# Load YOLO model (change path to your custom model if needed)
model = YOLO("yolov8n.pt")  # Replace with your trained weapon detection model if needed

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("❌ Webcam not accessible")

# Timing to avoid alarm spamming
last_alarm_time = 0
alarm_interval = 2  # seconds

# Function to detect if camera is blocked
def is_camera_blocked(frame, threshold=30):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)
    return avg_brightness < threshold

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    detected = False
    current_time = time.time()

    # Check if the camera is blocked
    if is_camera_blocked(frame):
        print("🛑 Camera appears to be blocked!")
        detected = True
        annotated_frame = np.zeros_like(frame)
        cv2.putText(annotated_frame, "Camera Blocked!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, (0, 0, 255), 3)
    else:
        # Run YOLO detection
        results = model(frame, stream=True)
        annotated_frame = frame.copy()

        for r in results:
            boxes = r.boxes
            names = r.names
            for box in boxes:
                cls_id = int(box.cls[0])  # Get class index
                class_name = names[cls_id]
                print("Detected:", class_name)

                # Check specifically for 'knife'
                if "knife" in class_name.lower():
                    print("🔪 Knife Detected!")
                    detected = True
                    break

            # Annotate frame
            annotated_frame = r.plot()

    # Play alarm if knife detected or camera is blocked
    if detected and (current_time - last_alarm_time > alarm_interval):
        print("🔊 Playing alarm now")
        alarm_sound.play()
        last_alarm_time = current_time

    # Show annotated frame
    cv2.imshow("Knife Detection", annotated_frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
g
# Cleanup
cap.release()
cv2.destroyAllWindows()
