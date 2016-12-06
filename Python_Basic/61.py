'''
Write a Python program to find the available built-in modules
'''

import sys
print ','.join(sorted(sys.builtin_module_names))