def custom_write(file_name, strings):
    file = open(file_name, 'w' , encoding= 'utf-8')
    strings_positions = {}
    num_str = 1
    for i in strings:
        a = file.tell()
        file.write(str(i)+'\n')
        strings_positions[(num_str, a)] = i
        num_str += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
