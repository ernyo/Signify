import requests
from bs4 import BeautifulSoup

# Replace 'url' with the actual URL of the webpage
url = 'https://www.signasl.org/sign/hello'

# Send an HTTP request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find the video element (replace 'video' with the appropriate tag)
video_element = soup.findAll('video')


for video in video_element:
    video_url = video.find('source')['src']
    print(video_url)

