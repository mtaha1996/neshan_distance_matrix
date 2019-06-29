import xlsxwriter


def excel(data, path):
    row, col = 0,0

    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    for line in data:
        for col in range(len(line)):
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
        row += 1

    workbook.close()
