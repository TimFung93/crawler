from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


#retrieves a list of all internal links found on a page
def get_internal_links(bs4, includeurl):
	internal_links = []
	#find all links that begin with '/'
	for link in bs4.findAll('a', href=re.compile('^(/|.*' + includeurl + ')')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internal_links:
				internal_links.append[link.attrs['href']]
	return internal_links


#retrieves a list of all external links found on a page


def get_external_link(bs4, excludedurl):
	external_link = []
	#finds all links that start with http or www that do
	#not contain the current url
	for link in bs4.findAll('a', href=re.compile('^(www|http)((?!' + excludedurl + ').)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in external_link:
				external_link.append(link.attrs['href'])
	return external_link


def split_address(address):
	print 'i am address %s' %address
	address_parts = address.replace('http://', '').split('/')
	print 'i am address parts %s' %address_parts
	return address_parts

def get_random_external_link(startingpage):
	html = urlopen(startingpage)
	bs4 = BeautifulSoup(html, 'html.parser')
	external_links = get_external_link(bs4, split_address(startingpage)[0])
	if len(external_links) == 0:
		internal_links = get_internal_links(startingpage)
		return get_next_external_link(internal_links[random.randint(0,len(internal_links) - 1)])
	else:
		return external_links[random.randint(0, len(external_links) - 1)]

def follow_external_only(startingsite):
	external_link = get_random_external_link('http://oreilly.com')
	print 'Random external link is:' + external_link
	follow_external_only(external_link)

follow_external_only('http://oreilly.com')
















