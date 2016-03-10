import requests

def email_result(name, email, theatre, gif):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxea85cf3d04a940f3937a79171ea4369c.mailgun.org/messages",
        auth=("api", "key-67a11246702a13e45a7feb14303b35ce"),
        data={"from": "Theatre Hack <shlee9817@gmail.com>",
              "to": email,
              "cc": "yellowfavour@gmail.com",
              "subject": "Your Recommendations",
              "html": "<html>Hello {},Your Recommended theatre is {} <img src={}></html>".format(name, theatre, gif)})

email_result("uri", "shlee9817@gmail.com", "old vic", "lol")    