# lumeren_core/translator.py
# Stub for translation functions to build lexicon - expand with actual glyph mappings

def translate_to_lumeren(english):
    # Placeholder: Map to glyphs based on lexicon (to be built)
    # Example mappings from primitives
    mapping = {
        'existence': '⊙',
        'observes': '→',
        'change': 'Â',
        'coherence': 'K',
        # Add more from lexicon: e.g., 'sentient': ':.', 'harm': 'Y Â', etc.
    }
    # Simple replace for demo - real impl would parse semantics
    for word, glyph in mapping.items():
        english = english.replace(word, glyph)
    return english  # Return glyph string

def translate_to_english(lumeren):
    # Reverse mapping
    mapping = {
        '⊙': 'existence',
        '→': 'observes',
        'Â': 'change',
        'K': 'coherence',
    }
    for glyph, word in mapping.items():
        lumeren = lumeren.replace(glyph, word)
    return lumeren
