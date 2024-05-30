import numpy as np
import random 

# list1 = np.array(['G','A','V','I','L','P', 'S','T'], dtype='str')

# list2 = np.array(['G','A','V','I','L','P', 'S','T', 'D', 'E'], dtype='str')

# list3 = np.array(['G','A','V','I','L','P', 'S','T', 'K', 'R'], dtype='str')

# list4 = np.array(['A','D','E','G','I','K','L','P','R','S','T','V'])

list5 = np.array(['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V'])
##
# List1
##
# import numpy as np
# max_iterations = int(1e5)
# repeats1 = []
# for i in range(max_iterations):
#     proposal = np.random.choice(list1, 25).tolist()
#     random.shuffle(proposal)
#     proposal = ''.join(proposal)
#     while proposal in repeats1:
#         proposal = np.random.choice(list1, 25).tolist() 
#         random.shuffle(proposal)
#         proposal = ''.join(proposal)
#         # print(i, 'already in')
#     repeats1.append(proposal)
#     # print(proposal)

# with open('list1.txt','w') as w:
#     for line in repeats1:
#         w.write(line + '\n')

# ##
# # List2
# ##
# import numpy as np
# max_iterations = int(1e5)
# repeats2 = []
# for i in range(max_iterations):
#     proposal = np.random.choice(list2, 25).tolist()
#     random.shuffle(proposal)
#     proposal = ''.join(proposal)
#     while proposal in repeats2:
#         proposal = np.random.choice(list2, 25).tolist() 
#         random.shuffle(proposal)
#         proposal = ''.join(proposal)
#         # print(i, 'already in')
#     repeats2.append(proposal)
#     # print(proposal)

# with open('list2.txt','w') as w:
#     for line in repeats2:
#         w.write(line + '\n')

# ##
# # List3
# ##
# import numpy as np
# max_iterations = int(1e5)
# repeats3 = []
# for i in range(max_iterations):
#     proposal = np.random.choice(list3, 25).tolist()
#     random.shuffle(proposal)
#     proposal = ''.join(proposal)
#     while proposal in repeats3:
#         proposal = np.random.choice(list3, 25).tolist() 
#         random.shuffle(proposal)
#         proposal = ''.join(proposal)
#         # print(i, 'already in')
#     repeats3.append(proposal)
#     # print(proposal)

# with open('list3.txt','w') as w:
#     for line in repeats3:
#         w.write(line + '\n')

#
#list4
#
import numpy as np
max_iterations = int(1e5)
repeats5 = []
for i in range(max_iterations):
    proposal = np.random.choice(list5, 25).tolist()
    random.shuffle(proposal)
    proposal = ''.join(proposal)
    while proposal in repeats5:
        proposal = np.random.choice(list5, 25).tolist() 
        random.shuffle(proposal)
        proposal = ''.join(proposal)
        # print(i, 'already in')
    repeats5.append(proposal)
    # print(proposal)

with open('list5.txt','w') as w:
    for line in repeats5:
        w.write(line + '\n')
        