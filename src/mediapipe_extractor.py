"""
mediapipe_extractor.py
----------------------
Handles all MediaPipe landmark extraction from video files.
Used in: notebooks/01_extraction.ipynb
"""

import cv2
import numpy as np
import mediapipe as mp


# MediaPipe setup
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


def extract_keypoints(results):
    """
    Extract and flatten landmark keypoints from a MediaPipe Holistic result.
    
    Returns a 1D numpy array of shape (258,):
      - Left hand:  21 landmarks × 3 (x, y, z) = 63
      - Right hand: 21 landmarks × 3 (x, y, z) = 63
      - Pose:       33 landmarks × 4 (x, y, z, visibility) = 132
      Total = 258 features
    
    If a hand or pose is not detected, zeros are returned for that part.
    """
    # Pose (33 landmarks × 4)
    pose = np.array([[lm.x, lm.y, lm.z, lm.visibility]
                     for lm in results.pose_landmarks.landmark]).flatten() \
           if results.pose_landmarks else np.zeros(33 * 4)

    # Left hand (21 landmarks × 3)
    left_hand = np.array([[lm.x, lm.y, lm.z]
                          for lm in results.left_hand_landmarks.landmark]).flatten() \
                if results.left_hand_landmarks else np.zeros(21 * 3)

    # Right hand (21 landmarks × 3)
    right_hand = np.array([[lm.x, lm.y, lm.z]
                           for lm in results.right_hand_landmarks.landmark]).flatten() \
                 if results.right_hand_landmarks else np.zeros(21 * 3)

    return np.concatenate([pose, left_hand, right_hand])


def process_video(video_path, target_frames=30):
    """
    Process a single video file and extract landmark sequences.
    
    Args:
        video_path (str): Path to the .mp4 video file.
        target_frames (int): Number of frames to standardize to (default: 30).
    
    Returns:
        np.ndarray of shape (target_frames, 258), or None if extraction fails.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Cannot open video: {video_path}")
        return None

    sequence = []
    detection_failures = 0

    with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # MediaPipe requires RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = holistic.process(image)

            # Track detection failures
            if not results.left_hand_landmarks and not results.right_hand_landmarks:
                detection_failures += 1

            keypoints = extract_keypoints(results)
            sequence.append(keypoints)

    cap.release()

    if len(sequence) == 0:
        print(f"[ERROR] No frames extracted from: {video_path}")
        return None

    # Quality warning: too many missed detections
    failure_rate = detection_failures / len(sequence)
    if failure_rate > 0.2:
        print(f"[WARNING] High hand detection failure rate: {failure_rate:.0%} in {video_path}")

    # Standardize to target_frames
    sequence = standardize_sequence(np.array(sequence), target_frames)
    return sequence


def standardize_sequence(sequence, target_frames=30):
    """
    Resize a sequence to exactly target_frames using interpolation.
    
    Args:
        sequence (np.ndarray): Shape (n_frames, n_features)
        target_frames (int): Target number of frames
    
    Returns:
        np.ndarray of shape (target_frames, n_features)
    """
    n_frames, n_features = sequence.shape
    if n_frames == target_frames:
        return sequence

    indices = np.linspace(0, n_frames - 1, target_frames).astype(int)
    return sequence[indices]
