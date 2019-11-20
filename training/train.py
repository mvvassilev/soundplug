# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# from matplotlib import style
# from sklearn import datasets, linear_model
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.manifold import TSNE
import pandas as pd
import sys
import numpy as np
from sklearn.cluster import KMeans
import pickle
from scipy.spatial import distance
from math import sqrt


#gets the list of songs for a search
def get_list(sp, songs_list):
    results = []

    # pickle_in = open('knear.pickle', 'rb')
    # clf = pickle.load(pickle_in)


    for result in np.array(songs_list[:20]):
        song_name = result[0]
        song_artist = result[1]
        song_image = '../../static/record.png'

        results.append((
            song_name,
            song_artist,
            song_image
            )
        )

    return results

# returns the distance between two 10-dimenstional arrays
def get_distance(a, b, dimensions=2):
    sum = 0
    for i in range(dimensions):
        sum += (a[i] - b[i])**2

    return sqrt(sum)


# custom knn algorithm which returns the closest k=20 entities
# returns the indexes of the 20 nearest_rows in the data frame 
def k_nearest_neighbors(search_title, k=20):
    
    #loading the data
    data_frame = pd.read_csv("songs_data.csv", encoding = "ISO-8859-1")
    data_frame.fillna(0, inplace=True)
    # print(data_frame)

    y = np.array(data_frame[['song_title', 'artist']])

    data_frame.drop(['song_title', 'artist'], 1, inplace=True)
    X = np.array(data_frame, dtype=np.float64)
    
    # find the row in y that matches the search and then use the index
    # as the index for X to get the predict value to be the corresponding
    # values in X for the search 
    temp = np.where(y == search_title)
    try:
        predict = X[temp[0]][0]
    except IndexError:
        return 'Song does not exist'
    # print(f'PREDICT STARTS______ {predict}_____PREDICT ENDS')

    distances = []
    # print(predict)

    for row in range(X.shape[0]):
        ed = get_distance(X[row], predict)
        if ed == 0:
            pass
        else:
            distances.append([ed, row])

    distances.sort()
    recom_songs_list = []


    for i in range(k):
        recom_songs_list.append((
            y[distances[i][1]][0], 
            y[distances[i][1]][1]
            )
        )

    return recom_songs_list



#training the K-Nearest-Neigbors algorithm and saving it to a pickle
# data_frame = pd.read_csv("songs_data.csv")
# data_frame.drop(['artist'], 1, inplace=True)
# data_frame.fillna(0, inplace=True)

# X = np.array(data_frame.drop(['song_title'], 1))
# y = np.array(data_frame['song_title'])

# clf = KMeans(n_clusters=100)
# clf.fit(X, y)

# with open('knear.pickle', 'wb') as f:
#     pickle.dump(clf, f)

def get_y_col():
    data_frame = pd.read_csv("songs_data.csv")
    data_frame.fillna(0, inplace=True)

    y = np.array(data_frame[['song_title', 'artist']])

    return y

print(k_nearest_neighbors('Mask Off'))