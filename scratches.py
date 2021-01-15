# with open('wow.txt' , 'r') as f , open('wower.txt' , 'w') as g:
#     whole = f.read().split('url')
#     for chunk in whole:
#         g.write(chunk + '\n')

with open('dict.txt' , 'r') as f:
    url = f.readline()

ls = []
for i , char in enumerate(url):
    if char == '%':
        ls.append(url[i:i+3])
print(set(ls))
