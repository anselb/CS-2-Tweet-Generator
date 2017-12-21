from diffbot import DiffbotClient,DiffbotCrawl
from config import API_TOKEN
import pprint
import time
import re

def get_article_text(article_url):
    print("Calling article API endpoint on the url: http://shitelonsays.com/transcript...\n")
    diffbot = DiffbotClient()
    token = API_TOKEN
    url = article_url
    api = "article"
    response = diffbot.request(url, token, api)
    return(response["objects"][0]["text"])
    # print("\nPrinting response:\n")
    # pp = pprint.PrettyPrinter(indent=4)
    # print(pp.pprint(response))

urls_file = open('pages.txt')
output_file = open('corpus.txt', 'w')

total_urls = 0
for line in urls_file:
    total_urls += 1

urls_file = open('pages.txt')

corpus = ''
current_url = 1
for line in urls_file:
    print('Getting text from url ' + str(current_url) + ' out of ' + str(total_urls) + ' urls')
    url = line.strip()
    article = get_article_text(url)
    corpus += article
    current_url += 1

clean_corpus = re.sub(r'\[.*\]\s|\[.*\],|\[.*\]\.', '', corpus)

output_file.write(clean_corpus)
print('Done creating corpus')
