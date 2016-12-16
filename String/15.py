'''
Write a Python function to create the HTML string with tags around the word(s). Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>' add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''

def add_tags(tag, inp):
    return "<"+tag+">"+inp+"</"+tag+">"

print add_tags('i', 'Python')
