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

    context = {
        'australia_list': australia_list,
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

    context = {
        'austria_list': austria_list,
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

    context = {
        'belgium_list': belgium_list,
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

    context = {
        'brazil_list': brazil_list,
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

    context = {
        'bulgaria_list': bulgaria_list,
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

    context = {
        'canada_list': canada_list,
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

    context = {
        'china_list': china_list,
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

    context = {
        'colombia_list': colombia_list,
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

    context = {
        'cuba_list': cuba_list,
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

    context = {
        'czech_list': czech_list,
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

    context = {
        'egypt_list': egypt_list,
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

    context = {
        'france_list': france_list,
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

    context = {
        'germany_list': germany_list,
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

    context = {
        'greece_list': greece_list,
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

    context = {
        'hongkong_list': hongkong_list,
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

    context = {
        'hungary_list': hungary_list,
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

    context = {
        'india_list': india_list,
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

    context = {
        'indonesia_list': indonesia_list,
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

    context = {
        'ireland_list': ireland_list,
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

    context = {
        'israel_list': israel_list,
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

    context = {
        'italy_list': italy_list,
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

    context = {
        'japan_list': japan_list,
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

    context = {
        'latvia_list': latvia_list,
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

    context = {
        'lithuania_list': lithuania_list,
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

    context = {
        'malaysia_list': malaysia_list,
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

    context = {
        'mexico_list': mexico_list,
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

    context = {
        'morocco_list': morocco_list,
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

    context = {
        'netherland_list': netherland_list,
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

    context = {
        'nzealand_list': nzealand_list,
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

    context = {
        'nigeria_list': nigeria_list,
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

    context = {
        'norway_list': norway_list,
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

    context = {
        'philip_list': philip_list,
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

    context = {
        'poland_list': poland_list,
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

    context = {
        'portugal_list': portugal_list,
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

    context = {
        'romania_list': romania_list,
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

    context = {
        'russia_list': russia_list,
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

    context = {
        'saudi_list': saudi_list,
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

    context = {
        'serbia_list': serbia_list,
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

    context = {
        'singapore_list': singapore_list,
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

    context = {
        'slovekia_list': slovekia_list,
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

    context = {
        'slovenia_list': slovenia_list,
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

    context = {
        'safrica_list': safrica_list,
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

    context = {
        'skorea_list': skorea_list,
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

    context = {
        'sweden_list': sweden_list,
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

    context = {
        'switz_list': switz_list,
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

    context = {
        'taiwan_list': taiwan_list,
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

    context = {
        'thai_list': thai_list,
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

    context = {
        'turkey_list': turkey_list,
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

    context = {
        'uae_list': uae_list,
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

    context = {
        'ukraine_list': ukraine_list,
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

    context = {
        'uk_list': uk_list,
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

    context = {
        'us_list': us_list,
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

    context = {
        'venuzuela_list': venuzuela_list,
    }
    #print(l)
    return render(request, 'countries/venuzuela.html', context)
