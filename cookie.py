import requests

url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1681938255?ModuleName=reg%2Fadd%2Fbrowse_schedule.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&ViewSem=Summer+1+2023&KeySem=20241&AddPlannerInd=&College=CAS&Dept=cs&Course=112&Section='

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'f5_cspm=1234;............................................',
    'Host': 'www.bu.edu',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response.content)
