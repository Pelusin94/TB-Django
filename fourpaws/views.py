from django.shortcuts import render, redirect
import csv, os
from django.contrib import messages
from . import models
from . import functions as f
from . import forms
import codecs


def main_response(request):
    template = 'fourpaws/main.html'
    context={}
    return render(request, template, context)

def fulfilment_response(request):
    template = 'fourpaws/fulfilment.html'
    FulfilmentOutputForm = forms.FulfilmentOutputForm()
    csv_form = forms.UploadedCsvFiles_form()
    word_form = forms.UploadedWordFiles_form()
    FulfilmentLetterSelectForm = forms.FulfilmentLetterSelectForm()
    letters_list = models.UploadedWordFiles_table.objects.all()
    tobe_thanked = False
    csv_uploaded = False
    letter_uploaded = False
    row_count = 0

    context = {
        'csv_form': csv_form,
        'form_output': FulfilmentOutputForm,
        'word_form': word_form,
        'form_letter_select': FulfilmentLetterSelectForm,
        'letters_list': letters_list,
        'tobe_thanked': tobe_thanked,
        'csv_uploaded': csv_uploaded,
        'letter_uploaded': letter_uploaded,
    }

    if request.method == 'GET':
        if 'download_letter' in request.GET:
            FulfilmentOutputForm = forms.FulfilmentOutputForm(request.GET)

            if FulfilmentOutputForm.is_valid():
                model = models.DateRange_table.objects.all()
                start_date = FulfilmentOutputForm.cleaned_data['date_from']
                end_date = FulfilmentOutputForm.cleaned_data['date_to']
                model.delete()
                model.create(
                    merge_date=f.today(),
                    start_date=start_date,
                    end_date=end_date,
                )
                tobe_thanked = models.FulfilmentddView.objects.all()

    elif request.method == 'POST':
        if 'upload_csv' in request.POST:
            csv_form = forms.UploadedCsvFiles_form(request.POST, request.FILES)
            if csv_form.is_valid():
                model = models.FulfilmentDD_table.objects.all()
                csv_file = csv_form.cleaned_data['file_path']
                data = csv_file.read().decode('UTF-8').splitlines()
                dic_data = csv.DictReader(data)
                csv_uploaded = True
                model.delete()
                for row in dic_data:
                    row_count += 1
                    model.create(
                        import_file_id=csv_file,
                        import_date=f.today(),
                        charity_urn=int(row['charity_urn']),
                        donor_charity_urn=row['donor_charity_urn'],
                        call_date=f.date_convertor(row['call_date']),
                        title=row['title'],
                        surname=row['surname'],
                        forename=row['forename'],
                        initials=row['initials'],
                        address1=row['address1'],
                        address2=row['address2'],
                        address3=row['address3'],
                        town=row['town'],
                        county=row['county'],
                        postcode=row['postcode'],
                        country=row['country'],
                        phone_number=row['phone_number'],
                        email_address=row['email_address'],
                        gift_aid=row['gift_aid'],
                        source_code=row['source_code'],
                        fund_code=row['fund_code'],
                        fund_title=row['fund_title'],
                        email_comms_pref=row['email_comms_pref'],
                        mail_comms_pref=row['mail_comms_pref'],
                        telephone_comms_pref=row['telephone_comms_pref'],
                        sms_comms_pref=row['sms_comms_pref'],
                        amount=float(row['amount']),
                        frequency=row['frequency'],
                        collection_date=f.date_convertor(row['collection_date']),
                        card_holders_name=row['card_holders_name'],
                        bank_name=row['bank_name'],
                        bank_account_number=int(row['bank_account_number']),
                        bank_sort_code=int(row['bank_sort_code']),
                    )
                csv_form.save()
                print(data)
                print(type(data))


        if 'upload_letter' in request.POST:
            word_form = forms.UploadedWordFiles_form(request.POST, request.FILES)
            if word_form.is_valid():
                word_form.save()
                letter_uploaded = True

    context = {
        'csv_form': csv_form,
        'form_output': FulfilmentOutputForm,
        'word_form': word_form,
        'form_letter_select': FulfilmentLetterSelectForm,
        'letters_list': letters_list,
        'tobe_thanked': tobe_thanked,
        'csv_uploaded': csv_uploaded,
        'letter_uploaded': letter_uploaded,
        'row_count': row_count,
    }

    return render(request, template, context)

















