from django.shortcuts import render

import pandas as pd 
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials 
import sys
import numpy as np

from training.train import k_nearest_neighbors, get_y_col
from . import models

# Create your views here.
def home(request):
    # y = get_y_col()
    # for row in range(y.shape[0]):
    #     models.Song.objects.create(song_title=y[row][0], artist=y[row][1])

    songs_list = models.Song.objects.all()
    
    context = {
        'songs_list': songs_list
    }
    return render(request, 'base.html', context)


# TODO: FINISH THE SEARCH FUNCTION
def new_search(request):

    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    CLIENT_ID = 'f0854c094bef4ba2b58edda86fad873a'
    CLIENT_SECRET = 'f319b8e4bb5444eea90151c035531b97'
    # scope = 'user-library-read'
    # username = 'd1rn1sj434k0822tfc19w6s1l'

    # token = util.prompt_for_user_token(username=username, scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://soundplug.herokuapp.com/")

    # client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    #get the results
    search_artist, search_title = search.split('-', 1)
    print(f'Searching for {search_title} by {search_artist} ...')
    
    results = k_nearest_neighbors(search_title=search_title.lstrip())

    context = {
        'search': search,
        'results': results
    }
    return render(request, 'recommender/new_search.html', context)