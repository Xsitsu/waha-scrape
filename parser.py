from bs4 import BeautifulSoup

from model import Model
from unit import Unit


def make_model_list(page_data):
	model_list = list()

	soup = BeautifulSoup(page_data, 'html.parser')
	sheets = soup.find_all(class_ = "dsOuterFrame")
	for sheet in sheets:
		model_name = _get_name_from_data_sheet(sheet)

		# print("Parsing:", unit_name)

		unit_list = _get_unit_comp_from_data_sheet(sheet)
		model_list.append(Model(model_name, unit_list))

	return model_list 


def _get_name_from_data_sheet(sheet):
	banner = sheet.find(class_ = "dsBannerWrap")
	header = banner.find(class_ = "dsH2Header")
	div = header.find("div")
	return div.text

def _get_unit_comp_from_data_sheet(sheet):
	units = list()

	ds2col = sheet.find(class_ = "ds2col")
	dsRightCol = ds2col.find(class_ = "dsRightСol")
	abilities = dsRightCol.find_all("div")

	index = 0
	while abilities[index].text != "UNIT COMPOSITION":
		index += 1
	index += 2

	prices = abilities[index]
	entries = prices.findChildren("tr")
	for tr in entries:
		tds = tr.find_all("td")
		num = tds[0].text.replace(" models", "").replace(" model", "")
		cost = tds[1].find("div").text
		units.append(Unit(num, cost))

	return units

