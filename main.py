#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser



ap = argparse.ArgumentParser()

args = ap.parse_args()




data = pagegetter.get_page()

unit_list = parser.make_unit_list()
print("unit_list:", unit_list)


