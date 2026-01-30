"""
Luméren Romanization System (LRS)
Bidirectional conversion between glyphs and Latin alphabet codes
"""

# Roman code to glyph mapping
ROMAN_TO_GLYPH = {
    # Primitives
    'EX': '月',    # Existence
    'CH': '今',    # Change
    'BO': '凵',    # Boundary
    'OB': '⁖',    # Observer
    
    # Invariants
    'KO': 'K',     # Coherence
    'RE': '圈',    # Relation
    'TA': '⊖',    # Target
    'BI': '⊗',    # Bind
    
    # Operators
    'AND': '⚭⚭',  # Tensor-And
    'OR': '⚮⚮',   # Tensor-Or
    'XOR': '⚯⚯',  # Tensor-Xor
    'IMP': '⊸',   # Tensor-Imply
    
    # Transformations
    'VE': '弁',    # Veyn
    'NO': '☽',    # Not
    'BE': '⟿',    # Become
    'TO': '→',    # Transform
    'BT': '⊣⊢',   # Between
    
    # Illocution
    'QU': '⸮',    # Interrogative
}

# Glyph to Roman code (reverse mapping)
GLYPH_TO_ROMAN = {v: k for k, v in ROMAN_TO_GLYPH.items()}

def roman_to_lumeren(text, delimiter='-'):
    \"\"\"
    Convert Roman codes to Luméren glyphs
    
    Args:
        text: Roman code string (e.g., "OB-TO-KO-TO-TA")
        delimiter: Separator between codes (default: '-')
    
    Returns:
        Glyph string (e.g., "⁖ → K → ⊖")
    \"\"\"
    codes = text.upper().split(delimiter)
    glyphs = [ROMAN_TO_GLYPH.get(code, code) for code in codes]
    return ' '.join(glyphs)

def lumeren_to_roman(glyphs, delimiter='-'):
    \"\"\"
    Convert Luméren glyphs to Roman codes
    
    Args:
        glyphs: Glyph string or list (e.g., "⁖ → K → ⊖")
        delimiter: Separator for output (default: '-')
    
    Returns:
        Roman code string (e.g., "OB-TO-KO-TO-TA")
    \"\"\"
    if isinstance(glyphs, str):
        glyphs = glyphs.split()
    
    codes = [GLYPH_TO_ROMAN.get(g, g) for g in glyphs]
    return delimiter.join(codes)

def is_valid_roman(text, delimiter='-'):
    \"\"\"Check if all codes are valid Roman codes\"\"\"
    codes = text.upper().split(delimiter)
    return all(code in ROMAN_TO_GLYPH for code in codes)

# Example usage
if __name__ == "__main__":
    # Roman to Glyphs
    roman = "OB-TO-KO-TO-TA"
    glyphs = roman_to_lumeren(roman)
    print(f"Roman:  {roman}")
    print(f"Glyphs: {glyphs}")
    print()
    
    # Glyphs to Roman
    original_glyphs = "⁖ ⚭⚭ 月 → K → 圈 ⊗ ⊖"
    roman_back = lumeren_to_roman(original_glyphs)
    print(f"Glyphs: {original_glyphs}")
    print(f"Roman:  {roman_back}")
    print()
    
    # Validation
    print(f"Valid: {is_valid_roman('OB-TO-KO-TO-TA')}")  # True
    print(f"Valid: {is_valid_roman('OB-TO-XX-TO-TA')}")  # False
