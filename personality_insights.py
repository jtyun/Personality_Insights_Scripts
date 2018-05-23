import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
import config

# authorize
personality_insights = PersonalityInsightsV3(
    version = config.version,
    username = config.username,
    password = config.password
    )

# json input with detailed json output (.json)
def profile_json(open_path,filename,save_path):
    with open(open_path + filename) as profile_json:

        profile = personality_insights.profile(
            profile_json.read(),
            content_type='application/json',
            accept = 'application/json',
            raw_scores=True,
            consumption_preferences=True)
        #print(json.dumps(profile, indent=2))
        with open(save_path + 'result-' + filename, 'w') as outfile:
            json.dump(profile,outfile)
            


        
# plain text input with json output (.txt)
def profile_plain(open_path, filename, save_path):
    with open(open_path + filename) as personality_text:
        profile = personality_insights.profile(
            text=personality_text.read().encode('utf-8','ignore'),
            raw_scores=True,
            consumption_preferences=True)
        
        #print(json.dumps(profile, indent = 2))
        with open(save_path + 'result-' + filename[:-4] + '.json', 'w') as outfile:
            json.dump(profile,outfile)
    

        
