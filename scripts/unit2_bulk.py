# Extra Unit 2 MCQs to bring the unit total near Unit 1 (~111 items).
# Merged by unit2_items.get_unit2_questions(); deduped by (subsection, stem).

from __future__ import annotations

S21 = "2.1 Types of Chemical Bonds"
S22 = "2.2 Intramolecular Force and Potential Energy"
S23 = "2.3 Structure of Ionic Solids"
S24 = "2.4 Structure of Metals and Alloys"
S25 = "2.5 Lewis Diagrams"
S26 = "2.6 Resonance and Formal Charge"
S27 = "2.7 VSEPR and Hybridization"


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


def _push(seen: set[tuple[str, str]], acc: list[dict], item: dict) -> None:
    k = (item["subsection"], item["stem"])
    if k in seen:
        return
    seen.add(k)
    acc.append(item)


def bulk_unit2_questions(seen: set[tuple[str, str]]) -> list[dict]:
    acc: list[dict] = []

    def add(item: dict) -> None:
        _push(seen, acc, item)

    # ----- 2.1 (12) -----
    add(
        _q(
            S21,
            "",
            "Bonding within one CO₂ molecule is best described as:",
            "C",
            [
                ("Fully ionic carbon cations and oxide ions as in a salt", "Incorrect. CO₂ is modeled with covalent sharing, not full electron transfer."),
                ("Metallic delocalization", "Incorrect."),
                ("Polar covalent C–O bonds", "Correct. Oxygen pulls electron density more than carbon."),
                ("Only London forces", "Incorrect. Those act between molecules."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Which interaction exists between separate Ne atoms in liquid neon?",
            "D",
            [
                ("Covalent bonds", "Incorrect."),
                ("Ionic bonds", "Incorrect."),
                ("Hydrogen bonds", "Incorrect."),
                ("London dispersion forces", "Correct. Noble gases interact via temporary dipoles."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Diamond is an example of:",
            "A",
            [
                ("A covalent network solid", "Correct. Each C is tetrahedrally bonded throughout the crystal."),
                ("An ionic crystal", "Incorrect."),
                ("A molecular solid held only by dipole forces", "Incorrect."),
                ("A metal", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Which molecule is nonpolar despite having polar bonds?",
            "B",
            [
                ("H₂O", "Incorrect. Bent shape gives a net dipole."),
                ("CCl₄ (tetrahedral)", "Correct. Symmetry cancels bond dipoles."),
                ("NH₃", "Incorrect."),
                ("HCl", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "The bond between identical Br atoms in Br₂ is:",
            "C",
            [
                ("Ionic", "Incorrect."),
                ("Polar covalent", "Incorrect."),
                ("Nonpolar covalent", "Correct. Equal sharing."),
                ("Metallic", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "MgO(s) is primarily classified as:",
            "A",
            [
                ("Ionic", "Correct. Mg\u00b2\u207a and O\u00b2\u207b in a lattice."),
                ("Molecular", "Incorrect."),
                ("Metallic", "Incorrect."),
                ("Network covalent like quartz", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Which requires a substance to have H bonded to N, O, or F for the strongest intermolecular case?",
            "B",
            [
                ("Dipole–dipole only", "Incorrect."),
                ("Hydrogen bonding", "Correct. The classic AP definition."),
                ("Metallic bonding", "Incorrect."),
                ("Ion–ion in NaCl", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "In PCl₃, the P–Cl bonds are:",
            "D",
            [
                ("Nonpolar", "Incorrect. Cl is more electronegative than P."),
                ("Pure ionic", "Incorrect."),
                ("Metallic", "Incorrect."),
                ("Polar covalent", "Correct."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Dry ice (CO₂) sublimes; the weak forces overcome between molecules are:",
            "C",
            [
                ("Covalent bonds breaking", "Incorrect. Intramolecular bonds stay intact."),
                ("Ionic attractions", "Incorrect."),
                ("London dispersion forces", "Correct. Nonpolar CO₂ relies on dispersion."),
                ("Hydrogen bonds", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Which is true of a sample of copper wire?",
            "A",
            [
                ("Metallic bonding allows electron flow under voltage", "Correct."),
                ("Electrons are localized between two Cu atoms only", "Incorrect."),
                ("It is held together by hydrogen bonds", "Incorrect."),
                ("It is an ionic crystal", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Intramolecular forces in a polyethylene chain refer to:",
            "B",
            [
                ("Forces between polymer chains", "Incorrect. Those are intermolecular."),
                ("C–C and C–H covalent bonds along the backbone", "Correct."),
                ("Only dispersion", "Incorrect."),
                ("Ion–dipole attractions", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S21,
            "",
            "Which has the greatest ionic character in the bond between the two atoms listed?",
            "D",
            [
                ("C–H", "Incorrect. Small ΔEN."),
                ("Cl–Cl", "Incorrect."),
                ("N–N", "Incorrect."),
                ("Cs–F", "Correct. Very large ΔEN."),
            ],
        )
    )

    # ----- 2.2 (12) -----
    add(
        _q(
            S22,
            "",
            "If two nuclei are squeezed closer than the equilibrium bond length, potential energy typically:",
            "A",
            [
                ("Increases sharply due to nuclear repulsion", "Correct."),
                ("Decreases without bound", "Incorrect."),
                ("Stays flat", "Incorrect."),
                ("Equals the separated-atom limit", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "A larger bond dissociation energy for a diatomic usually means:",
            "C",
            [
                ("Weaker attraction", "Incorrect."),
                ("Longer equilibrium bond", "Incorrect."),
                ("Harder to break into atoms", "Correct."),
                ("Lower electron density between nuclei", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Comparing C–C single and C=C in the same framework, the double bond has:",
            "B",
            [
                ("Lower bond energy", "Incorrect."),
                ("Higher bond energy", "Correct. π bonding adds stabilization."),
                ("Same bond energy", "Incorrect."),
                ("Undefined bond order", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Energy released when forming one mole of HF(g) from H(g) and F(g) is related to:",
            "D",
            [
                ("Only nuclear fusion", "Incorrect."),
                ("Breaking H–H bonds", "Incorrect."),
                ("Vaporization of HF", "Incorrect."),
                ("The depth of the HF potential well relative to separated atoms", "Correct."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "At equilibrium separation, net force on the nuclei is:",
            "A",
            [
                ("Zero", "Correct. Minimum of U implies F = −dU/dr = 0."),
                ("Maximized attractive", "Incorrect."),
                ("Maximized repulsive", "Incorrect."),
                ("Undefined", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Which process is endothermic?",
            "C",
            [
                ("Atoms combining to make N₂", "Incorrect. Bond formation releases energy."),
                ("Condensation of water", "Incorrect."),
                ("Breaking Cl–Cl bonds to Cl atoms", "Correct."),
                ("Freezing water", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Compared with N\u2082, the bond in N\u2082\u207a (one electron removed from a bonding orbital) is expected to:",
            "B",
            [
                ("Stay identical", "Incorrect."),
                ("Increase", "Correct. Lower bond order lengthens the bond in typical MO reasoning."),
                ("Decrease", "Incorrect."),
                ("Become infinite", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "The σ bond in ethane arises from:",
            "D",
            [
                ("Side-on p overlap only", "Incorrect. That describes π."),
                ("Complete electron transfer", "Incorrect."),
                ("Metallic sea overlap", "Incorrect."),
                ("End-on overlap along the internuclear axis", "Correct."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Which statement about bond order is accurate?",
            "A",
            [
                ("Higher bond order often correlates with shorter bond length for the same atom pair", "Correct."),
                ("Bond order is unrelated to bond length", "Incorrect."),
                ("Single bonds are always longer than triple bonds between different atoms", "Incorrect. Cross-comparing different elements is ambiguous."),
                ("Bond order applies only to ionic bonds", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Cooling a gas so atoms associate into diatomic molecules mainly:",
            "C",
            [
                ("Increases potential energy of the system", "Incorrect."),
                ("Prevents bond formation", "Incorrect."),
                ("Allows attractive interactions to form bonds lowering energy", "Correct."),
                ("Removes all kinetic energy at any finite T", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "A Morse-like curve shows bond stretching; a small vibrational displacement from R\u2091 typically:",
            "B",
            [
                ("Never changes energy", "Incorrect."),
                ("Raises energy approximately quadratically for small displacements (harmonic approximation)", "Correct."),
                ("Always dissociates", "Incorrect."),
                ("Removes all electrons", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S22,
            "",
            "Which has the shortest C–O bond among these (conceptual ranking)?",
            "D",
            [
                ("CH₃OH single C–O", "Incorrect."),
                ("CH₃OCH₃ C–O", "Incorrect."),
                ("CO₂ as if one single C–O contributor only", "Incorrect."),
                ("CO with a bond order near three", "Correct. Carbon monoxide has very strong short C–O linkage."),
            ],
        )
    )

    # ----- 2.3 (12) -----
    add(
        _q(
            S23,
            "",
            "Ionic solids typically ______ electricity when solid.",
            "A",
            [
                ("Do not conduct", "Correct. Ions are locked."),
                ("Conduct well", "Incorrect."),
                ("Conduct only by proton hopping", "Incorrect in the usual NaCl model."),
                ("Behave like metals", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Which factor increases lattice energy magnitude most directly?",
            "C",
            [
                ("Larger anion radius with same charge", "Incorrect."),
                ("Lower charges on ions", "Incorrect."),
                ("Higher product of ion charges with smaller radii", "Correct. Coulombic reasoning."),
                ("Molecular shape only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "CsCl structure type vs NaCl differs mainly in:",
            "B",
            [
                ("CsCl is molecular", "Incorrect."),
                ("Coordination number / packing arrangement", "Correct. Different common structure types."),
                ("CsCl has no ions", "Incorrect."),
                ("NaCl is always gas", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Hydration of ions in solution ______ the gas-phase ion assembly energy argument.",
            "D",
            [
                ("Is unrelated to lattice energy", "Incorrect."),
                ("Proves lattices do not exist", "Incorrect."),
                ("Eliminates Coulomb’s law", "Incorrect."),
                ("Provides additional stabilization when ions are solvated", "Correct."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Which compound is expected to have a higher lattice energy magnitude than RbI?",
            "A",
            [
                ("SrO", "Correct. +2/−2 and smaller ions beat +1/−1 in typical ranking."),
                ("CsBr", "Incorrect."),
                ("RbBr", "Incorrect."),
                ("HI molecular solid", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Brittle fracture in CaCO₃ is consistent with:",
            "C",
            [
                ("Metal slip", "Incorrect."),
                ("Hydrogen bond breaking only", "Incorrect."),
                ("Ion layers shifting to align like charges", "Correct."),
                ("Free electron loss", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "A ‘formula unit’ of BaCl₂ contains:",
            "B",
            [
                ("One Ba\u207a and one Cl\u207b", "Incorrect."),
                ("One Ba\u00b2\u207a and two Cl\u207b", "Correct."),
                ("Neutral BaCl₂ molecules only", "Incorrect."),
                ("Delocalized electrons only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Melting an ionic crystal primarily:",
            "D",
            [
                ("Removes all ions", "Incorrect."),
                ("Breaks only covalent bonds in NaCl", "Incorrect."),
                ("Converts ions to atoms in one step", "Incorrect."),
                ("Supplies energy to overcome lattice attractions so ions can move", "Correct."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Lattice energy is associated with:",
            "A",
            [
                ("Forming the ionic solid from gas-phase ions", "Correct in the standard definition."),
                ("Vaporizing metals only", "Incorrect."),
                ("Breaking all covalent bonds in diamond", "Incorrect."),
                ("Ideal gas expansion only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Which is NOT typical of many ionic crystals at room temperature?",
            "C",
            [
                ("High melting point", "Incorrect—it is typical."),
                ("Brittle", "Incorrect—it is typical."),
                ("Malleable like copper", "Correct. Malleability is a metals hallmark."),
                ("Insulating as solid", "Incorrect—it is typical."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Smallest ions among isoelectronic series often produce:",
            "B",
            [
                ("Weaker lattices", "Incorrect."),
                ("Stronger lattice attractions for the same charge pattern", "Correct. Shorter distances."),
                ("No effect", "Incorrect."),
                ("Metallic behavior", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S23,
            "",
            "Na\u207a and Cl\u207b in the crystal are held by:",
            "D",
            [
                ("Covalent sharing only", "Incorrect."),
                ("Hydrogen bonds", "Incorrect."),
                ("London forces only between molecules", "Incorrect."),
                ("Electrostatic attraction in a lattice", "Correct."),
            ],
        )
    )

    # ----- 2.4 (12) -----
    add(
        _q(
            S24,
            "",
            "Steel with interstitial carbon is an example of:",
            "A",
            [
                ("Interstitial alloying", "Correct. Small C fits in Fe voids."),
                ("Substitutional only with no carbon", "Incorrect."),
                ("Ionic substitution", "Incorrect."),
                ("A molecular crystal", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Heating a metal increases electrical resistance mainly because:",
            "C",
            [
                ("Electrons disappear", "Incorrect."),
                ("Ions become negative", "Incorrect."),
                ("Lattice vibrations scatter electron motion more", "Correct."),
                ("Metallic bonding turns ionic", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Gold’s shiny appearance relates to:",
            "B",
            [
                ("Ionic color centers only", "Incorrect."),
                ("Electron transitions involving the conduction band / sea", "Correct."),
                ("Only nuclear transitions", "Incorrect."),
                ("Hydrogen bond absorption", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Compared to sodium, magnesium metal has:",
            "D",
            [
                ("Fewer delocalized electrons per atom in the sea model", "Incorrect. Mg contributes more valence electrons per atom."),
                ("No mobile electrons", "Incorrect."),
                ("Ionic bonding", "Incorrect."),
                ("More valence electrons per atom contributing to the sea", "Correct."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Which property is least consistent with pure metallic bonding?",
            "A",
            [
                ("Low electrical conductivity as a solid", "Correct. Metals conduct."),
                ("Thermal conductivity", "Incorrect—it matches metals."),
                ("Malleability", "Incorrect."),
                ("Luster", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Bronze (Cu–Sn) is commonly:",
            "B",
            [
                ("A molecular compound", "Incorrect."),
                ("A substitutional alloy if Sn replaces some Cu sites", "Correct."),
                ("Pure ionic SnCu", "Incorrect."),
                ("A noble gas mixture", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "The electron sea model explains thermal conductivity in metals by:",
            "C",
            [
                ("Vibration of fixed molecules only", "Incorrect."),
                ("Hydrogen transfer", "Incorrect."),
                ("Mobile electrons carrying kinetic energy", "Correct."),
                ("Ion diffusion only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Work-hardening a metal ______ dislocation motion.",
            "D",
            [
                ("Eliminates all bonds", "Incorrect."),
                ("Has no effect", "Incorrect."),
                ("Always melts the sample", "Incorrect."),
                ("Can impede slip by introducing defects", "Correct."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Alloying often changes metal hardness because:",
            "A",
            [
                ("Different atom sizes disrupt regular layer slip", "Correct."),
                ("All electrons are removed", "Incorrect."),
                ("Ionic bonds replace metallic bonds completely", "Incorrect."),
                ("Hydrogen bonds dominate", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Mercury is a liquid at room temperature yet still metallic because:",
            "B",
            [
                ("It has no conduction electrons", "Incorrect."),
                ("It still has delocalized valence electrons despite weaker attractions", "Correct."),
                ("It is ionic", "Incorrect."),
                ("It is covalent only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Which statement contrasts metals and ionic solids fairly?",
            "C",
            [
                ("Both conduct well as solids", "Incorrect."),
                ("Neither has ordered structures", "Incorrect."),
                ("Metals conduct via electrons; ionic solids often conduct when molten or dissolved via ions", "Correct."),
                ("Both are always brittle", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S24,
            "",
            "Wires are drawn from metals rather than NaCl because:",
            "D",
            [
                ("NaCl has too many electrons", "Incorrect."),
                ("Metals lack positive centers", "Incorrect."),
                ("NaCl is too conductive as a solid", "Incorrect."),
                ("Metallic slip preserves bonding; ionic slip aligns repulsive faces", "Correct."),
            ],
        )
    )

    # ----- 2.5 (12) -----
    add(
        _q(
            S25,
            "",
            "Valence electrons for HCN (neutral):",
            "A",
            [
                ("10", "Correct. H1 + C4 + N5."),
                ("8", "Incorrect."),
                ("12", "Incorrect."),
                ("14", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "In SO₂ the central atom is:",
            "B",
            [
                ("O", "Incorrect."),
                ("S", "Correct."),
                ("Either atom with equal preference", "Incorrect."),
                ("There is no central atom", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "Total valence electrons for H₂CO (formaldehyde):",
            "C",
            [
                ("10", "Incorrect."),
                ("14", "Incorrect."),
                ("12", "Correct. H×2 + C4 + O6."),
                ("16", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "An expanded octet on P in PCl\u2085 implies:",
            "D",
            [
                ("P obeys octet strictly", "Incorrect."),
                ("Only two chlorines bond", "Incorrect."),
                ("P forms ionic bonds only", "Incorrect."),
                ("More than eight electrons around P in the Lewis representation", "Correct."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "For N₂, the Lewis structure shows:",
            "A",
            [
                ("A triple bond and one lone pair on each nitrogen", "Correct in the usual octet structure."),
                ("Only single bonds", "Incorrect."),
                ("Ionic N\u207a and N\u00b3\u207b", "Incorrect."),
                ("No lone pairs", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "The skeleton for ClO₃⁻ typically places ______ central.",
            "B",
            [
                ("O", "Incorrect."),
                ("Cl", "Correct."),
                ("A hydrogen", "Incorrect."),
                ("No central atom", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "BeCl₂ (g) often drawn with only four electrons on Be illustrates:",
            "C",
            [
                ("An octet on Be", "Incorrect."),
                ("Metallic bonding", "Incorrect."),
                ("An incomplete octet on Be", "Correct."),
                ("Resonance only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "How many lone pairs on terminal F in ClF₃ (each F completes octet)?",
            "D",
            [
                ("0", "Incorrect."),
                ("1", "Incorrect."),
                ("4", "Incorrect."),
                ("3", "Correct. Three lone pairs per terminal F with one bond."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "For CO, valence electron total is:",
            "A",
            [
                ("10", "Correct. C4 + O6."),
                ("12", "Incorrect."),
                ("8", "Incorrect."),
                ("14", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "A resonance-stabilized oxyacid anion often has multiple Lewis forms differing in:",
            "B",
            [
                ("Atom connectivity", "Incorrect."),
                ("\u03c0 bond placement", "Correct."),
                ("Nuclear charge", "Incorrect."),
                ("Number of atoms", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "CH₃OH: how many lone pairs on oxygen in the Lewis structure with two single bonds to C and H?",
            "C",
            [
                ("0", "Incorrect."),
                ("1", "Incorrect."),
                ("2", "Correct."),
                ("3", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S25,
            "",
            "XeF₄ Lewis picture requires ______ electron pairs around Xe in the expanded octet model.",
            "D",
            [
                ("4", "Incorrect."),
                ("5", "Incorrect."),
                ("7", "Incorrect."),
                ("6 bonding+lone domains (12 electrons in pairs around Xe in the usual count)", "Correct."),
            ],
        )
    )

    # ----- 2.6 (11) -----
    add(
        _q(
            S26,
            "",
            "The best resonance contributor to CO₂ often has:",
            "A",
            [
                ("Formal charges of zero on C and O with double bonds", "Correct in the symmetric preferred form."),
                ("Single bonds only", "Incorrect."),
                ("C with −2 and O with +1 each", "Incorrect as the favored picture."),
                ("Only one oxygen participating", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "Benzene’s equal C–C bond lengths imply:",
            "C",
            [
                ("Rapid single-double flipping", "Incorrect."),
                ("Only one Kekulé form is real", "Incorrect."),
                ("Delocalized π system", "Correct."),
                ("No π bonds", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "Formal charge on S in SO₂ with one S=O double and one S–O single (octets) in one contributor:",
            "B",
            [
                ("0", "Incorrect."),
                ("+1", "Correct with usual counting."),
                ("−2", "Incorrect."),
                ("+3", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "Which ion commonly needs resonance to match equal bond lengths experimentally?",
            "D",
            [
                ("Cl⁻", "Incorrect."),
                ("Na\u207a", "Incorrect."),
                ("OH⁻", "Incorrect."),
                ("NO₃⁻", "Correct."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "A contributor with adjacent like formal charges is usually:",
            "A",
            [
                ("Less important than one with separated opposite charges minimized", "Correct."),
                ("Always the best", "Incorrect."),
                ("Required for neutrals", "Incorrect."),
                ("Impossible to draw", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "O₃ bond order in the hybrid picture is between:",
            "C",
            [
                ("3 and 4", "Incorrect."),
                ("0 and 1", "Incorrect."),
                ("1 and 2 for each O–O link", "Correct."),
                ("Exactly 1 only", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "When ranking resonance structures, placing a negative formal charge on oxygen rather than carbon is often favored because:",
            "B",
            [
                ("Carbon is more electronegative", "Incorrect."),
                ("Oxygen is more electronegative", "Correct."),
                ("Oxygen has fewer protons", "Incorrect."),
                ("Formal charge ignores EN", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "The sum of formal charges in a neutral molecule must be:",
            "D",
            [
                ("+1", "Incorrect."),
                ("−1", "Incorrect."),
                ("Undefined", "Incorrect."),
                ("Zero", "Correct."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "Which species is NOT well described by a single Lewis structure without resonance arguments?",
            "A",
            [
                ("CO₃²⁻", "Correct."),
                ("H₂O", "Incorrect."),
                ("CH₄", "Incorrect."),
                ("NH₃", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "In N₂O (connectivity N–N–O for this item), formal charge arguments help choose:",
            "C",
            [
                ("Nuclear masses", "Incorrect."),
                ("Vibration frequency only", "Incorrect."),
                ("Which Lewis contributors are more important", "Correct."),
                ("Atomic radii", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S26,
            "",
            "Double-headed resonance arrows between Lewis structures mean:",
            "B",
            [
                ("The molecule physically flips between structures at ordinary speeds", "Incorrect."),
                ("The true wavefunction is a combination of those limiting forms", "Correct."),
                ("Only the left structure exists", "Incorrect."),
                ("Electrons are deleted", "Incorrect."),
            ],
        )
    )

    # ----- 2.7 (12) -----
    add(
        _q(
            S27,
            "",
            "Molecular geometry of BF₃:",
            "A",
            [
                ("Trigonal planar", "Correct. Three domains, no lone pairs on B."),
                ("Tetrahedral", "Incorrect."),
                ("Bent", "Incorrect."),
                ("Pyramidal", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Electron-domain geometry of NH₃:",
            "C",
            [
                ("Tetrahedral", "Incorrect—that is molecular shape name confusion."),
                ("Trigonal planar", "Incorrect."),
                ("Tetrahedral arrangement of four domains", "Correct. Three bonds + one lone pair."),
                ("Linear", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Hybridization of S in SF\u2086:",
            "D",
            [
                ("sp", "Incorrect."),
                ("sp²", "Incorrect."),
                ("sp³", "Incorrect."),
                ("sp³d²", "Correct for six σ domains in the expanded octet model."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Bond angle in CO₂:",
            "B",
            [
                ("109.5°", "Incorrect."),
                ("180°", "Correct. Linear."),
                ("120°", "Incorrect."),
                ("90°", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "ClF₃ molecular geometry:",
            "A",
            [
                ("T-shaped", "Correct. Five domains, two lone pairs equatorial."),
                ("Trigonal planar", "Incorrect."),
                ("Tetrahedral", "Incorrect."),
                ("Linear", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "PCl\u2085 in the gas phase has which electron-domain geometry?",
            "C",
            [
                ("Octahedral", "Incorrect."),
                ("Tetrahedral", "Incorrect."),
                ("Trigonal bipyramidal", "Correct. Five domains."),
                ("Square planar", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Hybridization of central C in CO₂:",
            "D",
            [
                ("sp³", "Incorrect."),
                ("sp³d", "Incorrect."),
                ("sp³d²", "Incorrect."),
                ("sp", "Correct. Two σ domains linear."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Which is polar?",
            "B",
            [
                ("CCl₄", "Incorrect."),
                ("CH₂Cl₂", "Correct. Asymmetric substitution."),
                ("CO₂", "Incorrect."),
                ("BF₃", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "XeF₂ molecular shape:",
            "A",
            [
                ("Linear", "Correct. Five domains, three lone pairs equatorial."),
                ("Bent", "Incorrect."),
                ("Tetrahedral", "Incorrect."),
                ("Square planar", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "Approximate H–C–H angle in ethene:",
            "C",
            [
                ("109.5°", "Incorrect."),
                ("104.5°", "Incorrect."),
                ("120°", "Correct. Trigonal planar carbons."),
                ("180°", "Incorrect."),
            ],
        )
    )
    add(
        _q(
            S27,
            "",
            "BrF\u2085 molecular geometry:",
            "B",
            [
                ("Octahedral", "Incorrect."),
                ("Square pyramidal", "Correct. Six domains, one lone pair."),
                ("Pentagonal planar", "Incorrect."),
                ("Tetrahedral", "Incorrect."),
            ],
        )
    )

    add(
        _q(
            S27,
            "",
            "Which has a tetrahedral electron geometry around the central atom?",
            "A",
            [
                ("CH₄", "Correct. Four bonding domains."),
                ("XeF₄", "Incorrect."),
                ("SF\u2086", "Incorrect."),
                ("CO₂", "Incorrect."),
            ],
        )
    )

    return acc
