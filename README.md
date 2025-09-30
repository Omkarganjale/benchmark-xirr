# benchmark-xirr
Get XIRR for investments and compare it with a benchmark

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


---

Low level frontend sketch

---
 
---------------------------------------------------------------
                     XIRR Calculator                          
"Understand your portfolio's true returns and see            
how it compares with benchmarks like NIFTY 50,             
Sensex, and more."
 
---------------------------------------------------------------
               CONDITIONAL INPUT SECTION                     
---------------------------------------------------------------
[✓] Calculate for SIP? then following fields appear

If clicked → dropdown form:
- Start Date of SIP: [ DD-MM-YYYY ]
- Investment Type: ( Monthly ☐ / Quarterly ☐ / Yearly ☐ )
- Date of Month: [ 1-28 ] (default = DD from start)
- Step Up: [   ] %  (0–100, monthly/yearly/quarterly)

---------------------------------------------------------------
                  TRANSACTIONS TABLE                         
---------------------------------------------------------------
Date        | Type (toggle)       | Amount                     
------------ |--------------------|----------------------------
01-01-2024  | [Invested/Red]     | [1000.00]                  
01-02-2024  | [Redeemed/Green]   | [2000.00]                  
...         | ...                | ...                         
[+ Add Row]
 
---------------------------------------------------------------
                  BENCHMARK SELECTION                        
---------------------------------------------------------------
"Select benchmarks to compare with:"                        
[☐ Nifty50]  [☐ Sensex]  [☐ SmallCap]  [☐ Gold]
 
---------------------------------------------------------------
                  SUBMIT + LOADER                             
---------------------------------------------------------------
[ SUBMIT ]

(Loader animation...)                                        
"Patience is the key to successful investing."
 
---------------------------------------------------------------
                     RESULTS SECTION                          
---------------------------------------------------------------
Results:
1. Linear Gauge: multi-colored markers on color gradient RG line

Linear Gauge (XIRR %)                                       
-40%    -20%      0%      20%      40%                        
|---------|---------|---------|---------|                   
    ● Nifty50                                         
              ● Sensex                                    
                        ● SmallCap                                            
          ● Gold                                  
                            ▲ Your Portfolio

2. Bullet chart on returns 

\---
|  |
|__|  Your Portfolio
|  |
|__|  Nifty50
|__|  Nifty100
|  |
|--|  Gold

Cards:                                                       
[ Total Invested ]
- Amount: 50,000
- Period: Jan 2024 – Sep 2025

[ Your Portfolio XIRR ]
- Total Returns: 12,000
- XIRR: 15%

[ Nifty50 XIRR ]
- Total Returns: 11,500
- XIRR: 14%

[ Sensex XIRR ]
- Total Returns: 11,800
- XIRR: 14.2%

[ SmallCap XIRR ]
- Total Returns: 13,000
- XIRR: 16%

[ Gold XIRR ]
- Total Returns: 10,500
- XIRR: 12%

---------------------------------------------------------------
                           FAQS                                
---------------------------------------------------------------
[ Q: What is XIRR? ]  (click to expand)                     
A: XIRR is the extended internal rate of return, which calculates returns considering exact dates of cashflows.

[ Q: How is it different from CAGR? ]  (click to expand)    
A: CAGR assumes uniform investment growth over time, while XIRR accounts for irregular cashflows and timings.

[ Q: Can I compare multiple benchmarks? ]  (click to expand)
A: Yes, you can select multiple benchmarks like Nifty50, Sensex, SmallCap, and Gold to compare against your portfolio.

[ Q: How often should I update transactions? ]  (click to expand)
A: Update transactions whenever you invest or redeem to get accurate XIRR calculations.
 
---------------------------------------------------------------
                           FOOTER                               
---------------------------------------------------------------
Made with ♥ by Omkar                                          
[ GitHub Link ]  [ Developer Profile Link ]                  
 