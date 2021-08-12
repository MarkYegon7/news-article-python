import urllib.request,json
from .models import Article, Source
 

api_key = None
source_url = None
cat_url = None

def configure_request(app):
    global api_key,source_url,cat_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_BASE_URL']
    
    
def get_source():
    get_source_url = source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None
        
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
            
    return source_results

def process_results(source_list):
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        if id:
            source_object = Source(id,name,description,url,language)
            source_results.append(source_object)
            
    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)
        
        article_source_results = None
        
        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)
            
    return article_source_results
            
def process_articles_results(news):
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get('title')
        
        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)
            
    return article_source_results



def get_headlines():
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        
        get_headlines_results = None
        
        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            
        
    return get_headlines_results


        

            