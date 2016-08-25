# trader turret

Multi-purpose market-focused command line tool for automating components of your trading workflow.  This tool combines typical ticker data (e.g. most objects exposed by the Yahoo Finance API - price, change, short interest, yield, etc.), as well as realted data of interest (e.g. realtime price, earnings date, pivot points, volume/percent of average volume, percent off high/low, etc.), and manual components of your daily/weekly workflow.  Some of the other features include, listing/counting 52-week highs/lows & all-time highs/lows, getting current and upcoming econ calendar data, getting fed watch predicitons for the upcoming meeting, getting futures data for US/ROW indicies, and more.   Also supported is running against a standard format config file (use ttrack.py to generate config file), populated with tickers and then alarming on price points passed from the config file (e.g. support & resistance levels, targets, etc. as well as common metrics (e.g. moving averages, volume, new highs, and more).     

Install
-------

Get the .py and install the pre-reqs.

Usage
-----
  -h, --help            show this help message and exit
  -i init, --init init  init file to use
  -e, --earningsdate    get earnings date
  -perf, --perfcheck    use with init file to check performance
  -fw, --fedwatch       Returns the liklihood of a Fed rate increase
  -ect ECONTOMORROW, --econtomorrow ECONTOMORROW
                        Returns tomorrow's economic calendar
  -ff, --floor          floor classic pivot formula
  -wf, --woodie         woddie pivot formula
  -kf, --kirk           kirk pivot formula
  -pp init, --purhcaseprice init
                        identify purchase price
  -t ticker, --ticker ticker
                        ticker for lookup
  -v, --volume          Get volume
  -c, --change          Get day's change
  -av, --avgvolume      Get avgerage volume
  -r, --realtime        Get realtime price
  -p, --price           Get delayed price
  -sr, --short          Get short ratio
  -pe, --peratio        Get PE ratio
  -ex, --exchange       Get listed exchange
  -mc, --marketcap      Get marketcap
  -go, --getopen        Get opening price
  -book, --getbook      Get book value
  -div, --dividendshare
                        Get dividend per share
  -divy, --dividendyield
                        Get dividend dividend yield
  -eps, --earnings      Get earnings per share
  -dh, --dayhigh        Get day high
  -dl, --daylow         Get day low
  -yh, --yearhigh       Get year high
  -yl, --yearlow        Get year low
  -ebitda, --ebitda     Get ebitda
  -ps, --ps             Get price to sales
  -peg, --pegratio      PEG ratio
  -pc, --percentchange  Percent change
  -poh, --percentoffhigh
                        Percent off high
  -pol, --percentofflow
                        Percent off low
  -poa, --percentofaverage
                        Percent of average volume
  -nv HIGHVOLUME, --highvolume HIGHVOLUME
                        Prints a volume
  -ah ATHIGH, --athigh ATHIGH
                        All time high
  -al ATLOW, --atlow ATLOW
                        All time low
  -ma MA, --movingaverage MA
                        Gets moving average; specify either 50 or 200 (e.g.
                        -ma 200, -ma 50)
  -d, --debug           debug
  -nyh NEWYEARHIGHS, --newyearhighs NEWYEARHIGHS
                        '-nyh list' produces a list of tickers hitting 52-week
                        highs. '-nyh count' produces a count of the tickers
                        hitting new 52-week highs
  -nyl NEWYEARLOWS, --newyearlows NEWYEARLOWS
                        '-nyl list' produces a list of tickers hitting 52-week
                        lows. '-nyl count' produces a count of the tickers
                        hitting new 52-week lows
  -f FUTURES, --futures FUTURES
                        Provides futures pricing - specify 'sp', 'dow', 'nas',
                        'row' for S&P, Dow, Nasdaq, or RestOfWorld.
    

Prerequisites
--------
pip install the prerequisites

argparse, yahoo_finance, yahoofinancecalc, re, os, ConfigParser, time, bs4, urllib2, requests, json

Usage Examples
--------

tt.py -r -c -pc -poa -t oled
Get's realtime price, change, percent change, percent of average volume for ticker symbol OLED

tt.py -nyh list 
Produces a list of tickers hitting new 52-week highs

tt.py -i configfile.txt -perf
Using the specified configuration file (use ttrack.py to create config ile), run ticker and price levels through all alarms (e.g. 50-day and 200-day moving averages, support and resistance levels, stop levels, price levels 1-3, target level), and then run through a performance check (-perf) to report change from the initial tracking/purchase prices.

tt.py -fw
Reports odds of a rate hike at the next fed meeting (e.g. 25-50, and 50-75 basis points - .82) today vs. the odds yesterday.


tt.py -ect this
Reports this week's econ calendar by day-of-week (next reports next week's calendar)


See Also
--------

NA
