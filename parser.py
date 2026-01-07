from bs4 import BeautifulSoup


def make_unit_list(page_data):
	unit_list = list()

	soup = BeautifulSoup(page_data, 'html.parser')
	sheets = soup.find_all(class_ = "dsOuterFrame")
	for sheet in sheets:
		unit_list.append(_get_name_from_data_sheet(sheet))

	return unit_list


def _get_name_from_data_sheet(sheet):
	return "jeff"

