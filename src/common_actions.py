import pandas as pd
from collections import Counter

df = pd.read_excel('../data/Veale_db/Veale_s script midpoints.xlsx', index_col=None, na_values=['NA'])

verbs_before_mp = df['Before Midpoint'].tolist()
verbs_after_mp = df['After Midpoint'].tolist()

new_verbs_after_mp = []
for i in verbs_after_mp:
    for verb in i.replace(" ", "").split(","):
        if verb in verbs_before_mp:
            new_verbs_after_mp.append(verb)
verbs_after_mp = new_verbs_after_mp

d = dict()

for verb in verbs_after_mp:
    if verb in d:
        d[verb] = d[verb] + 1
    else:
        d[verb] = 1

d = Counter(d)
common_verbs = d.most_common(100)
for i in common_verbs:
    print(i[0])
print(common_verbs)
