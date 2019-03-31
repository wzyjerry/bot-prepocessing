import pickle
names_cn = set()
with open('data/clean/names_zh.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        if len(line) == 2:
            names_cn.add(('%s %s' % (line[1], line[0])).lower())
        else:
            continue
names_en = set()
with open('data/entities/names (eng).txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        names_en.add(line.strip().lower())

with open('data/clean/names.pkl', 'wb') as fout:
    pickle.dump(names_cn | names_en, fout)
