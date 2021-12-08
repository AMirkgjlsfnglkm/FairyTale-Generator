from openpyxl import load_workbook


# Get character categories from Veale
workbook = load_workbook(filename='../data/Veale_db/Veale\'s category actions.xlsx')
work_sheet = workbook.active
characters = [work_sheet[i][1].value for i in range(2, 451)]        # start from 2, don't include header row


# Process fairytale dataset into one string
fairy_tales = ''
with open('../data/Fairytales_db/merged_clean.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        fairy_tales += line.lower()


# For each character, count how many times it occurs in fairytale dataset (adds spaces for 'word bounds')
counted_characters = [[character, fairy_tales.count(' ' + character.lower() + ' ')] for character in characters if fairy_tales.count(' ' + character.lower() + ' ') > 0]
counted_characters = sorted(counted_characters, key=lambda x: x[1], reverse=True)
print(counted_characters)


# Write all left over characters to file
f = open("../data/results/characters.txt", "w")
for i in range(0, len(counted_characters)):
    f.write(str(i + 1) + '. ' + counted_characters[i][0] + ' : ' + str(counted_characters[i][1]) + ' times\n')
f.close()


# Write most used characters to file based on treshold
# treshold = 15
# f = open("../data/results/" + str(treshold) + "_characters.txt", "w")
# for i in range(0, treshold):
#     f.write(str(i + 1) + '. ' + counted_characters[i][0] + ' : ' + str(counted_characters[i][1]) + ' times\n')
# f.close()
