from django.contrib import admin
from . models import Product, Certificate, Service, Client, Location, TestStandard, Users

# Register your models here.
admin.site.register(Service)
admin.site.register(Users)

@admin.register(Product)
class ProductStandard(admin.ModelAdmin):
    list_display= ['productName','cellTechnology','cellManufacturer']
    fields = ['cellTechnology', ('cellManufacturer',)]
    list_filter = ['cellManufacturer','cellTechnology']
    search_fields = ['productName', 'cellTechnology','cellManufacturer',]

@admin.register(Certificate)
class CertificateStandard(admin.ModelAdmin):
    list_display= ['certID','reportNum','issueDate']
    fields = ['certID', 'reportNum', ('issueDate',)]
    list_filter = ['issueDate','reportNum']
    search_fields = ['=certID', 'reportNum','issueDate']

@admin.register(Location)
class LocationStandard(admin.ModelAdmin):
    list_display= ['city','postalCode','country']
    fields = ['address1', 'address2','city','postalCode','country','phoneNum', ('faxNum',)]
    list_filter = ['country','city']
    search_fields = ['=postalCode','city','country']

@admin.register(TestStandard)
class TestStandard(admin.ModelAdmin):
    list_display= ['testStandard','description','publishDate']
    fields = ['publishDate', 'testStandard', ('description',)]
    list_filter = ['publishDate']
    search_fields = ['=testStandard', 'publishDate']

@admin.register(Client)
class ClientStaff(admin.ModelAdmin):
    list_display= ['clientCode','clientName','clientType']
    fields = ['clientCode', 'clientName', ('clientType',)]
    list_filter = ['clientType']
    search_fields = ['=clientCode', 'clientName']
