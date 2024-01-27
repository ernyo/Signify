import cv2
import numpy as np
import os
import mediapipe as mp
import shutil
import json

sign_name = "hello"

#video path 
PATH = f'https://media.signbsl.com/videos/asl/startasl/mp4/{sign_name}.mp4'

cap = cv2.VideoCapture(PATH)

#functions
mp_holistic = mp.solutions.holistic # create a Holistic model to make detections
mp_drawing = mp.solutions.drawing_utils # Drawing utilities to draw keypoints and skeletons

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB, this is because OpenCV reads in feed in BGR channel format but MediaPipe requires a format of RGB
    image.flags.writeable = False                  # Image is no longer writeable, this will safe memory usage
    results = model.process(image)                 # Make prediction on frames from OpenCV
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]) if results.pose_landmarks else np.zeros(33*3)
    return pose

# Path for exported data in the format of numpy arrays
DATA_PATH = os.path.join('Coordinates_Data')  
os.makedirs(DATA_PATH)

# Each video is going to be 30 frames in length, i.e., use 30 sets of keypoints to identify a particular action 
sequence_length = 30

# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    for frame_num in range(sequence_length):

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        # NEW Export keypoints
        keypoints = extract_keypoints(results)
        npy_path = os.path.join(DATA_PATH, str(frame_num)) #save each frame as a numpy array
        np.save(npy_path, keypoints)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
                    
cap.release()
cv2.destroyAllWindows()

# Path for exported data in the format of numpy arrays
DATA_PATH = os.path.join('Coordinates_Data')  


# Define the structure of the JSON object
json_object = {}
keypoint_names = ["nose", "left_eye_inner", "left_eye", "left_eye_outer", "right_eye_inner", "right_eye", "right_eye_outer", "left_ear", "right_ear", "mouth_left", "mouth_right", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index", "right_index", "left_thumb", "right_thumb", "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle", "left_heel", "right_heel", "left_foot_index", "right_foot_index"]

json_object = {}
# Loop through the array and create the JSON object
for i in range(sequence_length):
    frame_key = f"frame{i}"
    coordinates_array = np.load(DATA_PATH + f'/{i}.npy')
    json_object[frame_key] = {}
    for keypoint_name, frame_coordinates in zip(keypoint_names, coordinates_array):
        json_object[frame_key][keypoint_name] = {
            "x": float(frame_coordinates[0]),
            "y": float(frame_coordinates[1]),
            "z": float(frame_coordinates[2])
        }

# Convert the JSON object to a JSON-formatted string
json_string = json.dumps(json_object, indent=4)
# Print or save the resulting JSON string
print(json_string)


# Get the absolute path of the folder in the root directory
absolute_path = os.path.abspath("Coordinates_Data")

# Delete the folder and its contents
shutil.rmtree(absolute_path)