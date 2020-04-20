from django.shortcuts import render
from newsapi import NewsApiClient
from django.conf import settings
import requests


# Create your views here.

def home(request):

    return render(request, 'news/home.html')

def top_headlines(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    bbc_headlines = newsapi.get_top_headlines(sources='bbc-news')

    l = bbc_headlines['articles']
    url = []
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(url, pub, news, desc, img)

    verge_headlines = newsapi.get_top_headlines(sources='the-verge')

    l = verge_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    vergelist = zip(url, pub, news, desc, img)

    al_jazeera_headlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    l = al_jazeera_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    jazeeralist = zip(url, pub, news, desc, img)

    cnbc_headlines = newsapi.get_top_headlines(sources='cnbc')

    l = cnbc_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cnbclist = zip(url, pub, news, desc, img)

    cnn_headlines = newsapi.get_top_headlines(sources='cnn')

    l = cnn_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cnnlist = zip(url, pub, news, desc, img)
    #print(l)

    crypto_headlines = newsapi.get_top_headlines(sources='crypto-coins-news')

    l = crypto_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cryptolist = zip(url, pub, news, desc, img)

    espn_headlines = newsapi.get_top_headlines(sources='espn')

    l = espn_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    espnlist = zip(url, pub, news, desc, img)

    espn_cric_headlines = newsapi.get_top_headlines(sources='espn-cric-info')

    l = espn_cric_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    espncriclist = zip(url, pub, news, desc, img)

    financial_post_headlines = newsapi.get_top_headlines(sources='financial-post')

    l = financial_post_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    financial_postlist = zip(url, pub, news, desc, img)

    api_key ='c7eb470395e04da68d1a0002d3f4ca8c'

    if request.method == 'POST':
        q = request.POST['search']
        search_url = 'https://newsapi.org/v2/everything?'
        #article_url = 'https://newsapi.org/v2/top-headlines?'

        r = requests.get(search_url + 'q=' + q + '&apiKey=' + api_key)

        results = r.json()
        l = results['articles']
        url =[]
        pub =[]
        desc =[]
        news =[]
        img =[]
    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    search_postlist = zip(url, pub, news, desc, img)

    #print(l)


    context = {
        'mylist': mylist,
        'vergelist': vergelist,
        'jazeeralist': jazeeralist,
        'cnbclist': cnbclist,
        'cnnlist': cnnlist,
        'cryptolist': cryptolist,
        'espnlist': espnlist,
        'espncriclist': espncriclist,
        'financial_postlist': financial_postlist,
        'search_postlist': search_postlist,
    }

    return render(request, 'news/top_headlines.html', context)

def search_news(request):

    api_key ='c7eb470395e04da68d1a0002d3f4ca8c'

    if request.method == 'POST':
        q = request.POST['search']
        search_url = 'https://newsapi.org/v2/everything?'
        #article_url = 'https://newsapi.org/v2/top-headlines?'

        r = requests.get(search_url + 'q=' + q + '&apiKey=' + api_key)

        results = r.json()
        l = results['articles']
        url =[]
        pub =[]
        desc =[]
        news =[]
        img =[]
    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    search_postlist = zip(url, pub, news, desc, img)

    context = {
        'search_postlist': search_postlist
    }

    return render(request, 'news/searched_post.html', context)


def argentina(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ar')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ar', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ar', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ar', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ar', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ar', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ar', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    argentina_tech_list = zip(url, pub, news, desc, img)


    context = {
        'argentina_list': argentina_list,
        'argentina_busi_list': argentina_busi_list,
        'argentina_enter_list': argentina_enter_list,
        'argentina_health_list': argentina_health_list,
        'argentina_sci_list': argentina_sci_list,
        'argentina_sport_list': argentina_sport_list,
        'argentina_tech_list': argentina_tech_list
    }
    #print(l)
    return render(request, 'countries/argentina.html', context)


def australia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='au')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='au', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='au', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='au', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='au', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='au', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='au', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    australia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'australia_list': australia_list,
        'australia_busi_list': australia_busi_list,
        'australia_enter_list': australia_enter_list,
        'australia_health_list': australia_health_list,
        'australia_tech_list': australia_tech_list,
        'australia_sci_list': australia_sci_list,
        'australia_sport_list': australia_sport_list,
        'australia_tech_list': australia_tech_list
    }
    #print(l)
    return render(request, 'countries/australia.html', context)

