#!/usr/bin/env python

from splitwise import Splitwise

def handler(event, context):
    sw = Splitwise("sZtguyLTZgBvycBeLkUE8TyYAEDNfUgYwpAp5bTM", "zmeUMAm7ZNx4raAgpQvwf6bYdeI3et4XFqYoOMMb")
    sw.setDebug(True)
    url, secret = sw.getAuthorizeURL()
    print url
    print secret
    access_token = sw.getAccessToken(oauth_token,secret,oauth_verifier)

if __name__ == "__main__":
    handler(None, None)
