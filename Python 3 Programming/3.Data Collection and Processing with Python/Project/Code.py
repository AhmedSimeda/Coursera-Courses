#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests_with_caching
import json

def get_movies_from_tastedive(name):
    base_url = "https://tastedive.com/api/similar"
    params   = {}
    params['q'] = name
    params['type'] = "movies"
    params['limit'] = 5
    result = requests_with_caching.get(base_url,params=params)
    results = result.json()
    return results

def extract_movie_titles(results):
    return [d['Name'] for d in results['Similar']['Results']]

def get_movie_data(movie_title):
    base_url = "http://www.omdbapi.com/"
    params   = {}
    params['t'] = movie_title
    params['r'] = 'json'
    result = requests_with_caching.get(base_url,params=params)
    results = result.json()
    return results

def get_movie_rating(results):
    ratings = results['Ratings']
    for d in ratings:
        if d['Source'] == 'Rotten Tomatoes':
            return int(d['Value'].replace('%',''))
    return 0

def get_sorted_recommendations(movie_titles):
    sorted_recommendations = []
    for title in movie_titles:
        related_titles = extract_movie_titles(get_movies_from_tastedive(title))
        sorted_recommendations += related_titles
    sorted_recommendations = sorted(sorted_recommendations, reverse=True, key=lambda x:(get_movie_rating(get_movie_data(x)),x[0]))
    
    return sorted_recommendations

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

