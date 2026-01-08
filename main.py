#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser



ap = argparse.ArgumentParser()
ap.add_argument('list_file', help='Input file for list building')
ap.add_argument('-c', '--clean', help='Clean the cache', action='store_true')

args = ap.parse_args()


if args.clean:
	pagegetter.clean_cache()
	sys.exit()


data = pagegetter.get_page()

model_list = parser.make_model_list(data)
for model in model_list:
	print(model)
	for unit in model.units:
		print(f"\t{str(unit)}")


