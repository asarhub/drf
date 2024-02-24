from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.authentication import ThirdPartyAuthentication
from authentication.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth
from rest_framework.generics import ListAPIView
from authentication.models import User
from authentication.serializers import ReadUserSerializer
from authentication.permissions import Dummypermission, Dummypermission2, IsAdminUser
from authentication.throttle import CustomRateThrottle


# Create your views here.
class sign_up_view(APIView):
    # page_name="sign-up.html"
    def post(self, request):
        authentication_classes = []
        permissions_classes = []
        print("Not caching)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        print(username,email,password)
        if not username:
            return Response({"error": True, "msg": "Please add username"}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            # return render(request, page_name, {"error": True, "msg": "Please add email"})
            return Response({"error": True, "msg": "Please add email"}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            # return render(request, page_name, {"error": True, "msg": "Please add password"})
            return Response({"error": True, "msg": "Please add password"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            # return render(request, page_name, {"error": True, "msg": "Same username cannot be taken"})
            return Response({"error": True, "msg": "Same usename cannot be taken"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            # return render(request, page_name, {"error": True, "msg": "Same email cannot be taken"})
            return Response({"error": True, "msg": "Same email canot be taken"}, status=status.HTTP_400_BAD_REQUEST)

        # User=Model name
        # objects=model manager
        user = User.objects.create_user(username=username, password=password, email=email)
        print(user)
        # This part of the code required for sign in
        user = auth.authenticate(username=username, password=password)
        print(str(user) + "This is user name")
        if user:
            # return redirect("index")
            return Response({"success": True, "msg": "Authentication Successful,try signing back"},
                            status=status.HTTP_200_OK)
        else:
            # return render(request,page_name,{"error":True,"msg":"Authentication dint happened"}
            return Response({"error": True, "msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

class UserList(ListAPIView):
    #making userlist as None because to view regardless of specific user
    #permission_classes = [Dummypermission,Dummypermission2]#here ,is memtioned for 2 permission. This is and operation . if you want or then mention |
    #queryset = User.objects.all()
    #serializer_class = ReadUserSerializer
    #*Below is for third party authentication*#
    #Doing OR for authentication classes
    #authentication_classes = (ThirdPartyAuthentication,JWTAuthentication)
    #but for permissions doing OR means permission_classes = [Dummypermission,Dummypermission2]
    #This difference you need to note it down
    authentication_classes = (ThirdPartyAuthentication,JWTAuthentication)
    permission_classes = (IsAdminUser, )#This will paass in third party authentication because is_superuser= True will be coming from thirdpartauthentication class
    serializer_class = ReadUserSerializer
    #This is for throttling. Please follow the syntax below
    throttle_classes = (CustomRateThrottle, )

    def get_queryset(self):
        print("Request user id",self.request.user.id)
        print("request user username", self.request.user.username)
        queryset = User.objects.all()
        return queryset
