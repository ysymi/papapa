import grequests


def save_fuli(urls):
    with open(urls, 'r') as f:
        urls = f.read().split('\n')
        reqs = (grequests.get(url, timeout=1) for url in urls)

        for resp in grequests.imap(reqs, size=10):
            i = resp.url.rindex('/')
            name = resp.url[i + 1:]
            with open('result/' + name, 'wb') as pic:
                pic.write(resp.content)
            print(name + ' saved')


save_fuli('urls')
