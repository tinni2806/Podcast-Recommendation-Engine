import pandas
import numpy as np
import Populatrity_Recommender

from sklearn.cross_validation import train_test_split

triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'song_data.csv'

song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

song_df_2 =  pandas.read_csv(songs_metadata_file)
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

song_df = song_df.head(10000)
song_df.head()
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']
song_df['song'].head()

song_df_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
song_df_grouped.sort_values('listen_count',ascending = 0)

users = song_df['user_id'].unique()
len(users)

items = song_df['song'].unique()
len(items)

train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
print(train_data.head(5))

pr = Populatrity_Recommender.Recommender()
pr.create(train_data, 'user_id', 'song')

pr.recommend(users[5])
pr.recommend(users[100])
