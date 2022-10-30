print("Loading, please wait...")

 ## Automatically Install Module (v1.1) Speed: 3 seconds loading time. Prev Speed: 5 seconds loading time.
try:
## get data
    import yfinance as yf
## useful modules
    from time import *
    import pandas as pd
    import matplotlib.pyplot as plt
except:
    print("Error getting modules: 'yfinance', 'time', 'pandas' and 'matplotlib'. Please wait whilst we automatically install them..")
    try:   
        import os
        os.system("pip install yfinance time pandas matplotlib")
        import yfinance as yf
        from time import *
        import pandas as pd
        import matplotlib.pyplot as plt
    except:
        print("Fallback error. Cannot get module 'os' to install modules. Please wait for the next available error when it is safe to exit.")
try:
    import os
except:
    print("OS is unable to install.\n")
    
    
## Gets Google's Data

stock = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter a stock NASDAQ\n> ")
if stock == "admin":
    while True:
        os.system(input("Admin System. \nadmin@admin > "))
    
try:
    google = yf.Ticker(stock)
except:
    print("Error getting stock data.")

## Gets History
df = google.history(period='1d', interval="1m")
print(df.head())



df = google.history(period='1d', interval="1m")
df = df[['Low']]
df.head()

df['date'] = pd.to_datetime(df.index).time
df.set_index('date', inplace=True)
df.head()

## A.I 
X = df.index.values
y = df['Low'].values
offset = int(0.10*len(df))
X_train = X[:-offset]
y_train = y[:-offset]
X_test  = X[-offset:]
y_test  = y[-offset:]
plt.plot(range(0,len(y_train)),y_train, label='Previous')
plt.plot(range(len(y_train),len(y)),y_test,label='Prediction')
plt.legend()
plt.title(stock+" stock")
plt.show()