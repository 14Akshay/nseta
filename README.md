# nseta :nerd_face:

[![Build Status](https://travis-ci.com/pkjmesra/nseta.svg?branch=main)](https://travis-ci.com/pkjmesra/nseta)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/pkjmesra/nseta/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/nseta/month)](https://pepy.tech/project/nseta/month)
[![Python](https://img.shields.io/pypi/pyversions/nseta.svg?style=plastic)](https://badge.fury.io/py/nseta)
[![PyPI](https://badge.fury.io/py/nseta.svg)](https://badge.fury.io/py/nseta)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/14cc594e2dfe48519c699caa48136108)](https://app.codacy.com/gh/pkjmesra/nseta?utm_source=github.com&utm_medium=referral&utm_content=pkjmesra/nseta&utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/7c6a7a47c41a40638d6f9204219aed77)](https://www.codacy.com/gh/pkjmesra/nseta/dashboard?utm_source=github.com&utm_medium=referral&utm_content=pkjmesra/nseta&utm_campaign=Badge_Coverage)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/pkjmesra/nseta.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pkjmesra/nseta/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/pkjmesra/nseta.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pkjmesra/nseta/context:python)
[![codecov](https://codecov.io/gh/pkjmesra/nseta/branch/main/graph/badge.svg)](https://codecov.io/gh/pkjmesra/nseta)

Python Library (and console/CLI application) to 
-  Get publicly available data on [NSE India website](https://www1.nseindia.com/) <img src="/docs/assets/NSE_Logo.svg" width="118" height="28" alt="NSE India" > ie. stock live-quotes and historical data[ *EQUITY ONLY* AT THIS TIME. No support for Futures/Options/Derivatives yet.]
-  Plot various technical indicators
-  Pattern recognition and fitment using candlestick charts
-  Backtest trading strategies
-  Forecasting with standard as well as custom strategies
-  Create scanners and generate signals for various technical indicators or for BUY/SELL
-  Create and build your own trading strategy

## Disclaimer
- The recommendations that you receive when you run the scan for intraday or swing trading is only for academic research purposes.
- Though, you are free to take the recommended BUY/SELL positions, any loss you make from those are entirely at your own risk.
- The author of this library/console cannot be held responsible and is deemed free from any legal liability.

## Donate

It takes a lot of time/effort to develop, implement, test and maintain the codebase. When possible, please donate as per your wishes.
[![Otechie](https://api.otechie.com/pkjmes/badge.svg)](https://otechie.com/pkjmes)

## Tech Disclaimer
This has been built and tested only on macOS Big Sur (v11+). You may wish to check the `.travis.yml` or the `python-publish.yml` file to understand how to build from source. If you test it on a platform other than macOS and find issues, please do report those in the `issues` tab above.

## Libraries Required
- (See requirements.txt file for more)

For Windows systems you can install Anaconda, this will cover many dependancies (You'll have to install requests and beautifulsoup additionally though)

## Installation
-  From code
```
python3 setup.py clean build install
```
-  Python pip
```
pip3 install nseta
```
-  Installing specific version
```
pip3 install nseta==0.6.202
```
  You can also directly install specific versions from pypi.org:
```
pip install --index-url https://pypi.org/simple/ --extra-index-url https://pypi.org/simple nseta==<Specific_Version>
```

-  Python shell
``` 
python3 -m pip install --upgrade nseta
```
-  Wheel (.whl) file from PyPi.org

  Just go ahead and download the ```.whl``` file from ```https://pypi.org/project/nseta/#files``` and install from the downloaded directory:

```
pip3 install ./nseta-0.6.202-py3-none-any.whl
```
  where `0.6.202` is the version of the library.

- Specific test versions(under development) can be installed from test.pypi.org
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple nseta==<Specific_Version>
```

After installation you can check what version you got installed
```
python3 -c "import nseta; print(nseta.__version__)"
```

## Usage

- Top level command options that provide you with various features
```python

#Usage Commands (You can use nsetacli or nseta - either is good.)
$ $ nseta
Usage: nseta [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug  --debug to turn debugging on. Default is off
  --version             Shows the version of this library
  --trace / --no-trace  --trace to turn tracing on (works only with --debug).
                        Default is off.
  -f, --filter TEXT     --filter <TEXT> to show only logs that match the
                        filter text. Works only with --debug
  --help                Show this message and exit.

Commands:
  clear                  Force clears log files, downloaded contents etc.
  create-cdl-model       Create candlestick model.Plot uncovered patterns
  forecast-strategy      Forecast & measure performance of a trading model
  history                Get price history of a security for given dates
  live-quote             Get live price quote of a security
  pe-history             Get PE history of a security for given dates
  plot-ta                Plot various technical analysis indicators
  scan                   Scan live and intraday for prices and signals.
  scan-trading-strategy  Test/Measure the performance of your trading strategies
  test-trading-strategy  Measure the performance of your trading strategy
```
- Sample commands
```python

  Example:
  nseta clear -d
  nseta create-cdl-model -S bandhanbnk -s 2019-07-30 -e 2020-11-20 --steps
  nseta forecast-strategy -S bandhanbnk -s 2019-07-30 -e 2020-11-20 --strategy rsi
  nseta history -S bandhanbnk -s 2019-07-30 -e 2020-11-20
  nseta live-quote -S bandhanbnk
  nseta pe-history -S bandhanbnk -s 2019-07-30 -e 2020-11-20
  nseta plot-ta -S bandhanbnk -s 2019-07-30 -e 2020-11-20
  nseta scan -S HDFC,ABB -s
  nseta scan -i
  nseta scan -l
  nseta scan -s
  nseta scan -v
  nseta scan-trading-strategy -S bandhanbnk -s 2019-07-30 -e 2020-11-20 --strategy rsi
  nseta scan-trading-strategy -s 2019-07-30 -e 2020-11-20 --strategy rsi
  nseta scan-trading-strategy -s 2019-07-30 -e 2020-11-20
  nseta test-trading-strategy -S bandhanbnk -s 2019-07-30 -e 2020-11-20 --strategy rsi
```

- Test your trading strategies

```python
nseta test-trading-strategy
Please provide start and end date in format yyyy-mm-dd
Usage:  [OPTIONS]

  Measure the performance of your trading strategy

Options:
  -S, --symbol TEXT               Security code
  -s, --start TEXT                Start date in yyyy-mm-dd format
  -e, --end TEXT                  End date in yyyy-mm-dd format
  --strategy [rsi|smac|macd|emac|bbands|multi|custom]
                                  rsi, smac, macd, emac, bbands, multi,
                                  custom. Choose one.
  -u, --upper TEXT                Used as upper limit, for example, for RSI.
                                  Only when strategy is "custom", we buy the
                                  security when the predicted next day return
                                  is > +{upper} %
  -l, --lower TEXT                Used as lower limit, for example, for RSI.
                                  Only when strategy is "custom", we sell the
                                  security when the predicted next day return
                                  is < -{lower} %
  --autosearch / --no-autosearch  --auto for allowing to automatically measure
                                  the performance of your trading strategy on
                                  multiple combinations of parameters.
  -i, --intraday                  Test trading strategy for the current
                                  intraday price history (Optional)
  --help                          Show this message and exit.
```

- Test your trading strategies (for example, using *RSI* as technical indicator)

```python
$ nseta test-trading-strategy -S bandhanbnk -s 2020-01-01 -e 2020-10-03 --strategy rsi

Time used (seconds): 0.13728976249694824
Optimal parameters: {'init_cash': 100000, 'buy_prop': 1, 'sell_prop': 1, 'commission': 0.0075, 'execution_type': 'close', 'channel': None, 'symbol': None, 'rsi_period': 14, 'rsi_upper': 70, 'rsi_lower': 15}
Optimal metrics: {'rtot': 0.4850052910757702, 'ravg': 0.00255265942671458, 'rnorm': 0.9026928562651005, 'rnorm100': 90.26928562651005, 'sharperatio': None, 'pnl': 62418.36, 'final_value': 162418.36025}
   rsi_period  rsi_upper  rsi_lower  init_cash    final_value       pnl
0          14         70         15     100000  162418.360250  62418.36
1          11         70         15     100000  154007.773625  54007.77
2           7         70         15     100000   96213.602375  -3786.40
3          14         70         30     100000   83074.073000 -16925.93
4          11         70         30     100000   78397.304875 -21602.70
```
![](./docs/assets/trading_strategy_rsi.png)

- Check historical data and export to csv file

```
$ nseta history -S bandhanbnk -s 2019-01-01 -e 2020-09-30
       Symbol Series        Date  Prev Close    Open   High     Low    Last   Close    VWAP   Volume      Turnover  Trades  Deliverable Volume  %Deliverable
0  BANDHANBNK     EQ  2019-01-01      550.15  552.50  560.0  544.10  558.00  556.70  552.21   589317  3.254256e+13   16658              175430        0.2977
1  BANDHANBNK     EQ  2019-01-02      556.70  553.00  563.7  549.60  551.40  552.15  556.91   834846  4.649319e+13   32119              250782        0.3004
2  BANDHANBNK     EQ  2019-01-03      552.15  551.00  554.0  530.00  532.05  533.80  540.61   620161  3.352631e+13   18616              282037        0.4548
3  BANDHANBNK     EQ  2019-01-04      533.80  534.25  541.7  527.05  528.05  528.90  533.42   579027  3.088645e+13   22405              186702        0.3224
4  BANDHANBNK     EQ  2019-01-07      528.90  540.00  542.0  495.55  495.55  498.05  509.49  2684675  1.367813e+14   76816             1160901        0.4324
Saved to: bandhanbnk.csv
```
- Create candlestick model
```python
nseta create-cdl-model
Usage:  [OPTIONS]

  Create candlestick model.Plot uncovered patterns

Options:
  -S, --symbol TEXT       Security code
  -s, --start TEXT        Start date in yyyy-mm-dd format
  -e, --end TEXT          End date in yyyy-mm-dd format
  -o, --file TEXT         Output file name. Default is {symbol}.csv
  --steps / --no-steps    --steps for saving intermediate steps in output file
  -f, --format [csv|pkl]  Output format, pkl - to save as Pickel and csv - to
                          save as csv
  --help                  Show this message and exit.
```
- Create candlestick models with pattern recognition
```
$ nseta create-cdl-model -S bandhanbnk -s 2019-01-01 -e 2020-09-30 --steps
                Symbol Series  Prev Close    Open   High  ...  CDLUNIQUE3RIVER  CDLUPSIDEGAP2CROWS  CDLXSIDEGAP3METHODS  candlestick_pattern  candlestick_match_count
Date                                                      ...                                                                                                        
2019-01-01  BANDHANBNK     EQ      550.15  552.50  560.0  ...                0                   0                    0           CDLHARAMI_Bull                      0.0
2019-01-02  BANDHANBNK     EQ      556.70  553.00  563.7  ...                0                   0                    0           CDLHARAMI_Bull                      0.0
2019-01-03  BANDHANBNK     EQ      552.15  551.00  554.0  ...                0                   0                    0           CDLMATCHINGLOW_Bull                      0.0
2019-01-04  BANDHANBNK     EQ      533.80  534.25  541.7  ...                0                   0                    0           CDLBELTHOLD_Bull                      0.0
2019-01-07  BANDHANBNK     EQ      528.90  540.00  542.0  ...                0                   0                    0           CDLTHRUSTING_Bear                      0.0

[5 rows x 72 columns]
Model saved to: bandhanbnk.csv
Candlestick pattern model plot saved to: bandhanbnk_candles.html
```
![](./docs/assets/cdl_model.png)

- Create various plots for analysis with technical indicators 
```
$ nseta plot-ta -S bandhanbnk -s 2019-01-01 -e 2020-09-30
```
![](./docs/assets/ti_plots.png)

- Forecast strategies
```python
nseta forecast-strategy
Usage:  [OPTIONS]

  Forecast & measure performance of a trading model

Options:
  -S, --symbol TEXT               Security code
  -s, --start TEXT                Start date in yyyy-mm-dd format
  -e, --end TEXT                  End date in yyyy-mm-dd format
  --strategy [rsi|smac|macd|emac|bbands|multi|custom]
                                  rsi, smac, macd, emac, bbands, multi,
                                  custom. Choose one.
  -u, --upper FLOAT               Only when strategy is "custom". We buy the
                                  security when the predicted next day return
                                  is > +{upper} %
  -l, --lower FLOAT               Only when strategy is "custom". We sell the
                                  security when the predicted next day return
                                  is < -{lower} %
  --help                          Show this message and exit.
```
- Create forecast strategies and verify them
```python
$ nseta forecast-strategy -S bandhanbnk -s 2019-01-01 -e 2020-09-30 --upper 1.5 --lower 1.5
   init_cash   final_value       pnl
0     100000  137220.87825  37220.88
```
![](./docs/assets/forecast-closing.png)
![](./docs/assets/forecast.png)
![](./docs/assets/forecast-predictions.png)

-  Get live quotes for a security
```python
nseta live-quote
Please provide security/index code
Usage:  [OPTIONS]

  Get live price quote of a security along with other (Optional) parameters

Options:
  -S, --symbol TEXT  Security code
  --series TEXT      Default series - EQ (Equity) (Optional)
  -g, --general      Get the general (Name, ISIN) details also (Optional)
  -o, --ohlc         Get the OHLC values also (Optional)
  -w, --wk52         Get the 52 week high/low values also (Optional)
  -v, --volume       Get the traded volume details also (Optional)
  -b, --orderbook    Get the current bid/offer details also (Optional)
  -p, --plot         Plot the "Close" values (Optional)
  -r, --background   Keep running the process in the background (Optional)
  --help             Show this message and exit.
```
-  Get live quotes with multiple options along with intraday history
```python
nseta live-quote -S bandhanbnk -gowvb
------------------------------------------
                                           
Name                |  Bandhan Bank Limited
ISIN                |          INE545U01014
Last Updated        |  29-DEC-2020 16:00:00
Prev Close          |                406.15
Last Trade Price    |                413.50
Change              |                  7.35
% Change            |                  1.81
Avg. Price          |                414.43
Upper Band          |                437.95
Lower Band          |                358.35
Open                |                408.00
High                |                419.25
Low                 |                407.45
Close               |                413.20
52 Wk High          |                526.00
52 Wk Low           |                152.20
Quantity Traded     |             82,37,480
Total Traded Volume |             82,37,480
Total Traded Value  |             34,138.59
Delivery Volume     |             17,43,202
% Delivery          |                 21.16


             Bid Price Offer Quantity Offer Price
Bid Quantity                                     
2,981           302.80            472      302.90
200             302.70          1,739      302.95
391             302.65         13,936      303.00
4,368           302.60          3,471      303.05
5,469           302.55            767      303.10
```
- Scan live quotes of securities
```python
nseta scan -S HDFC,ABB
              Updated Symbol     Close       LTP
 30-DEC-2020 16:00:00   HDFC  2,518.95  2,521.70
 30-DEC-2020 16:00:00    ABB  1,203.05  1,205.30
```
- Scan live quotes of a bunch of securities listed in a resource file(stocks.txt under scanner folder)
```python
nseta scan -l
 All Stocks LTP and Signals:
              Updated      Symbol      Close        LTP  % Delivery  Buy - Sell TotalTradedVolume
 13-JAN-2021 15:30:02        ATUL   6,597.90   6,640.95       86.12     -7069.0          1,27,120
 13-JAN-2021 15:30:02   TEAMLEASE   2,774.05   2,822.00       74.94     -3491.0            39,713
 13-JAN-2021 15:30:02     MPHASIS   1,657.35   1,655.00       72.53     -8819.0          5,04,007
 13-JAN-2021 15:30:02   KOTAKBANK   1,903.45   1,880.00       71.40    -14945.0         55,82,559
 13-JAN-2021 15:30:02         FCL      64.50      62.10       71.16   -168378.0          5,86,217
 13-JAN-2021 15:30:02         FSL      99.05      97.65       67.68   -391015.0         23,45,958
 13-JAN-2021 15:30:02         MCX   1,686.50   1,696.00       66.67    -20385.0          1,90,965
 13-JAN-2021 15:30:02       GLAND   2,248.35   2,204.00       60.96     -8184.0          3,41,991
 13-JAN-2021 15:30:02         ABB   1,269.30   1,276.00       60.61     -3306.0          1,59,568
 13-JAN-2021 15:30:02      INDOCO     318.00     310.00       59.76     -6597.0          1,68,736
 13-JAN-2021 15:30:02    EVEREADY     207.10     204.45       59.62   -152053.0          2,70,159
 13-JAN-2021 15:30:02        HDFC   2,747.55   2,672.00       58.71    -19654.0         55,80,886
 13-JAN-2021 15:30:02    SYMPHONY   1,065.15   1,051.00       55.44     -8900.0            49,398
 13-JAN-2021 15:30:02  CASTROLIND     128.05     129.50       55.26   -388442.0         18,29,577
 13-JAN-2021 15:30:02         TCS   3,174.85   3,158.00       55.03     -8764.0         35,72,287
 13-JAN-2021 15:30:02  WOCKPHARMA     509.45     495.30       54.25    -47592.0          6,20,728
 13-JAN-2021 15:30:02   POWERGRID     203.70     205.00       54.17   -190444.0       1,33,82,757
 13-JAN-2021 15:30:02          LT   1,349.80   1,350.00       53.85   -282955.0         43,89,199
 13-JAN-2021 15:30:02        IDBI      32.15      31.40       53.66  -2591283.0       1,39,30,466
 13-JAN-2021 15:30:02  KAJARIACER     741.40     747.00       53.62    -14266.0          2,64,187
 13-JAN-2021 15:30:02    CROMPTON     403.30     397.25       53.12    -10720.0         11,89,119
 13-JAN-2021 15:30:02      RADICO     507.05     507.00       52.91    -86642.0          4,33,139
 13-JAN-2021 15:30:02  CHAMBLFERT     232.60     231.35       52.80   -105721.0          6,29,960
 13-JAN-2021 15:30:02   GODREJIND     434.55     434.00       52.45   -101223.0         17,55,353
 13-JAN-2021 15:30:02    GOODYEAR     959.15     955.95       51.76      2937.0            23,649
 13-JAN-2021 15:30:02      BIOCON     471.75     462.65       49.93   -219459.0         34,30,009
 13-JAN-2021 15:30:02      CONCOR     445.60     439.00       49.91   -185639.0         27,45,347
 13-JAN-2021 15:30:02  TORNTPHARM   2,833.50   2,767.95       48.54     -6328.0          3,70,961
 13-JAN-2021 15:30:02   REPCOHOME     270.70     265.00       48.17   -104416.0          6,37,267
 13-JAN-2021 15:30:02    HDFCBANK   1,481.00   1,473.65       48.13   -325155.0         84,65,607
 13-JAN-2021 15:30:02  ASIANPAINT   2,720.55   2,700.00       47.40     -7592.0         28,61,619
 13-JAN-2021 15:30:02      ARVIND      55.85      55.35       47.32   -335123.0         26,59,457
 13-JAN-2021 15:30:02     PRAJIND     130.10     125.55       47.28   -331887.0         16,32,592
 13-JAN-2021 15:30:02       SPARC     195.65     193.25       46.85   -256047.0          5,79,851
 13-JAN-2021 15:30:02    GODREJCP     762.20     770.50       45.95    -58223.0         1,756,953
 13-JAN-2021 15:30:02   BOMDYEING      82.25      80.10       45.72   -674830.0         25,32,984
 13-JAN-2021 15:30:02        INFY   1,371.75   1,388.65       45.01   -145870.0       1,44,41,047
 13-JAN-2021 15:30:02  TATACONSUM     624.30     619.95       44.29   -201096.0         36,59,235
 13-JAN-2021 15:30:02  BANDHANBNK     391.45     375.65       43.43   -664910.0       2,17,29,060
 13-JAN-2021 15:30:02  TORNTPOWER     337.45     330.50       43.35    -77974.0         13,58,268
 13-JAN-2021 15:30:02      FORTIS     171.80     166.90       43.32   -336844.0         50,97,715
 13-JAN-2021 15:30:02       TECHM   1,064.20   1,065.40       43.01    -54750.0         46,70,556
 13-JAN-2021 15:30:02  HINDUNILVR   2,375.90   2,371.00       42.95    -65291.0         17,02,421
 13-JAN-2021 15:30:02       TITAN   1,527.10   1,508.00       42.56      4940.0         35,26,352
 13-JAN-2021 15:30:02        MFSL     719.90     715.00       41.65      2322.0          9,73,158
 13-JAN-2021 15:30:02     HCLTECH   1,062.10   1,057.00       41.36    -85387.0         66,89,747
 13-JAN-2021 15:30:02         IGL     567.20     565.95       41.27    -41122.0         17,86,278
 13-JAN-2021 15:30:02     DCBBANK     121.80     120.55       40.73   -222881.0         12,38,863
 13-JAN-2021 15:30:02    HINDALCO     264.35     261.65       40.61   -222962.0       1,32,99,767
 13-JAN-2021 15:30:02  PIDILITIND   1,800.10   1,794.90       39.60      6666.0          5,29,910
 13-JAN-2021 15:30:02    RELIANCE   1,957.05   1,936.00       39.40   -807328.0       1,22,79,508
 13-JAN-2021 15:30:02   ICICIBANK     548.00     556.00       39.34   -966897.0       2,19,19,320
 13-JAN-2021 15:30:02     SBILIFE     925.00     928.40       39.22   -114140.0         19,96,264
 13-JAN-2021 15:30:02   BRITANNIA   3,631.65   3,622.00       39.20    -58004.0          7,98,011
 13-JAN-2021 15:30:02  CUMMINSIND     623.20     612.95       39.00    -32783.0         15,18,652
 13-JAN-2021 15:30:02  INDUSTOWER     261.35     259.00       38.89   -172048.0         4,287,757
 13-JAN-2021 15:30:02       IRCTC   1,480.45   1,461.00       38.61   -171114.0         11,80,044
 13-JAN-2021 15:30:02  CENTURYTEX     430.10     425.00       38.33   -101445.0          6,53,028
 13-JAN-2021 15:30:02      ASHOKA      95.75      94.25       37.28   -316686.0         13,75,611
 13-JAN-2021 15:30:02  MUTHOOTFIN   1,276.65   1,237.95       36.27    -68347.0         39,80,304
 13-JAN-2021 15:30:02    INDIACEM     168.50     170.20       35.09   -404328.0         37,81,430
 13-JAN-2021 15:30:02      VOLTAS     903.20     894.90       34.96      6551.0         12,45,754
 13-JAN-2021 15:30:02       DABUR     541.00     536.60       34.91   -188787.0         29,32,616
 13-JAN-2021 15:30:02         ITC     206.45     211.20       34.43  -1712366.0       6,39,04,353
 13-JAN-2021 15:30:02     HAVELLS   1,018.80   1,011.70       34.32    -25099.0         22,10,914
 13-JAN-2021 15:30:02    AXISBANK     675.70     686.05       33.52    -27742.0       1,56,45,019
 13-JAN-2021 15:30:02  GODREJPROP   1,474.00   1,430.00       33.44    -31071.0          8,52,039
 13-JAN-2021 15:30:02   AMBUJACEM     268.10     264.50       32.88   -145332.0         52,65,065
 13-JAN-2021 15:30:02        SAIL      75.90      74.10       32.70  -3393571.0       3,30,35,958
 13-JAN-2021 15:30:02        NMDC     127.45     125.40       32.04   -488350.0         84,38,234
 13-JAN-2021 15:30:02  ULTRACEMCO   5,639.00   5,645.50       31.95      4382.0          4,23,130
 13-JAN-2021 15:30:02  BHARTIARTL     565.75     576.30       31.54  -1329795.0       8,36,53,265
 13-JAN-2021 15:30:02     DRREDDY   5,353.85   5,280.00       31.30    -12741.0          6,58,940
 13-JAN-2021 15:30:02    MINDTREE   1,750.85   1,742.80       31.04    -11366.0          4,98,998
 13-JAN-2021 15:30:02         UPL     501.50     491.00       30.97   -266679.0         46,93,036
 13-JAN-2021 15:30:02         HAL     901.60     919.95       30.87   -118629.0          8,05,801
 13-JAN-2021 15:30:02    ASHOKLEY     121.60     121.50       30.49  -1659575.0       5,13,19,295
 13-JAN-2021 15:30:02  AUROPHARMA     958.25     940.55       30.42    -98793.0         29,98,155
 13-JAN-2021 15:30:02        BEML     966.25     963.95       30.27   -102130.0          4,07,744
 13-JAN-2021 15:30:02   HINDPETRO     224.90     226.80       30.07   -766753.0       1,15,49,624
 13-JAN-2021 15:30:02    CADILAHC     490.35     487.00       29.93   -353619.0         27,27,242
 13-JAN-2021 15:30:02    GLENMARK     517.25     512.90       29.75   -274058.0         19,63,497
 13-JAN-2021 15:30:02       WIPRO     457.70     459.00       29.71   -339092.0       2,91,81,001
 13-JAN-2021 15:30:02        VEDL     181.10     180.55       29.57  -1185879.0       1,67,79,793
 13-JAN-2021 15:30:02        NTPC     100.15     102.50       29.43  -1087932.0       4,92,30,289
 13-JAN-2021 15:30:02         LTI   4,285.15   4,430.00       29.04     -1554.0          3,76,219
 13-JAN-2021 15:30:02  FEDERALBNK      76.20      74.75       28.77  -2313685.0       4,17,59,426
 13-JAN-2021 15:30:02         PFC     121.45     121.05       28.24   -737947.0         55,61,616
 13-JAN-2021 15:30:02  MCDOWELL-N     644.00     639.35       28.12    -58907.0         24,38,564
 13-JAN-2021 15:30:02         ACC   1,795.10   1,788.95       28.09     -7598.0          9,22,665
 13-JAN-2021 15:30:02   NESTLEIND  17,999.10  18,015.00       27.82     -2651.0          1,09,381
 13-JAN-2021 15:30:02    EXIDEIND     204.30     201.50       27.80   -315475.0         91,66,650
 13-JAN-2021 15:30:02        GAIL     141.40     141.45       26.92  -1174576.0       2,71,65,471
 13-JAN-2021 15:30:02         BEL     134.45     133.70       26.71   -788405.0       1,28,15,348
 13-JAN-2021 15:30:02  IDFCFIRSTB      47.15      46.05       26.60  -3366528.0       5,65,33,589
 13-JAN-2021 15:30:02  HEROMOTOCO   3,248.25   3,256.00       26.49    -33410.0         14,23,881
 13-JAN-2021 15:30:02     ESCORTS   1,377.45   1,360.00       26.48   -109294.0         14,03,891
 13-JAN-2021 15:30:02      INDIGO   1,680.00   1,640.00       26.00      7530.0         13,12,936
 13-JAN-2021 15:30:02  BAJFINANCE   5,042.20   4,894.00       25.74    -72782.0         32,68,429
 13-JAN-2021 15:30:02         M&M     779.85     824.00       25.24     63029.0       1,96,05,430
 13-JAN-2021 15:30:02        BPCL     402.55     411.50       25.16   -983991.0       2,11,75,970
 13-JAN-2021 15:30:02   BANKINDIA      53.90      54.05       25.13  -2563022.0       2,25,70,545
 13-JAN-2021 15:30:02   LICHSGFIN     438.80     437.25       24.86   -203596.0       1,34,33,112
 13-JAN-2021 15:30:02  APOLLOTYRE     192.85     191.85       24.78   -314888.0         84,89,771
 13-JAN-2021 15:30:02   SUNPHARMA     609.65     602.45       24.78   -214719.0         61,85,389
 13-JAN-2021 15:30:02        ONGC     103.45     105.50       24.49  -2231590.0       4,23,83,660
 13-JAN-2021 15:30:02         PNB      36.50      36.50       23.29  -9043640.0      22,73,96,221
 13-JAN-2021 15:30:02       LUPIN   1,060.30   1,065.90       22.66   -112428.0         28,03,745
 13-JAN-2021 15:30:02  BERGEPAINT     803.15     798.00       22.52     11109.0          7,15,677
 13-JAN-2021 15:30:02        SBIN     292.50     305.95       22.45   -282891.0       7,80,34,626
 13-JAN-2021 15:30:02     SIEMENS   1,642.55   1,630.50       22.27     -2223.0          4,24,845
 13-JAN-2021 15:30:02         MGL   1,126.65   1,113.90       21.92    -43560.0          4,38,535
 13-JAN-2021 15:30:02  SRTRANSFIN   1,262.60   1,215.85       21.49   -127729.0         53,06,679
 13-JAN-2021 15:30:02       CIPLA     843.15     840.90       21.34    -16450.0         35,94,632
 13-JAN-2021 15:30:02         MRF  85,746.90  85,422.45       21.23      -906.0            57,613
 13-JAN-2021 15:30:02        BHEL      39.35      40.75       21.18  -7405715.0      15,44,12,403
 13-JAN-2021 15:30:02        MOIL     146.05     153.00       20.67   -234848.0         42,53,184
 13-JAN-2021 15:30:02      MARUTI   8,188.05   8,132.00       20.50    -25620.0          8,77,169
 13-JAN-2021 15:30:02    GMRINFRA      27.10      27.00       20.10  -2305909.0       1,61,78,790
 13-JAN-2021 15:30:02         SRF   5,929.40   6,020.00       19.26     32332.0          1,60,848
 13-JAN-2021 15:30:02     RBLBANK     257.50     254.00       18.81   -766251.0       1,75,60,356
 13-JAN-2021 15:30:02         IOC      97.95     101.05       17.81  -1193693.0       5,59,32,924
 13-JAN-2021 15:30:02   BATAINDIA   1,624.25   1,636.00       17.44    -33289.0         10,16,486
 13-JAN-2021 15:30:02    TVSMOTOR     518.75     510.60       17.44   -120370.0         29,63,845
 13-JAN-2021 15:30:02  BANKBARODA      70.75      75.35       17.29    127363.0      12,75,12,244
 13-JAN-2021 15:30:02   TATAELXSI   2,087.60   2,398.95       17.28    424055.0         53,67,299
 13-JAN-2021 15:30:02   EICHERMOT   2,881.65   2,877.00       17.03     -4381.0         18,77,984
 13-JAN-2021 15:30:02        ZEEL     226.15     228.45       16.70   -828424.0       1,34,41,022
 13-JAN-2021 15:30:02  INDUSINDBK     927.65     942.15       16.63   -396281.0         94,72,201
 13-JAN-2021 15:30:02         PEL   1,564.50   1,565.10       15.66    -94828.0         39,40,511
 13-JAN-2021 15:30:02         PVR   1,452.45   1,457.00       15.49    -78072.0         20,50,096
 13-JAN-2021 15:30:02   TATASTEEL     694.90     709.90       15.36   -385224.0       1,93,51,481
 13-JAN-2021 15:30:02    JSWSTEEL     399.55     401.80       14.88   -121780.0         68,83,661
 13-JAN-2021 15:30:02    TATACHEM     523.00     544.90       14.44   -125633.0       1,66,60,559
 13-JAN-2021 15:30:02  BHARATFORG     621.40     626.50       13.40    -91469.0       1,51,11,888
 13-JAN-2021 15:30:02  TATAMOTORS     237.80     242.85       12.47  -1893323.0      16,46,24,772
 13-JAN-2021 15:30:02         DLF     267.55     279.10       10.27   -148217.0       5,31,91,510
 13-JAN-2021 15:30:02    ADANIENT     525.40     533.00        9.95    -13314.0         49,48,295
 13-JAN-2021 15:30:02  JINDALSTEL     294.40     298.65        9.85   -271520.0       1,05,45,511
No signals to show here.
Live scanning finished.

```

## Signals and Scanners

### Scanners
- When RSI(14) > 75
- When RSI(14) < 25
- When LTP > SMA(10)
- When LTP < SMA(10)
- When LTP > EMA(9)
- When LTP < SMA(9)
- When LTP < lower BBand
- When LTP > higher BBand

- Scanning options
```python
nseta scan --help
Usage:  [OPTIONS]

  Scan live and intraday for prices and signals.

Options:
  -S, --stocks TEXT               Comma separated security codes(Optional).
                                  When skipped, all stocks configured in
                                  stocks.txt will be scanned.)
  -l, --live                      Scans (every min. when in background) the
                                  live-quote and lists those that meet the
                                  signal criteria. Works best with
                                  --background.
  -i, --intraday                  Scans (every 10 sec when in background) the
                                  intraday price history and lists those that
                                  meet the signal criteria
  -s, --swing                     Scans (every 10 sec when in background) the
                                  past 90 days price history and lists those
                                  that meet the signal criteria
  -v, --volume                    Scans (every 10 sec when in background) the
                                  past 7 days price history and lists those
                                  that meet the signal criteria
  -t, --indicator [rsi|smac|emac|macd|bbands|all]
                                  rsi, smac, emac, macd, bbands, all. Choose
                                  one.
  -o, --orderby [intraday|momentum]
                                  intraday, momentum. Choose one.
  -c, --clear                     Clears the cached data for the given
                                  options.
  -r, --background                Keep running the process in the background
                                  (Optional)
  --help                          Show this message and exit.
```

For example:
- Scanning intraday based on Bollinger bands
```python
nseta scan -i -t bbands
INFO - tiscanner.py(scan_intraday - 123)
This run of intraday scan took 10.7 sec

INFO - livecli.py(scan_intraday_results - 150)
Saved to: Scan_Results.csv

Saved to: Scan_Results.csv
INFO - livecli.py(scan_intraday_results - 155)

We recommend taking the following BUY/SELL positions immediately for day trading. Intraday Signals:
               Date      Symbol     BBands-U     BBands-L      LTP                   Signal
2021-01-04 14:30:04      ASHOKA    93.434693    93.170307    93.40  (SELL) [LTP ~ BBands-U]
2021-01-04 14:30:00   BANKINDIA    50.440129    50.294871    50.40  (SELL) [LTP ~ BBands-U]
2021-01-04 14:30:01        BHEL    40.154087    39.935913    40.10  (SELL) [LTP ~ BBands-U]
2021-01-04 14:30:00  JINDALSTEL   284.777021   282.052979   284.80  (SELL) [LTP > BBands-U]
2021-01-04 14:30:00        NTPC    99.039443    98.860557    99.00  (SELL) [LTP ~ BBands-U]
2021-01-04 14:30:00        SAIL    77.886024    77.103976    77.85  (SELL) [LTP ~ BBands-U]
2021-01-04 14:30:00  ULTRACEMCO  5313.098214  5301.341786  5313.15  (SELL) [LTP > BBands-U]
```
- Scanning live-quotes during trading session
```python
nseta scan -l
All Stocks LTP and Signals:
              Updated      Symbol      Close        LTP  % Delivery  Buy - Sell TotalTradedVolume
 13-JAN-2021 15:30:02        ATUL   6,597.90   6,640.95       86.12     -7069.0          1,27,120
 13-JAN-2021 15:30:02   TEAMLEASE   2,774.05   2,822.00       74.94     -3491.0            39,713
 13-JAN-2021 15:30:02     MPHASIS   1,657.35   1,655.00       72.53     -8819.0          5,04,007
 13-JAN-2021 15:30:02   KOTAKBANK   1,903.45   1,880.00       71.40    -14945.0         55,82,559
 13-JAN-2021 15:30:02         FCL      64.50      62.10       71.16   -168378.0          5,86,217
 13-JAN-2021 15:30:02         FSL      99.05      97.65       67.68   -391015.0         23,45,958
 13-JAN-2021 15:30:02         MCX   1,686.50   1,696.00       66.67    -20385.0          1,90,965
 13-JAN-2021 15:30:02       GLAND   2,248.35   2,204.00       60.96     -8184.0          3,41,991
 13-JAN-2021 15:30:02         ABB   1,269.30   1,276.00       60.61     -3306.0          1,59,568
 13-JAN-2021 15:30:02      INDOCO     318.00     310.00       59.76     -6597.0          1,68,736
 13-JAN-2021 15:30:02    EVEREADY     207.10     204.45       59.62   -152053.0          2,70,159
 13-JAN-2021 15:30:02        HDFC   2,747.55   2,672.00       58.71    -19654.0         55,80,886
 13-JAN-2021 15:30:02    SYMPHONY   1,065.15   1,051.00       55.44     -8900.0            49,398
 13-JAN-2021 15:30:02  CASTROLIND     128.05     129.50       55.26   -388442.0         18,29,577
 13-JAN-2021 15:30:02         TCS   3,174.85   3,158.00       55.03     -8764.0         35,72,287
 13-JAN-2021 15:30:02  WOCKPHARMA     509.45     495.30       54.25    -47592.0          6,20,728
 13-JAN-2021 15:30:02   POWERGRID     203.70     205.00       54.17   -190444.0       1,33,82,757
 13-JAN-2021 15:30:02          LT   1,349.80   1,350.00       53.85   -282955.0         43,89,199
 13-JAN-2021 15:30:02        IDBI      32.15      31.40       53.66  -2591283.0       1,39,30,466
 13-JAN-2021 15:30:02  KAJARIACER     741.40     747.00       53.62    -14266.0          2,64,187
 13-JAN-2021 15:30:02    CROMPTON     403.30     397.25       53.12    -10720.0         11,89,119
 13-JAN-2021 15:30:02      RADICO     507.05     507.00       52.91    -86642.0          4,33,139
 13-JAN-2021 15:30:02  CHAMBLFERT     232.60     231.35       52.80   -105721.0          6,29,960
 13-JAN-2021 15:30:02   GODREJIND     434.55     434.00       52.45   -101223.0         17,55,353
 13-JAN-2021 15:30:02    GOODYEAR     959.15     955.95       51.76      2937.0            23,649
```
- Scanning for swing trading
```python
nseta scan -s
This run of swing scan took 36.5 sec

We recommend taking the following BUY/SELL positions for swing trading. Swing Signals:
     Symbol       Date    RSI   EMA(9)  macd(12)  macdsignal(9)  macdhist(26)  BBands-U  BBands-L      LTP Signal           Remarks Confidence
   ADANIENT 2021-01-13  78.71   512.08     24.53          19.08          5.46    540.15    433.29   536.05   SELL       [RSI >= 75]       20 %
   ASHOKLEY 2021-01-13  85.71   112.24      6.14           2.63          3.51    121.06     83.93   121.65   SELL       [RSI >= 75]       30 %
     ARVIND 2021-01-13  73.24    52.04      1.92           1.41          0.51     55.43     42.52    55.45   SELL  [LTP > BBands-U]       30 %
 BANKBARODA 2021-01-13  77.69    67.68      1.13           0.50          0.63     71.74     56.65    75.25   SELL       [RSI >= 75]       30 %
 BHARATFORG 2021-01-13  75.41   591.40     14.56           1.63         12.94    627.04    485.89   628.25   SELL       [RSI >= 75]       30 %
 BHARTIARTL 2021-01-13  77.49   545.25     13.74           9.90          3.85    565.51    481.84   578.25   SELL       [RSI >= 75]       30 %
        DLF 2021-01-13  80.37   253.49     13.07          11.52          1.56    267.99    209.78   280.45   SELL       [RSI >= 75]       30 %
  EICHERMOT 2021-01-13  77.02  2733.29    106.27          29.89         76.38   2872.25   2283.86  2868.65   SELL       [RSI >= 75]       20 %
       GAIL 2021-01-13  79.57   134.22      4.72           2.47          2.25    141.37    112.35   141.25   SELL       [RSI >= 75]       20 %
   GMRINFRA 2021-01-13  53.35    27.00      0.18          -0.11          0.30     28.37     24.97    27.05    BUY    [LTP > EMA(9)]       60 %
    HAVELLS 2021-01-13  81.00   978.66     46.03          39.09          6.95   1022.68    842.39  1012.45   SELL       [RSI >= 75]       40 %
    HCLTECH 2021-01-13  77.34  1009.59     53.99          42.17         11.82   1065.45    840.21  1055.95   SELL       [RSI >= 75]       20 %
        IGL 2021-01-13  77.63   543.35     25.17          13.90         11.27    572.96    451.60   565.60   SELL       [RSI >= 75]       20 %
       INFY 2021-01-13  77.84  1324.04     60.16          52.29          7.86   1388.67   1134.20  1387.15   SELL       [RSI >= 75]       20 %
        LTI 2021-01-13  77.46  4087.24    306.71         235.82         70.89   4410.78   3122.27  4402.45   SELL       [RSI >= 75]       20 %
        M&M 2021-01-13  75.18   770.40     15.71          -2.31         18.02    802.97    669.92   828.35   SELL       [RSI >= 75]       30 %
     RADICO 2021-01-13  75.98   490.61     12.22           1.33         10.90    512.44    422.56   507.55   SELL       [RSI >= 75]       20 %
       SBIN 2021-01-13  76.97   288.21      8.71           5.65          3.06    300.68    253.14   306.80   SELL       [RSI >= 75]       30 %
        SRF 2021-01-13  76.59  5819.21    184.53         143.22         41.31   6018.07   5226.76  6008.95   SELL       [RSI >= 75]       20 %
   TATACHEM 2021-01-13  81.15   506.85      1.60          -0.88          2.49    525.12    454.61   541.95   SELL       [RSI >= 75]       30 %
  TATAELXSI 2021-01-13  85.08  2065.71    174.65         113.52         61.12   2258.77   1477.74  2371.85   SELL       [RSI >= 75]       30 %
 TATAMOTORS 2021-01-13  87.18   212.61     12.80           3.92          8.88    231.93    150.03   242.60   SELL       [RSI >= 75]       30 %
      TECHM 2021-01-13  75.67  1032.22     44.72          29.42         15.30   1081.25    882.72  1069.65   SELL       [RSI >= 75]       40 %
      WIPRO 2021-01-13  88.42   427.88     26.79          17.74          9.05    457.49    332.60   459.00   SELL       [RSI >= 75]       30 %
Swing scanning finished.

```

- Scanning based on volumes
```python
$ nseta scan -v -c
Done.                                                                                                                            
This run of volume scan took 38.4 sec

As of 2021-01-28 14:16:39.955641+05:30, Volume Signals:

        Symbol      LTP     VWAP   %Chng  Vol_TDY  Vol_7D    S1-R3         Remarks Del_TDY
       HAVELLS  1176.90  1114.08    5.74    550.0   125.0  1153.70       LTP >= R3   16.62
     TEAMLEASE  2813.10  2783.31    1.41    414.0   153.0  2826.67  PP <= LTP < R1   39.66
         ABFRL   152.45   164.95   -5.95    209.0   161.0   148.48       LTP >= S3   50.51
         IRCTC  1460.00  1433.52    1.51    205.0   269.0  1456.12       LTP >= R2   29.85
        RADICO   496.75   496.43   -0.31    171.0    75.0   508.45  PP <= LTP < R1   28.40
       DCBBANK   103.50   110.92   -5.00    170.0   335.0    99.38       LTP >= S3   69.16
        ARVIND    53.90    49.46    8.56    134.0   149.0    53.32       LTP >= R3   33.39
    MCDOWELL-N   597.80   642.02   -7.30    108.0   200.0   613.00        LTP < S3   30.90
      AXISBANK   660.90   641.63    4.56    102.0   239.0   654.80       LTP >= R1   31.76
       PRAJIND   116.85   113.56    3.68     77.0    36.0   114.90       LTP >= R1   36.69
    BANKBARODA    66.15    73.84  -10.67     69.0   166.0    68.70        LTP < S3   26.11
    MADRASFERT    29.30    28.66    3.17     66.0   -15.0    29.88  PP <= LTP < R1   39.44
           PNB    32.55    33.70   -2.40     53.0    14.0    32.35       LTP >= S2   27.43
   ** GLENMARK   480.60   490.14   -1.09     45.0    54.0   480.65              S1   23.19
    FEDERALBNK    71.45    70.58    2.36     39.0    38.0    71.33       LTP >= R1   35.15
     ** MARUTI  7655.00  7972.54   -2.74     39.0    89.0  7657.63              S2   19.78
      HDFCBANK  1354.50  1437.02   -3.91     36.0    93.0  1320.78       LTP >= S3   55.02
    CENTURYTEX   418.50   399.95    3.87     35.0   102.0   411.48       LTP >= R1   39.89
     REPCOHOME   242.35   245.96   -2.06     32.0    -6.0   238.95       LTP >= S2   65.10
        VOLTAS   934.00   926.47    2.24     26.0     0.0   936.03  PP <= LTP < R1   17.57
          SAIL    56.90    58.24   -0.70     24.0    58.0    56.03  PP > LTP >= S1   53.29
      ADANIENT   514.85   514.84    0.40     21.0    -8.0   520.55  PP <= LTP < R1   13.30
    HEROMOTOCO  3411.95  3415.36    1.59     21.0     9.0  3451.72  PP <= LTP < R1   19.69
    HINDUNILVR  2314.00  2376.31   -3.23     19.0    78.0  2293.77       LTP >= S2   42.49
        ** PFC   108.95   112.24   -2.33     18.0    30.0   109.02              S2   30.12
          NTPC    91.15    91.79   -0.16     17.0    35.0    90.37  PP > LTP >= S1   39.90
           SRF  5401.00  5388.80    0.73     15.0    -6.0  5439.45  PP <= LTP < R1   38.47
           ABB  1360.60  1376.47   -2.03     15.0    -8.0  1356.57  PP > LTP >= S1   57.69
           PEL  1375.35  1458.75   -3.22     14.0    11.0  1357.72       LTP >= S2   29.32
    BAJAJFINSV  8980.00  9160.23   -1.60     14.0   -19.0  8908.13       LTP >= S2   23.79
    BANDHANBNK   311.70   306.90    2.63     12.0   -23.0   312.03  PP <= LTP < R1   38.21
          BPCL   384.35   384.57    0.99     12.0    21.0   387.32  PP <= LTP < R1   41.09
         DABUR   527.60   530.46    0.02      9.0    -1.0   522.93  PP > LTP >= S1   35.21
     JKLAKSHMI   315.30   322.11   -1.47      7.0   -25.0   311.40       LTP >= S2   55.56
  ** VISAKAIND   436.50   434.30   -0.16      6.0   -50.0   436.48              PP   56.08
    TATACONSUM   563.90   578.75   -1.53      5.0     2.0   563.28  PP > LTP >= S1   45.95
    BAJFINANCE  4839.10  4857.86   -0.12      3.0   -18.0  4788.80  PP > LTP >= S1   11.44
    IDFCFIRSTB    47.70    48.01   -0.21      3.0   -25.0    46.73  PP > LTP >= S1   20.66
 ** OBEROIRLTY   526.35   544.23   -1.93      3.0    16.0   526.57              S1   69.43
          IDBI    28.35    27.46    2.35      0.0     1.0    28.43  PP <= LTP < R1   37.41
 ** GODREJPROP  1243.35  1299.75   -4.15     -4.0    -8.0  1243.72              S2   24.19
    CHAMBLFERT   238.90   236.28    3.38     -7.0    11.0   239.13  PP <= LTP < R1   40.73
          BHEL    35.95    35.82    0.70    -11.0   -13.0    36.13  PP <= LTP < R1   22.06
  ** SUNPHARMA   560.75   572.43   -1.59    -11.0    42.0   560.40              S1   22.73
          SBIN   280.05   278.67    1.60    -12.0    11.0   282.77  PP <= LTP < R1   30.15
           MCX  1670.60  1642.18    1.15    -14.0    21.0  1680.13  PP <= LTP < R1   59.88
        ** TCS  3222.70  3265.48   -1.18    -24.0   -14.0  3223.22              S1   54.12
        BIOCON   382.15   378.58    1.22    -27.0   -12.0   386.82  PP <= LTP < R1   28.90
    CUMMINSIND   630.20   622.05    0.92    -27.0    62.0   632.75  PP <= LTP < R1   24.05
           IOC    92.65    91.25    1.37    -32.0    -7.0    93.38  PP <= LTP < R1   34.78
  ** BOMDYEING    74.20    74.15    0.34    -32.0   -52.0    74.15              PP   32.03
   ** GODREJCP   775.50   776.00    0.20    -34.0   -51.0   775.25              PP   37.32
      JSWSTEEL   379.70   377.59    0.92    -35.0   -28.0   381.65  PP <= LTP < R1   27.43
       ** ONGC    90.15    90.09    0.50    -36.0    -5.0    90.12              PP   24.72
    ** RAYMOND   325.30   325.19   -0.63    -36.0     0.0   325.52              PP   44.15
      CROMPTON   423.65   417.12   -1.03    -37.0   -22.0   444.40  PP <= LTP < R1   66.16
    INDUSTOWER   241.40   241.10    1.28    -38.0    25.0   245.23  PP <= LTP < R1   36.59
     HINDPETRO   220.60   216.74    1.82    -42.0   -19.0   220.37       LTP >= R1   39.98
      EVEREADY   192.90   189.48   -0.85    -43.0   -23.0   199.80  PP <= LTP < R1   68.86
      ** CIPLA   840.95   843.08   -0.18    -52.0   -22.0   841.38              PP   25.68
       ** INFY  1282.30  1308.99   -1.44    -57.0   -45.0  1281.55              S1   50.59
    TRITURBINE    85.40    84.49    1.36    -61.0   -84.0    85.83  PP <= LTP < R1   57.39
      GRAPHITE   314.80   312.42   -1.04    -64.0   -35.0   326.40  PP <= LTP < R1   34.02
      ** SPARC   181.60   185.24   -1.33    -65.0   -47.0   181.58              S1   40.26
    CASTROLIND   125.30   124.98    1.21    -68.0   -54.0   126.65  PP <= LTP < R1   48.23
Volume scanning finished.

```

### Signals
- SELL : When RSI(14) > 75
- BUY : When RSI(14) < 25
- BUY : When LTP > SMA(10) and SMA(10) is upstrending
- SELL : When LTP < SMA(10) and SMA(10) is downtrending
- BUY : When LTP > EMA(9) and EMA(9) is upstrending
- SELL : When LTP < EMA(9) and EMA(9) is downtrending
- BUY : When LTP < lower BBand
- SELL : When LTP > higher BBand

- Scanning and measuring PnL for a specific trading strategy
```python
nseta scan-trading-strategy -s 2020-06-01 -e 2021-01-17 --strategy macd
     Symbol Strategy        PnL
        ABB     MACD   20872.60
      ABFRL     MACD   30435.55
        ACC     MACD   12013.20
   ADANIENT     MACD   80550.45
 APOLLOTYRE     MACD   17806.75
     ASHOKA     MACD   83436.70
   ASHOKLEY     MACD   43338.70
  AMBUJACEM     MACD   25194.55
     ARVIND     MACD   31915.25
 ASIANPAINT     MACD   11657.95
       ATUL     MACD    4857.30
 AUROPHARMA     MACD    2989.20
   AXISBANK     MACD   21038.30
 BAJFINANCE     MACD   34446.10
 BANDHANBNK     MACD   -4542.00
  BANKINDIA     MACD   32309.60
 BANKBARODA     MACD   19733.65
  BATAINDIA     MACD   12822.60
        BEL     MACD   21450.45
       BEML     MACD   32654.95
 BERGEPAINT     MACD   23705.10
 BHARATFORG     MACD   31721.15
 BHARTIARTL     MACD    9626.95
       BHEL     MACD   31404.60
     BIOCON     MACD    4582.10
  BOMDYEING     MACD   -8950.80
       BPCL     MACD  -12436.60
  BRITANNIA     MACD     233.95
   CADILAHC     MACD   24261.40
 CASTROLIND     MACD   20391.75
 CENTURYTEX     MACD    9182.05
 CHAMBLFERT     MACD   12977.00
      CIPLA     MACD    7624.20
     CONCOR     MACD   -2469.55
   CROMPTON     MACD   11714.40
 CUMMINSIND     MACD   28751.55
      DABUR     MACD   -1913.30
    DCBBANK     MACD   37922.05
        DLF     MACD   22538.40
    DRREDDY     MACD   30566.95
  EICHERMOT     MACD   31716.85
    ESCORTS     MACD   10337.75
   EVEREADY     MACD   45995.60
   EXIDEIND     MACD   11972.75
        FCL     MACD   38800.30
 FEDERALBNK     MACD    2213.45
     FORTIS     MACD   19794.90
        FSL     MACD   38322.30
       GAIL     MACD   25255.80
      GLAND     MACD       0.00
   GLENMARK     MACD   -4359.40
   GMRINFRA     MACD   -9999.10
   GODREJCP     MACD   14678.70
  GODREJIND     MACD   21429.80
 GODREJPROP     MACD    1315.25
   GOODYEAR     MACD    5865.00
   GRAPHITE     MACD   60779.80
        HAL     MACD    6131.25
    HAVELLS     MACD    8157.90
    HCLTECH     MACD   29272.50
       HDFC     MACD   11412.25
   HDFCBANK     MACD   25864.10
 HEROMOTOCO     MACD   13396.35
   HINDALCO     MACD   17708.35
 HINDUNILVR     MACD   -4230.35
  HINDPETRO     MACD  -10507.75
  ICICIBANK     MACD   11866.40
       IDBI     MACD     732.05
 IDFCFIRSTB     MACD   17466.45
        IGL     MACD    2397.30
   INDIACEM     MACD   11737.00
     INDIGO     MACD    6517.70
     INDOCO     MACD   32519.45
 INDUSINDBK     MACD   34631.80
   INFRATEL     MACD   11225.50
        IOC     MACD    1309.35
      IRCTC     MACD  -20473.00
        ITC     MACD    5600.20
 JINDALSTEL     MACD   36702.30
  JKLAKSHMI     MACD   11350.60
     JKTYRE     MACD   18180.60
   JSWSTEEL     MACD   52773.25
 KAJARIACER     MACD   15712.40
  KOTAKBANK     MACD   28569.05
       INFY     MACD   29785.70
  LICHSGFIN     MACD   10250.80
         LT     MACD   19256.15
        LTI     MACD   28679.65
      LUPIN     MACD   24670.20
     MARUTI     MACD    6284.70
 MCDOWELL-N     MACD   -8786.80
        MCX     MACD   11295.15
       MFSL     MACD   11407.65
        MGL     MACD   -1508.80
   MINDTREE     MACD   29167.35
       MOIL     MACD    3383.75
    MPHASIS     MACD   26060.00
        MRF     MACD       0.00
 MUTHOOTFIN     MACD   -5394.70
        M&M     MACD   13413.55
  NESTLEIND     MACD   -9398.45
       NMDC     MACD   14495.60
       NTPC     MACD    3423.20
       ONGC     MACD   18047.35
        PEL     MACD  -19022.85
        PFC     MACD   35832.75
 PIDILITIND     MACD    8380.60
        PNB     MACD   31335.15
  POWERGRID     MACD    7184.85
    PRAJIND     MACD   36877.10
     RADICO     MACD  -16972.55
    RBLBANK     MACD    4123.55
   RELIANCE     MACD   -3521.40
  REPCOHOME     MACD   27195.25
       SAIL     MACD   44876.65
    SBILIFE     MACD    1915.70
       SBIN     MACD    4255.70
    SIEMENS     MACD    2711.65
      SPARC     MACD   -9381.10
        SRF     MACD    7573.80
 SRTRANSFIN     MACD   35118.95
  SUNPHARMA     MACD    3568.35
   SYMPHONY     MACD   -5981.95
   TATACHEM     MACD   55305.70
 TATACONSUM     MACD    9566.75
  TATAELXSI     MACD   83517.95
 TATAMOTORS     MACD   92873.20
  TATASTEEL     MACD   48819.75
        TCS     MACD   18190.70
  TEAMLEASE     MACD    -501.45
      TECHM     MACD    2085.85
      TITAN     MACD    1354.80
 TORNTPHARM     MACD   16931.80
 TORNTPOWER     MACD    4451.40
 TRITURBINE     MACD   30637.05
   TVSMOTOR     MACD    2687.80
 ULTRACEMCO     MACD    8666.40
        UPL     MACD   -8312.20
       VEDL     MACD   57579.85
     VOLTAS     MACD    6356.35
      WIPRO     MACD   27728.35
 WOCKPHARMA     MACD  111416.80
       ZEEL     MACD   42323.85
```
- Scanning and measuring PnL for a specific trading strategy intraday
```python
nseta scan-trading-strategy -i --strategy macd

     Symbol Strategy      PnL
        ABB     MACD  -713.85
      ABFRL     MACD  -808.50
        ACC     MACD   -21.35
   ADANIENT     MACD   203.35
 APOLLOTYRE     MACD -1098.20
     ASHOKA     MACD   501.90
   ASHOKLEY     MACD  2411.40
  AMBUJACEM     MACD    85.75
     ARVIND     MACD -1426.60
 ASIANPAINT     MACD  -716.90
       ATUL     MACD    90.20
 AUROPHARMA     MACD  -655.20
   AXISBANK     MACD  -166.75
 BAJFINANCE     MACD    26.30
 BANDHANBNK     MACD  1381.00
  BANKINDIA     MACD -1476.65
 BANKBARODA     MACD -1407.40
  BATAINDIA     MACD  -826.50
        BEL     MACD  -875.35
       BEML     MACD -1997.85
 BERGEPAINT     MACD -1486.90
 BHARATFORG     MACD    -7.20
 BHARTIARTL     MACD  -111.30
       BHEL     MACD -1435.00
     BIOCON     MACD  -892.95
  BOMDYEING     MACD -1220.95
       BPCL     MACD  -685.15
  BRITANNIA     MACD  -858.35
   CADILAHC     MACD -1234.65
 CASTROLIND     MACD  -423.20
 CENTURYTEX     MACD   -80.20
 CHAMBLFERT     MACD -1418.75
      CIPLA     MACD -1160.50
     CONCOR     MACD  -381.05
   CROMPTON     MACD   283.45
 CUMMINSIND     MACD  -537.10
      DABUR     MACD   388.15
    DCBBANK     MACD -2050.10
        DLF     MACD   273.90
    DRREDDY     MACD  -232.75
  EICHERMOT     MACD   396.50
    ESCORTS     MACD  -901.35
   EVEREADY     MACD -2653.60
   EXIDEIND     MACD  1448.85
        FCL     MACD -1885.20
 FEDERALBNK     MACD -1352.30
     FORTIS     MACD -1972.85
        FSL     MACD  -965.40
       GAIL     MACD  -950.95
      GLAND     MACD  2852.60
   GLENMARK     MACD  -109.85
   GMRINFRA     MACD -1728.45
   GODREJCP     MACD  -802.90
  GODREJIND     MACD -2218.75
 GODREJPROP     MACD -1124.50
   GOODYEAR     MACD -1827.70
   GRAPHITE     MACD  -823.45
        HAL     MACD   685.75
    HAVELLS     MACD -2386.80
    HCLTECH     MACD -2345.20
       HDFC     MACD    10.30
   HDFCBANK     MACD   312.85
 HEROMOTOCO     MACD   681.75
   HINDALCO     MACD -1190.10
 HINDUNILVR     MACD  -330.05
  HINDPETRO     MACD  -470.05
  ICICIBANK     MACD -1072.55
       IDBI     MACD  -733.15
 IDFCFIRSTB     MACD  3636.25
        IGL     MACD -2109.05
   INDIACEM     MACD -1855.15
     INDIGO     MACD -1338.65
     INDOCO     MACD   123.80
 INDUSINDBK     MACD  1379.90
 INDUSTOWER     MACD   635.85
        IOC     MACD   489.05
      IRCTC     MACD -1230.30
        ITC     MACD  1301.55
 JINDALSTEL     MACD    58.50
  JKLAKSHMI     MACD -1119.05
     JKTYRE     MACD   201.20
   JSWSTEEL     MACD -1732.15
 KAJARIACER     MACD -1796.40
  KOTAKBANK     MACD  -299.65
       INFY     MACD -1374.00
  LICHSGFIN     MACD  -815.10
         LT     MACD   168.10
        LTI     MACD  -264.00
      LUPIN     MACD   988.30
     MARUTI     MACD  -228.50
 MCDOWELL-N     MACD -1026.45
        MCX     MACD -1817.40
       MFSL     MACD  -975.35
        MGL     MACD  -876.00
   MINDTREE     MACD -1221.60
       MOIL     MACD -1758.00
    MPHASIS     MACD   219.35
        MRF     MACD     0.00
 MUTHOOTFIN     MACD -2764.90
        M&M     MACD  -880.80
  NESTLEIND     MACD  -634.05
       NMDC     MACD -2078.75
       NTPC     MACD -1301.55
       ONGC     MACD -1991.80
        PEL     MACD  1484.20
        PFC     MACD -1058.30
 PIDILITIND     MACD  -602.45
        PNB     MACD -2444.15
  POWERGRID     MACD  -227.20
    PRAJIND     MACD   -71.75
        PVR     MACD   455.00
     RADICO     MACD -1372.10
    RBLBANK     MACD   990.80
   RELIANCE     MACD  -501.80
  REPCOHOME     MACD  2263.05
       SAIL     MACD  2844.90
    SBILIFE     MACD  -936.15
       SBIN     MACD -1015.25
    SIEMENS     MACD  -910.50
      SPARC     MACD  -492.00
        SRF     MACD -1024.45
 SRTRANSFIN     MACD  -312.55
  SUNPHARMA     MACD -1050.20
   SYMPHONY     MACD -1454.65
   TATACHEM     MACD -1615.30
 TATACONSUM     MACD   777.35
  TATAELXSI     MACD -3287.15
 TATAMOTORS     MACD  3454.80
  TATASTEEL     MACD -1065.65
        TCS     MACD   -42.80
  TEAMLEASE     MACD -1967.20
      TECHM     MACD -1806.35
      TITAN     MACD  -682.65
 TORNTPHARM     MACD  -604.10
 TORNTPOWER     MACD -3910.40
 TRITURBINE     MACD -2657.65
   TVSMOTOR     MACD   282.70
 ULTRACEMCO     MACD  -267.35
        UPL     MACD  -616.05
       VEDL     MACD   -14.60
     VOLTAS     MACD -2398.05
      WIPRO     MACD -2831.85
 WOCKPHARMA     MACD -2918.15
       ZEEL     MACD -1279.65
```
- Scanning for buy/sell signals and measuring those(backtesting) for a specific security
```python
nseta test-trading-strategy -S TATAMOTORS -s 2020-06-01 -e 2021-01-17 --strategy macd
# Using fastquant:
   fast_period  slow_period  signal_period  init_cash    final_value       pnl
0           12           26              9     100000  131719.153375  31719.15

# Using this nseta lib:

   DateTime Signal   Price                             Pattern       Direction      Funds Order_Size Holdings_Size Portfolio_Value
 2020-07-20    BUY  105.05                   Direction.Neutral    Direction.Up   50101.25        475           475        100000.0
 2020-07-21    BUY  108.45                   Direction.Neutral    Direction.Up   25157.75        230           705        101615.0
 2020-07-23   SELL  106.05                   Direction.Neutral  Direction.Down    99923.0        705             0         99923.0
 2020-07-31    BUY  104.65    Direction.PossibleReversalUpward  Direction.Down   50004.95        477           477         99923.0
 2020-08-03    BUY  113.05    Direction.PossibleReversalUpward    Direction.Up    25020.9        221           698        103929.8
 2020-08-03    BUY  113.05                         Direction.V    Direction.Up    12585.4        110           808        103929.8
 2020-08-06    BUY   116.8                         Direction.V    Direction.Up     6395.0         53           861        106959.8
 2020-08-07    BUY   119.1                Direction.HigherHigh    Direction.Up     3298.4         26           887        108940.1
 2020-08-10    BUY  123.85                Direction.HigherHigh    Direction.Up    1688.35         13           900       113153.35
 2020-08-11    BUY   122.3                Direction.HigherHigh    Direction.Up     954.55          6           906       111758.35
 2020-08-12    BUY  125.35                Direction.HigherHigh    Direction.Up      578.5          3           909       114521.65
 2020-08-13    BUY  131.15                Direction.HigherHigh    Direction.Up      316.2          2           911       119793.85
 2020-08-14    BUY   124.6                Direction.HigherHigh    Direction.Up      191.6          1           912        113826.8
 2020-08-21   SELL   120.9  Direction.PossibleReversalDownward    Direction.Up   110452.4        912             0        110452.4
 2020-08-27    BUY  144.25                 Direction.InvertedV    Direction.Up    55348.9        382           382        110452.4
 2020-08-27    BUY  144.25                         Direction.V    Direction.Up   27797.15        191           573        110452.4
 2020-08-28    BUY   142.8                         Direction.V    Direction.Up   13945.55         97           670       109621.55
 2020-08-28    BUY   142.8                         Direction.V    Direction.Up    7091.15         48           718       109621.55
 2020-09-01   SELL   143.8                         Direction.V  Direction.Down  110339.55        718             0       110339.55
 2020-09-03    BUY  151.85                 Direction.InvertedV    Direction.Up    55218.0        363           363       110339.55
 2020-09-03    BUY  151.85                         Direction.V    Direction.Up   27733.15        181           544       110339.55
 2020-09-04    BUY   147.8                         Direction.V    Direction.Up   13987.75         93           637       108136.35
 2020-09-04    BUY   147.8                         Direction.V    Direction.Up    7041.15         47           684       108136.35
 2020-09-07    BUY   149.4                         Direction.V    Direction.Up    3604.95         23           707       109230.75
 2020-09-08    BUY   142.3                Direction.HigherHigh    Direction.Up    1897.35         12           719       104211.05
 2020-09-09    BUY   140.1                Direction.HigherHigh    Direction.Up    1056.75          6           725       102629.25
 2020-09-10    BUY   143.3                Direction.HigherHigh    Direction.Up     626.85          3           728       104949.25
 2020-09-11   SELL   144.3  Direction.PossibleReversalDownward    Direction.Up  105677.25        728             0       105677.25
 2020-10-08    BUY  140.95    Direction.PossibleReversalUpward  Direction.Down   52961.95        374           374       105677.25
 2020-10-09    BUY  138.45    Direction.PossibleReversalUpward    Direction.Up    26518.0        191           565       104742.25
 2020-10-09    BUY  138.45                         Direction.V    Direction.Up   13365.25         95           660       104742.25
 2020-10-12    BUY   135.9                         Direction.V    Direction.Up    6706.15         49           709       103059.25
 2020-10-12    BUY   135.9                         Direction.V    Direction.Up    3444.55         24           733       103059.25
 2020-10-13    BUY   134.1                         Direction.V    Direction.Up    1835.35         12           745       101739.85
 2020-10-14    BUY   130.7                Direction.HigherHigh    Direction.Up     920.45          7           752        99206.85
 2020-10-15    BUY  126.95                Direction.HigherHigh    Direction.Up      539.6          3           755        96386.85
 2020-10-16    BUY  127.75                Direction.HigherHigh    Direction.Up      284.1          2           757        96990.85
 2020-10-19    BUY  128.25                Direction.HigherHigh    Direction.Up     155.85          1           758        97369.35
 2020-10-22   SELL   133.5  Direction.PossibleReversalDownward    Direction.Up  101348.85        758             0       101348.85
 2020-10-28    BUY   134.8  Direction.PossibleReversalDownward    Direction.Up   50798.85        375           375       101348.85
 2020-11-02    BUY  132.85                Direction.HigherHigh    Direction.Up    25424.5        191           566        100617.6
 2020-11-03    BUY   134.1                Direction.HigherHigh    Direction.Up    12819.1         94           660        101325.1
 2020-11-03    BUY   134.1                         Direction.V    Direction.Up     6516.4         47           707        101325.1
 2020-11-04    BUY   135.9                         Direction.V    Direction.Up     3390.7         23           730        102597.7
 2020-11-05    BUY  137.65                Direction.HigherHigh    Direction.Up     1738.9         12           742        103875.2
 2020-11-06    BUY   139.0                Direction.HigherHigh    Direction.Up      904.9          6           748        104876.9
 2020-11-09    BUY   141.0                Direction.HigherHigh    Direction.Up      481.9          3           751        106372.9
 2020-11-10    BUY   146.0                Direction.HigherHigh    Direction.Up      335.9          1           752        110127.9
 2020-11-11    BUY  150.95                Direction.HigherHigh    Direction.Up     184.95          1           753        113850.3
 2020-12-07   SELL  183.55  Direction.PossibleReversalDownward    Direction.Up   138398.1        753             0        138398.1
 2020-12-31    BUY  183.85    Direction.PossibleReversalUpward  Direction.Down    69270.5        376           376        138398.1
 2021-01-01    BUY   186.5    Direction.PossibleReversalUpward    Direction.Up    34768.0        185           561        139394.5
 2021-01-01    BUY   186.5                         Direction.V    Direction.Up    17423.5         93           654        139394.5
 2021-01-06    BUY   195.4                         Direction.V    Direction.Up     8825.9         44           698        145215.1
 2021-01-07    BUY  196.75                Direction.HigherHigh    Direction.Up     4497.4         22           720        146157.4
 2021-01-08    BUY  198.15                Direction.HigherHigh    Direction.Up    2317.75         11           731        147165.4
 2021-01-11    BUY  220.65                Direction.HigherHigh    Direction.Up     1214.5          5           736        163612.9
 2021-01-12    BUY   237.8                Direction.HigherHigh    Direction.Up      738.9          2           738        176235.3
 2021-01-13    BUY   242.6                Direction.HigherHigh    Direction.Up      496.3          1           739        179777.7
 2021-01-14    BUY   245.1                Direction.HigherHigh    Direction.Up      251.2          1           740        181625.2
 2021-01-15   SELL   260.3                Direction.HigherHigh    Direction.Up   192873.2        740             0        192873.2


     Symbol Strategy      PnL
 TATAMOTORS     MACD  92873.2
```
- Compare all trading strategies through backtesting

```python
nseta scan-trading-strategy -s 2020-06-01 -e 2021-01-22


 Done.                                                                                                                                
This run of trading strategy scan took 124.9 sec

     Symbol   RSI-PnL   MACD-PnL  BBANDS-PnL Reco-RSI Reco-MACD Reco-BBANDS
        ABB   2001.65   10381.40     8419.90  Unknown       Buy     Unknown
  EICHERMOT -65228.45  -15406.95   -30387.85      Buy       Buy         Buy
        MRF      0.00       0.00        0.00  Unknown       Buy     Unknown
   MINDTREE  18711.95   13120.65    17001.25  Unknown       Buy     Unknown
   CROMPTON  12021.85   -2428.30    17970.65  Unknown       Buy     Unknown
   RELIANCE   2592.05   -6538.90    -2374.05     Sell       Buy        Sell
  GODREJIND  16671.80   21816.40    26177.55      Buy       Buy         Buy
 CHAMBLFERT  16565.85   22188.80    30350.80      Buy       Buy         Buy
   GOODYEAR   9890.85   26561.75     2804.05  Unknown       Buy     Unknown
  BRITANNIA  -4414.30   -7655.70     -218.55  Unknown       Buy     Unknown
    HAVELLS  38824.50   14944.75    39997.35     Sell       Buy        Sell
 MADRASFERT  -1987.85    3819.30    24400.60      Buy       Buy         Buy
 HEROMOTOCO  12380.95    7190.65    23257.40  Unknown       Buy     Unknown
 TATAMOTORS  72553.15  125909.35    47051.45  Unknown       Buy     Unknown
 HINDUNILVR    816.80    -365.30     6380.25      Buy       Buy         Buy
 BHARATFORG  51284.30   37607.55    55649.10  Unknown       Buy     Unknown
   ASHOKLEY  26382.90   37486.45    12371.50  Unknown       Buy     Unknown
  BAJAJELEC  14848.05   24464.40     7105.90  Unknown       Buy     Unknown
     VOLTAS  25630.15   11733.20    10959.25     Sell       Buy        Sell
 KAJARIACER  29899.35    6014.95    18198.15      Buy       Buy         Buy
  VISAKAIND  39846.30   14623.15    45640.85      Buy       Buy         Buy
     VGUARD   9702.40    2542.45     6752.60  Unknown       Buy     Unknown
 APOLLOTYRE  36391.15   22442.35    28386.05      Buy       Buy         Buy
     JKTYRE  22340.80   99510.55    26563.35      Buy       Buy         Buy
        UPL  19662.55    6522.75     2230.80     Sell       Buy        Sell
  NESTLEIND  -3636.95   -7961.75     1337.10  Unknown      Sell     Unknown
 JINDALSTEL  14071.85   23148.30    31277.05     Sell      Sell        Sell
 MUTHOOTFIN  -7348.95   -8294.40    -8255.35     Sell      Sell        Sell
    MPHASIS  20840.75   -3853.55    10362.70     Sell      Sell        Sell
       MOIL  -2411.95  -10175.70   -13105.55     Sell      Sell        Sell
  JKLAKSHMI  15080.45    7366.70     9165.35     Sell      Sell        Sell
        LTI  21342.45   20271.20     6096.40     Sell      Sell        Sell
         LT  -5743.25   21459.75     5938.55     Sell      Sell        Sell
       MFSL  -1270.15   12190.70    14175.50     Sell      Sell        Sell
        MCX  -2070.85   -1863.05     2027.90  Unknown      Sell     Unknown
   JSWSTEEL  30158.70   50909.55    21781.55     Sell      Sell        Sell
 MCDOWELL-N   9771.85    7303.55     4796.40  Unknown      Sell     Unknown
     MARUTI   6509.50    4483.05     5651.05     Sell      Sell        Sell
       NMDC  17227.00   22252.20    15177.85     Sell      Sell        Sell
  KOTAKBANK   9750.65   16006.10    19880.95     Sell      Sell        Sell
        M&M   2888.25   15932.60    14378.45     Sell      Sell        Sell
      LUPIN  20286.30    6448.20     5136.45  Unknown      Sell     Unknown
  LICHSGFIN  12547.80   31683.15     6849.50     Sell      Sell        Sell
        MGL   -276.95   10999.05    -7390.50     Sell      Sell        Sell
       NTPC  32334.15    7878.15    18086.50     Sell      Sell        Sell
  POWERGRID   -517.05    1997.05     3999.85     Sell      Sell        Sell
        PEL  -2506.20   -4936.90    11560.90     Sell      Sell        Sell
      WIPRO  33190.85   38708.70    20412.25  Unknown      Sell     Unknown
       VEDL  18468.65   56375.75    34460.20     Sell      Sell        Sell
 ULTRACEMCO  21509.75   10356.05     9070.75     Sell      Sell        Sell
 TRITURBINE  24789.15   22530.00    23231.05  Unknown      Sell     Unknown
 TORNTPOWER  -2795.50    7296.20    -2500.20     Sell      Sell        Sell
 TORNTPHARM  11024.95   -1035.75    11807.30  Unknown      Sell     Unknown
      TITAN  11782.60    8714.45    13886.40     Sell      Sell        Sell
      TECHM  28612.60   27675.60    14190.40     Sell      Sell        Sell
  TEAMLEASE  28422.90   17050.30     8771.40     Sell      Sell        Sell
  TATASTEEL  32270.30   76080.75     9378.60     Sell      Sell        Sell
  TATAELXSI  36476.95   93427.40    15800.25     Sell      Sell        Sell
 TATACONSUM   4169.75   32354.45      452.15     Sell      Sell        Sell
   TATACHEM   2013.65   36156.90    -1991.30     Sell      Sell        Sell
       ONGC  20577.20   33639.75      736.10     Sell      Sell        Sell
   SYMPHONY  -2720.60   -3843.00     1463.80  Unknown      Sell     Unknown
 SRTRANSFIN  26921.05   38725.70    40349.50     Sell      Sell        Sell
        SRF   7892.20    4602.15    -1200.40     Sell      Sell        Sell
      SPARC  -5107.55   -6680.00     2692.00     Sell      Sell        Sell
    SIEMENS  12188.80    7822.70     8987.00     Sell      Sell        Sell
       SBIN  27090.15   30052.60    28696.65     Sell      Sell        Sell
    SBILIFE  -2242.30    1368.10     6883.45     Sell      Sell        Sell
       SAIL  11021.50   86778.75    14752.55     Sell      Sell        Sell
    RBLBANK  25275.90     920.80    55111.85     Sell      Sell        Sell
    PRAJIND  14660.40   56713.40    35471.10     Sell      Sell        Sell
        ITC   4965.80    5179.80    -5404.95     Sell      Sell        Sell
        PNB   1244.20   15302.55    -2017.45     Sell      Sell        Sell
 PIDILITIND   3723.60    4443.40     7504.55  Unknown      Sell     Unknown
        PFC  25937.00   18628.85    15473.40     Sell      Sell        Sell
  SUNPHARMA  10176.55    8764.25    11934.85     Sell      Sell        Sell
      IRCTC   5889.50   -7910.80     5381.90  Unknown      Sell     Unknown
     INDOCO  36822.30   16298.35    18239.35     Sell      Sell        Sell
       INFY  23501.60    9045.90     6037.15      Buy      Sell         Buy
 CUMMINSIND  28357.75   50103.70    22421.25  Unknown      Sell     Unknown
     CONCOR   3958.15   -7644.10    12931.75  Unknown      Sell     Unknown
      CIPLA   -863.90  -11001.30    -1615.70     Sell      Sell        Sell
 CENTURYTEX  -1534.10   -7385.15     -277.95     Sell      Sell        Sell
 CASTROLIND   7748.55   16730.20     2313.65      Buy      Sell         Buy
   CADILAHC  11190.45   -4418.00     3921.05     Sell      Sell        Sell
       BPCL   8059.85    8036.85    -4497.15     Sell      Sell        Sell
  BOMDYEING  -6737.00  -12670.20     2696.05     Sell      Sell        Sell
     BIOCON -13393.40    5797.00    -9141.10     Sell      Sell        Sell
       BHEL  -8407.15   26815.25   -10605.35     Sell      Sell        Sell
 BHARTIARTL  -3680.55   -3268.95   -14718.10     Sell      Sell        Sell
 BERGEPAINT  28668.65   18113.10    17560.65  Unknown      Sell     Unknown
       BEML   8935.70   43903.25    10403.80  Unknown      Sell     Unknown
        IOC  13763.95   20124.65    11087.05     Sell      Sell        Sell
        BEL  25612.35   26593.00    20960.45     Sell      Sell        Sell
  BANKINDIA  -8490.60   10402.65     1421.55     Sell      Sell        Sell
 BANKBARODA  -1982.90   18592.05     -414.45     Sell      Sell        Sell
 BANDHANBNK   7075.00   29110.25    27895.70     Sell      Sell        Sell
   AXISBANK  10243.80   30327.15    13906.45  Unknown      Sell     Unknown
 AUROPHARMA   5399.60    4011.95    10874.30  Unknown      Sell     Unknown
       ATUL   7856.85   17283.40     4561.70      Buy      Sell         Buy
 ASIANPAINT  18558.10   21408.20     9758.05  Unknown      Sell     Unknown
     ASHOKA  18267.15   59326.95    20278.60     Sell      Sell        Sell
     ARVIND  40644.55   19603.10    27942.25     Sell      Sell        Sell
  AMBUJACEM    948.15   21780.15    15247.05  Unknown      Sell     Unknown
   ADANIENT  26281.95   58859.20    39130.70     Sell      Sell        Sell
        ACC  21227.55   11803.15    11822.90  Unknown      Sell     Unknown
      ABFRL  14611.75    2862.35    -5585.80  Unknown      Sell     Unknown
  BATAINDIA   4438.65       2.95     5548.70     Sell      Sell        Sell
      DABUR   4908.15   -1420.00     6744.50     Sell      Sell        Sell
       ZEEL  37259.95   38965.80     1523.75     Sell      Sell        Sell
        DLF  19716.05   11898.85    11771.65     Sell      Sell        Sell
 INDUSTOWER  16502.15   31680.60    24006.85     Sell      Sell        Sell
 INDUSINDBK  29827.65   18584.20    43392.45     Sell      Sell        Sell
 WOCKPHARMA   5274.15   66126.90    11580.35     Sell      Sell        Sell
   INDIACEM  19836.30   11050.80    27692.95     Sell      Sell        Sell
        IGL  -3178.95   11829.45   -20391.55  Unknown      Sell     Unknown
 IDFCFIRSTB  25145.55   27393.10    30041.65     Sell      Sell        Sell
       IDBI  15280.40  -10982.05    10550.85      Buy      Sell         Buy
  ICICIBANK  17175.95   11631.65    17862.15  Unknown      Sell     Unknown
  HINDPETRO   1399.65   -3863.15   -13296.90     Sell      Sell        Sell
   HINDALCO  40117.50   37981.95    18571.20     Sell      Sell        Sell
   HDFCBANK   2504.35   18294.15     2456.80     Sell      Sell        Sell
       HDFC  11953.15   35841.10    23806.40     Sell      Sell        Sell
    DCBBANK  24698.10   26477.50     2014.35     Sell      Sell        Sell
        HAL  64975.60   41141.35    11387.05     Sell      Sell        Sell
    HCLTECH   9045.00   13588.75     3366.50     Sell      Sell        Sell
 GODREJPROP  20744.25    1375.40    16732.95     Sell      Sell        Sell
    DRREDDY  29046.30   11387.80    20607.60     Sell      Sell        Sell
    ESCORTS   -678.15   -8119.60    -1496.70  Unknown      Sell     Unknown
   EVEREADY  24017.50   24217.60    37900.65  Unknown      Sell     Unknown
   EXIDEIND  23685.95   12995.70    15756.20  Unknown      Sell     Unknown
        FCL  41558.75    5484.55    35716.05  Unknown      Sell     Unknown
   GRAPHITE   3464.05   33707.65    27880.65     Sell      Sell        Sell
     FORTIS  11551.40   -1273.40     -732.10  Unknown      Sell     Unknown
 FEDERALBNK  14979.60   30841.25    40875.20     Sell      Sell        Sell
       GAIL   1118.45   28179.15     6749.95  Unknown      Sell     Unknown
   GLENMARK  -4047.55    8135.60     7957.45     Sell      Sell        Sell
   GMRINFRA   7569.15   -5216.65    12415.65     Sell      Sell        Sell
   GODREJCP   1456.80    5730.00    16351.60     Sell      Sell        Sell
 BAJFINANCE  10279.00   18712.05     5742.30  Unknown   Unknown     Unknown
   TVSMOTOR   7782.35    2295.35    11448.50      Buy   Unknown         Buy
  REPCOHOME  71396.60   49798.70    49716.15  Unknown   Unknown     Unknown
     INDIGO   8979.00   29612.90    11815.05  Unknown   Unknown     Unknown
        TCS   5153.20   17996.65     1796.85  Unknown   Unknown     Unknown
        FSL  61118.35   35050.20    58745.90     Sell   Unknown        Sell
     RADICO  18186.15    9358.40    29067.85  Unknown   Unknown     Unknown
```

- To view just the logs of your interest, you can filter those:
  ```python
    nseta --debug --filter filter_text_goes_here <command> [command options]
    nseta --debug --trace --filter filter_text_goes_here <command> [command options]
  ```

- To view the time taken by each method:
  ```python
    nseta --debug --filter time_taken <command> [command options]
    nseta --debug --trace --filter time_taken <command> [command options]
  ```
- Configuration based display outputs
 
 You can use the `config.txt` file and make changes as per your wish to view the results in a specific order or add/remove columns.

### Submit patches

If you have fixed an issue or added a new feature, please fork this repository, make your changes and submit a pull request. [Here's good article on how to do this.](https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267) 

## License
[MIT License](https://github.com/pkjmesra/nseta/blob/main/LICENSE)

## Inspirations (Thank you so much!)
-  [nsepy](https://github.com/swapniljariwala/nsepy)
-  [fastquant](https://github.com/enzoampil/fastquant)
-  [fbprophet](https://github.com/facebook/prophet)
-  [nsetools](https://github.com/vsjha18/nsetools)
-  [ta-lib](https://github.com/mrjbq7/ta-lib)
-  [medium](https://github.com/CanerIrfanoglu/medium)
