Introduction
------------

This script will release a pre made JSON file, which holds all of the languages you want to add to a specific app in the Google Play.

To create a translated JSON file for your app use [os_android_google_play_translations_maker-py](https://github.com/osfunapps/os_android_google_play_translations_maker-py). 

Notice: this library is using [Google Edits](https://developers.google.com/android-publisher/edits), an open api for the Google Play Developer. 
Google's sample codes for [Python](https://github.com/googlesamples/android-play-publisher-api/tree/master/v3/python) and Java seems 
old and deprecated so they may not work. This is why this repo is handy (it's updated up to version 3 of Edits).


## Installation
- Copy the [translations_publisher.py](translations_publisher.py) and [client_secrets.json](client_secrets.json) to your computer (make sure you copy them to the same directory).
- Open the Google Play API for your account: go to Google Play Console and on the left menu, open Setting -> API Access (it may have changed by now) and create a new OAuth Client.  
- Copy the Client ID you obtained from the OAuth Client to your [client_secrets.json](client_secrets.json) file.
- Sign in to your [Google Developer Console](https://console.developers.google.com/) account and open your project (it usually is 'Google Play Android Developer') and in the credentials, click on the OAuth 2.0 Client ID. Copy the Client Secret from there to "client_secret" in [client_secrets.json](client_secrets.json)  

That's it. Now you are ready to use this repo.


## Usage

After you made sure that the [translations_publisher.py](translations_publisher.py) and [client_secrets.json](client_secrets.json) are both on your project, and [client_secrets.json](client_secrets.json) has client_id and client_secret filled, create a new Python file (in the same project) and:        
    
    import translations_publisher as tp
    tp.update_app_translations(package_name="com.osapps.myCoolPackageName", json_path='path/to/json/file.json')


# Links
[os_android_google_play_translations_maker-py](https://github.com/osfunapps/os_android_google_play_translations_maker-py)

## Licence
MIT