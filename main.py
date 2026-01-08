#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser



ap = argparse.ArgumentParser()

args = ap.parse_args()




data = pagegetter.get_page()

model_list = parser.make_model_list(data)
for model in model_list:
	print(model)
	for unit in model.units:
		print(f"\t{str(unit)}")


