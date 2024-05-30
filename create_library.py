import numpy as np 
import random

#####
# Crerating the initial list
#####
hydrophobic_aa_list = np.array(['G','P','A','V','I','L','M','F','W','Y'], dtype='str')
polar_aa_list = np.array(['S','T','N','Q','C'], dtype='str')
charged_aa_list = np.array(['R','H','K','D','E'], dtype='str')

# from itertools import combinations_with_replacement

# h = list(combinations_with_replacement(hydrophobic_aa_list,15))
# p = list(combinations_with_replacement(polar_aa_list, 5))
# c = list(combinations_with_replacement(charged_aa_list, 5))

# print(len(h))
# print(len(p))
# print(len(c))

##
# Hacky way
##
# for hi,pi,ci in zip(h,p,c):
#     # print(hi, pi,ci)
#     l = list(hi) + list(pi) + list(ci)
#     # print(l)
#     random.shuffle(l)
#     # print(l)
#     proposal = ''.join(l)
#     print(proposal)

##
# Actual Coverage
##
# for hi in h:
#     for pi in p:
#         for ci in c:
#             l = list(hi) + list(pi) + list(ci)
#             random.shuffle(l)
#             proposal = ''.join(l)
#             print(proposal)

##
# Subset Version
##
import numpy as np
max_iterations = int(1e6)
repeats = []
for i in range(max_iterations):
    proposal = np.random.choice(hydrophobic_aa_list, 15).tolist() + np.random.choice(polar_aa_list,5).tolist() + np.random.choice(charged_aa_list, 5).tolist()
    random.shuffle(proposal)
    proposal = ''.join(proposal)
    while proposal in repeats:
        proposal = np.random.choice(hydrophobic_aa_list, 15).tolist() + np.random.choice(polar_aa_list,5).tolist() + np.random.choice(charged_aa_list, 5).tolist()
        random.shuffle(proposal)
        proposal = ''.join(proposal)
        print(i, 'already in')
    repeats.append(proposal)
    print(proposal)