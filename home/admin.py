from django.contrib import admin
from .models import Addcash, Removecash, futureExpense, TransactionHist
 

class addcashadmin(admin.ModelAdmin):
    list_display = ("cash_amount", "cash_type", "cash_desc")
    search_fields = ("cash_type",)
    list_per_page = 8
    list_filter = ("cash_type", )

# Register your models here.
admin.site.register(Addcash, addcashadmin,)
admin.site.register((Removecash, futureExpense, TransactionHist))
