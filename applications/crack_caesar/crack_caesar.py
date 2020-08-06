# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("ciphertext.txt") as c:
  text = c.read()

text = text.replace('\n', '')
ignore = ('"', ':', ';', ',', '.', '+', '=', '/', '|', '[', ']', '{', '}' ,'(' ,')', '*', '^', '&', '-', "'", '!', '?', '1')

encode_table = {}

decode_table = {}

total_letters = 0

message = """"""

for i in text:
  if i == " " or i in ignore:
    continue

  if i not in encode_table:
    encode_table[i] = 0

  encode_table[i] += 1
  total_letters += 1


items = list(encode_table.items())

items.sort(key=lambda e: e[1], reverse=True)

print("items:", items)
print("length of items:", len(items))

for i in range(len(frequency)):
  encode_letter = frequency[i]
  decode_letter = items[i][0]

  decode_table[decode_letter] = encode_letter


for i in text:
  if i in decode_table:
    message += decode_table[i]

  else:
    message += i

print(message)