import collections
f = open('species.py', 'r')
text = f.read()
text = text.split('\n')
entries = {}
for j in range(len(text)):
    if 'Species(#' in text[j]:
        entry = ""
        index = 0
        for i in range(14):
            entry += text[j + i] + '\n'
            if i == 2:
                index = int(text[j + i].replace(',', '').strip())
        entries.update({index: entry})

od = collections.OrderedDict(sorted(entries.items()))

for e, v in od.items():
    print(v)
