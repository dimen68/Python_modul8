# задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_) for str_ in first_strings if len(str_) >= 5]
second_result = [(str_1, str_2) for str_1 in first_strings for str_2 in second_strings if len(str_1) == len(str_2)]
third_result = {str_:len(str_) for str_ in first_strings + second_strings if not len(str_) % 2}

print(first_result)
print(second_result)
print(third_result)