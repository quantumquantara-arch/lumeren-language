"""
Enhanced Luméren Parser with Error Handling and Repair
"""

import numpy as np

class EnhancedLumerenParser:
    def __init__(self):
        self.glyphs = {
            # Primitives
            \"月\": {\"type\": \"primitive\", \"name\": \"Existence\", \"required\": False},
            \"今\": {\"type\": \"primitive\", \"name\": \"Change\", \"required\": False},
            \"凵\": {\"type\": \"primitive\", \"name\": \"Boundary\", \"required\": False},
            \"⁖\": {\"type\": \"primitive\", \"name\": \"Observer\", \"required\": False},
            
            # Invariants
            \"K\": {\"type\": \"invariant\", \"name\": \"Coherence\", \"required\": True},
            \"圈\": {\"type\": \"invariant\", \"name\": \"Relation\", \"required\": False},
            \"⊖\": {\"type\": \"invariant\", \"name\": \"Target\", \"required\": True},
            \"⊗\": {\"type\": \"operator\", \"name\": \"Bind\", \"required\": False},
            
            # Operators
            \"⚭⚭\": {\"type\": \"operator\", \"name\": \"Tensor-And\"},
            \"⚮⚮\": {\"type\": \"operator\", \"name\": \"Tensor-Or\"},
            \"⚯⚯\": {\"type\": \"operator\", \"name\": \"Tensor-Xor\"},
            \"⊸\": {\"type\": \"operator\", \"name\": \"Tensor-Imply\"},
            \"弁\": {\"type\": \"operator\", \"name\": \"Veyn\"},
            
            # Transformations
            \"☽\": {\"type\": \"transformation\", \"name\": \"Not\"},
            \"⟿\": {\"type\": \"transformation\", \"name\": \"Become\"},
            \"→\": {\"type\": \"transformation\", \"name\": \"Transform\"},
            
            # Illocution
            \"⸮\": {\"type\": \"illocution\", \"name\": \"Interrogative\"},
        }
    
    def parse_with_repair(self, sequence):
        \"\"\"Parse and suggest repairs for invalid sequences\"\"\"
        parsed = self.parse(sequence)
        is_valid, errors = self.validate_detailed(sequence)
        
        if not is_valid:
            repaired = self.repair_sequence(sequence, errors)
            return {
                'original': sequence,
                'parsed': parsed,
                'valid': False,
                'errors': errors,
                'repaired': repaired
            }
        
        return {
            'original': sequence,
            'parsed': parsed,
            'valid': True,
            'errors': [],
            'repaired': None
        }
    
    def parse(self, sequence):
        \"\"\"Parse glyph sequence\"\"\"
        return [self.glyphs.get(g, {\"type\": \"unknown\", \"name\": g}) for g in sequence]
    
    def validate_detailed(self, sequence):
        \"\"\"Validate with detailed error reporting\"\"\"
        errors = []
        
        # Check for unknown glyphs
        for g in sequence:
            if g not in self.glyphs:
                errors.append(f\"Unknown glyph: {g}\")
        
        # Check for required elements
        has_k = any(g == 'K' for g in sequence)
        has_target = any(g == '⊖' for g in sequence)
        has_primitive = any(g in ['月', '今', '凵', '⁖'] for g in sequence)
        
        if not has_k:
            errors.append(\"Missing K (Coherence axis) - required for valid sequence\")
        if not has_target:
            errors.append(\"Missing ⊖ (Target) - sequence needs endpoint\")
        if not has_primitive:
            errors.append(\"Missing primitive (月,今,凵,⁖) - sequence needs foundation\")
        
        return (len(errors) == 0, errors)
    
    def repair_sequence(self, sequence, errors):
        \"\"\"Suggest repairs for invalid sequence\"\"\"
        repaired = list(sequence)
        
        # Auto-fix: Add missing K
        if \"Missing K\" in str(errors):
            # Insert K after first glyph
            if len(repaired) > 0:
                repaired.insert(1, '→')
                repaired.insert(2, 'K')
        
        # Auto-fix: Add missing target
        if \"Missing ⊖\" in str(errors):
            repaired.extend(['→', '⊖'])
        
        # Auto-fix: Add missing primitive
        if \"Missing primitive\" in str(errors):
            repaired.insert(0, '⁖')
            if repaired[1] != '→':
                repaired.insert(1, '→')
        
        return repaired
    
    def kappa_score_optimized(self, sequence):
        \"\"\"Vectorized κ-score calculation\"\"\"
        parsed = self.parse(sequence)
        
        # Structural stability (vectorized)
        type_counts = {}
        for g in parsed:
            t = g['type']
            type_counts[t] = type_counts.get(t, 0) + 1
        
        stability = 1.0 - (np.std(list(type_counts.values())) / len(sequence))
        
        # Semantic precision
        unknown_count = sum(1 for g in parsed if g['type'] == 'unknown')
        precision = 1.0 - (unknown_count / len(sequence))
        
        # Ambiguity
        ambiguity = 0.1 + (0.1 * (len(sequence) > 10))
        
        kappa = (stability * precision) / ambiguity
        return np.clip(kappa, 0, 1)

if __name__ == \"__main__\":
    parser = EnhancedLumerenParser()
    
    # Test invalid sequence
    invalid_seq = ['⁖', '→', '⊖']  # Missing K
    result = parser.parse_with_repair(invalid_seq)
    
    print(\"=== Parser Enhancement Demo ===\")
    print(f\"Original: {' '.join(result['original'])}\")
    print(f\"Valid: {result['valid']}\")
    if not result['valid']:
        print(f\"Errors: {result['errors']}\")
        print(f\"Repaired: {' '.join(result['repaired'])}\")
