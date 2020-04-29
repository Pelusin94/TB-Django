import datetime
from django.http import HttpResponse, FileResponse



#Returns string dates '02/10/2020' as datetime.date type 2020/10/02
def date_convertor(DDMMYYYY):
    day = int(DDMMYYYY[0:2])
    month = int(DDMMYYYY[4:5])
    year = int(DDMMYYYY[6:10])
    return datetime.date(year, month, day)

#Returns current date as datime.date type YYYYMMDD
def today():
    return datetime.date.today()

#Returns a FileResponse object of the given file path
def download(path, name, type):
    open_file = open(path,'rb')
    file = FileResponse(open_file)
    file['Content-Disposition'] = 'filename="{file_name}{file_format}"'.format(file_name=name, file_format=type)
    return file

