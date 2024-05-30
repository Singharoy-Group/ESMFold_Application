from transformers import AutoTokenizer, EsmForProteinFolding
from transformers import EsmModel

from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
from transformers.models.esm.openfold_utils.feats import atom14_to_atom37

import sys

##
# PDB Conversation function from: https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/protein_folding.ipynb#scrollTo=1c9de19e
# NOTE: Changes added such that outputs are detached from GPU
##
def convert_outputs_to_pdb(outputs):
    final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
    #outputs = {k: v.to("cpu").numpy() for k, v in outputs.items()}
    outputs = {k: v.detach().to("cpu").numpy() for k, v in outputs.items()}
    #final_atom_positions = final_atom_positions.cpu().numpy()
    final_atom_positions = final_atom_positions.detach().cpu().numpy()
    final_atom_mask = outputs["atom37_atom_exists"]
    pdbs = []
    for i in range(outputs["aatype"].shape[0]):
        aa = outputs["aatype"][i]
        pred_pos = final_atom_positions[i]
        mask = final_atom_mask[i]
        resid = outputs["residue_index"][i] + 1
        pred = OFProtein(
            aatype=aa,
            atom_positions=pred_pos,
            atom_mask=mask,
            residue_index=resid,
            b_factors=outputs["plddt"][i],
            chain_index=outputs["chain_index"][i] if "chain_index" in outputs else None,
        )
        pdbs.append(to_pdb(pred))
    return pdbs

model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", cache_dir="/scratch/sdutta46/")

tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")

import glob
import random
import numpy as np
import os
import sys

files = glob.glob('*.txt')
folders = [f.replace('.txt','') for f in files]

rep_file = sys.argv[1]
rep_dic = []
with open(rep_file,'r') as f:
    for line in f:
        line = line.strip('\n')
        rep_dic.append(line)

##
# Go through each cluster file and get the folding
##
for folder, file_  in zip(folders,files):
    os.makedirs(folder,exist_ok=True)
    cluster_seq = []
    with open(file_,'r') as f:
        for line in f:
            line = line.strip('\n')
            if line in rep_dic:
                continue
            cluster_seq.append(line)
    for i, line in enumerate(cluster_seq):
        #rep = random.choice(line)
        rep = line
        input_rep = tokenizer([rep], return_tensors='pt', add_special_tokens=False)
        outputs = model(**input_rep)
        pdb = convert_outputs_to_pdb(outputs)
        with open(folder +  '/seq_' + str(i) + '_' + rep + '.pdb','w') as w:
            w.write(pdb[0])

print('Folding Done')