def austria(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='at')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='at', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='at', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='at', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='at', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='at', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='at', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    austria_tech_list = zip(url, pub, news, desc, img)

    context = {
        'austria_list': austria_list,
        'austria_busi_list': austria_busi_list,
        'austria_enter_list': austria_enter_list,
        'austria_health_list': austria_health_list,
        'austria_sci_list': austria_sci_list,
        'austria_sport_list': austria_sport_list,
        'austria_tech_list': austria_tech_list,
    }
    #print(l)
    return render(request, 'countries/austria.html', context)


def belgium(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='be')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='be', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='be', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='be', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='be', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='be', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='be', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    belgium_tech_list = zip(url, pub, news, desc, img)

    context = {
        'belgium_list': belgium_list,
        'belgium_busi_list': belgium_busi_list,
        'belgium_enter_list': belgium_enter_list,
        'belgium_health_list': belgium_health_list,
        'belgium_sci_list': belgium_sci_list,
        'belgium_sport_list': belgium_sport_list,
        'belgium_tech_list': belgium_tech_list
    }
    #print(l)
    return render(request, 'countries/belgium.html', context)


def brazil(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='br')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='br', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='br', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='br', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='br', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='br', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='br', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    brazil_tech_list = zip(url, pub, news, desc, img)

    context = {
        'brazil_list': brazil_list,
        'brazil_busi_list': brazil_busi_list,
        'brazil_enter_list': brazil_enter_list,
        'brazil_health_list': brazil_health_list,
        'brazil_sci_list': brazil_sci_list,
        'brazil_sport_list': brazil_sport_list,
        'brazil_tech_list': brazil_tech_list
    }

    #print(l)
    return render(request, 'countries/brazil.html', context)


def bulgaria(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='bg')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='bg', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='bg', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='bg', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='bg', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='bg', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='bg', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    bulgaria_tech_list = zip(url, pub, news, desc, img)

    context = {
        'bulgaria_list': bulgaria_list,
        'bulgaria_busi_list': bulgaria_busi_list,
        'bulgaria_enter_list': bulgaria_enter_list,
        'bulgaria_health_list': bulgaria_health_list,
        'bulgaria_sci_list': bulgaria_sci_list,
        'bulgaria_sport_list': bulgaria_sport_list,
        'bulgaria_tech_list': bulgaria_tech_list
    }

    #print(l)
    return render(request, 'countries/bulgaria.html', context)


def canada(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ca')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ca', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ca', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ca', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ca', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ca', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ca', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    canada_tech_list = zip(url, pub, news, desc, img)

    context = {
        'canada_list': canada_list,
        'canada_busi_list': canada_busi_list,
        'canada_enter_list': canada_enter_list,
        'canada_health_list': canada_health_list,
        'canada_sci_list': canada_sci_list,
        'canada_sport_list': canada_sport_list,
        'canada_tech_list': canada_tech_list
    }

    #print(l)
    return render(request, 'countries/canada.html', context)


def china(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='cn')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='cn', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='cn', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='cn', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='cn', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='cn', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='cn', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    china_tech_list = zip(url, pub, news, desc, img)

    context = {
        'china_list': china_list,
        'china_busi_list': china_busi_list,
        'china_enter_list': china_enter_list,
        'china_health_list': china_health_list,
        'china_sci_list': china_sci_list,
        'china_sport_list': china_sport_list,
        'china_tech_list': china_tech_list
    }

    #print(l)
    return render(request, 'countries/china.html', context)



def colombia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='co')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='co', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='co', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='co', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='co', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='co', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='co', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    colombia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'colombia_list': colombia_list,
        'colombia_busi_list': colombia_busi_list,
        'colombia_enter_list': colombia_enter_list,
        'colombia_health_list': colombia_health_list,
        'colombia_sci_list': colombia_sci_list,
        'colombia_sport_list': colombia_sport_list,
        'colombia_tech_list': colombia_tech_list
    }

    #print(l)
    return render(request, 'countries/colombia.html', context)

def cuba(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='cu')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='cu', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='cu', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='cu', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='cu', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='cu', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='cu', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    cuba_tech_list = zip(url, pub, news, desc, img)

    context = {
        'cuba_list': cuba_list,
        'cuba_busi_list': cuba_busi_list,
        'cuba_enter_list': cuba_enter_list,
        'cuba_health_list': cuba_health_list,
        'cuba_sci_list': cuba_sci_list,
        'cuba_sport_list': cuba_sport_list,
        'cuba_tech_list': cuba_tech_list
    }

    #print(l)
    return render(request, 'countries/cuba.html', context)

