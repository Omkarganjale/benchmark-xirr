# benchmark-xirr
Get XIRR for investments and compare it with a benchmark

TODO FIX:
for input :
{
"dates": ["2001-01-01", "2002-01-01", "2025-09-01"],
"cashflows": [-10000, -10000, 150000],
"benchmarks": ["NIFTY50"]
}

2025-09-29 20:31:38,013 - services.CalculationService - INFO - len of cashflows: 2 & len of benchmark_values: 1 & len of dates: 3

TODO:
* Backend:
    * SIP
    * Add Benchmark tickers: S&P500, NASDAQ100, INRUSD, LargeCapMidCap, Commodity(Gold, Silver, Crude Oil in INR)

* Frontend:
    * XIRR basics
    * Sorted on dates
    * Last cashflow value is positive and current portfolio value
    * In case future date, benchmark xirr is not possible
    * Yahoo Finance notice
    * Investment Disclaimer
    * FAQs