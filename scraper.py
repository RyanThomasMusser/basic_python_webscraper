import urllib.parse
import urllib.request
import re

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

print('Welcome to my python barebones webscraper.')
print('\n')
print('\n')
print('This script will return the title of the page specified by a URL of your choice.')
print('\n')
print('\n')
url = input('Enter a URL: ')

f = urllib.request.urlopen(url)

g = (f.read())

h = g.decode('utf-8')

start = "<title>"
end = "</title>"

title = re.search('%s(.*)%s' % (start, end), h).group(1)

print('\n')
print('\n')

print(title)

print('\n')
print('\n')


'''
#the below content is a template to return specific body content from the page

start2 = ""
end2 = ""
#the start and end of the body content is relative to each website

i = h.find(start2)
#search for the start

if i:
    print('yes')
#if we find a match, print yes

j = h.find(end2)
#search for the end

if j:
    print('yes')
#if we find a match, print yes

body = re.search('%s(.*)%s' % (start2, end2), h).group()
#find the body content between the specified start and the end

print(body)

'''