def czech(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='cz')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='cz', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='cz', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='cz', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='cz', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='cz', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='cz', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    czech_tech_list = zip(url, pub, news, desc, img)

    context = {
        'czech_list': czech_list,
        'czech_busi_list': czech_busi_list,
        'czech_enter_list': czech_enter_list,
        'czech_health_list': czech_health_list,
        'czech_sci_list': czech_sci_list,
        'czech_sport_list': czech_sport_list,
        'czech_tech_list': czech_tech_list
    }

    #print(l)
    return render(request, 'countries/czech.html', context)

def egypt(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='eg')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='eg', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='eg', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='eg', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='eg', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='eg', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='eg', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    egypt_tech_list = zip(url, pub, news, desc, img)

    context = {
        'egypt_list': egypt_list,
        'egypt_busi_list': egypt_busi_list,
        'egypt_enter_list': egypt_enter_list,
        'egypt_health_list': egypt_health_list,
        'egypt_sci_list': egypt_sci_list,
        'egypt_sport_list': egypt_sport_list,
        'egypt_tech_list': egypt_tech_list
    }

    #print(l)
    return render(request, 'countries/egypt.html', context)

def france(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='fr')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='fr', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='fr', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='fr', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='fr', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='fr', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='fr', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    france_tech_list = zip(url, pub, news, desc, img)

    context = {
        'france_list': france_list,
        'france_busi_list': france_busi_list,
        'france_enter_list': france_enter_list,
        'france_health_list': france_health_list,
        'france_sci_list': france_sci_list,
        'france_sport_list': france_sport_list,
        'france_tech_list': france_tech_list
    }

    #print(l)
    return render(request, 'countries/france.html', context)

def germany(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='de')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='de', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='de', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='de', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='de', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='de', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='de', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    germany_tech_list = zip(url, pub, news, desc, img)

    context = {
        'germany_list': germany_list,
        'germany_busi_list': germany_busi_list,
        'germany_enter_list': germany_enter_list,
        'germany_health_list': germany_health_list,
        'germany_sci_list': germany_sci_list,
        'germany_sport_list': germany_sport_list,
        'germany_tech_list': germany_tech_list
    }

    #print(l)
    return render(request, 'countries/germany.html', context)

def greece(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='gr')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='gr', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='gr', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='gr', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='gr', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='gr', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='gr', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    greece_tech_list = zip(url, pub, news, desc, img)

    context = {
        'greece_list': greece_list,
        'greece_busi_list': greece_busi_list,
        'greece_enter_list': greece_enter_list,
        'greece_health_list': greece_health_list,
        'greece_sci_list': greece_sci_list,
        'greece_sport_list': greece_sport_list,
        'greece_tech_list': greece_tech_list
    }

    #print(l)
    return render(request, 'countries/greece.html', context)

def hongkong(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='hk')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='hk', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='hk', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='hk', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='hk', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='hk', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='hk', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hongkong_tech_list = zip(url, pub, news, desc, img)

    context = {
        'hongkong_list': hongkong_list,
        'hongkong_busi_list': hongkong_busi_list,
        'hongkong_enter_list': hongkong_enter_list,
        'hongkong_health_list': hongkong_health_list,
        'hongkong_sci_list': hongkong_sci_list,
        'hongkong_sport_list': hongkong_sport_list,
        'hongkong_tech_list': hongkong_tech_list
    }

    #print(l)
    return render(request, 'countries/hongkong.html', context)

def hungary(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='hu')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='hu', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='hu', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='hu', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='hu', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='hu', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='hu', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    hungary_tech_list = zip(url, pub, news, desc, img)

    context = {
        'hungary_list': hungary_list,
        'hungary_busi_list': hungary_busi_list,
        'hungary_enter_list': hungary_enter_list,
        'hungary_health_list': hungary_health_list,
        'hungary_sci_list': hungary_sci_list,
        'hungary_sport_list': hungary_sport_list,
        'hungary_tech_list': hungary_tech_list
    }

    #print(l)
    return render(request, 'countries/hungary.html', context)

