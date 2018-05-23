## Python code's initial writing by Chen Wang, and edited by Joseph T. Yun.

## python SDK
To install, use pip or easy_install:

$ pip install --upgrade watson-developer-cloud
or

$ easy_install --upgrade watson-developer-cloud

## First, register to IBM Bluemix
https://console.ng.bluemix.net/dashboard/apps/

To create an instance of the service:

Log in to Bluemix.
Create an instance of the service:
In the Bluemix Catalog, select the Watson service you want to use. For example, select the Conversation service.
Type a unique name for the service instance in the Service name field. For example, type my-service-name. Leave the default values for the other options.
Click Create.
To get your service credentials:

Copy your credentials from the Service details page. To find the the Service details page for an existing service, navigate to your Bluemix dashboard and click the service name.

On the Service Details page, click Service Credentials, and then View credentials.
Copy username and password.

# fill in your credentials in config.py file

# change directories and input filename in main.py
1. ".txt" file is corresponding to the function profile_plain
2. ".json" file is corresponding to the function profile_json. (Please make sure your .json file is in correct format!)
3. the number of word must be larger than 100!

# Run "python main.py", results will be saved in the folder you specified.
if you want to see process in the console, uncomment the "print" in the "personality_insights.py" file
