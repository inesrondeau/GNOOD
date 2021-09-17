import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import numpy as np
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
CLIENT_ID = '112611cf1e204dfd93ac56899676e4ac'
CLIENT_SECRET = 'a2929c0b24f6469085d8f234e90a8515'
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))
spoty_df=pd.read_csv('spoty.csv')
spoty_scaled_df=pd.read_csv('spoty_scaled.csv')
songs_df=pd.read_csv('trending.csv')
X_id=spoty_scaled_df[['title','artist','type','id','uri','track_href','analysis_url']]
X_feat=spoty_scaled_df.drop(['title','artist','type','id','uri','track_href','analysis_url','Unnamed: 0','cluster'],axis=1)
spoty_df0=spoty_df[spoty_df['cluster']==0]
spoty_df1=spoty_df[spoty_df['cluster']==1]
spoty_df2=spoty_df[spoty_df['cluster']==2]
spoty_df3=spoty_df[spoty_df['cluster']==3]
spoty_df4=spoty_df[spoty_df['cluster']==4]
spoty_df5=spoty_df[spoty_df['cluster']==5]
spoty_df6=spoty_df[spoty_df['cluster']==6]
spoty_df7=spoty_df[spoty_df['cluster']==7]
spoty_df8=spoty_df[spoty_df['cluster']==8]
titles= list(songs_df['title'].values)

def track(song):
    if len(sp.search(q=song, type="track", limit=1)['tracks']['items'])>0 :
                         features=sp.audio_features(sp.search(q=song, type="track", limit=1)['tracks']['items'][0]['uri'])
                         song_features_values=[list(features[0].values())]
                         song_features_name=features[0].keys()
                         
                         song= pd.DataFrame(song_features_values,columns=song_features_name)
                         
                         X_idsong=song[['type','id','uri','track_href','analysis_url']]
                         X_featsong=song.drop(['type','id','uri','track_href','analysis_url'],axis=1)
                        
                         X_featsong_scaled = StandardScaler().fit_transform(X_feat)
                         
                         kmeans = KMeans(n_clusters=4,
                                n_init=4, 
                                random_state=42)
                          
                         kmeans.fit(X_feat)
                         
                         pred=kmeans.predict(X_featsong_scaled)
                         
                         return list(pred)[0]   
    else:
                         return 9
while True:
    song=input('Song i like: ')
    if song in titles:
        titles.remove(song)
        selected=random.choice(titles)
        art=songs_df[songs_df['title']==selected]['artist']
        print(selected,art)
    else:
        if track(song)==0:
            selected0= random.choice(list(spoty_df0['title']))
            art0=spoty_df0[spoty_df0['title']==selected0]['artist']
            print(selected0,art0)
            break
        elif track(song)==1:
            selected1= random.choice(list(spoty_df1['title']))
            art1=spoty_df1[spoty_df1['title']==selected1]['artist']
            print(selected1,art1)
            break
        elif track(song)==2:
            selected2= random.choice(list(spoty_df2['title']))
            art2=spoty_df2[spoty_df2['title']==selected2]['artist']
            print(selected2,art2)
            break
        elif track(song)==3:
            selected3= random.choice(list(spoty_df3['title']))
            art3=spoty_df3[spoty_df3['title']==selected3]['artist']
            print(selected3,art3)
            break
        elif track(song)==4:
            selected4= random.choice(list(spoty_df4['title']))
            art4=spoty_df4[spoty_df4['title']==selected4]['artist']
            print(selected4,art4)
            break
        elif track(song)==5:
            selected5= random.choice(list(spoty_df5['title']))
            art5=spoty_df5[spoty_df5['title']==selected5]['artist']
            print(selected5,art5)
            break
        elif track(song)==6:
            selected6= random.choice(list(spoty_df6['title']))
            art6=spoty_df6[spoty_df6['title']==selected6]['artist']
            print(selected6,art6)
            break
        elif track(song)==7:
            selected7= random.choice(list(spoty_df7['title']))
            art7=spoty_df6[spoty_df7['title']==selected7]['artist']
            print(selected7,art7)
            break
        elif track(song)==8:
            selected8= random.choice(list(spoty_df8['title']))
            art8=spoty_df8[spoty_df8['title']==selected8]['artist']
            print(selected8,art8)
            break
        elif track(song)==9:
            print('try another one')
