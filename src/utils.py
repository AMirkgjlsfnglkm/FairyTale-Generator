from openpyxl import load_workbook

workbook = load_workbook(filename="../data/Veale_db/Veale_s script midpoints.xlsx")
work_sheet = workbook.active

possible_verbs = ['are_disrespected_by', 'are_deceived_by', 'kill', 'manipulate', 'fall_in_love_with', 'profit_from']

ending_verbs = []
for row in range(2, 2761):
    ending_verbs.extend(work_sheet[row][2].value.split(", "))

options = []
for row in range(2, 2761):
    for verb in possible_verbs:
        if verb in work_sheet[row][2].value.split(", ") and work_sheet[row][0].value in ending_verbs:
            options.append(row)

options = list(dict.fromkeys(options))
for i in options:
    print(work_sheet[i][0].value, "\t", work_sheet[i][1].value[0:], "\t", work_sheet[i][2].value[0:])
