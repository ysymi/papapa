import grequests
from bs4 import BeautifulSoup, Tag

def find_image(html):
    result = []
    try:
        soup = BeautifulSoup(html, 'html.parser')
        content_div = soup.find_all('div', class_='article_content')
        p_list = content_div[0].find_all('p')[-4::2]
        for p in p_list:
            span = p.contents[0]
            if len(span.contents) == 1:
                img = span.contents[0]
                if type(img) == Tag and img.name == 'img':
                    src = 'http:' + img['jason']
                    next_p = p.next_sibling
                    next_span = next_p.contents[0]
                    author = next_span.text.replace('Via ', '')
                    if 0 < len(author) < 30:
                        result.append(src)
        return result if len(result) == 2 else []
    except Exception:
        return []


def find_fuli(group):
    base_url = 'http://qt.qq.com/php_cgi/news/php/varcache_article.php'
    id_range = group * 1000, (group + 1) * 1000
    urls = (base_url + '?id=' + str(page_id) for page_id in range(*id_range))
    reqs = (grequests.get(url, timeout=1) for url in urls)
    print('trying group ' + str(group))
    with open('urls', 'a', 1) as f:
        for resp in grequests.imap(reqs, size=30):
            result = find_image(resp.text)
            for url in result:
                f.write('%s\n' % url)


if __name__ == '__main__':
    for i in range(50):
        find_fuli(i)

