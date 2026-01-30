"""
Integration tests for Luméren workflow
"""
import pytest
import sys
sys.path.append('..')
from lumeren_core.enhanced_parser import EnhancedLumerenParser
from lumeren_core.coherence import kappa_score

def test_full_translation_pipeline():
    parser = EnhancedLumerenParser()
    
    # Natural language -> Glyphs -> Validation
    glyphs = ['⁖', '→', 'K', '→', '圈', '→', '⊖']
    result = parser.parse_with_repair(glyphs)
    
    assert result['valid'] == True
    kappa = parser.kappa_score_optimized(glyphs)
    assert kappa > 0.7

def test_ethical_scenario():
    parser = EnhancedLumerenParser()
    
    # Privacy-first sequence
    privacy_seq = ['⁖', '→', 'K', '→', '凵', '⊗', '⊖']
    result = parser.parse_with_repair(privacy_seq)
    
    assert result['valid'] == True
    assert result['parsed'][2]['name'] == 'Coherence'
    assert result['parsed'][4]['name'] == 'Boundary'
