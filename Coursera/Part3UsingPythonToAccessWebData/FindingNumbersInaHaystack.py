import re

# hand = open('regex_sum_369917.txt')
# addtot = 0

# for line in hand:
#     line = line.rstrip()
#     nrlist = re.findall('[0-9]+', line)
#     for el in nrlist:
#         addtot += int(el)
#
# print (addtot)


# one line solution
print(sum([int(x) for x in re.findall('[0-9]+',open('regex_sum_369917.txt').read())]))