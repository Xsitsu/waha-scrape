import os
import shutil
import requests


PAGE_CACHE_PATH = os.path.expanduser("~/.waha-scrape/cache/")
URL_BASE = "https://wahapedia.ru/wh40k10ed/factions/"
URL = "https://wahapedia.ru/wh40k10ed/factions/necrons/datasheets.html"


def clean_cache():
	shutil.rmtree(PAGE_CACHE_PATH)

def _url_to_cache_page_name(url):
	file_name = url.replace(URL_BASE, "")
	file_name = file_name.replace("/", "_")
	return file_name


def get_page():
	os.makedirs(PAGE_CACHE_PATH, exist_ok=True)

	# Make work for not just Necrons later if I care
	url = URL
	file_name = _url_to_cache_page_name(url)
	file_path = PAGE_CACHE_PATH + file_name

	if os.path.exists(file_path):
		print("File exists! Returning cached page.")
		with open(file_path, 'r') as file:
			data = file.read()
		return data

	else:
		print("File does not exist. Fetching from url.")

		response = requests.get(url)
		if response.status_code == 200:
			with open(file_path, 'x') as file:
				file.write(response.text)
			return response.text

	return ""


