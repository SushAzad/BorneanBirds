# file download script by Khalsa Labs
# MP3 file download

import urllib.request
import sys

mp3_link = input('Enter the link for mp3 file e.g: http://abc.com/fil1.mp3: ')

try:
    urllib.request.urlretrieve(mp3_link, "bird1.mp3")
except Exception as e:
    print(e)
    sys.exit()
    
ext = mp3_link.split('.')[-1]
if not ext in ['mp3','Mp3','MP3']:
    print ('The file in internet link is not an mp3 file..')
    print ('Downloading on your own risk...')

# mp3_link = mp3_link.strip('/')
# name = "bird1.mp3"

# mp3_file = open(name, 'w+')
# mp3_file.write(sound)
# mp3_file.close()