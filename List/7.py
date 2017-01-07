'''
Write a Python program to remove duplicates from a list.
'''

lst = ['hi', 'hello', 2, 3, 5, 2, 5, 'hi']
st = set()
for i in lst:
    st.add(i)
print (st)