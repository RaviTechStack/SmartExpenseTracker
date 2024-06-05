from django.db import models

# Create your models here.
class Addcash(models.Model):
    cash_id = models.AutoField(primary_key=True)
    cash_amount = models.IntegerField()
    cash_type = models.CharField(max_length=15)
    cash_desc = models.CharField(max_length=500)
    
class Removecash(models.Model):
    cash_id = models.AutoField(primary_key=True)
    cash_amount = models.IntegerField()
    cash_type = models.CharField(max_length=15)
    cash_desc = models.CharField(max_length=500)

class futureExpense(models.Model):
    exp_id = models.AutoField(primary_key=True)
    exp_amt = models.IntegerField()
    exp_desc = models.CharField(max_length = 500)
    exp_type = models.CharField(max_length=15, default="note")


# auto_mow_add = True

class TransactionHist(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_amt = models.IntegerField()
    trans_desc = models.CharField(max_length=500)
    trans_type = models.CharField(max_length=15)
    is_withdrwal = models.BooleanField()
    trans_time = models.DateTimeField(auto_now_add= True)
