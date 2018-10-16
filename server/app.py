# coding: utf8
from __future__ import unicode_literals

import hug
import spacy
import json
from hug_middleware_cors import CORSMiddleware
from tinydb import TinyDB, Query
from fuzzywuzzy import process, fuzz
db = TinyDB('./lessons.json')
STOP_WORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']


MODELS = {
    # 'en_core_web_sm': spacy.load('en_core_web_sm'),
    'en': spacy.load('en_core_web_sm'),
}


def get_model_desc(nlp, model_name):
    """Get human-readable model name, language name and version."""
    lang_cls = spacy.util.get_lang_class(nlp.lang)
    lang_name = lang_cls.__name__
    model_version = nlp.meta['version']
    return '{} - {} (v{})'.format(lang_name, model_name, model_version)


@hug.get('/models')
def models():
    return {name: get_model_desc(nlp, name) for name, nlp in MODELS.items()}


@hug.post('/report')
def report_upload(title: str, description: str, construction_technology: str, project_type: str, experience_type: str, 
                  importance: int = 2, country: str = 'US'):
    lesson = {
        'country': country,
        'title': title,
        'description': description,
        'project_type': project_type,
        'construction_technology': construction_technology,
        'importance': importance,
        'description': description,
    }
    db.insert(lesson)
    return lesson

def score_lesson(keywords, lesson):
    x = "%s %s %s %s" % (lesson['title'], lesson['description'], lesson['project_type'], lesson['construction_technology'])
    tokens = list(filter(lambda x: x not in STOP_WORDS, set(x.lower().strip('.').split())))
    x = ' '.join(tokens)
    # print(keywords, x)
    lesson['score'] = fuzz.token_set_ratio(keywords, x)
    # lesson['score'] = fuzz.partial_ratio(keywords, x)
    return lesson

@hug.post('/search')
def search(keywords: str = 'building'):
    keywords = keywords.lower()
    # print('keywords', keywords)
    lessons = db.all()
    scored_lessons = map(lambda lesson: score_lesson(keywords, lesson), lessons)
    results = sorted(scored_lessons, key=lambda x: x['score'], reverse=True)
    # results = process.extract(keywords, lessons, limit=20)
    # lessons = list(map(lambda x: x['lesson'], db.all()))
    # print('results', results)
    return {'data': results, 'keywords': keywords}


@hug.post('/dep')
def dep(text: str = "Hello World.", model: str = "en", collapse_punctuation: bool=False,
        collapse_phrases: bool=False):
    """Get dependencies for displaCy visualizer."""
    # print(text, model)
    nlp = MODELS[model]
    doc = nlp(text)
    if collapse_phrases:
        for np in list(doc.noun_chunks):
            np.merge(tag=np.root.tag_, lemma=np.root.lemma_,
                     ent_type=np.root.ent_type_)
    options = {'collapse_punct': collapse_punctuation}
    return spacy.displacy.parse_deps(doc, options)


@hug.post('/ent')
def ent(text: str, model: str):
    """Get entities for displaCy ENT visualizer."""
    nlp = MODELS[model]
    doc = nlp(text)
    return [{'start': ent.start_char, 'end': ent.end_char, 'label': ent.label_}
            for ent in doc.ents]


if __name__ == '__main__':
    import waitress
    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))
    waitress.serve(__hug_wsgi__, port=8080)
