import pytest
from lumeren_core.parser import parse  # Adjust import if function name differs

def test_valid_sequence():
    expression = '⊙ → K → Â'  # Example valid glyph sequence: Existence observes Change via Coherence
    result = parse(expression)
    assert result is not None
    assert 'coherence_axis' in result  # Example assertion; customize based on parse output

def test_invalid_sequence():
    expression = '⊙ → Â'  # Missing coherence axis K
    with pytest.raises(ValueError):  # Assume it raises ValueError on invalid
        parse(expression)
