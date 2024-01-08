import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('td.title > span.titleline')
subtext = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('td.title > span.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2
def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse= True)

def create_custom_hn(links, subtext): 
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].a.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))