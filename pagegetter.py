import os
import shutil
import requests


URL = "https://wahapedia.ru/wh40k10ed/factions/necrons/datasheets.html"


def get_page():
	response = requests.get(URL)
	if response.status_code == 200:
		return response.text
	return ""


