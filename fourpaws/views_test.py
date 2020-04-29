from django.shortcuts import render
import csv, os
from django.contrib import messages
from . import models
from . import functions as f
from django.http import HttpResponse, FileResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'staticfiles')
FULFILMENT_DIR = os.path.join(BASE_DIR,'staticfiles\\fourpaws\\fulfilment\\')

def DataImportView(request):
    template = 'fourpaws/dataimportpage.html'
    context = {}
    model = models.FulfilmentDD.objects.all()

    if request.method == 'GET':
        return render(request, template, context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not a .CSV File')

    model.delete()
    new_data = csv_file.read().decode('UTF-8').splitlines()
    dic_data = csv.DictReader(new_data)
    print(dic_data)
    # for row in new_data:
    #     print(row)
        # model.create(
        #              import_file_id= csv_file,
        #              import_date=f.today(),
        #              charity_urn=int(row['charity_urn']),
        #              donor_charity_urn=row['donor_charity_urn'],
        #              call_date=f.date_convertor(row['call_date']),
        #              title=row['title'],
        #              surname=row['surname'],
        #              forename=row['forename'],
        #              initials=row['initials'],
        #              address1=row['address1'],
        #              address2=row['address2'],
        #              address3=row['address3'],
        #              town=row['town'],
        #              county=row['county'],
        #              postcode=row['postcode'],
        #              country=row['country'],
        #              phone_number=row['phone_number'],
        #              email_address=row['email_address'],
        #              gift_aid=row['gift_aid'],
        #              source_code=row['source_code'],
        #              fund_code=row['fund_code'],
        #              fund_title=row['fund_title'],
        #              email_comms_pref=row['email_comms_pref'],
        #              mail_comms_pref=row['mail_comms_pref'],
        #              telephone_comms_pref=row['telephone_comms_pref'],
        #              sms_comms_pref=row['sms_comms_pref'],
        #              amount=float(row['amount']),
        #              frequency=row['frequency'],
        #              collection_date=f.date_convertor(row['collection_date']),
        #              card_holders_name=row['card_holders_name'],
        #              bank_name=row['bank_name'],
        #              bank_account_number=int(row['bank_account_number']),
        #              bank_sort_code=int(row['bank_sort_code']),
        #              )

    return f.download(FULFILMENT_DIR,'izi pizi nub','.docx')

# def DataImportView2(request):
#     template = 'fourpaws/dataimportpage2.html'
#     form = forms.FulfilmentFilesFormInput()
#     model = models.FulfilmentDD.objects.all()
#     context = {
#         'form': form
#     }
#
#     if request.method=='GET':
#         return render(request,template,context)
#
#     form = forms.FulfilmentFilesFormInput(request.POST, request.FILES)
#     if form.is_valid():
#         csv_file = form.cleaned_data['file']
#         csv_file2 = csv_file.read().decode('UTF-8')
#         print(csv_file2)
#     return render(request, template, context)
#
# def fulfilment(request):
#     template = 'fourpaws/fulfilment.html'
#     context={}
#
#     if request.method=='GET':
