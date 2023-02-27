from urllib.request import urlopen, Request


def download_and_save(url, file_name):
    req = Request(url, method='GET')
    with urlopen(req) as r:
        with open(file_name, 'wb') as f:
            f.write(r.read())
