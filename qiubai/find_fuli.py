import grequests
from bs4 import BeautifulSoup


def find_image(html):
    result = []
    try:
        soup = BeautifulSoup(html, 'html.parser')
        div_list = soup.find_all('div', class_='ui-module')
        for div in div_list:
            img = div.find_all('img')[0]
            if img['alt'] and img['src']:
                result.append(img['alt'] + ' ' + img['src'] + '\n')
        return result
    except Exception:
        return []


def find_fuli():
    url_tpl = 'http://www.qiubaichengren.com/%d.html'
    urls = (url_tpl % pid for pid in range(814))
    reqs = (grequests.get(url, timeout=3) for url in urls)

    with open('urls', 'w', 1) as f:
        for resp in grequests.imap(reqs, size=50):
            resp.encoding = 'gb18030'
            result = find_image(resp.text)
            if result:
                f.writelines(result)


if __name__ == '__main__':
    find_fuli()
