import os 
from platform import system
platformD = system()
if platformD == 'Windows':
    os.system('pip install instaloader')
else:
    os.system('pip3 install instaloader')

import instaloader

import json
import requests
from pathlib import Path
import time


insta = instaloader.Instaloader(
        download_pictures=True,
        download_videos=True,
        filename_pattern="post",
        download_video_thumbnails=True,
        compress_json=False,
        download_geotags=False,
        post_metadata_txt_pattern=None,
        max_connection_attempts=0,
        download_comments=False,
        )




instagram = input('insert your instagram account (no need for @): ')

profile = instaloader.Profile.from_username(insta.context, instagram)
posts = profile.get_posts()
answer = input('Is you profile public? (Y/N): ')

if answer == "Y": 
    print('ok, dude')
else: 
    insta.interactive_login(profile.username)

print("Username: " + profile.username)
print("Post Count: " + str(profile.mediacount))
print("IGTV Count: " + str(profile.igtvcount))
print("Followers: " + str(profile.followers))
print("Bio: " + profile.biography) 



channel_id =input('Please insert the Claim Id of the desired LBRY channel: ')
bid = input('insert the desired BID value for each post: ')

for index, post in enumerate(posts, 1):
    

    insta.download_post(post, target=f"{profile.username}_{index}") 
    name = f"{profile.username}_{index}"
    title = "recovered_memories" +"_" +str(index)
    path = os.getcwd()
    folder = str(os.path.join(path +"/"f"{profile.username}_{index}"))
    my_file = folder+ '/post.txt'
    my_thumb = folder + '/post.json'
    if os.path.isfile(my_thumb):
        os.chdir(folder)
        f = open('post.json',)
        data = json.load(f) 
        global thumbnail_url
        thumbnail_url = data['node']['display_url']
        
        os.chdir(path)
    if os.path.isfile(my_file): 
        os.chdir(folder)
         
        with open('post.txt', 'r', encoding='utf-8') as file:
            global description 
            description = file.read()
        
        print("\n"+ description)
        os.chdir(path)
    else : 
        description ="# Don't Be Evil"
        print(description)
    if post.is_video: 
        try:
            filepath = os.path.join(path +"/"f"{profile.username}_{index}"+"/" + f'post.mp4')
        except:
            for x in range(1,10):
                filepath = os.path.join(path +"/"f"{profile.username}_{index}"+"/" + f'post_{x}.mp4')
                return_stream_create = requests.post("http://localhost:5279",
                     json={"method": "stream_create",
                          "params": {"name": name,
                                     "title": title,
                                     "bid": bid,
                                     "file_path": filepath,
                                     "description": description,
                                     "validate_file": False, 
                                     "optimize_file": True, 
                                     "tags": [],
                                     "languages": [], 
                                     "locations": [],
                                     "channel_id": channel_id,
                                     "channel_account_id": "",
                                     "funding_account_ids": [],
                                     "preview": False,
                                     "thumbnail_url": thumbnail_url,
                                     "blocking": False}}).json()
                print(return_stream_create)  
    
                time.sleep(10)  

    else: 
        try:
            filepath = os.path.join(path +"/"f"{profile.username}_{index}"+"/" + f'post.jpg')
        except:
            for x in range(1,10):
                filepath = os.path.join(path +"/"f"{profile.username}_{index}"+"/" + f'post_{x}.jpg')
                return_stream_create = requests.post("http://localhost:5279",
                     json={"method": "stream_create",
                          "params": {"name": name,
                                     "title": title,
                                     "bid": bid,
                                     "file_path": filepath,
                                     "description": description,
                                     "validate_file": False, 
                                     "optimize_file": True, 
                                     "tags": [],
                                     "languages": [], 
                                     "locations": [],
                                     "channel_id": channel_id,
                                     "channel_account_id": "",
                                     "funding_account_ids": [],
                                     "preview": False,
                                     "thumbnail_url": thumbnail_url,
                                     "blocking": False}}).json()
                print(return_stream_create)  
    
                time.sleep(10)  


    
    return_stream_create = requests.post("http://localhost:5279",
                     json={"method": "stream_create",
                          "params": {"name": name,
                                     "title": title,
                                     "bid": bid,
                                     "file_path": filepath,
                                     "description": description,
                                     "validate_file": False, 
                                     "optimize_file": True, 
                                     "tags": [],
                                     "languages": [], 
                                     "locations": [],
                                     "channel_id": channel_id,
                                     "channel_account_id": "",
                                     "funding_account_ids": [],
                                     "preview": False,
                                     "thumbnail_url": thumbnail_url,
                                     "blocking": False}}).json()
    print(return_stream_create)  
    
    time.sleep(10)  

