from django.http.response import HttpResponse
from rest_framework.views import APIView


class GetFightDataset(APIView):
    def get(self, request, *args, **kwargs):
        file_path = "static/fights.csv"
        file_pointer = open(file_path, "r")
        response = HttpResponse(file_pointer, content_type='application/text-csv')
        response['Content-Disposition'] = 'attachment; filename=fights.csv'
        return response

class GetBorderDataset(APIView):
    def get(self, request, *args, **kwargs):
        file_path = "static/Border_Crossing_Entry_Data.csv"
        file_pointer = open(file_path, "r")
        response = HttpResponse(file_pointer, content_type='application/text-csv')
        response['Content-Disposition'] = 'attachment; filename=crossings.csv'
        return response
