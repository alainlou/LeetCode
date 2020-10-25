import os

os.system("ls > tmp.txt")

nums = set()

s = []

with open('tmp.txt', 'r') as f:
  for line in f:
    spl = line.split('.')
    if len(spl) == 2 and (spl[1] == 'py\n' or spl[1] == 'cpp\n' or spl[1] == 'c\n') and '-' not in spl[0] and spl[0] != 'script':
      nums.add(int(spl[0][1:]))

for n in nums:
  if n not in s:
    print("File not submitted on lc:", n)

print()

for e in s:
  if e not in nums:
    print("lc submission not in file:", e)

os.system("rm tmp.txt")
