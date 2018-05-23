import personality_insights as PI

if __name__ == "__main__":

    # input .json file
    PI.profile_json(
        open_path = 'C:\\scripts\\IBM-personality\\',           #change to your own path
        filename  = 'profile.json',                             #change to your own filename
        save_path = 'C:\\scripts\\IBM-personality\\result\\',   #change to your own save directory
        )

    # input .txt file
    PI.profile_plain(
        open_path = 'C:\\scripts\\IBM-personality\\',           #change to your own path
        filename  = 'president-trump-tweets.txt',               #change to your own filename
        save_path = 'C:\\scripts\\IBM-personality\\result\\'    #change to your own save directory
        )
