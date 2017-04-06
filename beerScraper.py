from bs4 import BeautifulSoup
import urllib2
import csv

#BASE_URL = "https://www.ratebeer.com/beer/paradox-beer-skully-barrel-no-43/463083/"

linkList = ["https://www.ratebeer.com/beer/austin-beerworks-bloodwork-orange-ipa/391722/","https://www.ratebeer.com/beer/cellarmaker--trillium--other-half-juice-gymnastics/488468/","https://www.ratebeer.com/beer/fieldwork-pulp/442557/","https://www.ratebeer.com/beer/fieldwork-pulp/442557/","https://www.ratebeer.com/beer/fieldwork-galaxy-juice/407730/","https://www.ratebeer.com/beer/firestone-walker-krieky-bones/276246/","https://www.ratebeer.com/beer/lone-pint-yellow-rose/208800/","https://www.ratebeer.com/beer/paradox-beer-skully-barrel-no-43/463083/","https://www.ratebeer.com/beer/tusk-grain-barrel-blend-no-02/477064/","https://www.ratebeer.com/beer/stone-enjoy-by-ipa--coffee-chocolate/467096/","https://www.ratebeer.com/beer/lawsons-finest-sip-of-sunshine-ipa/258973/","https://www.ratebeer.com/beer/pipeworks-ninja-vs-unicorn-double-ipa/165816/","https://www.ratebeer.com/beer/trillium-vicinity/311024/"]


def beerScrape(section_url):
	hdr = {'User-Agent': 'Magic Browser'}
	req = urllib2.Request(section_url,headers=hdr)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html, "lxml")
	beer = soup(itemprop="name")[0].text.encode("utf-8")
	brewery = soup(itemprop="name")[1].text.encode("utf-8")
	styleLocation = soup.select("div[class=col-md-10] > div > a")
	altStyleLocation = soup.select("div[class=col-sm-8] > div > div > div > div > a")
	style = styleLocation[0].text.encode("utf-8") if styleLocation else altStyleLocation[0].text.encode("utf-8")
	city = styleLocation[1].text.encode("utf-8") if styleLocation else altStyleLocation[1].text.encode("utf-8")
	state = styleLocation[2].text.encode("utf-8") if styleLocation else altStyleLocation[2].text.encode("utf-8")
	#leaving below line in, but it's bad for ABV -- varies because of variability of number of strongs
	#abv = soup.select("div[class=stats-container] > small > big > strong")[0].text.encode("utf-8")
	#this one is way better (below)
	abv = soup.find(title="Alcohol By Volume").find_next('strong').text.encode("utf-8")
	print "Beer: " + beer + "\n" + "Brewery: " + brewery + "\n" + "Style: " + style + "\n" + "Location: " + city + ", " + state + "\n" + "ABV: " + abv + "\n\n"





for x in linkList:
	beerScrape(x)


#beerScrape(BASE_URL)

