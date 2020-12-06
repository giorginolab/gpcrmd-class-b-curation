
from htmd.ui import *
import numpy as np
import sys

glr_pdb_list = ["5YQZ", "5EE7"]
glp1r_pdb_list = ["6KJV", "6KK1", "6KK7", "5NX2", "5VEW", "5VEX"]

pdb_list = glr_pdb_list + glp1r_pdb_list

if len(sys.argv) > 1:
    pdb_list = [sys.argv[1]]

indir = "/Users/toni/Sync/work_in_progress/gpcrmd-glucagon/Toni_Giorgino"
outdir = "/Users/toni/Sync/work_in_progress/gpcrmd-glucagon/generator/outputs"

for pdb in pdb_list:
    for typ in ["apo", "complex"]:
        m = Molecule(f"{indir}/{pdb}/{pdb}_{typ}.pdb")

        # Remove NA
        m.remove("resname NA")

        # Peptide ligand with water clashes
        if pdb == "5YQZ" and typ == "complex":
            m.remove("water within 3 of chain P")
        if pdb == "5NX2" and typ == "complex":
            m.remove("water within 3 of chain L")

        if pdb in ["6KJV", "6KK1", "5VEW"]:
            m.remove("resid 204 to 215")
        if pdb in ["6KK7", "5VEX"]:
            m.remove("resid 204 to 217")

        if pdb == "5NX2":
            m.remove("resid 199 to 229")
            n = Molecule("5nx2.pdb")
            n.filter("resid 199 to 229")
            n.mutateResidue("resid 207", "THR")
            n.mutateResidue("resid 211", "GLN")
            n.mutateResidue("resid 215", "ASP")
            n.set("resname", "CYX", "resid 226")
            n.set("segid", "P0")
            n.set("chain", "P")
            wh = m.get("index", "resid 230")[0]
            m.insert(n, wh)

        m.write(f"{outdir}/{pdb}/{pdb}_{typ}_curated.pdb")
        print(f"Done {pdb} {typ}")
