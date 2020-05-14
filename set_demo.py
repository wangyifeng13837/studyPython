'''
集合的特征：
集合内数据无序，即无法使用索引和分片
集合内部数据元素具有唯一性，可以用来排除重复数据
集合内的数据，str,int, float,tuple,冰冻集合等，即内部只能放置可哈希数据

'''
#  集合序列操作
#  成员检测
#  in ，not in

s = {'1', 2, 4, 'i', 34, 14, 'beijing', 'fagongzi'}
print(s)
if 34 in s:
    print('true')
if 'mafan' not in s :
    print('money')

# 集合遍历
# for 循环

for i in s:
    print(i, end=' ')

print("--"*10)
# 带有元组的集合遍历
s = {(1, 2, 3), ('my', 'name', 'joker'), (4, 5, 6)}
# 如果每个元组里的元素个数不相同那么会出现 too many values to unpack 报错
for k,m,n in s:
    print(k, "-", m, "-", n)
print('_'*30)
for k in s:
    print(k)