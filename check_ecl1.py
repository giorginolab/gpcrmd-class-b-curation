
from htmd.ui import *
import numpy as np

glr_pdb_list = ["5YQZ", "5EE7"]
glp1r_pdb_list = ["6KJV", "6KK1", "6KK7", "5NX2", "5VEW", "5VEX"]

ra = set(range(190, 229))

for pdb in glp1r_pdb_list:
    m = Molecule(pdb)
    r1 = m.get("resid", sel="resid 190 to 228")
    r1 = set(r1)
    dr = ra.difference(r1)
    print(f"{pdb}: missing {dr}")