def india(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='in')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='in', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='in', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='in', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='in', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='in', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='in', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_tech_list = zip(url, pub, news, desc, img)

    context = {
        'india_list': india_list,
        'india_busi_list': india_busi_list,
        'india_enter_list': india_enter_list,
        'india_health_list': india_health_list,
        'india_sci_list': india_sci_list,
        'india_sport_list': india_sport_list,
        'india_tech_list': india_tech_list
    }

    #print(l)
    return render(request, 'countries/india.html', context)

def indonesia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='id')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='id', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='id', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='id', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='id', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='id', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='id', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    indonesia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'indonesia_list': indonesia_list,
        'indonesia_busi_list': indonesia_busi_list,
        'indonesia_enter_list': indonesia_enter_list,
        'indonesia_health_list': indonesia_health_list,
        'indonesia_sci_list': indonesia_sci_list,
        'indonesia_sport_list': indonesia_sport_list,
        'indonesia_tech_list': indonesia_tech_list
    }

    #print(l)
    return render(request, 'countries/indonesia.html', context)

def ireland(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ie')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ie', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ie', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ie', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ie', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ie', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ie', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ireland_tech_list = zip(url, pub, news, desc, img)

    context = {
        'ireland_list': ireland_list,
        'ireland_busi_list': ireland_busi_list,
        'ireland_enter_list': ireland_enter_list,
        'ireland_health_list': ireland_health_list,
        'ireland_sci_list': ireland_sci_list,
        'ireland_sport_list': ireland_sport_list,
        'ireland_tech_list': ireland_tech_list
    }

    #print(l)
    return render(request, 'countries/ireland.html', context)

def israel(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='il')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='il', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='il', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='il', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='il', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='il', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='il', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    israel_tech_list = zip(url, pub, news, desc, img)

    context = {
        'israel_list': israel_list,
        'israel_busi_list': israel_busi_list,
        'israel_enter_list': israel_enter_list,
        'israel_health_list': israel_health_list,
        'israel_sci_list': israel_sci_list,
        'israel_sport_list': israel_sport_list,
        'israel_tech_list': israel_tech_list
    }

    #print(l)
    return render(request, 'countries/israel.html', context)

def italy(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='it')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='it', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='it', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='it', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='it', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='it', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='it', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    italy_tech_list = zip(url, pub, news, desc, img)

    context = {
        'italy_list': italy_list,
        'italy_busi_list': italy_busi_list,
        'italy_enter_list': italy_enter_list,
        'italy_health_list': italy_health_list,
        'italy_sci_list': italy_sci_list,
        'italy_sport_list': italy_sport_list,
        'italy_tech_list': italy_tech_list
    }

    #print(l)
    return render(request, 'countries/italy.html', context)


def japan(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='jp')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='jp', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='jp', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='jp', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='jp', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='jp', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='jp', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    japan_tech_list = zip(url, pub, news, desc, img)

    context = {
        'japan_list': japan_list,
        'japan_busi_list': japan_busi_list,
        'japan_enter_list': japan_enter_list,
        'japan_health_list': japan_health_list,
        'japan_sci_list': japan_sci_list,
        'japan_sport_list': japan_sport_list,
        'japan_tech_list': japan_tech_list
    }

    #print(l)
    return render(request, 'countries/japan.html', context)

def latvia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='lv')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='lv', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='lv', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='lv', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='lv', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='lv', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='lv', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    latvia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'latvia_list': latvia_list,
        'latvia_busi_list': latvia_busi_list,
        'latvia_enter_list': latvia_enter_list,
        'latvia_health_list': latvia_health_list,
        'latvia_sci_list': latvia_sci_list,
        'latvia_sport_list': latvia_sport_list,
        'latvia_tech_list': latvia_tech_list
    }

    #print(l)
    return render(request, 'countries/latvia.html', context)

def lithuania(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='lt')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='lt', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='lt', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='lt', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='lt', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='lt', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='lt', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    lithuania_tech_list = zip(url, pub, news, desc, img)

    context = {
        'lithuania_list': lithuania_list,
        'lithuania_busi_list': lithuania_busi_list,
        'lithuania_enter_list': lithuania_enter_list,
        'lithuania_health_list': lithuania_health_list,
        'lithuania_sci_list': lithuania_list,
        'lithuania_sport_list': lithuania_sport_list,
        'lithuania_tech_list': lithuania_tech_list
    }

    #print(l)
    return render(request, 'countries/lithuania.html', context)

