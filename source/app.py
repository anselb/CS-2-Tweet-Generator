import sample
import histogram
from markov import nth_markov_dictograms, nth_markov_chain

from flask import Flask
app = Flask(__name__)

with open('../scraper/corpus.txt', 'r') as myfile:
    elon_corpus = myfile.read().replace('\n', '')

@app.route('/')
def return_sentence():
    elon_markov_dict = nth_markov_dictograms(elon_corpus, 2)
    return nth_markov_chain(elon_markov_dict)

    # histo = histogram.histogram_dictionary('fish.txt')
    # return sample.weighted_dict_sampling(histo)
