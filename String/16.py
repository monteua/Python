'''
Write a Python function to insert a string in the middle of a string. Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''

def insert_string_middle(base_string, string):
    length = len(base_string)/2

    return base_string[:length]+string+base_string[length:]


print insert_string_middle('[[]]<<>>', 'Python')
print insert_string_middle('{{}}', 'PHP')