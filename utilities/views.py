from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from . import details , price , forms

# Create your views here.
def home(request):
    return render(request,'home.html')
    
@login_required
def balance(request):
    form2 = forms.Balance
    balance = 0
    context = {
        'form2':form2,
    }
    if request.method == 'POST':
        form2 = form2(request.POST)
        if form2.is_valid():
            Address = form2.cleaned_data['Address']
            Coin = form2.cleaned_data['Coin']
        if details.checkaddress(Address) == True:
            if Coin == 'ETH':
                balance = details.getbalanceeth(Address)
                balanceedit = str(balance) + ' ' + Coin
                context_edit = {
                    'balance': balanceedit,
                    'Address': Address,
                }
            else:
                print('1',Address,Coin)
                balance = details.getbalance(Address,Coin)
                balanceedit = str(balance) + ' ' + Coin
                print(balance,balanceedit)
                context_edit = {
                    'balance': balanceedit,
                    'Address': Address,
                }
        else:
            context_edit = {
                'balance': 'Invalid Address',
                'Address': Address,
            }
        context.update(context_edit)

    return render(request,'balance.html',context)

#price = price.getPrice('BTC','INR')

currency = [
    'USD',
    'AUB',
    'CAD',
    'CNY',
    'EUR',
    'INR',
    'JPY',
    'SGD'
]

@login_required
def converter(request):
    price1 = 0
    price2 = 0
    form = forms.Converter
    context = {
    'form': form,
    }
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            ConvertFrom = form.cleaned_data['ConvertFrom']
            ConvertTo = form.cleaned_data['ConvertTo']
            Quantity = form.cleaned_data['Quantity']
            if ConvertTo in currency:
                convert = ConvertTo
                symbol = ConvertFrom
                price1 = price.getPrice(symbol,convert)
                convertedamount = Quantity*price1
            else:
                convert = 'USD'
                symbol = ConvertFrom
                price1 = price.getPrice(symbol,convert)
                symbol = ConvertTo
                price2 = price.getPrice(symbol,convert)
                convertedamount = Quantity*(price1/price2)
            print('convertedamount-',convertedamount)
                
            
            print('convert from',ConvertFrom,'convert to',ConvertTo,'quantity',Quantity)
            context_edit = {
                    'convert': convert,
                    'symbol': symbol,
                    'convertedamount' : convertedamount,
                    'convertFrom': ConvertFrom,
                    'convertTo': ConvertTo,
                    'Quantity': Quantity,
                    'price1': price1,
                    'price2':price2,
                            }
            context.update(context_edit)


    return render(request,'converter.html',context)

    
@login_required
def dashboard(request):
    return render(request,'dashboard.html')