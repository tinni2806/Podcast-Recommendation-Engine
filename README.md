## **Podcast Popularity based recommendation system**

As the name suggests the recommendation system works with the trend and recommend radio shows and podcasts to listen to. It basically uses the items which are in trend right now. For example, if any product which is usually bought by every new user then there are chances that it may suggest that item to the user who just signed up.

There are some problems as well with the popularity based recommender system and it also solves some of the problems with it as well.

The problems with popularity based recommendation system is that the personalization is not available with this method i.e. even though you know the behaviour of the user you cannot recommend items accordingly.


## **Getting Started**

Python Packages: 
 - numpy
 - pandas
 - [Recommender](https://github.com/tinni2806/Podcast-Recommendation-Engine/blob/master/Populatrity_Recommender.py), includes the methods which will basically create the recommendations and the recommend which recommends the items to the user.

Dataset:

- [song.csv](https://github.com/tinni2806/Podcast-Recommendation-Engine/blob/master/songs.csv)

In this section we import our dataset as a triplets_file and songs_metadata_file. 
- The triplet_file contains user_id, song_id and listen_count. 
- The songs_metadata_file contains song_id, title, release_by and artist_name.

We will merge both the dataset by droping the dupliactes song_id.

    song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
    
Because it is a large dataset I have only considered first 10k rows.

After changing the length of dataset I have done some additional modification in which I included the one column named song and which concatenates the title and the artist of the song.

I have grouped the dataset using the pandas function *groupby* by song field and aggregated with the listen_count field and after that the values are sorted in non increasing order according to the listen_count.

After finding out the unique users and items in the dataset, I have split the dataset into training and the test dataset using 80–20 ratio.

    from sklearn.cross_validation import train_test_split
    train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
  
The Recommender() function create takes the three parameters the training data, user id for which the recommendation is created and the column of the item for which you want to make recommendation in our case it is song.  
    
    pr = Popularity_Recommender.Recommender()
    pr.create(train_data, 'user_id', 'song')

As I said before that the method recommend gives the recommendation to the user which is passed as a parameter. So, it returns the list of the popular songs for the user but since it is popularity based recommendation system the recommendation for the users will not be affected.

Result of the recommendation system for 6th user

    pr.recommend(users[5])
    
![](https://github.com/tinni2806/Podcast-Recommendation-Engine/blob/master/Snapshots/Capture1.jpg)


Result of the recommendation system for 99th user

    pr.recommend(users[100])

![](https://github.com/tinni2806/Podcast-Recommendation-Engine/blob/master/Snapshots/Capture1.jpg)

So, as you can see here that although if we change the user the result that we get from the system is the same since it is a popularity based recommendation system.


    

