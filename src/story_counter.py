# This code is used to count the amount of fairy tales in merged_clean.txt

with open('../data/Fairytales_db/merged_clean.txt') as f:
    lines = f.readlines()
    counter = 0
    current_empty_lines = 0
    for line in lines:
        if line == '' or line == '\n' or line == '\r\n' or line == '\n\r' or line == '\r':
            current_empty_lines += 1

        else:
            if current_empty_lines > 3:
                counter += 1
            current_empty_lines = 0
    print('', counter, 'stories found')
