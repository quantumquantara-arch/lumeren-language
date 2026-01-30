/**
 * Luméren Romanization System (LRS)
 * Bidirectional conversion between glyphs and Latin alphabet codes
 */

const ROMAN_TO_GLYPH = {
    // Primitives
    'EX': '月',    // Existence
    'CH': '今',    // Change
    'BO': '凵',    // Boundary
    'OB': '⁖',    // Observer
    
    // Invariants
    'KO': 'K',     // Coherence
    'RE': '圈',    // Relation
    'TA': '⊖',    // Target
    'BI': '⊗',    // Bind
    
    // Operators
    'AND': '⚭⚭',  // Tensor-And
    'OR': '⚮⚮',   // Tensor-Or
    'XOR': '⚯⚯',  // Tensor-Xor
    'IMP': '⊸',   // Tensor-Imply
    
    // Transformations
    'VE': '弁',    // Veyn
    'NO': '☽',    // Not
    'BE': '⟿',    // Become
    'TO': '→',    // Transform
    'BT': '⊣⊢',   // Between
    
    // Illocution
    'QU': '⸮',    // Interrogative
};

// Create reverse mapping
const GLYPH_TO_ROMAN = {};
for (const [roman, glyph] of Object.entries(ROMAN_TO_GLYPH)) {
    GLYPH_TO_ROMAN[glyph] = roman;
}

function romanToLumeren(text, delimiter = '-') {
    const codes = text.toUpperCase().split(delimiter);
    const glyphs = codes.map(code => ROMAN_TO_GLYPH[code] || code);
    return glyphs.join(' ');
}

function lumerenToRoman(glyphs, delimiter = '-') {
    if (typeof glyphs === 'string') {
        glyphs = glyphs.split(' ');
    }
    const codes = glyphs.map(g => GLYPH_TO_ROMAN[g] || g);
    return codes.join(delimiter);
}

function isValidRoman(text, delimiter = '-') {
    const codes = text.toUpperCase().split(delimiter);
    return codes.every(code => code in ROMAN_TO_GLYPH);
}

// Export for Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { romanToLumeren, lumerenToRoman, isValidRoman };
}

// Example usage
if (typeof require !== 'undefined' && require.main === module) {
    console.log('=== Luméren Romanization Demo ===\n');
    
    const roman = 'OB-TO-KO-TO-TA';
    const glyphs = romanToLumeren(roman);
    console.log(\Roman:  \\);
    console.log(\Glyphs: \\);
    console.log();
    
    const original = '⁖ ⚭⚭ 月 → K → 圈 ⊗ ⊖';
    const romanBack = lumerenToRoman(original);
    console.log(\Glyphs: \\);
    console.log(\Roman:  \\);
}
