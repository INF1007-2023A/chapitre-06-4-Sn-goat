#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
    evenKeys = set(
		key 
			for key, value in dictionary.items()
				if (key % 2) == 0)
    return evenKeys
	

def join_dictionaries(dictionaries):
    jointDict = {
		key:value
			for dict in dictionaries
        		for key,value in dict.items()}
    
    return jointDict

def dictionary_from_lists(keys, values):
    dict = {}
    for key in keys:
        for value in values:
            dict[key] = value
            break
    return dict


def get_greatest_values(dictionnary, num_values):
    
	listMax = sorted([dictionnary[key] for key in dictionnary], reverse=True)[:num_values]
	return listMax


def get_sum_values_from_key(dictionnaries, key):
    sum_ = sum(
		dict[key]
			for dict in dictionnaries
				if key in dict)
    
    return sum_


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
