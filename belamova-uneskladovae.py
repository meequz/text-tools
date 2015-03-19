#! /usr/bin/env python3
# coding: utf-8
import sys


def find(what_find, where_find):
	cn_max = where_find.count(what_find)
	pos = []
	short = where_find[:]
	for cn in range(cn_max):
		res_f = short.index(what_find)
		if cn != 0:
			res_f += (pos[cn-1] + 1)
		pos.append(res_f)
		short = where_find[pos[cn]+1:]
	return pos


def red(text):
    return '\033[91m' + text + '\033[0m'


def prepare_to_print(line_n, line, start, end):
    to_print = str(line_n+1) + ', \t' + line[:start] +\
               red(line[start:end]) + line[end:-1]
    return to_print


filename = sys.argv[1]

ab_a = 'аеёіоуыэюя'
ab_b = 'бвгґджзйклмнпрстўфхцчшь\''
ab_a_upper = ab_a.upper()
ab_b_upper = ab_b.upper()

with open(filename) as f:
    lines = f.readlines()


for line_n, line in enumerate(lines):
    u = find('у', line)
    U = find('У', line)
    
    for u_i in u:
        prev = line[u_i-1]
        #~ калі папярэдняя - галосная
        if prev in ab_a or prev in ab_a_upper:
            print(prepare_to_print(line_n, line, u_i-1, u_i+1))
        #~ калі папярэдні знак - прагал і перад ім галосная
        if prev == ' ':
            prev_prev = line[u_i-2]
            if prev_prev in ab_a or prev_prev in ab_a_upper:
                print(prepare_to_print(line_n, line, u_i-2, u_i+1))
    
    for u_i in U:
        prev = line[u_i-1]
        #~ калі папярэдняя - галосная
        if prev in ab_a or prev in ab_a_upper:
            print(prepare_to_print(line_n, line, u_i-1, u_i+1))
        #~ калі папярэдні знак - прагал і перад ім галосная і пасля вялікая
        if prev == ' ':
            prev_prev = line[u_i-2]
            if prev_prev in ab_a or prev_prev in ab_a_upper:
                next_ = line[u_i+1]
                if next_.is_upper():
                    print(prepare_to_print(line_n, line, u_i-2, u_i+1))
