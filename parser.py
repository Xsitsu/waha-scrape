from bs4 import BeautifulSoup

from model import Model
from unit import Unit


def make_model_list(page_data):
	model_list = dict()

	soup = BeautifulSoup(page_data, 'html.parser')
	sheets = soup.find_all(class_ = "dsOuterFrame")
	for sheet in sheets:
		model_name = _get_name_from_data_sheet(sheet)

		ds2col = sheet.find(class_ = "ds2col")
		dsRightCol = ds2col.find(class_ = "dsRightСol")
		abil_list = dsRightCol.find_all("div")

		abilities = _get_core_abilities(abil_list)
		unit_list = _get_unit_comp(abil_list)
		model_list[model_name] = Model(model_name, abilities, unit_list)

	return model_list 


def _get_name_from_data_sheet(sheet):
	banner = sheet.find(class_ = "dsBannerWrap")
	header = banner.find(class_ = "dsH2Header")
	div = header.find("div")
	return div.text

def _get_abilities_index(abil_list, key):
	index = 0
	while abil_list[index].text != key:
		index += 1
	return index

def _get_core_abilities(abil_list):
	abilities = dict()

	index = _get_abilities_index(abil_list, "ABILITIES") + 1
	if "CORE" not in abil_list[index].text:
		return {"None": True}

	text = abil_list[index].text.replace("CORE: ", "")
	bits = text.split(",")
	for bit in bits:
		abilities[bit] = True

	return abilities

def _get_unit_comp(abil_list):
	units = dict()

	index = _get_abilities_index(abil_list, "UNIT COMPOSITION") + 2
	prices = abil_list[index]
	entries = prices.findChildren("tr")
	for tr in entries:
		tds = tr.find_all("td")
		num = tds[0].text.replace(" models", "").replace(" model", "")
		cost = tds[1].find("div").text
		units[num] = Unit(num, cost)

	return units


