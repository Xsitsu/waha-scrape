from bs4 import BeautifulSoup

def make_unit_list(page_data):
	unit_list = list()

	soup = BeautifulSoup(page_data, 'html.parser')



