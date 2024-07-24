import cv2
import mediapipe as mp
import numpy as np

# Paths to multiple filter images
filter_paths = [
    "images/filter1.png",
    "images/filter2.jpg",
]
logo_path = "spslogo.jpeg"

# Load all filter images
filters = [cv2.imread(path, cv2.IMREAD_UNCHANGED) for path in filter_paths]

# Check if filters are loaded correctly
if any(filter is None for filter in filters):
    print("Error: One or more filter images could not be loaded.")
    exit()

# Load logo image
logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)

# Check if logo is loaded correctly
if logo is None:
    print("Error: Logo image could not be loaded.")
    exit()

# Resize the logo
logo_height, logo_width = 100, 100  # Desired size of the logo
logo = cv2.resize(logo, (logo_width, logo_height))

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Define initial filter index
current_filter_index = 0

# Define scaling factors for filters
scale_factors = [1.5, 1.9]  # Different scale factors for each filter

def blend_filter(filter_part, x, y, width, height):
    if filter_part.shape[2] == 4:  # Check if filter has an alpha channel
        alpha_s = filter_part[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(3):
            frame[y:y+height, x:x+width, c] = alpha_s * filter_part[:, :, c] + alpha_l * frame[y:y+height, x:x+width, c]
    else:
        frame[y:y+height, x:x+width] = filter_part

# Start video capture
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Could not read frame from video capture.")
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Face Mesh
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, c = frame.shape
            
            # Convert normalized coordinates to pixel format
            x_coords = [int(landmark.x * w) for landmark in face_landmarks.landmark]
            y_coords = [int(landmark.y * h) for landmark in face_landmarks.landmark]

            x_min = min(x_coords)
            x_max = max(x_coords)
            y_min = min(y_coords)
            y_max = max(y_coords)

            face_width = x_max - x_min
            face_height = y_max - y_min

            # Apply scaling factor for the current filter
            filter_width = int(face_width * scale_factors[current_filter_index])
            filter_height = int(face_height * scale_factors[current_filter_index])

            # Resize the selected filter image
            selected_filter = filters[current_filter_index]
            resized_filter = cv2.resize(selected_filter, (filter_width, filter_height))

            # Calculate the position to center the filter on the face
            filter_x = x_min - (filter_width - face_width) // 2
            filter_y = y_min - (filter_height - face_height) // 2

            # Ensure the filter is within the frame boundaries
            def clamp(value, min_value, max_value):
                return max(min_value, min(value, max_value))

            filter_x = clamp(filter_x, 0, w - filter_width)
            filter_y = clamp(filter_y, 0, h - filter_height)

            # Blend the filter image onto the frame
            blend_filter(resized_filter, filter_x, filter_y, filter_width, filter_height)

    # Display current filter option
    cv2.putText(frame, f"Filter {current_filter_index + 1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Blend the logo onto the frame at the top-right corner
    logo_x = frame.shape[1] - logo_width - 10  # 10 pixels from the right edge
    logo_y = 10  # 10 pixels from the top edge
    blend_filter(logo, logo_x, logo_y, logo_width, logo_height)

    # Show the frame with filter and logo applied
    cv2.imshow("Snapchat Filter", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n'):
        # Switch to the next filter
        current_filter_index = (current_filter_index + 1) % len(filters)

# Release the video capture and destroy all windows
video.release()
cv2.destroyAllWindows()
face_mesh.close()
