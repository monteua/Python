'''
Write a Python program to get OS name, platform and release information.
'''
import platform
print "OS name: ", (platform.uname())[0], (platform.uname())[2]
print "Platform: ", (platform.uname())[4]
print "Release information: ", platform.platform()