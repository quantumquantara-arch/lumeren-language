# examples/translations/english_to_lumeren.py
# Example script for translating English sentences to Lumeren glyphs and back, to test lexicon functionality

from lumeren_core.translator import translate_to_lumeren, translate_to_english  # Assume these exist or to be implemented in translator.py

# Simple sentence translations for testing various issues: ambiguity, context, cross-species concepts
sentences = [
    "The quick brown fox jumps over the lazy dog.",  # Pangram for basic lexicon coverage
    "Existence observes change in coherence.",  # Direct mapping to primitives: ⊙ → K → Â
    "Do not harm sentient beings.",  # Ethical dilemma, testing invariants and operators
    "Share knowledge freely across intelligences.",  # Cross-species communication intent
    "The alien entity communicates via light patterns."  # Hypothetical non-human scenario
]

for sentence in sentences:
    lumeren = translate_to_lumeren(sentence)
    back_to_english = translate_to_english(lumeren)
    print(f"Original: {sentence}")
    print(f"Luméren: {lumeren}")
    print(f"Round-trip: {back_to_english}")
    assert back_to_english.lower() == sentence.lower(), f"Translation mismatch for '{sentence}'"

# If translator.py doesn't exist yet, implement stubs here or in core
