# задание по теме "Генераторы"

def all_variants(text):
    for k in range(len(text)):
        for j in range(k,len(text)):
            yield text[k:j+1]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
