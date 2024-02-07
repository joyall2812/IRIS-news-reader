from newsapi import NewsApiClient
from modules import irismod as imo
api=NewsApiClient(api_key='bae08d244cf244f39842f4a146bb0ce5')

#get sources
def ex_sources():
    sources=api.get_sources()
    srces=[]
    for i in sources['sources']:
        for j in range(len(sources['sources'])):
            
            src=sources['sources'][j]['name']
            srces.append(src)
        return srces

#to get headline articles
def ex_articles(filters_se=None):
    if filters_se:
        headlines=api.get_top_headlines(**filters_se)
        art=headlines['articles']
        return art
    else:
        headlines=api.get_top_headlines()
        art=headlines['articles']
        return art

        

#to get supported languages
def ex_lang():
    language_names = {
    'all languages':None,
    'Arabic': 'ar',
    'German': 'de',
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'Hebrew': 'he',
    'Italian': 'it',
    'Dutch': 'nl',
    'Norwegian': 'no',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Swedish': 'sv',
    'Undefined': 'ud',
    'Chinese': 'zh'}
    return language_names

#to get supported country names

def ex_countries():
    country_names = {
    'all countries':None,
    'United Arab Emirates': 'ae',
    'Argentina': 'ar',
    'Austria': 'at',
    'Australia': 'au',
    'Belgium': 'be',
    'Bulgaria': 'bg',
    'Brazil': 'br',
    'Canada': 'ca',
    'Switzerland': 'ch',
    'China': 'cn',
    'Colombia': 'co',
    'Czech Republic': 'cz',
    'Germany': 'de',
    'Egypt': 'eg',
    'France': 'fr',
    'United Kingdom': 'gb',
    'Greece': 'gr',
    'Hong Kong': 'hk',
    'Hungary': 'hu',
    'Indonesia': 'id',
    'Ireland': 'ie',
    'Israel': 'il',
    'India': 'in',
    'Italy': 'it',
    'Japan': 'jp',
    'South Korea': 'kr',
    'Lithuania': 'lt',
    'Latvia': 'lv',
    'Morocco': 'ma',
    'Mexico': 'mx',
    'Malaysia': 'my',
    'Nigeria': 'ng',
    'Netherlands': 'nl',
    'Norway': 'no',
    'New Zealand': 'nz',
    'Philippines': 'ph',
    'Poland': 'pl',
    'Portugal': 'pt',
    'Romania': 'ro',
    'Serbia': 'rs',
    'Russia': 'ru',
    'Saudi Arabia': 'sa',
    'Sweden': 'se',
    'Singapore': 'sg',
    'Slovenia': 'si',
    'Slovakia': 'sk',
    'Thailand': 'th',
    'Turkey': 'tr',
    'Taiwan': 'tw',
    'Ukraine': 'ua',
    'United States': 'us',
    'Venezuela': 've',
    'South Africa': 'za'}

    return country_names

#category filter

def ex_category():
    categories = [None,'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    return categories

#get all articles function
def ex_all_art(srch_keys):
    news=api.get_everything(**srch_keys)
    all_art=news['articles']
    return all_art

#testing new function

def find_art(mode,filters_se=None):
    headlines=imo.mode(filters_se)
    for i in range (len(headlines)):
        with st.container(border=True):
            col1,col2=st.columns(2)
            with col1:
                if headlines[i]['title']=='[Removed]' or headlines[i]['title']==None:
                    pass
                else:
                   st.markdown(f"<h1><a href='{headlines[i]['url']}'>{headlines[i]['title']}</a></h1>", unsafe_allow_html=True)
                   st.text(f'source : {headlines[i]["source"]["name"]}')
                   st.text(headlines[i]['publishedAt'])
            with col2:
                if headlines[i]['urlToImage']==None:
                    st.image('https://github.com/joyall2812/IRIS-news-reader/blob/main/images/no-image-icon-23489%20(1).png?raw=true')
                else:
                    st.image(headlines[i]['urlToImage'])



