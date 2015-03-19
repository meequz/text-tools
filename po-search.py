#! /usr/bin/env python3
# coding: utf-8
import os
import sys

# args
path = sys.argv[1]
search = sys.argv[2]
grep = 'grep --color=always -rni -I -e "{}" "{}" 2>/dev/null'
added_chars = ['_', '&']

# grepping
output = os.popen(grep.format(search, path)).read()
for idx, letter in enumerate(search):
    for added_char in added_chars:
        new_search = search[:idx] + added_char + search[idx:]
        grep_line = grep.format(new_search, path)
        output += os.popen(grep_line).read()

# sorting
output = output.split('\n')
output.sort()
output = '\n'.join(output)

print(output.strip())
