'''
Write a Python program to find the list of words that are longer than n from a given list of words.
'''

def longest_word(num, string):
    new_string = list()
    string = string.split(" ")
    for i in string:
        if len(i) > int(num):
            new_string.append(i)


    print ("Words, which are longer than", num, 'characters:')
    print (new_string)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed feugiat libero sollicitudin urna ullamcorper " \
       "vestibulum. Maecenas iaculis justo velit, eget sodales odio aliquet a. Mauris aliquam, diam ac iaculis varius, " \
       "augue quam pretium dolor, et ullamcorper justo risus ac lorem. Proin ultrices mi felis, et vehicula risus " \
       "lacinia ut. Nam bibendum, nunc sed euismod elementum, erat leo fermentum urna, id rhoncus dui lectus " \
       "at lectus. Sed dapibus tempor magna nec egestas. Ut tristique sodales molestie. Ut vitae pharetra diam. " \
       "Vivamus malesuada elit nisi, non posuere ipsum egestas at. Duis aliquam magna ut bibendum ornare. Mauris " \
       "pellentesque ex justo, eget congue ligula pulvinar quis. Aenean molestie tempus vulputate. Praesent sit " \
       "amet dignissim nulla. Maecenas et odio vestibulum, ultrices risus ac, convallis nulla."
longest_word(10, text)