from django.shortcuts import render, redirect, HttpResponse
from .models import Addcash, Removecash, futureExpense, TransactionHist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):

    # CALCULATING VALUE FOR TOTAL SAVING
    total = Addcash.objects.all()
    total_withdrawal = Removecash.objects.all()
    total_amt = 0
    total_remove = 0

    for amt in total:
        total_amt += amt.cash_amount

    for amt in total_withdrawal:
        total_remove += amt.cash_amount
    
    exact_total_saving = total_amt - total_remove
    usd = exact_total_saving/82.03

    # CALCULATING NOTES VALUE     
    notes = Addcash.objects.filter(cash_type = "note")
    note_withdrwal = Removecash.objects.filter(cash_type = "note")
    note_amt = 0
    note_remove = 0

    for amt in notes:
        note_amt += amt.cash_amount
    
    for amt in note_withdrwal:
        note_remove += amt.cash_amount
    
    exact_note_saving = note_amt - note_remove


    # CALCULATING COIN VALUE  
    coin = Addcash.objects.filter(cash_type = "coin")
    coin_withdrwal = Removecash.objects.filter(cash_type = "coin")
    coin_amt = 0
    coin_remove = 0
    
    for amt in coin:
        coin_amt += amt.cash_amount
    
    for amt in coin_withdrwal:
        coin_remove += amt.cash_amount

    excat_coin_saving = coin_amt - coin_remove


    # CALCULATING BANK VALUE  
    bank = Addcash.objects.filter(cash_type = "bank")
    bank_withdrwal = Removecash.objects.filter(cash_type = "bank")
    bank_amt = 0
    bank_remove = 0 
    
    for amt in bank:
        bank_amt += amt.cash_amount
    
    for amt in bank_withdrwal:
        bank_remove += amt.cash_amount
    
    excat_bank_saving = bank_amt - bank_remove


    # CALCULATING OTHER'S VALUE  
    other = Addcash.objects.filter(cash_type = "other")
    other_withdrawal = Removecash.objects.filter(cash_type = "other")
    other_amt = 0
    other_remove = 0
    
    for amt in other:
        other_amt += amt.cash_amount

    for amt in other_withdrawal:
        other_remove += amt.cash_amount
    
    excat_other_saving = other_amt - other_remove

    # SENDING RECENT TRANSACTION HISTORY
    recent_hist = TransactionHist.objects.all().order_by("-trans_time")[0:5]
    params = {
        "total_cash" : exact_total_saving,
        "total_note" : exact_note_saving,
        "total_coin" : excat_coin_saving,
        "total_bank" : excat_bank_saving,
        "total_other" : excat_other_saving,
        "histories" : recent_hist,
        "usd" : round(usd, 3)

    }
    return render(request, "index.html", params)

def handelsignup(request):
    if request.method ==  "POST":
        fname =  request.POST.get("firstname")
        lname = request.POST.get("lastname")
        username =  request.POST.get("username1")
        password = request.POST.get("password1")

        user = User.objects.create_user(username, fname, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect("/")
    return render(request, "index.html")

def handellogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("invalid credential")
    return render(request, "index.html")


def handellogout(request):
    logout(request)
    return redirect("/")

def futureExpen(request):
    all_future_exp = futureExpense.objects.all()
    params = {
        "allExp" : all_future_exp
    }
    return render(request, "futureexe.html", params)

def addexpense(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        trans_type = request.POST.get("trans-type")
        add_future_expense = futureExpense(exp_amt= amount, exp_desc = desc, exp_type = trans_type)
        add_future_expense.save()
        return redirect("/futureExpen")
    return render(request, "addexpense.html")

def paid(request, id):
    exp = futureExpense.objects.get(exp_id = id)
    add = Removecash(cash_amount = exp.exp_amt, cash_type = exp.exp_type, cash_desc = exp.exp_desc)
    add.save()
    trans =  TransactionHist(trans_amt = exp.exp_amt, trans_desc = exp.exp_desc, trans_type = exp.exp_type, is_withdrwal = False)
    trans.save()
    exp.delete()
    return redirect("/futureExpen")

def delete(request, id):
    exp = futureExpense.objects.get(exp_id = id)
    exp.delete()
    return redirect("/futureExpen")

def updates(request , id):
    exp = futureExpense.objects.get(exp_id = id)
    if request.method == "POST" :
        exp.exp_amt = request.POST.get("amount")
        exp.exp_desc = request.POST.get("desc")
        exp.exp_type = request.POST.get("trans-type")

        exp.save()
        return redirect("/futureExpen")
    return render(request, "addexpense.html")


def history(request):
    recent_hist = TransactionHist.objects.all().order_by("-trans_time")
    params = {
        "histories": recent_hist,
    }
    return render(request, "history.html", params)

def addnote(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Addcash(cash_amount = amount, cash_type = "note", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "note", is_withdrwal = False)
        trans.save()
        print("notes")
        return redirect("/")
    return render(request, "addcash.html")

def withdrawnote(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Removecash(cash_amount = amount, cash_type = "note", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "note", is_withdrwal = True)
        trans.save()
        return redirect("/")
    return render (request, "addcash.html")

def addcoin(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Addcash(cash_amount = amount, cash_type = "coin", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "coin", is_withdrwal = False)
        trans.save()
        print("coin")
        return redirect("/")
    return render(request, "addcash.html")

def withdrawcoin(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Removecash(cash_amount = amount, cash_type = "coin", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "coin", is_withdrwal = True)
        trans.save()
        return redirect("/")
    return render (request, "addcash.html")

def addbank(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Addcash(cash_amount = amount, cash_type = "bank", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "bank", is_withdrwal = False)
        trans.save()
        return redirect("/")
    return render(request, "addcash.html")

def withdrawbank(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Removecash(cash_amount = amount, cash_type = "bank", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "bank", is_withdrwal = True)
        trans.save()
        return redirect("/")
    return render (request, "addcash.html")

def addother(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Addcash(cash_amount = amount, cash_type = "other", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "other", is_withdrwal = False)
        trans.save()
        return redirect("/")
    return render(request, "addcash.html")

def withdrawother(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        add = Removecash(cash_amount = amount, cash_type = "other", cash_desc = desc)
        add.save()
        trans =  TransactionHist(trans_amt = amount, trans_desc = desc, trans_type = "other", is_withdrwal = True)
        trans.save()
        return redirect("/")
    return render (request, "addcash.html")