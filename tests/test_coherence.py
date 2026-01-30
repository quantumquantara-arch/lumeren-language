import pytest
from lumeren_core.coherence import calculate_kappa  # Adjust import if function name differs

def test_perfect_coherence():
    vector1 = [1, 1, 0]
    vector2 = [1, 1, 0]
    score = calculate_kappa(vector1, vector2)
    assert score == 1.0

def test_partial_coherence():
    vector1 = [1, 1, 0]
    vector2 = [1, 0, 0]
    score = calculate_kappa(vector1, vector2)
    assert score == 0.5  # Assume simple cosine similarity or similar metric
