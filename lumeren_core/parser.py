"""
Luméren Semantic Parser
Parses glyph sequences into semantic structures
"""

class LumerenParser:
    def __init__(self):
        self.glyphs = {
            # Primitives
            "月": {"type": "primitive", "name": "Existence"},
            "今": {"type": "primitive", "name": "Change"},
            "凵": {"type": "primitive", "name": "Boundary"},
            "⁖": {"type": "primitive", "name": "Observer"},
            
            # Invariants
            "K": {"type": "invariant", "name": "Coherence"},
            "圈": {"type": "invariant", "name": "Relation"},
            "⊖": {"type": "invariant", "name": "Target"},
            
            # Operators
            "⚭⚭": {"type": "operator", "name": "Tensor-And"},
            "⚮⚮": {"type": "operator", "name": "Tensor-Or"},
            "⚯⚯": {"type": "operator", "name": "Tensor-Xor"},
            "⊸": {"type": "operator", "name": "Tensor-Imply"},
            "弁": {"type": "operator", "name": "Veyn"},
            "⊗": {"type": "operator", "name": "Bind"},
            
            # Transformations
            "☽": {"type": "transformation", "name": "Not"},
            "⟿": {"type": "transformation", "name": "Become"},
            "→": {"type": "transformation", "name": "Transform"},
        }
    
    def parse(self, sequence):
        """Parse glyph sequence"""
        return [self.glyphs.get(g, {"type": "unknown", "name": g}) for g in sequence]
    
    def validate(self, sequence):
        """Validate sequence"""
        parsed = self.parse(sequence)
        unknown = [g for g in parsed if g["type"] == "unknown"]
        return len(unknown) == 0

if __name__ == "__main__":
    parser = LumerenParser()
    
    # Test with Gemini's sequence
    gemini_seq = ["⁖", "⚭⚭", "月", "→", "K", "→", "圈", "⊗", "⊖"]
    
    print("=== Parsing Gemini's Sequence ===")
    print(f"Glyphs: {' '.join(gemini_seq)}")
    print(f"Valid: {parser.validate(gemini_seq)}")
    
    print("\nStructure:")
    for g in parser.parse(gemini_seq):
        print(f"  {g}")
