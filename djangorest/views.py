from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from djangorest.models import Snippet
from djangorest.serializers import SnippetSerializer

# Create your views here.
class SnippetViewSet(viewsets.ModelViewSet):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer

import pandas as pd
import numpy as np
import re
from ast import literal_eval
# genres = ["액션","코미디","공포"]   

class models1(APIView):
    import pandas as pd

    def get(self, request, pk) :
        print(pk)

        genres = pk
        # 전처리 된 db로 바꾸고 all 가져오면
        
        data = pd.read_excel(r'./djangorest/movie_2022.xlsx')
        movie_2022_drop = data.dropna(axis=0)
        fmovie = pd.DataFrame()
        for g in genres : 
            fmovie = fmovie.append(movie_2022_drop[movie_2022_drop["genre"].str.contains(g)])

        fmovie = fmovie.drop_duplicates("title")
        
        fmovie_sort = fmovie.sort_values(by=fmovie.columns[8],ascending = False)
        fmovie_sort_four = fmovie_sort.head(4)
        fmovie_sort_four_code = fmovie_sort_four['code']
        
        return Response(fmovie_sort_four_code)

class models3(APIView):
    import pandas as pd

    def get(self, request, pk) :
        genres = pk
        # 전처리 된 db로 바꾸고 all 가져오면
        
        data = pd.read_excel(r'movie_2022.xlsx')
        movie_2022_drop = data.dropna(axis=0)
        fmovie = pd.DataFrame()
        for g in genres : 
            fmovie = fmovie.append(movie_2022_drop[movie_2022_drop["genre"].str.contains(g)])

        fmovie = fmovie.drop_duplicates("title")
        
        fmovie_sort = fmovie.sort_values(by=fmovie.columns[8],ascending = False)
        fmovie_sort_four = fmovie_sort.head(4)
        fmovie_sort_four_code = fmovie_sort_four['code']
        
        return Response(fmovie_sort_four_code)    



class models2(APIView):
    def get(self, request):
        print("get된다")
        return Response("답도없네")

    def post(self, request) :    
        print("poset된다.")
        data = request.data
        newdata = data["deal"]
        print(newdata)
        return Response(data, status=status.HTTP_201_CREATED)