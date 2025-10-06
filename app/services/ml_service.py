# Simple placeholder for ML integration.
# Replace with actual model loading & inference (ONNX, TinyLlama wrapper, etc.)

from typing import Tuple

def predict_phishing(payload: str) -> Tuple[str, float]:
    """
    Returns (label, score) for the given payload.
    This is a dummy heuristic. Replace with a real model call.
    """
    text = (payload or "").lower()
    suspicious_keywords = ["bank", "login", "password", "verify", "urgent", "click", "update"]
    score = sum(1 for k in suspicious_keywords if k in text) / len(suspicious_keywords)
    label = "phishing" if score >= 0.3 else "benign"
    return label, float(score)
