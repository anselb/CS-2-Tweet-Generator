import sample
import histogram
from markov import nth_markov_dictograms, nth_markov_chain

from flask import Flask
from flask import render_template
app = Flask(__name__)

# Code to make viewing changes easier (avoids caching)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

with open('../scraper/corpus.txt', 'r') as myfile:
    elon_corpus = myfile.read().replace('\n', '')

@app.route('/')
def return_sentence():
    elon_markov_dict = nth_markov_dictograms(elon_corpus, 2)
    sentence = nth_markov_chain(elon_markov_dict)
    return render_template('index.html', message=sentence)

    # histo = histogram.histogram_dictionary('fish.txt')
    # return sample.weighted_dict_sampling(histo)
