'''
Automate Notion using Python
Author: Ayushi Rawat
'''

#import the necessary module!
from notion.client import NotionClient

#fetch the token_v2
token = 'your token goes here'

client = NotionClient(token_v2=token)

#fetch the tracker URL
list_url = 'the tracker url goes here'

collection_view = client.get_collection_view(list_url)             

#add new role
new_row = collection_view.collection.add_row()

#populate the data
new_row.running = True
new_row.Journaling = True

new_row.screen_time_minutes = 30

print('New Row has been successfully created!)
