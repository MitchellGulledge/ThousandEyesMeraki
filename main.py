import urllib.parse
import requests, json, time

# Authors: Mitchell Gulledge, Zach Brewer

"""
ThousandEyesApi class.
"""

class ThousandEyesApi:
    """
    ThousandEyesApi class provides methods to interact with the ThousandEyes API
    Attributes
    ----------
    email : str
        ThousandEyes platform user account
    authToken : str
        ThousandEyes platform user API token
    """

    email = ''
    # encoding email so it can be appended to ThousandEyes URL
    encoded_email = urllib.parse.quote(email)

    """
    Auth token obtained from the  Account Settings > Users and Roles page 
    under the “Profile” tab, in the “User API Tokens” section.
    """
    authToken = ''


    api_url = 'https://'+encoded_email+':'+authToken+'@api.thousandeyes.com/v6/'
    api_status_url = api_url + 'status'


print(requests.get(ThousandEyesApi.api_status_url).content)
