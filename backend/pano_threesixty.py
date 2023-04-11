import requests
import random

def format(url):
    code = f'''
    <iframe id="onloadframe" width="100%" height="950px" allowFullScreen="true"
        allow="accelerometer; magnetometer; gyroscope"
        style="display:block; margin:0px auto; border:0 none; max-width:100vw; max-height: 100vh;border-radius:8px; box-shadow: 0 1px 1px rgba(0,0,0,0.11),0 2px 2px rgba(0,0,0,0.11),0 4px 4px rgba(0,0,0,0.11),0 6px 8px rgba(0,0,0,0.11),0 8px 16px rgba(0,0,0,0.11);"
        src="{url}">
    </iframe>
    
    '''

    return code


def fetch():


    url = 'https://rajyavardhanbithale.github.io/rajson/panoraj.json'


    resp = requests.get(url=url)
    data = resp.json() 

    ranurl = f"{str(random.randint(0,len(data)-1))}"

    return format(data[ranurl])





