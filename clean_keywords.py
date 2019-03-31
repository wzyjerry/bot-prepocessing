import pickle
keywords_zh = set()
with open('data/clean/keywords_zh.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        keywords_zh.add(line.strip().lower())
keywords_en = set()
with open('data/entities/Keyword (Eng).txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        keywords_en.add(line.strip().lower())
with open('data/clean/keywords.pkl', 'wb') as fout:
    pickle.dump(keywords_en | keywords_zh, fout)
