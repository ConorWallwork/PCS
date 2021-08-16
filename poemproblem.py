from sys import stdin, stdout
import string
import copy

nrules = int(input())
nlines = int(input())

rule_map = {x:x for x in string.ascii_uppercase}
rule_map["_"] = "_"
reverse_rule_map = copy.copy(rule_map)

for _ in range(nrules):
    x, y = input().split()
    rule_map[x] = y
    reverse_rule_map[y] = x

for _ in range(nlines):
    direction, word = input().split()
    dict = rule_map if direction == "E" else reverse_rule_map
    new_word = ""
    for c in word:
        new_word += dict[c]
    print(new_word)
