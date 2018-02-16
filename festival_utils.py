def check_similarity(preference, artists):
    return list(set(preference) & set(artists))


def trim_url(url):
    if url[len(url) - 5:len(url)] == 'shop/':
        return url[0:len(url) - 10]
    else:
        return url[0:len(url) - 5]
