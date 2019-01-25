import csv
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import File
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, FileSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
from Language_detection.classify import predict_lang
from Sentiment_analysis.classiy import predict_sentiment_ara,predict_sentiment_tun
from django.http import FileResponse
#class Languagecheck(APIView)




class FileView(APIView):
    # queryset = File.objects.all()
    serializer_class = FileSerializer
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)


    def put(self, request, format=None):
        file_obj = request.data['file']
        for line in file_obj.readlines():
            print(line)
        return Response(status=204)


    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            uploaded_file = self.request.FILES['file']
            name = uploaded_file.name.strip('.')
            with open(name+'result.csv', "w", encoding="utf-8", newline='') as result_file:
                writer = csv.writer(result_file, dialect='excel', delimiter=',')
                for line in uploaded_file:
                    predicted_lang = predict_lang(line.decode("utf-8",'ignore').strip())
                    if predicted_lang == 'TUN':
                        writer.writerow(['TUN', predict_sentiment_tun(line.decode("utf-8",'ignore').strip())])
                    elif predicted_lang == 'ARA':
                        writer.writerow(['ARA', predict_sentiment_ara(line.decode("utf-8",'ignore').strip())])
                    else:
                        writer.writerow(['OTHER', 'UNPREDICTABLE'])
            response = FileResponse(open(name+'result.csv', 'rb'))
            return response
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def predict(request):
        sentance = request.data['Sentance']

        predicted_lang = predict_lang(sentance.strip())

        if predicted_lang == 'TUN':
            return Response({"Language": "TUN","Sentiment": predict_sentiment_tun(sentance.strip())})
        elif predicted_lang == 'ARA':
            return Response({"Language": "ARA","Sentiment": predict_sentiment_ara(sentance.strip())})

        else:
            return Response({"Language": "OTHER", "Sentiment": "UNPREDICTABLE"})






class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer