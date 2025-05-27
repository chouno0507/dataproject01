import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 시총 상위 10개 기업의 티커 리스트
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "BRK-B", "TSLA", "TSM", "2222.SR"]

# 기간 설정
end = datetime.today()
start = end - timedelta
