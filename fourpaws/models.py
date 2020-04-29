from django.db import models

from django.db import models

class FulfilmentDD(models.Model):
    import_file_id = models.CharField(max_length=50, null=True)
    import_date = models.DateField(null=True)
    charity_urn = models.IntegerField(null=True)
    donor_charity_urn = models.CharField(max_length=15, null=True)
    call_date = models.DateField(null=True)
    title = models.CharField(max_length=10, null=True)
    surname = models.CharField(max_length=20, null=True)
    forename = models.CharField(max_length=20, null=True)
    initials = models.CharField(max_length=5, null=True)
    address1 = models.CharField(max_length=50, null=True)
    address2 = models.CharField(max_length=50, null=True)
    address3 = models.CharField(max_length=50, null=True)
    town = models.CharField(max_length=50, null=True)
    county = models.CharField(max_length=50, null=True)
    postcode = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(null=True, max_length=20)
    email_address = models.EmailField(null=True)
    gift_aid = models.CharField(max_length=2, null=True)
    source_code = models.CharField(max_length=10, null=True)
    fund_code = models.CharField(max_length=10, null=True)
    fund_title = models.CharField(max_length=10, null=True)
    email_comms_pref = models.CharField(max_length=2, null=True)
    mail_comms_pref = models.CharField(max_length=2, null=True)
    telephone_comms_pref = models.CharField(max_length=2, null=True)
    sms_comms_pref = models.CharField(max_length=2, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    frequency = models.CharField(max_length=10, null=True)
    collection_date = models.DateField(null=True)
    card_holders_name = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=50, null=True)
    bank_account_number = models.IntegerField(null=True)
    bank_sort_code = models.IntegerField(null=True)

    def __str__(self):
        return self.forename

class DateRange(models.Model):
    merge_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

class UploadedFiles(models.Model):
    file_name = models.CharField(max_length=50)
    file_path = models.FileField(upload_to='fourpaws/letters')
    upload_date = models.DateField(auto_now_add=True, blank=True, null=True)


class FulfilmentDdView(models.Model):
    id = models.IntegerField(primary_key=True)
    import_file_id = models.CharField(max_length=50, blank=True, null=True)
    import_date = models.DateField(blank=True, null=True)
    charity_urn = models.IntegerField(blank=True, null=True)
    donor_charity_urn = models.CharField(max_length=15, blank=True, null=True)
    call_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=10, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    forename = models.CharField(max_length=20, blank=True, null=True)
    initials = models.CharField(max_length=5, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    address3 = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.CharField(max_length=254, blank=True, null=True)
    gift_aid = models.CharField(max_length=2, blank=True, null=True)
    source_code = models.CharField(max_length=10, blank=True, null=True)
    fund_code = models.CharField(max_length=10, blank=True, null=True)
    fund_title = models.CharField(max_length=10, blank=True, null=True)
    email_comms_pref = models.CharField(max_length=2, blank=True, null=True)
    mail_comms_pref = models.CharField(max_length=2, blank=True, null=True)
    telephone_comms_pref = models.CharField(max_length=2, blank=True, null=True)
    sms_comms_pref = models.CharField(max_length=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frequency = models.CharField(max_length=10, blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    card_holders_name = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_account_number = models.IntegerField(blank=True, null=True)
    bank_sort_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'fulfilment_dd_view'
