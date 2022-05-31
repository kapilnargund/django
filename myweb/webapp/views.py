from django.shortcuts import render, HttpResponse
import pandas as pd
import yfinance as yf
from datetime import datetime

# Create your views here.
def indexPage(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        print(symbol)
        
        df = yf.download(symbol, period='2wk', progress=False)
        df['pct_price_change'] = df['Close'].pct_change() * 100

        last_trade_price = df['Close'][-1]
        second_last_day_price = df['Close'][-2]
        ohlc = [symbol, str(df.index[-1]), df['Open'][-1], df['High'][-1], df['Low'][-1], df['Close'][-1]]
        price_change_today = last_trade_price - second_last_day_price


        dict1 = {'symbol':symbol, 'data':ohlc, 'last_trade_price':last_trade_price, 'price_change_today':price_change_today, 'df':df}

        return render(request, 'index.html', dict1)
    else:
        return render(request, 'index.html')

def about(request):
    return HttpResponse('This is all about us.')

def contact(request):
    return HttpResponse('This is how you can reach us.')