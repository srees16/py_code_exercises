import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aapl = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
aapl