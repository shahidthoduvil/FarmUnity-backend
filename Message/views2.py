from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.db.utils import IntegrityError
import requests
from rest_framework import status
from django.conf import settings




class PreviousMessagesView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user1 = int(self.kwargs['user1'])
        user2 = int(self.kwargs['user2'])

        thread_suffix = f"{user1}_{user2}" if user1 > user2 else f"{user2}_{user1}"
        thread_name = 'chat_'+thread_suffix
        queryset = Messages.objects.filter(
            thread_name=thread_name
        )
        return queryset
    


class FetchAndStoreInitialNews(APIView):
    def post(self, request, format=None):
        try:
         
            api_key = settings.API_KEY
            api_url = f'https://newsapi.org/v2/everything?q=agriculture&apikey={api_key}'
            response = requests.get(api_url)
            print(response)
            news_data = response.json().get('articles', [])

            if not news_data:
                print("API response does not contain news data. Skipping addition.")
                return Response({'message': 'API response does not contain news data.'})

            News.objects.all().delete()
            print("Cleared existing news data")

            news_added = 0
            max_news_count = 100

            for article in news_data:
                if news_added >= max_news_count:
                    print("Maximum news limit reached. Stopping further addition.")
                    break
                try:
                    News.objects.create(
                        author=article['author'],
                        title=article['title'],
                        description=article['description'],
                        url=article['url'],
                        url_to_image=article['urlToImage'],
                    )
                    news_added += 1
                except IntegrityError as e:
                    print('Error adding news article:', exc_info=True)
                    continue  
            
            
            return Response({'message': 'News data fetched and stored successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error fetching and storing news data.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CachedNewsListView(APIView):
    def get(self, request, *args, **kwargs):

        cache_time_threshold = datetime.now() - timedelta(days=1)
        cached_news = News.objects.all().order_by('-id')

        if cached_news.exists():
            serialized_news = [{'title': news.title, 'description': news.description, 'url': news.url, 'urlToImage': news.url_to_image,'author':news.author} for news in cached_news]
            return Response(serialized_news)
        else:
            return Response({'message': 'No cached news data available.'}, status=204) 
