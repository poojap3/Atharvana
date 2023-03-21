from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib import auth
import random
from .backend import *



from rest_framework.generics import GenericAPIView

class LoginView(GenericAPIView):
    serializer_class =UserSerializer

    def post(self, request):
        response = {}
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user_check = User.objects.filter(username= username)
        if user_check:
            user = auth.authenticate(username=username, password=password)
            if user:
                # custom_user = User.objects.get(id=user.id)

                auth_token = jwt.encode(
                    { 'username': user.username}, str(settings.JWT_SECRET_KEY), algorithm="HS256")

                serializer = UserSerializer(user)
                authorization = 'Bearer'+' '+auth_token
                response_result = {}
                response_result['result'] = {
                    'detail': 'Login successfull',
                    'token':authorization,
                    'user_id':user.id,
                    'username':user.username,

                    'status': status.HTTP_200_OK}
                response['Authorization'] = authorization

                response['status'] = status.HTTP_200_OK
            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid credentials', 'status': status.HTTP_401_UNAUTHORIZED}}

                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
            return Response(response_result, headers=response,status= status.HTTP_200_OK)
        else:
            response='Invalid username'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskValueAPIView(APIView):

    def post(self, request):
        data = request.data
        mm = data.get('mm')
        s1 = data.get('s1')
        s2 = data.get('s2')
        # created=date.get('created')


        if data:


            regcreate = TaskValue.objects.create(mm=mm, s1=s1, s2=s2)

            value=TaskValue.objects.filter(id=regcreate.id)
            for i in value:
                mm=i.mm
                s1=i.s1
                s2=i.s2
            mm1=eval(mm)
            s11=eval(s1)
            s22=eval(s2)


            if mm1[-1]==0 & s11[-1]==0 & s22[-1]==0 :
                return Response("Status : OK")


            else:
                return Response("Status: NOT OK ")

            # print(data)
        else:
            return Response ("enter value")



    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            appdata = TaskValue.objects.filter(id=id).values()
            return Response(appdata)
        else:

            appdata = TaskValue.objects.all().values()
            return Response(appdata)




class ValueDateAPIView(APIView):
    def post(self, request):
        data = request.data

        dates = data.get('datename')
        Arr=[]
        user_check=TaskValue.objects.filter(created__date=dates)
        for i in user_check:
            Arr.append({
                'mm':i.mm,
                's1':i.s1,
                's2':i.s2,
                'created':i.created

            })

        return Response(Arr)
