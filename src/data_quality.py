"""
data_quality.py
---------------
Functions to validate and report on dataset quality.
Run these checks BEFORE delivering .npy files to Membre 2.
"""

import numpy as np
from collections import Counter


def check_class_balance(y, class_names):
    """
    Print class distribution and flag imbalanced classes.
    A class is flagged if it has less than 70% of the median count.
    """
    counts = Counter(y)
    median = np.median(list(counts.values()))
    print("\n📊 Class Distribution:")
    print(f"{'Class':<15} {'Count':>6} {'Status':>10}")
    print("-" * 35)
    for idx, name in enumerate(class_names):
        count = counts.get(idx, 0)
        status = "✅ OK" if count >= 0.7 * median else "⚠️  LOW"
        print(f"{name:<15} {count:>6} {status:>10}")
    print(f"\nMedian count per class: {median:.0f}")


def check_nan_inf(X, name="X"):
    """Check for NaN or infinite values in the feature array."""
    has_nan = np.isnan(X).any()
    has_inf = np.isinf(X).any()
    if has_nan or has_inf:
        print(f"[ERROR] {name} contains NaN={has_nan} | Inf={has_inf} — fix before delivery!")
    else:
        print(f"[OK] {name} — no NaN or Inf values found.")
    return not (has_nan or has_inf)


def check_shape(X, expected_shape, name="X"):
    """Verify the shape of a dataset array matches expectations."""
    if X.shape[1:] != expected_shape:
        print(f"[ERROR] {name} shape mismatch. Got {X.shape}, expected (n, {expected_shape})")
        return False
    print(f"[OK] {name} shape: {X.shape}")
    return True


def check_zero_sequences(X, threshold=0.9):
    """
    Flag sequences where more than `threshold` of values are zero.
    This usually means MediaPipe failed to detect hands for most frames.
    """
    flagged = 0
    for i, seq in enumerate(X):
        zero_ratio = (seq == 0).mean()
        if zero_ratio > threshold:
            flagged += 1
    if flagged > 0:
        print(f"[WARNING] {flagged}/{len(X)} sequences have >{threshold:.0%} zero values — likely detection failures.")
    else:
        print(f"[OK] No heavily-zeroed sequences detected.")
    return flagged


def run_full_quality_report(X_train, X_val, X_test, y_train, y_val, y_test, class_names):
    """Run all quality checks and print a summary report."""
    print("=" * 50)
    print("🔍 FULL DATA QUALITY REPORT")
    print("=" * 50)

    expected_features = (30, 258)  # (frames, features)

    check_shape(X_train, expected_features, "X_train")
    check_shape(X_val,   expected_features, "X_val")
    check_shape(X_test,  expected_features, "X_test")

    check_nan_inf(X_train, "X_train")
    check_nan_inf(X_val,   "X_val")
    check_nan_inf(X_test,  "X_test")

    check_zero_sequences(X_train)

    check_class_balance(y_train, class_names)

    print("\n✅ Quality report complete. Fix any [ERROR] or [WARNING] before delivery.")
    print("=" * 50)
