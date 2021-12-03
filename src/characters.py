from openpyxl import load_workbook


# Get character categories from Veale
workbook = load_workbook(filename='../data/Veale_db/Veale\'s category actions.xlsx')
work_sheet = workbook.active
characters = [work_sheet[i][1].value for i in range(1, 451)]


# Process fairytale dataset into one string
fairy_tales = ''
with open('../data/Fairytales_db/merged_clean.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        fairy_tales += line


# For each character, count how many times it occurs in fairytale dataset
counted_characters = [[character, fairy_tales.count(character)] for character in characters if fairy_tales.count(character) > 0]
counted_characters = sorted(counted_characters, key=lambda x: x[1], reverse=True)
print(counted_characters)


# Write all left over characters to file
f = open("../data/results/characters.txt", "w")
for i in range(0, len(counted_characters)):
    f.write(str(i + 1) + '. ' + counted_characters[i][0] + ' : ' + str(counted_characters[i][1]) + ' times\n')
f.close()


# Write 15 most used characters to file
f = open("../data/results/15_characters.txt", "w")
for i in range(0, 15):
    f.write(str(i + 1) + '. ' + counted_characters[i][0] + ' : ' + str(counted_characters[i][1]) + ' times\n')
f.close()

