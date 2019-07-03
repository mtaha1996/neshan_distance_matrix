import xlsxwriter


def excel(data_min, data_meter, path):
    row, col = 0, 0

    workbook = xlsxwriter.Workbook('output_min.xlsx')
    worksheet = workbook.add_worksheet()

    for line in data_min:
        for col in range(len(line)):
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
        row += 1

    workbook.close()

    row, col = 0, 0

    workbook = xlsxwriter.Workbook('output_meter.xlsx')
    worksheet = workbook.add_worksheet()

    for line in data_meter:
        for col in range(len(line)):
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
            worksheet.write(row, col, line[col])
        row += 1

    workbook.close()
