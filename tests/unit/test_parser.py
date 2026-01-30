"""
Unit tests for Luméren parser
"""
import pytest
import sys
sys.path.append('..')
from lumeren_core.enhanced_parser import EnhancedLumerenParser

def test_parser_initialization():
    parser = EnhancedLumerenParser()
    assert parser is not None
    assert len(parser.glyphs) >= 23  # Should have at least 23 glyphs

def test_valid_sequence():
    parser = EnhancedLumerenParser()
    sequence = ['⁖', '→', 'K', '→', '⊖']
    result = parser.parse_with_repair(sequence)
    assert result['valid'] == True
    assert len(result['errors']) == 0

def test_missing_coherence():
    parser = EnhancedLumerenParser()
    sequence = ['⁖', '→', '⊖']  # Missing K
    result = parser.parse_with_repair(sequence)
    assert result['valid'] == False
    assert 'Missing K' in str(result['errors'])
    assert result['repaired'] is not None

def test_kappa_score():
    parser = EnhancedLumerenParser()
    sequence = ['⁖', '→', 'K', '→', '⊖']
    kappa = parser.kappa_score_optimized(sequence)
    assert 0.0 <= kappa <= 1.0
    assert kappa > 0.5  # Should be reasonably coherent

def test_interrogative_marker():
    parser = EnhancedLumerenParser()
    sequence = ['⸮', 'K', '→', '⊖']
    parsed = parser.parse(sequence)
    assert parsed[0]['type'] == 'illocution'
    assert parsed[0]['name'] == 'Interrogative'
