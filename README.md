# bot-prepocessing

main.py
prepocessing(text) -> Continue?, text, 'name'/'keyword'/None
是否继续传给NLU, 英文文本, 实体类型

example:
tang jie
(True, 'tang jie', None)
jie tang
(False, 'jie tang', 'name')
唐杰
(False, 'jie tang', 'name')
智能
(False, 'intelligence', 'keyword')
人工智能
(False, 'artificial intelligence', 'keyword')