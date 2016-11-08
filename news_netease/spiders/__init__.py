# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

xpaths_p = ['div[@class="ns-wnews mb20"]',
            'div[@class="ns-wnews mb30"]',
            'div[@class="ns-wnews mb30"]',
            'div[@class="ns-wnews mb40"]',
            'div[@class="ns-wnews mb40"]',
            'div[@class="ns-wnews ns-recommand"]',
            'div[@class="ns-wnews ns-recommand"]',
            'div[@class="ns-wnews mb40 line"]',
            'div[@class="ns-wnews mb40 line"]',
            'div[@class="ns-wnews mb30 line"]',
            'div[@class="ns-wnews mb30 line"]',
            ]

xpaths_tl = ['h3/a',
             'h4/a',
             'ul/li/a',
             'h4/a',
             'ul/li/a',
             'h4/a',
             'ul/li/a',
             'h4/a',
             'ul/li/a',
             'h4/a',
             'ul/li/a',
             ]


# xpath_p parent xpath
# xpath_tl xpath of title and link
def parse_parent_xpath(response, xpath_p, xpath_tl):
    sel = response.xpath('//' + xpath_p)
    l = {'title': [],
         'link': []}
    for a_sel in sel:
        title = a_sel.xpath('.//' + xpath_tl + '/text()').extract()
        link = a_sel.xpath('.//' + xpath_tl + '/@href').extract()
        l['title'].append(title)
        l['link'].append(link)
    return l


def parse_parent_xpaths(response, xpaths_p, xpaths_tl):
    l_ = []
    for _iter in range(0, len(xpaths_p)):
        item_i = parse_parent_xpath(response, xpaths_p[_iter], xpaths_tl[_iter])
        l_.append(item_i)
    return l_
