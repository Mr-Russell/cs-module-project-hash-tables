# Your code here
with open("robin.txt") as r:
  # words = f"{r.read()}"
  words = r.read()

count = {}
punct = '":;,.-+=/\|[]{}()*^&'
word_list = words.lower().split()

for word in word_list:
  word = word.strip(punct)
  if word not in count:
    count[word] = ''
  count[word] += "#"


items = list(count.items())

def histo_sort(e):
  hash_length = len(e[1])
  return (-hash_length, (e[0]))


items.sort(key=histo_sort)

longest = None
length = 0
for i in items:
  if len(i[0]) > length:
    longest = i[0]
    length = len(i[0])
  print(f"{i[0]:15}  {i[1]}")

print(f"{longest} is the longest word, with {length} characters")