import grequests


def parse_result(file):
    with open(file, 'r') as f:
        result = {}
        lines = f.read().split('\n')
        for l in lines:
            i = l.find('http')
            if i > 0:
                filename, url = l[:i - 1], l[i:]
                ext = url[-4:] if url[-4] == '.' else '.gif'
                result[url] = filename + ext
        return result

    return {}


def save_fuli(result):
    result = parse_result(result)
    reqs = (grequests.get(url, timeout=1) for url in result)
    for resp in grequests.imap(reqs, size=20):
        if resp.url in result:
            with open('result/' + result[resp.url], 'wb') as pic:
                pic.write(resp.content)
            print('saved : ' + resp.url)


save_fuli('result')