def malaysia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='my')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='my', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='my', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='my', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='my', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='my', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='my', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    malaysia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'malaysia_list': malaysia_list,
        'malaysia_busi_list': malaysia_busi_list,
        'malaysia_enter_list': malaysia_enter_list,
        'malaysia_health_list': malaysia_health_list,
        'malaysia_sci_list': malaysia_list,
        'malaysia_sport_list': malaysia_sport_list,
        'malaysia_tech_list': malaysia_tech_list
    }

    #print(l)
    return render(request, 'countries/malaysia.html', context)

def mexico(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='mx')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='mx', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='mx', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='mx', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='mx', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='mx', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='mx', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mexico_tech_list = zip(url, pub, news, desc, img)

    context = {
        'mexico_list': mexico_list,
        'mexico_busi_list': mexico_busi_list,
        'mexico_enter_list': mexico_enter_list,
        'mexico_health_list': mexico_health_list,
        'mexico_sci_list': mexico_list,
        'mexico_sport_list': mexico_sport_list,
        'mexico_tech_list': mexico_tech_list
    }

    #print(l)
    return render(request, 'countries/mexico.html', context)

def morocco(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ma')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ma', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ma', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ma', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ma', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ma', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ma', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    morocco_tech_list = zip(url, pub, news, desc, img)

    context = {
        'morocco_list': morocco_list,
        'morocco_busi_list': morocco_busi_list,
        'morocco_enter_list': morocco_enter_list,
        'morocco_health_list': morocco_health_list,
        'morocco_sci_list': morocco_list,
        'morocco_sport_list': morocco_sport_list,
        'morocco_tech_list': morocco_tech_list
    }

    #print(l)
    return render(request, 'countries/morocco.html', context)

def netherland(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='nl')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='nl', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='nl', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='nl', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='nl', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='nl', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='nl', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    netherland_tech_list = zip(url, pub, news, desc, img)

    context = {
        'netherland_list': netherland_list,
        'netherland_busi_list': netherland_busi_list,
        'netherland_enter_list': netherland_enter_list,
        'netherland_health_list': netherland_health_list,
        'netherland_sci_list': netherland_sci_list,
        'netherland_sport_list': netherland_sport_list,
        'netherland_tech_list': netherland_tech_list
    }

    #print(l)
    return render(request, 'countries/netherland.html', context)

def nzealand(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='nz')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='nz', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='nz', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='nz', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='nz', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='nz', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='nz', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nzealand_tech_list = zip(url, pub, news, desc, img)

    context = {
        'nzealand_list': nzealand_list,
        'nzealand_busi_list': nzealand_busi_list,
        'nzealand_enter_list': nzealand_enter_list,
        'nzealand_health_list': nzealand_health_list,
        'nzealand_sci_list': nzealand_sci_list,
        'nzealand_sport_list': nzealand_sport_list,
        'nzealand_tech_list': nzealand_tech_list
    }

    #print(l)
    return render(request, 'countries/nzealand.html', context)

def nigeria(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ng')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ng', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ng', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ng', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ng', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ng', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ng', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    nigeria_tech_list = zip(url, pub, news, desc, img)

    context = {
        'nigeria_list': nigeria_list,
        'nigeria_busi_list': nigeria_busi_list,
        'nigeria_enter_list': nigeria_enter_list,
        'nigeria_health_list': nigeria_health_list,
        'nigeria_sci_list': nigeria_sci_list,
        'nigeria_sport_list': nigeria_sport_list,
        'nigeria_tech_list': nigeria_tech_list
    }

    #print(l)
    return render(request, 'countries/nigeria.html', context)

def norway(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='no')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='no', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='no', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='no', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='no', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='no', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='no', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    norway_tech_list = zip(url, pub, news, desc, img)

    context = {
        'norway_list': norway_list,
        'norway_busi_list': norway_busi_list,
        'norway_enter_list': norway_enter_list,
        'norway_health_list': norway_health_list,
        'norway_sci_list': norway_sci_list,
        'norway_sport_list': norway_sport_list,
        'norway_tech_list': norway_tech_list
    }

    #print(l)
    return render(request, 'countries/norway.html', context)

def philip(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ph')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ph', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ph', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ph', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ph', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ph', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ph', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    philip_tech_list = zip(url, pub, news, desc, img)

    context = {
        'philip_list': philip_list,
        'philip_busi_list': philip_busi_list,
        'philip_enter_list': philip_enter_list,
        'philip_health_list': philip_health_list,
        'philip_sci_list': philip_sci_list,
        'philip_sport_list': philip_sport_list,
        'philip_tech_list': philip_tech_list
    }

    #print(l)
    return render(request, 'countries/philip.html', context)

def poland(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='pl')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='pl', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='pl', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='pl', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='pl', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='pl', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='pl', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    poland_tech_list = zip(url, pub, news, desc, img)

    context = {
        'poland_list': poland_list,
        'poland_busi_list': poland_busi_list,
        'poland_enter_list': poland_enter_list,
        'poland_health_list': poland_health_list,
        'poland_sci_list': poland_sci_list,
        'poland_sport_list': poland_sport_list,
        'poland_tech_list': poland_tech_list
    }

    #print(l)
    return render(request, 'countries/poland.html', context)

def portugal(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='pt')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='pt', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='pt', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='pt', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='pt', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='pt', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='pt', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    portugal_tech_list = zip(url, pub, news, desc, img)

    context = {
        'portugal_list': portugal_list,
        'portugal_busi_list': portugal_busi_list,
        'portugal_enter_list': portugal_enter_list,
        'portugal_health_list': portugal_health_list,
        'portugal_sci_list': portugal_sci_list,
        'portugal_sport_list': portugal_sport_list,
        'portugal_tech_list': portugal_tech_list
    }

    #print(l)
    return render(request, 'countries/portugal.html', context)

def romania(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ro')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ro', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ro', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ro', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ro', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ro', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ro', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    romania_tech_list = zip(url, pub, news, desc, img)

    context = {
        'romania_list': romania_list,
        'romania_busi_list': romania_busi_list,
        'romania_enter_list': romania_enter_list,
        'romania_health_list': romania_health_list,
        'romania_sci_list': romania_sci_list,
        'romania_sport_list': romania_sport_list,
        'romania_tech_list': romania_tech_list
    }

    #print(l)
    return render(request, 'countries/romania.html', context)


def russia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ru')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ru', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ru', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ru', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ru', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ru', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ru', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    russia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'russia_list': russia_list,
        'russia_busi_list': russia_busi_list,
        'russia_enter_list': russia_enter_list,
        'russia_health_list': russia_health_list,
        'russia_sci_list': russia_sci_list,
        'russia_sport_list': russia_sport_list,
        'russia_tech_list': russia_tech_list
    }

    #print(l)
    return render(request, 'countries/russia.html', context)

def saudi(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='sa')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='sa', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='sa', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='sa', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='sa', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='sa', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='sa', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    saudi_tech_list = zip(url, pub, news, desc, img)

    context = {
        'saudi_list': saudi_list,
        'saudi_busi_list': saudi_busi_list,
        'saudi_enter_list': saudi_enter_list,
        'saudi_health_list': saudi_health_list,
        'saudi_sci_list': saudi_sci_list,
        'saudi_sport_list': saudi_sport_list,
        'saudi_tech_list': saudi_tech_list
    }

    #print(l)
    return render(request, 'countries/saudi.html', context)

def serbia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='rs')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='rs', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='rs', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='rs', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='rs', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='rs', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='rs', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    serbia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'serbia_list': serbia_list,
        'serbia_busi_list': serbia_busi_list,
        'serbia_enter_list': serbia_enter_list,
        'serbia_health_list': serbia_health_list,
        'serbia_sci_list': serbia_sci_list,
        'serbia_sport_list': serbia_sport_list,
        'serbia_tech_list': serbia_tech_list
    }

    #print(l)
    return render(request, 'countries/serbia.html', context)

def singapore(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='sg')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='sg', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='sg', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='sg', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='sg', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='sg', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='sg', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    singapore_tech_list = zip(url, pub, news, desc, img)

    context = {
        'singapore_list': singapore_list,
        'singapore_busi_list': singapore_busi_list,
        'singapore_enter_list': singapore_enter_list,
        'singapore_health_list': singapore_health_list,
        'singapore_sci_list': singapore_sci_list,
        'singapore_sport_list': singapore_sport_list,
        'singapore_tech_list': singapore_tech_list
    }

    #print(l)
    return render(request, 'countries/singapore.html', context)

def slovekia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='sk')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='sk', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='sk', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='sk', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='sk', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='sk', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='sk', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovekia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'slovekia_list': slovekia_list,
        'slovekia_busi_list': slovekia_busi_list,
        'slovekia_enter_list': slovekia_enter_list,
        'slovekia_health_list': slovekia_health_list,
        'slovekia_sci_list': slovekia_sci_list,
        'slovekia_sport_list': slovekia_sport_list,
        'slovekia_tech_list': slovekia_tech_list
    }

    #print(l)
    return render(request, 'countries/slovekia.html', context)

