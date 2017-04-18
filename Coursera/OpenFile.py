xfile = open('file1.txt')

## print each line in the file
# for line in xfile:
#     print (line)

## count each line in the file
# count = 0
# for line in xfile:
#     count += 1
# print (count)

## read xfile in a file: inp - the file will not be separated into lines anymore
## if the xfile is to big, "inp" will not feat into RAM memory
# inp = xfile.read()
# print (len(inp))
# for line in inp:
#     print(line)
# print (inp[:20])

## search through a file
for line in xfile:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

## print automatically add '\n' new line so in case you want to eliminate the blank line space
## when printing in a loop, use line.rstrip()
# for line in xfile:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         print(line)
