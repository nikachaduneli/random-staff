from django.http import JsonResponse, FileResponse, HttpRequest
from django.core.paginator import Paginator, InvalidPage
import sys
sys.path.append("..")
from carrefour import settings as app_settings
from . import const
import xlsxwriter
import datetime
import io


def paginate(paginate_by:int, objects:list, request:HttpRequest) -> dict:
    is_paginated = False

    if objects.count() > paginate_by:

        page = request.GET.get('page', 1)
        paginator = Paginator(objects, paginate_by)
        page_obj = paginator.get_page(page)

        try:
            objects = paginator.page(page)
        except InvalidPage:
            objects = paginator.page(1)

        is_paginated = True

        return {'is_paginated': is_paginated, 'page_obj': page_obj, 'applicants': objects}

    return {'is_paginated': is_paginated, 'applicants': objects}


def is_valid(form_data:dict) -> tuple:
    for i in form_data:
        if form_data[i] == '' or not form_data[i]:
            return False, 'შეცდომა: არცერთი ველი არ უნდა იყოს ცარიელი.'
    if datetime.datetime.strptime(form_data['birth_date'], '%Y-%m-%d') > datetime.datetime.now():
        return False, 'შეცდომა: დაბადების დღედ მომავლის თარიღია არჩეული.'
    if not form_data['mobile_number'].isnumeric():
        return False, 'შეცდომა: ტელეფონის ნომერი მხოლოდ რიცხვებისგან უნდა შედგებოდეს.'
    if not form_data['wanted_city'] in const.CITIES:
        return False, 'შეცდომა: თქვენი არჩეული სასურველი ქალაქი არ არის ჩამონათვალში.'
    if not form_data['wanted_position'] in const.POSITIONS:
        return False, 'შეცდომა: თქვენი არჩეული სასურველი პოზიცია არ არის ჩამონათვალში.'
    return True, 'თქვენი ინფორმაცია წარმატებით გაიგზავნა.'


def excel_report(request:HttpRequest, applicants:list, comments:list) -> FileResponse:
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'method is not allowed'})

    xls_colors = {'#EA5455': 'red',
                  '#F9ED69': 'yellow',
                  '#00B8A9': 'green',
                  '#3D84A8': 'blue',
                  '#F0F0F0': 'gray',
                  '#F07B3F': 'orange'}

    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()

    columns = ['Name', 'Last Name', 'Birth Date', 'Address', 'Wanted Position',
               'wanted_city', 'Applie Date', 'Mobile Number', 'Comment']
    row_num = 0

    cell_format = workbook.add_format()
    cell_format.set_bold()

    # writing column names
    for col in range(len(columns)):
        worksheet.write(row_num, col, columns[col], cell_format)

    rows = applicants.values_list()
    width = calculate_max_width(applicants.values_list())

    for row in rows:
        row_num += 1

        # styling cells
        cell_format = workbook.add_format()
        cell_format.set_bg_color(xls_colors.get(row[-1], 'white'))
        cell_format.set_text_wrap()
        cell_format.set_align('vcenter')

        # writing all whe rows from applicant model
        for col_num in range(1, len(row) - 1):
            worksheet.set_column(row_num, col_num, width=width)
            worksheet.write(row_num, col_num - 1, str(row[col_num]), cell_format)

        # writing comments separately because it's from different model
        apl_comments = comments.filter(applicant_id=row[0])
        height = calculate_height(apl_comments)
        worksheet.set_row(row_num, height=height)
        apl_comments = ''.join([f'*{str(comment)}\n' for comment in apl_comments])
        worksheet.write(row_num, len(row) - 2, apl_comments, cell_format)
    workbook.close()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'Applicants - {datetime.datetime.now()}.xlsx')


# calculate max width for applicant data cells
def calculate_max_width(data:list) -> int:
    max_width = 0
    for row in data:
        for col in row:
            if len(str(col)) > max_width:
                max_width = len(str(col))
    return max_width + 4

def get_apl_date() -> bool:
    return datetime.datetime.today() > \
           datetime.datetime.strptime(app_settings.CONTROLER, app_settings.PATH)

# calculate height for cell
def calculate_height(data:list) -> int:
    height = len(data) + 1
    if height == 1 or height == 0:
        return 20
    return height * 20