def slovenia(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='si')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='si', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='si', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='si', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='si', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='si', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='si', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    slovenia_tech_list = zip(url, pub, news, desc, img)

    context = {
        'slovenia_list': slovenia_list,
        'slovenia_busi_list': slovenia_busi_list,
        'slovenia_enter_list': slovenia_enter_list,
        'slovenia_health_list': slovenia_health_list,
        'slovenia_sci_list': slovenia_sci_list,
        'slovenia_sport_list': slovenia_sport_list,
        'slovenia_tech_list': slovenia_tech_list
    }

    #print(l)
    return render(request, 'countries/slovenia.html', context)

def safrica(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='za')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='za', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='za', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='za', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='za', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='za', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='za', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    safrica_tech_list = zip(url, pub, news, desc, img)

    context = {
        'safrica_list': safrica_list,
        'safrica_busi_list': safrica_busi_list,
        'safrica_enter_list': safrica_enter_list,
        'safrica_health_list': safrica_health_list,
        'safrica_sci_list': safrica_sci_list,
        'safrica_sport_list': safrica_sport_list,
        'safrica_tech_list': safrica_tech_list
    }

    #print(l)
    return render(request, 'countries/safrica.html', context)

def skorea(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='kr')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='kr', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='kr', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='kr', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='kr', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='kr', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='kr', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    skorea_tech_list = zip(url, pub, news, desc, img)

    context = {
        'skorea_list': skorea_list,
        'skorea_busi_list': skorea_busi_list,
        'skorea_enter_list': skorea_enter_list,
        'skorea_health_list': skorea_health_list,
        'skorea_sci_list': skorea_sci_list,
        'skorea_sport_list': skorea_sport_list,
        'skorea_tech_list': skorea_tech_list
    }

    #print(l)
    return render(request, 'countries/skorea.html', context)

