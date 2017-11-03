import sample
import histogram

from flask import Flask
app = Flask(__name__)


@app.route('/')
def return_word():
    histo = histogram.histogram_dictionary('fish.txt')
    return sample.weighted_dict_sampling(histo)
