# AP Chemistry Unit 2 — detailed MCQ bank (same JSON shape as Unit 1).
# Loaded by rebuild_unit2_bank.py; subsection strings must match Subsection.java / quiz.js.

from unit2_bulk import bulk_unit2_questions


def _q(subsection: str, stimulus: str, stem: str, correct: str, options: list[tuple[str, str, str]]) -> dict:
    labels = "ABCD"
    return {
        "subsection": subsection,
        "stimulus": stimulus,
        "stem": stem,
        "correct": correct,
        "options": [
            {"label": labels[i], "text": options[i][0], "rationale": options[i][1]} for i in range(4)
        ],
    }


def get_unit2_questions() -> list[dict]:
    """Four items per subsection (2.1–2.7); each rationale is written for AP-style review."""
    out: list[dict] = []

    S21 = "2.1 Types of Chemical Bonds"
    S22 = "2.2 Intramolecular Force and Potential Energy"
    S23 = "2.3 Structure of Ionic Solids"
    S24 = "2.4 Structure of Metals and Alloys"
    S25 = "2.5 Lewis Diagrams"
    S26 = "2.6 Resonance and Formal Charge"
    S27 = "2.7 VSEPR and Hybridization"

    # --- 2.1 ---
    out.append(
        _q(
            S21,
            "",
            "Which description best matches the bonding in solid NaCl?",
            "B",
            [
                (
                    "A continuous covalent network of shared electron pairs only",
                    "Incorrect. NaCl is composed of Na\u207a and Cl\u207b ions held by ionic attractions, not an extended covalent network like diamond.",
                ),
                (
                    "Ions arranged in a three-dimensional lattice with electrostatic attractions",
                    "Correct. Ionic solids consist of alternating cations and anions in a repeating lattice; stability comes from Coulombic attraction.",
                ),
                (
                    "Neutral NaCl molecules held by London dispersion forces only",
                    "Incorrect. The ionic model emphasizes ions in a lattice, not discrete NaCl molecules with only dispersion forces.",
                ),
                (
                    "Delocalized electrons moving through fixed Na and Cl nuclei only",
                    "Incorrect. That picture fits metallic bonding, not the localized ion charges in NaCl.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S21,
            "",
            "Compared to a C–C bond in ethane, the intramolecular O–H bond inside a single water molecule is best classified as:",
            "C",
            [
                (
                    "Intermolecular because water can hydrogen-bond to other molecules",
                    "Incorrect. Hydrogen bonding between separate water molecules is intermolecular; the O–H bond inside one H₂O is intramolecular.",
                ),
                (
                    "Ionic because oxygen is more electronegative than hydrogen",
                    "Incorrect. Large ΔEN can give polar covalent character, but O–H is still modeled as a covalent bond within the molecule.",
                ),
                (
                    "Polar covalent: shared electrons are pulled toward oxygen",
                    "Correct. Oxygen is more electronegative than hydrogen, so the bond is covalent with a partial negative on O and partial positive on H.",
                ),
                (
                    "Nonpolar covalent because both atoms appear in many organic molecules",
                    "Incorrect. Polarity depends on ΔEN between the two bonded atoms, not on general organic occurrence.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S21,
            "",
            "Which interaction is strictly intermolecular?",
            "D",
            [
                (
                    "The Si–O bonds within a quartz network",
                    "Incorrect. Those are strong bonds within an extended structure (intramolecular / network covalent in the usual particulate model).",
                ),
                (
                    "The C\u2261C triple bond in ethyne",
                    "Incorrect. That bond is inside one molecule.",
                ),
                (
                    "The N\u2261N triple bond in N₂",
                    "Incorrect. That is an intramolecular covalent bond.",
                ),
                (
                    "Dipole–dipole attractions between separate acetone molecules in the liquid",
                    "Correct. These attractions act between different molecules in the bulk phase.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S21,
            "",
            "Two identical chlorine atoms form Cl₂. The bond is best described as:",
            "A",
            [
                (
                    "Nonpolar covalent with equal sharing",
                    "Correct. Identical atoms have the same electronegativity, so electron density is shared symmetrically.",
                ),
                (
                    "Polar covalent with δ− on the left Cl",
                    "Incorrect. There is no basis to assign different partial charges to identical atoms.",
                ),
                (
                    "Ionic with separate Cl\u207a and Cl\u207b ions in the bond",
                    "Incorrect. Electron transfer to form ions is not the model for homonuclear diatomic chlorine.",
                ),
                (
                    "Purely metallic",
                    "Incorrect. Cl₂ is a molecular substance, not a metal.",
                ),
            ],
        )
    )

    # --- 2.2 ---
    out.append(
        _q(
            S22,
            "",
            "At the equilibrium bond distance, the potential energy of a diatomic molecule is:",
            "B",
            [
                (
                    "Always zero by definition",
                    "Incorrect. The zero of potential energy is arbitrary; what matters is the minimum relative to separated atoms.",
                ),
                (
                    "At a minimum for that bond’s potential-energy curve",
                    "Correct. Equilibrium separation corresponds to the bottom of the well on a typical bond-energy diagram.",
                ),
                (
                    "At a maximum because attraction and repulsion cancel",
                    "Incorrect. At the minimum, net force is zero, but the energy is low, not at a crest.",
                ),
                (
                    "Unrelated to bond length",
                    "Incorrect. The energy curve is explicitly a function of internuclear separation.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S22,
            "",
            "Which change requires an input of energy in the usual bond-dissociation convention?",
            "C",
            [
                (
                    "Forming bonds from gas-phase atoms",
                    "Incorrect. Bond formation typically releases energy as the system drops toward the potential minimum.",
                ),
                (
                    "Moving bonded atoms even closer than the equilibrium bond length from a compressed state",
                    "Incorrect. That can release energy if starting from an artificially stretched state, but the standard BDE question focuses on breaking bonds.",
                ),
                (
                    "Homolytically breaking one mole of gaseous H–H bonds into H atoms",
                    "Correct. Breaking bonds separates atoms and raises the system’s energy; ΔH for bond breaking is endothermic.",
                ),
                (
                    "Allowing atoms to approach from infinite separation to the equilibrium bond length",
                    "Incorrect. That process corresponds to bond formation and is exothermic relative to separated atoms.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S22,
            "",
            "For comparable single bonds between the same two elements, a shorter bond most often implies:",
            "A",
            [
                (
                    "Greater bond strength (higher bond dissociation energy)",
                    "Correct. Shorter bonds usually mean stronger attraction and harder dissociation for the same bond order and pair of elements.",
                ),
                (
                    "Weaker bonding and easier dissociation",
                    "Incorrect. That trend is usually opposite for similar bond types.",
                ),
                (
                    "No relationship to bond energy",
                    "Incorrect. Length and strength are correlated in introductory models.",
                ),
                (
                    "A lower potential energy for separated atoms",
                    "Incorrect. Separated atoms are typically higher in energy than the bonded minimum.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S22,
            "",
            "Why does a double bond between the same two atoms typically have a higher bond energy than a single bond between them?",
            "D",
            [
                (
                    "Because double bonds are always longer",
                    "Incorrect. Multiple bonds are usually shorter than single bonds between the same atoms.",
                ),
                (
                    "Because π orbitals do not overlap",
                    "Incorrect. π overlap is part of the multiple-bond model.",
                ),
                (
                    "Because only σ bonds store energy",
                    "Incorrect. π bonding contributes to overall bond strength.",
                ),
                (
                    "Because greater electron density between nuclei lowers energy relative to a single bond",
                    "Correct. Additional bonding interactions (σ + π) increase net stabilization for a double bond versus a single bond.",
                ),
            ],
        )
    )

    # --- 2.3 ---
    out.append(
        _q(
            S23,
            "",
            "Which statement about lattice energy is most accurate in a qualitative AP argument?",
            "B",
            [
                (
                    "Lattice energy is unrelated to ion charge",
                    "Incorrect. Coulombic attraction depends strongly on ion charges; higher |q| usually means a more exothermic lattice formation (larger magnitude).",
                ),
                (
                    "For similar structures, increasing ion charge magnitude tends to increase lattice energy magnitude",
                    "Correct. Coulombic attraction scales with |q₁q₂|; higher charges pull ions together more strongly in the lattice model.",
                ),
                (
                    "Larger ions always give larger lattice energies",
                    "Incorrect. Larger ions increase separation and usually weaken attraction compared with smaller ions of the same charge.",
                ),
                (
                    "Ionic solids contain freely moving molecular ions like an ideal gas",
                    "Incorrect. Ions occupy fixed lattice sites with vibrational motion, not gas-like free motion.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S23,
            "",
            "Why are many ionic crystals brittle when hammered?",
            "C",
            [
                (
                    "Because metallic layers slip easily",
                    "Incorrect. Layer slipping is a metals explanation, not the primary ionic one.",
                ),
                (
                    "Because covalent bonds rotate freely",
                    "Incorrect. Ionic lattices do not behave like freely rotating molecular chains.",
                ),
                (
                    "Because shifting layers can bring like charges adjacent, causing repulsion and fracture",
                    "Correct. Small shifts can align ions of the same sign along planes, producing strong repulsion.",
                ),
                (
                    "Because ionic bonds are weaker than all covalent bonds",
                    "Incorrect. Brittleness is about mechanical response, not a blanket comparison of bond strengths.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S23,
            "",
            "In the particulate model, a formula unit of CaF₂ in the crystal contains:",
            "A",
            [
                (
                    "One Ca\u00b2\u207a and two F\u207b in the stoichiometric ratio",
                    "Correct. The formula reflects charge balance: one calcium ion and two fluoride ions per formula unit.",
                ),
                (
                    "One Ca\u207a and one F\u207b",
                    "Incorrect. That would not balance charges for calcium and fluorine in CaF₂.",
                ),
                (
                    "Neutral CaF₂ molecules only",
                    "Incorrect. The extended lattice model emphasizes ions, not isolated neutral triatomic molecules as the sole picture.",
                ),
                (
                    "Delocalized electrons only",
                    "Incorrect. That describes metals, not the ionic fluoride lattice.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S23,
            "",
            "Compared to Na\u207a and Cl\u207b, Mg\u00b2\u207a and O\u00b2\u207b typically produce a crystal with:",
            "D",
            [
                (
                    "Lower lattice energy magnitude because both ions are smaller",
                    "Incorrect. Smaller, higher-charge ions usually strengthen lattice attractions.",
                ),
                (
                    "Identical lattice energy because both are 1:1 salts",
                    "Incorrect. MgO is not 1:1 in the same way as NaCl regarding charge magnitudes; MgO has doubly charged ions.",
                ),
                (
                    "Weaker attraction because oxygen is less electronegative than chlorine",
                    "Incorrect. Lattice energy arguments focus on ion charges and distances, not EN of neutral atoms alone.",
                ),
                (
                    "Greater lattice energy magnitude due to higher charges and short ion separation",
                    "Correct. +2/−2 attractions and small ions combine to a very stable lattice.",
                ),
            ],
        )
    )

    # --- 2.4 ---
    out.append(
        _q(
            S24,
            "",
            "The ‘electron sea’ model explains which observation best?",
            "B",
            [
                (
                    "Ionic crystals shattering along planes",
                    "Incorrect. That is tied to ion stacking and repulsion, not delocalized electrons.",
                ),
                (
                    "Electrical conductivity in copper wire",
                    "Correct. Mobile delocalized electrons can move under a potential difference.",
                ),
                (
                    "Hydrogen bonding in ice",
                    "Incorrect. That is molecular and intermolecular, not metallic.",
                ),
                (
                    "π delocalization in benzene",
                    "Incorrect. That is a covalent resonance picture in a molecule, not bulk metallic bonding.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S24,
            "",
            "A substitutional alloy is formed when:",
            "A",
            [
                (
                    "Some host metal atoms are replaced by atoms of similar size",
                    "Correct. Substitutional alloys substitute solute atoms onto lattice sites of the solvent metal.",
                ),
                (
                    "Only nonmetals fill interstitial holes",
                    "Incorrect. That pattern is closer to an interstitial model with small atoms in voids.",
                ),
                (
                    "Ions pack in an NaCl-type lattice only",
                    "Incorrect. That describes an ionic structure type, not the general definition of substitutional alloying.",
                ),
                (
                    "All electrons are localized in lone pairs",
                    "Incorrect. Metallic bonding relies on delocalization.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S24,
            "",
            "Why can metals be drawn into wires (ductile)?",
            "C",
            [
                (
                    "Because ionic layers repel and slide",
                    "Incorrect. That is not the primary metals explanation.",
                ),
                (
                    "Because all metallic bonds break and reform as gases",
                    "Incorrect. The solid remains metallic while layers slip.",
                ),
                (
                    "Because metal ions can slide past one another while the electron sea maintains attraction",
                    "Correct. Delocalized electrons still attract cations after slip, so the material does not shatter like many ionic solids.",
                ),
                (
                    "Because hydrogen bonds reform continuously",
                    "Incorrect. Metals are not held by hydrogen bonding.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S24,
            "",
            "Compared to a typical ionic solid, a metal’s melting point trend is not universally higher or lower, but metals are distinguished at the particulate level by:",
            "D",
            [
                (
                    "Fixed molecular formula units only",
                    "Incorrect. Metals are not described as discrete small molecules in the sea model.",
                ),
                (
                    "Complete absence of positive centers in the lattice",
                    "Incorrect. Cations (or atomic cores) are present in the metallic lattice.",
                ),
                (
                    "Only van der Waals attractions",
                    "Incorrect. Metallic bonding is stronger than dispersion-only solids for many metals.",
                ),
                (
                    "Delocalized valence electrons shared among many atoms",
                    "Correct. This feature differentiates metallic bonding from localized ionic or molecular pictures.",
                ),
            ],
        )
    )

    # --- 2.5 ---
    out.append(
        _q(
            S25,
            "",
            "How many valence electrons must be accounted for in a Lewis structure for phosphate ion PO₄³⁻?",
            "B",
            [
                (
                    "5",
                    "Incorrect. That counts only phosphorus valence electrons and ignores oxygen and charge.",
                ),
                (
                    "32",
                    "Correct. P contributes 5, each O contributes 6 (×4 = 24), and the 3− charge adds 3: total 32 valence electrons.",
                ),
                (
                    "26",
                    "Incorrect. This misses electrons from oxygen or the charge.",
                ),
                (
                    "29",
                    "Incorrect. Re-sum valence electrons including the anionic charge.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S25,
            "",
            "In a correct Lewis structure for formaldehyde CH₂O with carbon central, how many lone pairs are on the oxygen atom in the usual octet representation?",
            "C",
            [
                (
                    "None",
                    "Incorrect. Oxygen typically completes an octet with lone pairs in this molecule.",
                ),
                (
                    "One",
                    "Incorrect. That would not give oxygen eight electrons in a typical double-bonded aldehyde oxygen.",
                ),
                (
                    "Two",
                    "Correct. A double-bonded oxygen with two lone pairs gives eight valence electrons on O.",
                ),
                (
                    "Three",
                    "Incorrect. Three lone pairs plus a double bond would exceed an octet on oxygen in this model.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S25,
            "",
            "Which violates the octet rule for a second-row central atom in a common AP Lewis drill?",
            "A",
            [
                (
                    "BF₃ with boron as central atom and three B–F single bonds",
                    "Correct. Boron has only six valence electrons in that structure—an incomplete octet that AP often highlights.",
                ),
                (
                    "NH₃ with three N–H bonds and one lone pair on nitrogen",
                    "Incorrect. Nitrogen has a complete octet in NH₃.",
                ),
                (
                    "H₂O with two O–H bonds and two lone pairs on oxygen",
                    "Incorrect. Oxygen has a complete octet.",
                ),
                (
                    "CH₄ with four C–H bonds",
                    "Incorrect. Carbon has a complete octet.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S25,
            "",
            "The skeleton N–C–N for cyanamide H₂NCN (simplified) reminds you that the least electronegative atom that can expand the skeleton is often placed central. For HCN, the skeleton is:",
            "A",
            [
                (
                    "H–C–N",
                    "Correct. Carbon is less electronegative than nitrogen and forms the chain H–C–N; the finished Lewis structure includes a C\u2261N triple bond.",
                ),
                (
                    "C–H–N",
                    "Incorrect. Hydrogen forms one bond and is not a central atom with two heavy-atom neighbors in HCN.",
                ),
                (
                    "N–H–C",
                    "Incorrect. That is not the usual connectivity for hydrogen cyanide.",
                ),
                (
                    "H–N–C",
                    "Incorrect. Nitrogen is not the central atom in the standard HCN Lewis skeleton.",
                ),
            ],
        )
    )

    # --- 2.6 ---
    out.append(
        _q(
            S26,
            "",
            "The carbonate ion CO₃²⁻ is often drawn with three equivalent C–O bonds experimentally because:",
            "B",
            [
                (
                    "The ion rapidly isomerizes between single and double bonds in time",
                    "Incorrect. Resonance is not mechanical flipping at ordinary timescales in this model.",
                ),
                (
                    "π electron density is delocalized over all three C–O linkages in the resonance hybrid",
                    "Correct. Multiple Lewis contributors average to equivalent C–O bonds in the hybrid.",
                ),
                (
                    "Carbon has a +2 formal charge in all structures",
                    "Incorrect. Formal charges vary by contributor; the hybrid rationalizes equal bond lengths.",
                ),
                (
                    "Oxygen never obeys an octet in carbonate",
                    "Incorrect. Oxygen can obey an octet in standard contributors.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S26,
            "",
            "In one Lewis contributor for ozone O₃ with a central O, a terminal O is double-bonded and the other terminal O is single-bonded. The actual O–O bond lengths:",
            "C",
            [
                (
                    "Match the single bond exactly in one pair and double in the other",
                    "Incorrect. Experimentally, ozone has intermediate character between single and double.",
                ),
                (
                    "Are impossible to measure",
                    "Incorrect. Bond lengths can be measured spectroscopically or by diffraction.",
                ),
                (
                    "Are intermediate between typical O–O single and double bonds due to delocalization",
                    "Correct. The resonance hybrid predicts partial double-bond character for both linkages.",
                ),
                (
                    "Prove ozone is always O=O–O with no resonance",
                    "Incorrect. The equal-ish bond lengths support delocalization.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S26,
            "",
            "For nitrate NO₃⁻, what is the formal charge on nitrogen in a contributor where N forms one N=O double bond and two N–O single bonds (assuming oxygens complete octets)?",
            "A",
            [
                (
                    "+1",
                    "Correct. A common bookkeeping gives N with four bonds worth of shared electrons in that skeleton; FC = 5 − 0 − 4 = +1 with the usual counting.",
                ),
                (
                    "0",
                    "Incorrect. Recompute formal charge for that contributor carefully.",
                ),
                (
                    "−1",
                    "Incorrect. Nitrogen is less electronegative than oxygen but formal charge depends on bonding pattern.",
                ),
                (
                    "+2",
                    "Incorrect. That overcounts positive character for this contributor.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S26,
            "",
            "When choosing the best set of resonance contributors, AP reasoning often prefers structures with:",
            "D",
            [
                (
                    "The largest possible formal charges on all atoms",
                    "Incorrect. Large magnitudes of FC usually mean a less important contributor.",
                ),
                (
                    "Negative formal charge on the least electronegative atom",
                    "Incorrect. Negative charge typically resides on more electronegative atoms in better contributors.",
                ),
                (
                    "Expanded octets on second-row elements only",
                    "Incorrect. That is not a general selection rule for all species.",
                ),
                (
                    "Formal charges closest to zero, with negative charge on more electronegative atoms when possible",
                    "Correct. This minimizes charge separation consistent with electronegativity.",
                ),
            ],
        )
    )

    # --- 2.7 ---
    out.append(
        _q(
            S27,
            "",
            "What is the molecular geometry of SF₄ if the central sulfur has four bonding domains and one lone pair (five total electron domains)?",
            "B",
            [
                (
                    "Tetrahedral",
                    "Incorrect. Tetrahedral is the geometry for four domains and no lone pairs on the central atom.",
                ),
                (
                    "Seesaw",
                    "Correct. Five domains with one lone pair in a trigonal-bipyramidal electron arrangement gives a seesaw molecular shape.",
                ),
                (
                    "Square planar",
                    "Incorrect. Square planar arises from six domains with two lone pairs in an octahedral-based arrangement.",
                ),
                (
                    "Trigonal planar",
                    "Incorrect. That corresponds to three domains around the central atom.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S27,
            "",
            "The H–N–H bond angle in NH₃ is slightly less than the ideal 109.5° because:",
            "A",
            [
                (
                    "A lone pair on nitrogen repels bonding pairs more strongly than bonding pairs repel each other",
                    "Correct. Lone-pair–bond-pair repulsion compresses angles between bonds.",
                ),
                (
                    "Nitrogen uses sp hybridization only",
                    "Incorrect. NH₃ is commonly described with sp³ hybridization on nitrogen.",
                ),
                (
                    "Hydrogen atoms are too large",
                    "Incorrect. The angle trend is explained by electron-domain repulsion, not H size alone.",
                ),
                (
                    "Ammonia is linear",
                    "Incorrect. NH₃ is pyramidal.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S27,
            "",
            "What is the hybridization of the central carbon in ethene C₂H₄?",
            "C",
            [
                (
                    "sp³",
                    "Incorrect. sp³ would suggest four σ domains in a tetrahedral arrangement; the π bond in C=C requires a different hybrid picture.",
                ),
                (
                    "sp",
                    "Incorrect. sp fits two σ domains (linear).",
                ),
                (
                    "sp2",
                    "Correct. Each carbon is trigonal planar with three σ domains (two C–H and one C–C σ component), described by sp² hybridization.",
                ),
                (
                    "unhybridized p only",
                    "Incorrect. σ framework still uses hybrid orbitals in the usual model.",
                ),
            ],
        )
    )
    out.append(
        _q(
            S27,
            "",
            "XeF₄ with square planar molecular geometry implies how many lone pairs on xenon in the octahedral-based electron-domain picture?",
            "D",
            [
                (
                    "Zero",
                    "Incorrect. Square planar is not the shape for six bonding pairs only.",
                ),
                (
                    "One",
                    "Incorrect. One lone pair on six domains gives square pyramidal molecular geometry.",
                ),
                (
                    "Two lone pairs that are cis (90° apart) on the octahedron",
                    "Incorrect. Pairing lone pairs at 90° maximizes lone-pair repulsion; XeF\u2084 places lone pairs trans (180° apart).",
                ),
                (
                    "Two lone pairs arranged trans on an octahedral electron geometry",
                    "Correct. Six domains: four F and two lone pairs opposite each other gives square planar molecular geometry.",
                ),
            ],
        )
    )

    seen: set[tuple[str, str]] = {(q["subsection"], q["stem"]) for q in out}
    out.extend(bulk_unit2_questions(seen))
    return out