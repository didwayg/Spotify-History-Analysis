import pandas as pd
import os


# List my JSON file paths
json_files = ['Streaming_History_Audio_2016-2018_0.json', 'Streaming_History_Audio_2018-2019_1.json', 'Streaming_History_Audio_2019-2020_2.json',
              'Streaming_History_Audio_2020-2021_3.json', 'Streaming_History_Audio_2022_5.json', 'Streaming_History_Audio_2022-2023_6.json']

# List to hold DataFrames
dfs = []

# Loop through JSON files and read each one into a DataFrame
for file in json_files:
    print(file)
    df = pd.read_json(os.path.join('MyData 6',file))
    dfs.append(df)

# Concatenate all DataFrames into one
stream = pd.concat(dfs, ignore_index=True)



stream['mins_played'] = (stream['ms_played'])/1000/60
stream.drop(['ms_played','username', 'platform','conn_country','ip_addr_decrypted','user_agent_decrypted','episode_name','episode_show_name','spotify_episode_uri','skipped','offline','offline_timestamp','incognito_mode'], axis=1, inplace=True)
stream.rename(columns={"master_metadata_track_name": "track name", "master_metadata_album_artist_name": "artist name", "master_metadata_album_album_name": "album name", "spotify_track_uri": "uri"}, inplace=True)

stream.to_csv('stream.csv')

