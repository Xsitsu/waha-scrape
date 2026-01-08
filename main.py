#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser


class BadFileException:
	pass


ap = argparse.ArgumentParser()
ap.add_argument('list_file', help='Input file for list building')
ap.add_argument('-c', '--clean', help='Clean the cache', action='store_true')
ap.add_argument('-o', '--output', help='Output model list', action='store_true')

args = ap.parse_args()


if args.clean:
	pagegetter.clean_cache()
	sys.exit()


data = pagegetter.get_page()

model_list = parser.make_model_list(data)

if args.output:
	for model_name, model in model_list.items():
		print(model)
		for unit in model.units:
			print(f"\t{str(unit)}")
	sys.exit()


army_list = list()
total_points = 0

with open(args.list_file, 'r') as f:
	entries = f.readlines()
	for entry in entries:
		if entry[0] == "#":
			continue

		bits = entry.replace("\n", "").split(",")
		if len(bits) != 2:
			raise BadFileException()

		model_name = bits[0]
		num_models = bits[1]

		model = model_list[model_name]
		unit = model.units[num_models]

		army_list.append(unit)
		total_points += unit.cost

		print(unit, "\t\t", model_name)


print("Total:", total_points)


