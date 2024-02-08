import streamlit as st
import pandas as pd
from newsapi import NewsApiClient
import streamlit_antd_components as sac
from modules import irismod as imo
from datetime import datetime,timedelta

#connecting with api
api=NewsApiClient(api_key='bae08d244cf244f39842f4a146bb0ce5')

#setting page configurations
icon_p='https://github.com/joyall2812/IRIS-news-reader/blob/main/images/IRIS-logos_white_new_cropped.png?raw=true'
st.set_page_config(page_title='IRIS',page_icon=icon_p,layout='wide',initial_sidebar_state="auto")
with st.container():
    st.image('https://github.com/joyall2812/IRIS-news-reader/blob/main/images/IRIS-logos_white_new_cropped.png?raw=true')

#setting background image
pg_bg_img="""
<style>
[data-testid="stSidebar"]{background-image:url('https://github.com/joyall2812/IRIS-news-reader/blob/main/images/1707320145015.jpg?raw=true');
background-size:150%;
}
</style>
"""
st.markdown(pg_bg_img,unsafe_allow_html=True)


# setting tab
tab=sac.tabs([
    sac.TabsItem(label='headlines',icon='newspaper'),
    sac.TabsItem(label='topics',icon='search'),
    sac.TabsItem(label='about',icon='chat-left-heart-fill')
    ], align='start')

#function to print articles

def find_art(mode,filters_se=None):
    headlines=mode(filters_se)
    if len(headlines)==0:
        with st.container(border=True):
            st.image('https://github.com/joyall2812/IRIS-news-reader/blob/main/images/no_image-removebg-preview.png?raw=true',width=300)
            st.subheader('couldnt find articles for your query')
            st.markdown('''
            ### Troubleshooting Help

            If you're unable to find articles for your query, here are some possible solutions:

            1. **Check and Correct Parameters**: Ensure that the parameters you've entered are correct. Double-check the filters, keywords, date range, and any other parameters you've set for your news search. Sometimes, a small mistake in the parameters can lead to no search results.

            2. **Check Spelling of Keyword**: Verify that the keyword you're searching for is spelled correctly. Even a minor spelling mistake can result in no matching articles being found. Correct any spelling errors in your search query.

            3. **Check Your Internet Connection**: Ensure that your internet connection is stable and working properly. A poor or unstable internet connection can sometimes prevent your web app from fetching articles from the news API. Try refreshing the page or checking your internet connection status.

            If you've tried the above solutions and are still unable to find articles for your query, please contact support for further assistance.''')
    else:
        for i in range (len(headlines)):
            with st.container(border=True):
                col1,col2=st.columns(2)
                with col1:
                    if headlines[i]['title']=='[Removed]' or headlines[i]['title']==None:
                         pass
                    else:
                        st.markdown(f"<h3><a href='{headlines[i]['url']}'>{headlines[i]['title']}</a></h3>", unsafe_allow_html=True)
                        st.text(f'source : {headlines[i]["source"]["name"]}')
                        st.text(headlines[i]['publishedAt'])
                with col2:
                    if headlines[i]['title']=='[Removed]' or headlines[i]['title']==None:
                         pass
                    elif headlines[i]['urlToImage']==None:
                        st.image('https://github.com/joyall2812/IRIS-news-reader/blob/main/images/no-image-icon-23489%20(1).png?raw=true')
                    else:
                        try:
                            st.image(headlines[i]['urlToImage'])
                        except Exception as e :
                            continue

# filters
def news_filters():
    with st.container(border=True):
        st.header(':rainbow[FILTERS]',divider='red')
        
        #language filter
        languages=imo.ex_lang()
        lang_name=list(languages.keys())
        lang_se=st.selectbox('Select a Language:',lang_name,placeholder='Choose')

        #country filter
        crydict=imo.ex_countries()
        countries=list(crydict.keys())
        cry_se=st.selectbox('Select a country :',countries)
        
        #category filter
        categories=imo.ex_category()
        cat_se=st.selectbox('select a category :',categories)
        
        #page size
        size_se=st.slider('number of results',min_value=20,max_value=100)
        
        filters_se={'language':languages[lang_se],'country':crydict[cry_se],'category':cat_se,'page_size':size_se,'page':1}
        apply=st.button('apply')
        if apply:
            st.write('FILTERS:')
            st.write(filters_se)
            return filters_se
        else:
            pass

#filters for topic search
def topic_func_filt():
    with st.container(border=True):

        
        #getting keyword
        keyword=st.text_input('SEARCH :')
        st.header(':rainbow[FILTERS]',divider='red')

        #language filter
        languagest=imo.ex_lang()
        lang_namet=list(languagest.keys())
        lang_se_t=st.selectbox('Select a Language:',lang_namet,placeholder='Choose')

        #add sources filter later

        # from-to date filter
        with st.container(border=True):
            today = datetime.now()
            one_month_ago = today - timedelta(days=30)
            from_dt=st.date_input(label='From:',format='YYYY/MM/DD',max_value=today,min_value=one_month_ago)
        
            to_dt=st.date_input(label='To:',format='YYYY/MM/DD',max_value=today,min_value=from_dt)

        #page size
        size_t=st.slider('number of results',min_value=20,max_value=100)

        #sorting
        sort_se=st.radio('Sort By:',['relevancy','popularity','publishedAt'],captions=['articles more closely related to the keyword come first.','articles from popular sources and publishers come first.',' newest articles come first.'],index=None,)

        kywrd={'q':keyword,'language':languagest[lang_se_t],'from_param':from_dt,'to':to_dt,'page_size':size_t,'page':1,'sort_by':sort_se}
        search=st.button('Search')
        if search:
            st.write(kywrd)
            return kywrd
        else:
            pass

#actual ui

#headlines tab
if tab =='headlines':
    with st.sidebar:
        filters_se=news_filters()
    

    sac.alert(label='hello!!!', description='Check sidebar for filters', size='lg', radius=20, variant='quote', color='blue', banner=True, icon=True, closable=True)
    find_art(mode=imo.ex_articles,filters_se=filters_se)

#topics tab

if tab=='topics':
    
    with st.sidebar:
       kywrd=topic_func_filt()
    if kywrd:
        find_art(mode=imo.ex_all_art,filters_se=kywrd)
    else:
        st.header('Search any topic you want')

#about tab

if tab=='about':
    st.markdown('''
    # Welcome to IRIS News Reader

IRIS News Reader is a web application designed to provide users with the latest news articles from various sources around the world. With a simple and intuitive interface, IRIS makes it easy to stay informed about current events and trending topics.

## Features:

- **Headlines Tab:**
  Explore top headlines from different categories such as business, technology, sports, and more. Customize your news feed with language, country, and category filters.

- **Topics Tab:**
  Search for news articles on specific topics or keywords. Refine your search results with language, date range, and sorting options to find relevant articles quickly.

- **About Tab:**
  Learn more about the IRIS News Reader web application and its features. Get information on how to use the app effectively and connect with the development team.

## How to Use:

1. **Headlines Tab:**
   - Navigate to the Headlines tab to view top news headlines.
   - Use the sidebar filters to customize your news feed based on language, country, and category.

2. **Topics Tab:**
   - Visit the Topics tab to search for news articles on specific topics or keywords.
   - Enter your desired keyword in the search box and apply filters to narrow down your search results.

3. **About Tab:**
   - Click on the About tab to access information about the IRIS News Reader web application.
   - Explore the features and functionalities of the app and learn how to use it effectively.

## Connect with us:

- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joyall2812/HERMES-CONVERTER)

- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joyalvs380@gmail.com)

Thank you for using IRIS News Reader! ''')

    
