
"""
 Copyright 2019 Pablo Sanderson Ramos


"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '567%&/(HUJNIJ8gjdb3t)&/;:_47r'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    ARTICLES_PER_PAGE = 30


    #delete
    HOURS_IN_BOARD = 18
    TFIDF_UPDATE_HOURS = 2
    MINIMUM_WORDS_PER_ARTICLE = 100
    MAXIMUM_WORD_LENGTH = 20
    TOP_WORDS_NUMBER = 5
    NEWSPAPERS = ['https://www.canarias7.es/', 'https://www.laprovincia.es/','https://www.eldia.es/',\
    'http://www.canarias24horas.com/','http://tribunadecanarias.es/',\
    'https://canariasnoticias.es/']

    #make sure both equal 1
    VALUE_NLP = 0.7
    VALUE_VOTES = 0.3

    JOB_TIMEOUT = 60*180
    SLEEP_TIME = 60*120