#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript", "Perl", "99"}
set_2 = { "Bash", "C", "Ruby", "Perl", "99"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
