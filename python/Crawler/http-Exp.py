def grab_json(url):
    ret = None
    try:
        result = requests.get(url)
        ret = result.json()
    except:
        print "No result find for url:", url
    return ret
