"""
pipeline_utils.py
-----------------
General utility functions: file I/O, logging, Drive paths, dataset splitting.
Used across all notebooks.
"""

import os
import json
import numpy as np
from sklearn.model_selection import train_test_split


# ── Labels ────────────────────────────────────────────────────────────────────

CLASSES = [
    "eat", "drink", "water", "sleep", "medicine",
    "hello", "please", "thank_you", "sorry", "goodbye",
    "yes", "no", "help", "who", "what",
    "home", "school", "mother", "father", "friend"
]

LABEL_MAP = {label: idx for idx, label in enumerate(CLASSES)}


def save_label_map(output_path):
    """Save the class label mapping to a JSON file."""
    with open(output_path, "w") as f:
        json.dump(LABEL_MAP, f, indent=2)
    print(f"[INFO] Label map saved to {output_path}")


# ── File I/O ──────────────────────────────────────────────────────────────────

def get_video_paths(raw_video_dir):
    """
    Walk the raw video directory and return a list of (video_path, label) tuples.
    
    Expected structure:
        raw_video_dir/
          eat/
            video1.mp4
          drink/
            video1.mp4
    """
    video_paths = []
    for class_name in os.listdir(raw_video_dir):
        class_dir = os.path.join(raw_video_dir, class_name)
        if not os.path.isdir(class_dir):
            continue
        if class_name not in LABEL_MAP:
            print(f"[WARNING] Unknown class folder: {class_name} — skipping")
            continue
        for fname in os.listdir(class_dir):
            if fname.lower().endswith((".mp4", ".avi", ".mov")):
                video_paths.append((os.path.join(class_dir, fname), class_name))
    return video_paths


def save_npy(array, path):
    """Save a numpy array and print confirmation."""
    np.save(path, array)
    print(f"[INFO] Saved {array.shape} → {path}")


# ── Dataset Splitting ─────────────────────────────────────────────────────────

def split_dataset(X, y, val_size=0.15, test_size=0.15, random_state=42):
    """
    Split dataset into train / val / test sets.
    Split is done on VIDEO level (not frame level) to avoid data leakage.
    
    Args:
        X: np.ndarray of shape (n_samples, n_frames, n_features)
        y: np.ndarray of shape (n_samples,)
    
    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test
    """
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=(val_size + test_size), random_state=random_state, stratify=y
    )
    relative_test_size = test_size / (val_size + test_size)
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=relative_test_size, random_state=random_state, stratify=y_temp
    )

    print(f"[INFO] Train: {len(X_train)} | Val: {len(X_val)} | Test: {len(X_test)}")
    return X_train, X_val, X_test, y_train, y_val, y_test


# ── Logging ───────────────────────────────────────────────────────────────────

def log_processing_result(log_path, video_path, label, status, notes=""):
    """Append a processing result to the CSV quality log."""
    import csv
    file_exists = os.path.isfile(log_path)
    with open(log_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["video_path", "label", "status", "notes"])
        writer.writerow([video_path, label, status, notes])
