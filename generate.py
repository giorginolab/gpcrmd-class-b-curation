import os
from docxtpl import DocxTemplate
import pandas as pd
import time


data = pd.read_csv("Curation results - Sheet1.csv", skiprows=1)


for i, d in data.iterrows():
    if not isinstance(d.pdb, str):
        break
    os.makedirs(f"outputs/{d.pdb}", exist_ok=True)
    doc = DocxTemplate("template.docx")
    d["time"] = time.asctime() 
    doc.render(d)
    doc.save(f"outputs/{d.pdb}/{d.pdb}_{d.type}_curation_form.docx")

