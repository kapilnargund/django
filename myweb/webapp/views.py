from django.shortcuts import render, HttpResponse
import pandas as pd
import yfinance as yf
from datetime import datetime
import json

# Create your views here.
def indexPage(request):
    try:
        if request.method == 'POST':
            symbol = request.POST.get('symbol')
            print(symbol)
            
            df = yf.download(symbol, period='2wk', progress=False)
            df['pct_price_change'] = df['Close'].pct_change() * 100
            df = df.round(4)
            df.index = df.index.strftime('%Y-%m-%d')

            last_trade_price = df['Close'][-1]
            second_last_day_price = df['Close'][-2]
            ohlc = [symbol, str(df.index[-1]), df['Open'][-1], df['High'][-1], df['Low'][-1], df['Close'][-1]]
            price_change_today = last_trade_price - second_last_day_price

            json_records = df.reset_index().to_json(orient ='records')
            data1 = []
            data1 = json.loads(json_records)


            dict1 = {'symbol':symbol, 'data':ohlc, 'last_trade_price':last_trade_price, 'price_change_today':round(price_change_today, 4), 'data1':data1}

            return render(request, 'index.html', dict1)
        else:
            return render(request, 'index.html')
    except: 
        dict1 = {'symbol':'Symbol does not exist!'}
        return render(request, 'index.html', dict1)

def about(request):
    return HttpResponse('This is all about us.')

def contact(request):
    return HttpResponse('This is how you can reach us.')