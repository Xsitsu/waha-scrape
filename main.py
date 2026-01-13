#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser


class BadFileException:
	pass


ap = argparse.ArgumentParser()
ap.add_argument('-l', '--list_file', help='Input file for list building')
ap.add_argument('-c', '--clean', help='Clean the cache', action='store_true')
ap.add_argument('-a', '--abilities', help='Only list models with these abilities (comma-delimited)')

args = ap.parse_args()


if args.clean:
	pagegetter.clean_cache()
	sys.exit()



def _model_has_abilities(model, abilities):
	for ability in abilities:
		if ability.lower() not in model.get_ability_string().lower():
			return False
	return True

def output_models(model_list):
	ability_req = None
	if args.abilities is not None:
		ability_req = args.abilities.split(",")

	for model_name, model in model_list.items():
		if ability_req is None or _model_has_abilities(model, ability_req):
			print(model)
			for unit in model.units:
				print(f"\t{str(unit)}")


def build_list(list_file):
	army_list = list()
	total_points = 0

	with open(list_file, 'r') as f:
		entries = f.readlines()
		for entry in entries:
			if entry[0] == "#":
				continue

			if entry == "" or entry == "\n":
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




data = pagegetter.get_page()
model_list = parser.make_model_list(data)

if args.list_file:
	build_list(args.list_file)
else:
	output_models(model_list)

