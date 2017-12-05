from diffbot import DiffbotClient,DiffbotCrawl
from config import API_TOKEN
import pprint
import time

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

corpus = ''

for line in urls_file:
    url = line.strip()
    article = get_article_text(url)
    corpus += article

output_file.write(corpus)
print('Done creating corpus')