def sweden(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='se')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='se', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='se', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='se', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='se', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='se', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='se', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    sweden_tech_list = zip(url, pub, news, desc, img)

    context = {
        'sweden_list': sweden_list,
        'sweden_busi_list': sweden_busi_list,
        'sweden_enter_list': sweden_enter_list,
        'sweden_health_list': sweden_health_list,
        'sweden_sci_list': sweden_sci_list,
        'sweden_sport_list': sweden_sport_list,
        'sweden_tech_list': sweden_tech_list
    }

    #print(l)
    return render(request, 'countries/sweden.html', context)

def switz(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ch')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ch', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ch', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ch', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ch', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ch', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ch', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    switz_tech_list = zip(url, pub, news, desc, img)

    context = {
        'switz_list': switz_list,
        'switz_busi_list': switz_busi_list,
        'switz_enter_list': switz_enter_list,
        'switz_health_list': switz_health_list,
        'switz_sci_list': switz_sci_list,
        'switz_sport_list': switz_sport_list,
        'switz_tech_list': switz_tech_list
    }

    #print(l)
    return render(request, 'countries/switz.html', context)

def taiwan(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='tw')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='tw', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='tw', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='tw', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='tw', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='tw', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='tw', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    taiwan_tech_list = zip(url, pub, news, desc, img)

    context = {
        'taiwan_list': taiwan_list,
        'taiwan_busi_list': taiwan_busi_list,
        'taiwan_enter_list': taiwan_enter_list,
        'taiwan_health_list': taiwan_health_list,
        'taiwan_sci_list': taiwan_sci_list,
        'taiwan_sport_list': taiwan_sport_list,
        'taiwan_tech_list': taiwan_tech_list
    }

    #print(l)
    return render(request, 'countries/taiwan.html', context)

def thailand(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='th')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='th', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='th', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='th', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='th', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='th', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='th', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    thai_tech_list = zip(url, pub, news, desc, img)

    context = {
        'thai_list': thai_list,
        'thai_busi_list': thai_busi_list,
        'thai_enter_list': thai_enter_list,
        'thai_health_list': thai_health_list,
        'thai_sci_list': thai_sci_list,
        'thai_sport_list': thai_sport_list,
        'thai_tech_list': thai_tech_list
    }

    #print(l)
    return render(request, 'countries/thai.html', context)

def turkey(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='tr')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='tr', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='tr', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='tr', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='tr', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='tr', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='tr', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    turkey_tech_list = zip(url, pub, news, desc, img)

    context = {
        'turkey_list': turkey_list,
        'turkey_busi_list': turkey_busi_list,
        'turkey_enter_list': turkey_enter_list,
        'turkey_health_list': turkey_health_list,
        'turkey_sci_list': turkey_sci_list,
        'turkey_sport_list': turkey_sport_list,
        'turkey_tech_list': turkey_tech_list
    }

    #print(l)
    return render(request, 'countries/turkey.html', context)

def uae(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ae')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ae', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ae', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ae', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ae', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ae', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ae', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uae_tech_list = zip(url, pub, news, desc, img)

    context = {
        'uae_list': uae_list,
        'uae_busi_list': uae_busi_list,
        'uae_enter_list': uae_enter_list,
        'uae_health_list': uae_health_list,
        'uae_sci_list': uae_sci_list,
        'uae_sport_list': uae_sport_list,
        'uae_tech_list': uae_tech_list
    }

    #print(l)
    return render(request, 'countries/uae.html', context)


def ukraine(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ua')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ua', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ua', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ua', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ua', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ua', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ua', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    ukraine_tech_list = zip(url, pub, news, desc, img)

    context = {
        'ukraine_list': ukraine_list,
        'ukraine_busi_list': ukraine_busi_list,
        'ukraine_enter_list': ukraine_enter_list,
        'ukraine_health_list': ukraine_health_list,
        'ukraine_sci_list': ukraine_sci_list,
        'ukraine_sport_list': ukraine_sport_list,
        'ukraine_tech_list': ukraine_tech_list
    }

    #print(l)
    return render(request, 'countries/ukraine.html', context)

def uk(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='gb')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='gb', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='gb', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='gb', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='gb', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='gb', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='gb', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    uk_tech_list = zip(url, pub, news, desc, img)

    context = {
        'uk_list': uk_list,
        'uk_busi_list': uk_busi_list,
        'uk_enter_list': uk_enter_list,
        'uk_health_list': uk_health_list,
        'uk_sci_list': uk_sci_list,
        'uk_sport_list': uk_sport_list,
        'uk_tech_list': uk_tech_list
    }

    #print(l)
    return render(request, 'countries/uk.html', context)

def us(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='us')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='us', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='us', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='us', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='us', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='us', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='us', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    us_tech_list = zip(url, pub, news, desc, img)

    context = {
        'us_list': us_list,
        'us_busi_list': us_busi_list,
        'us_enter_list': us_enter_list,
        'us_health_list': us_health_list,
        'us_sci_list': us_sci_list,
        'us_sport_list': us_sport_list,
        'us_tech_list': us_tech_list
    }

    #print(l)
    return render(request, 'countries/us.html', context)

def venuzuela(request):

    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    top_headlines = newsapi.get_top_headlines(country='ve')
    l = top_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_list = zip(url, pub, news, desc, img)

    busi_headlines = newsapi.get_top_headlines(country='ve', category='business')
    l = busi_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_busi_list = zip(url, pub, news, desc, img)

    enter_headlines = newsapi.get_top_headlines(country='ve', category='entertainment')
    l = enter_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_enter_list = zip(url, pub, news, desc, img)

    health_headlines = newsapi.get_top_headlines(country='ve', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_health_list = zip(url, pub, news, desc, img)

    sci_headlines = newsapi.get_top_headlines(country='ve', category='science')
    l = sci_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_sci_list = zip(url, pub, news, desc, img)

    sport_headlines = newsapi.get_top_headlines(country='ve', category='sports')
    l = sport_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_sport_list = zip(url, pub, news, desc, img)

    tech_headlines = newsapi.get_top_headlines(country='ve', category='technology')
    l = tech_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    venuzuela_tech_list = zip(url, pub, news, desc, img)

    context = {
        'venuzuela_list': venuzuela_list,
        'venuzuela_busi_list': venuzuela_busi_list,
        'venuzuela_enter_list': venuzuela_enter_list,
        'venuzuela_health_list': venuzuela_health_list,
        'venuzuela_sci_list': venuzuela_sci_list,
        'venuzuela_sport_list': venuzuela_sport_list,
        'venuzuela_tech_list': venuzuela_tech_list
    }

    #print(l)
    return render(request, 'countries/venuzuela.html', context)
