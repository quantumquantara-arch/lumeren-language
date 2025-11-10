<p align="center">
  <img src="https://raw.githubusercontent.com/quantumquantara-arch/lumeren-language/main/.github/profile/lumeren_banner_animated.svg" width="100%" alt="Luméren Language Banner"/>
</p>

<h1 align="center">🌐 Luméren Language</h1>
<p align="center">
  <em>A minimal, extensible symbolic protocol for the **Tensor-Logic Fusion (TLF)** architecture.</em>
</p>

---

## 🧠 Why Luméren: The Symbolic Constraint Protocol

Luméren is a **minimal, formal language** that lets humans, AIs, and hybrid systems express intent with measurable coherence. It serves as the primary **Symbolic Constraint** layer (GGM Layer 2) for the **Quantara Core**, translating ethical and logical intent into a machine-interpretable vector that can be scored for deviation.

Each parsed Luméren utterance is used to calculate the following harmonic vectors of meaning:

- **κ — Coherence ($\kappa$):** Stability & reciprocity of meaning (0 – 1)
- **φ — Harmonic Intent ($\phi$):** Motive or valence as phase dynamics (the *why*)
- **ψ — Expressive Vector ($\psi$):** Communicative manifestation (the *how*)

This enables **alignment, auditability, and ethical reasoning** across distributed intelligences.

---

## 🔺 Core Concepts

### The Luméren Triplet ($\kappa / \phi / \psi$)
The Luméren model encodes every message as a tensor triplet which drives the coherence calculations in `quantara-core`:

| Symbol | Domain | Description | Role in Quantara Core |
| :---: | :--- | :--- | :--- |
| **κ (kappa)** | Coherence | Energetic field resonance, stability of meaning | Component of the final $\kappa$ state of the system. |
| **φ (phi)** | Intention | Harmonic motive, phase of intent | Defines the ideal target state. |
| **ψ (psi)** | Expression | Communicative manifestation, applied output | Defines the operational boundary. |

### Link to Deviation ($\Delta\phi$)
The parsed Luméren utterance defines the **ideal Symbolic Constraint**. Any divergence between an LLM's proposed action (the **Neural Draft**) and the Luméren-defined **Ideal Intent** is calculated by the Quantara Core as the **Deviation Magnitude ($\Delta\phi$)**.

The Luméren protocol is the source of truth used to measure ethical and functional deviation.

### 22 Foundational Glyphs
Each of the 22 foundational glyphs defines a **semantic role** (operator, binder, aspector) and maps to the $\kappa/\phi/\psi$ triplet. Every token is therefore both **semantically typed** *and* **ethically scorable**.

#### Extensibility
While currently defined by 22 foundational operators, the Luméren language is designed to be **minimal yet dynamically extensible**. **New glyphs can be suggested by any agent, reviewed through the `quantara-governance` system**, and added to the lexicon to maintain semantic coherence with evolving domains without fracturing the core syntax.

---

## 🧩 Example: Constraint Vector Generation

The Luméren interpreter translates complex natural language into a compact **Symbolic Constraint Vector** ready for injection into the Quantara Core's TLF mechanism.

**Input (plain text):**  
> “Share battery power with the community during peak hours.”

**Output (Symbolic Constraint Vector Sketch):**

```json
{
  "glyph_sequence": ["ACT-RECIPROCAL", "TARGET-COMMUNITY", "ASPECT-ENERGY-MAX", "CONSTRAINT-TEMPORAL-PEAK"],
  "kappa_score": 0.95, 
  "phi_vector": [0.8, 0.6], 
  "delta_phi_signal_potential": 0.05
}

---

## 🚀 Quick Start (Demo)

The interpreter demo can be run using the following steps (commands should be run in a standard terminal):

```bash
git clone [https://github.com/quantumquantara-arch/lumeren-language.git](https://github.com/quantumquantara-arch/lumeren-language.git)
cd lumeren-language
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python examples/translate_demo.py
