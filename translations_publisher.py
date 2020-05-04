#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Changes the description, promo text and title of an app in en-US and en-GB.
"""

import argparse
import json
from apiclient import sample_tools
from oauth2client import client
import os_tools.file_handler as fh

TRACK = 'production'  # Can be 'alpha', beta', 'production' or 'rollout'

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('package_name',
                       help='The package name. Example: com.android.sample')
argparser.add_argument('languages_array',
                       help='nope')


def update_app_translations(package_name, json_path):
    # Authenticate and construct service.
    json_dict = fh.json_file_to_dict(json_path)
    json_str = json.dumps(json_dict)
    argv = ["", package_name, json_str]
    service, flags = sample_tools.init(
        argv,
        'androidpublisher',
        'v3',
        __doc__,
        __file__, parents=[argparser],
        scope='https://www.googleapis.com/auth/androidpublisher')

    # Process flags and read their values.
    package_name = flags.package_name
    languages_array = json.loads(flags.languages_array)

    try:
        edit_request = service.edits().insert(body={}, packageName=package_name)
        result = edit_request.execute()
        edit_id = result['id']

        # counter = 0
        for i in range(0, len(languages_array)):
            language_json = languages_array[i]

            if 'updated' in language_json and language_json['updated'] is True:
                continue

            # strip props
            lang = language_json["lang"]
            full_desc = language_json["fullDescription"]
            short_desc = language_json["shortDescription"]
            title = language_json["title"]

            if 'iconPath' in language_json:
                icon_path = language_json["iconPath"]
                service.edits().images().upload(
                    editId=edit_id,
                    language=lang,
                    imageType='icon',
                    packageName=package_name,
                    media_body=icon_path
                ).execute()
                print('Listing ICON for language %s was updated.'
                      % lang)

            else:
                try:
                    service.edits().listings().update(
                        editId=edit_id, packageName=package_name, language=lang,
                        body={'fullDescription': full_desc,
                              'shortDescription': short_desc,
                              'title': title}).execute()

                except RuntimeError as error:
                    print(error)
            print('Listing DESCRIPTION for language %s was updated.'
                  % lang)
            languages_array[i]["updated"] = True
            fh.dict_to_json_file(json_path, languages_array)

        try:
            service.edits().commit(editId=edit_id, packageName=package_name).execute()

            # update the json file

        except RuntimeError as error:
            print(error)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')

# if __name__ == '__main__':
#     main(sys.argv)
