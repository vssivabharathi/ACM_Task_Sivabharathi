# Build an Unsupervised Learning Model on a Spotify Most Streamed Song

dataset used; Spotify Most Streamed song

### here we are clustering;
We are clustering songs based on their musical attributes, such as:

1. ```Danceability:``` How suitable the track is for dancing, measured in percentage.
2. ```Energy:``` The intensity and activity level of the song.
3. ```Valence:``` A measure of the musical "positiveness."
4. ```Acousticness:``` Likelihood that the track is acoustic.
5. ```Instrumentalness:``` Whether a song contains vocals or is purely instrumental.
6. ```Liveness:``` The probability that a song was recorded live.
7. ```Speechiness:``` How much spoken word is in the track.
8. ```Beats per minute (BPM):``` The tempo of the track.
9. ```Artist Count:``` The number of artists on the track.



### things that we did with the dataset
1. removed the     'track_name', 'artist(s)_name', 'streams', 'cover_url', 
    'key', 'mode', 'released_year', 'released_month', 'released_day', 
    'in_spotify_playlists', 'in_spotify_charts', 'in_apple_playlists', 'in_apple_charts', 
    'in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts'
2. filling NaN where data not present
3. 

### Reference material that i used
https://github.com/codebasics/py/tree/master/ML/13_kmeans