#!/usr/bin/env python

from bs4 import BeautifulSoup
import yahoofinancecalc
import urllib2
from yahoo_finance import Share

#updated 8/18 - change in realtime scrape (scraper4)
#update 8/19 - changetargetdown, changetargetup fixed. (-i -perf)

baseurl = 'http://finance.yahoo.com/q?s='
endurl = '&ql=1'

def scrape1(ticker):
	"""
	Returns the real time price of supplied ticker, scraped from Yahoo Finance
	"""

	url = baseurl + ticker + endurl
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "lxml")
	#target = soup.find("span", {"class": "time_rtq_ticker"}).span.contents

	target = soup.find("div", {"id": "app"})
	target = soup.find("span", {"class": "Fw(500) D(ib) Fz(36px)"}) #finds the real-time price in the revised Yahoo interface (e.g. post 7/12/2016)
	print target.text


	return target.text

	#return target[0] (old yahoo finance interface prior to 7/12/16)


def scraper2(ticker):
	"""
	Deprecated by scraper3 - returned price, change, percent, and timestamp for realtimeChangeWork
	"""
	url = baseurl + ticker + endurl
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "lxml")
	target = soup.find("div", {"class": "yfi_rt_quote_summary"})
	target = soup.find_all("span")
	rtprice = target[33].text
	rtchange = target[35].text #doesn't get positive or negative
	rtchange = rtchange.replace(" ","")
	rtpercent = target[36].text
	rtpercent = rtpercent.replace("(", "")
	rtpercent = rtpercent.replace(")", "")
	rttimestamp = target[39].text
	#print rtprice + ", " +  rtchange + ", " + rtpercent + ", " + rttimestamp
	return rtprice, rtchange, rtpercent, rttimestamp

def scraper3(ticker):
	"""
	Deprecated - Yahoo Finance upgrade on 7/12/2016 broke this.  Scraper4 restores functionality
	Returns real time price and realted info (realtime[0], targettime, changetarget, targetpercent, openprice) scraped from URL for supplied ticker 
	subrealtimequote, subtime, subchange, subpercent, openprice = realtime.scraper3(ticker)

	"""
	sp500string = 'GSPC'

	if sp500string in ticker:
		print "YES!"
		sp500percentchange, sp500dayhigh, sp500open, sp500change, sp500price, sp500index, sp500desc = yahoofinancecalc.sp500info()
		targettime = 'NA'
		targetpercent = 0
		print repr(sp500price)
		return sp500price, targettime, sp500percentchange, targetpercent, sp500open
	else:


		url = baseurl + ticker + endurl
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.read(), "lxml")
		#realtime = soup.find("span", {"class": "time_rtq_ticker"}).span.contents
		realtime = soup.find("div", {"id": "app"})
		realtime = soup.find("span", {"class": "Fw(500) D(ib) Fz(36px)"}) #finds the real-time price in the revised Yahoo interface (e.g. post 7/12/2016)
		#print target.text


		#openprice = soup.find("td", {"class": "yfnc_tabledata1"})
		#openprice = openprice.text
		openprice = stock.get_open()

		target2 = soup.find("div", {"class": "yfi_rt_quote_summary"})
		target3 = target2.find_all('span')

		#search strings
		change = "yfs_c63_" + ticker
		percent = "yfs_p43_" + ticker
		tickertimestamp = "yfs_t53_" + ticker
		
		#Search string and getting afterhours pricing (testing - as of .60)
		ahprice = "yffs_c85_" + ticker
		ahchange = "yfs_c85_" + ticker
		ahpercent = "yfs_c86_" + ticker
		ahtimestamp = "yfs_t54_" + ticker
		ahpricetarget = target2.find(id=ahprice)
		ahchangetarget = target2.find(id=ahchange)
		ahpercenttarget = target2.find(id=ahpercent)


		#finding the search strings
		changetarget = target2.find(id=change)
		targetpercent = target2.find(id=percent)
		targettime = target2.find(id=tickertimestamp)


		#cleaning the found strings
		if changetarget is not None:
			changetarget = changetarget.text
			changetarget = changetarget.replace(" ", "")
			changetarget = changetarget.replace("'", "")
			targetpercent = targetpercent.text
			targetpercent = targetpercent.replace("(","")
			targetpercent = targetpercent.replace(")","")
		else:
			changetarget = '0'
			targetpercent = '0'

		if targettime is not None: #handles if S&P 500 index ^gspc is passed - in which case, there is no last trade time.
			targettime = targettime.text
		



		#realtime = realtime[0]
		#realtime = realtime.replace("'","")
		#print "Count"
		#print realtime[0]

		#if there's an afterhours price target... do this stuff:

		if ahpricetarget is not None:
			print ahpricetarget, ahchangetarget.text, ahpercenttarget.text

		#return realtime[0], targettime, changetarget, targetpercent, openprice

		return realtime.text, targettime, changetarget, targetpercent, openprice

def scraper4(ticker):
	"""
	Returns real time price and realted info (realtime[0], targettime, changetarget, targetpercent, openprice) scraped from URL for supplied ticker 
	#Replaces scraper3; scraper3 broke after update to Yahoo Finance

	"""
	url = baseurl + ticker + endurl
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "lxml")
	targettime = 'NA'
	#realtime = soup.find("span", {"class": "time_rtq_ticker"}).span.contents
	realtime = soup.find("div", {"id": "app"})
	realtime = soup.find("span", {"class": "Fw(b) D(ib) Fz(36px) Mb(-4px)"}) # Fw(500) D(ib) Fz(36px)
	changetargetdown = soup.find("span", {"class": "Fw(500) D(ib) Pstart(10px) Fz(24px) C($dataRed)"}) #dataRed is down, dataGreen is up
	changetargetup = soup.find("span", {"class": "Fw(500) D(ib) Pstart(10px) Fz(24px) C($dataGreen)"}) #$datagreen is up
	#prevclose = soup.find("td", {"class": "Ta(end) Fw(b)"}).text
	stock = Share(ticker)
	marketopen = stock.get_open()
	#print marketopen

	#print realtime.text #prints the realtime price 

	if changetargetdown is not None:
		#print changetargetdown.text
		changeindollars = changetargetdown.text.split("(")[0] #might be broken?
		changeinpercent = changetargetdown.text.split("(")[1].strip(")")
		#print changeindollars
		#print changeinpercent
		

	if changetargetup is not None:
		#print changetargetup.text
		changeindollars = changetargetup.text.split("(")[0]
		changeinpercent = changetargetup.text.split("(")[1].strip(")")
		#print changeinpercent
		#print changeindollars
		#print changeinpercent

		
		#subtime, change ,subpercent, openprice
	


	#print realtime.text, targettime, changeindollars, changeinpercent, marketopen
	return realtime.text, targettime, changeindollars, changeinpercent, marketopen  

