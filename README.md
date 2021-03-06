## NewsX 
NewsX is build on top of the newsapi. It uses newsapi to fetch top-headlines of different news sites. You can search topnews by keyword. You can also get the country-wise top-headlines.

![Image of Yaktocat](https://res.cloudinary.com/dwltrduan/image/upload/v1587306151/Screenshot_199_bzstbl.png)

## Installation:

#### From GitHub:
  * Clone this repo. 
  
#### Create new django project (https://www.djangoproject.com/start/):
    pip install django
    
    django-admin startproject 'project_name'
 
 #### move to project directory and run:
 
    python manage.py migrate
    
    python manage.py runserver
 
    python manage.py startapp 'app_name'
    
    
## Installation:
#### Also available on PyPI site. github link - (https://github.com/mattlisiv/newsapi-python):
    pip install newsapi-python (with developer account, you can only do 500 request in 24 hours and 250 request in 12 hours)
    

## How to use:

#### Initialising the instance/api: (https://newsapi.org/)
```
from newsapi import NewsApiClient

 Init
newsapi = NewsApiClient(api_key='your_newsapi_key') 

 /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

 /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

 /v2/sources
sources = newsapi.get_sources()
```
