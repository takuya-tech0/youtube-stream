import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

aapl = yf.Ticker('AAPL')
aapl.history()
