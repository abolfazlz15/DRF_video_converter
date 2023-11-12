from django.core.cache import cache
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api import serializers
from accounts.otp_service import OTP


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserLoginSerializer
    
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save(validated_data=serializer.validated_data)
        return Response(result, status=status.HTTP_200_OK)
    

class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            clean_data = serializer.validated_data
            otp_service = OTP()
            otp_code = otp_service.generate_otp(clean_data['email'])
            cache.set(key=otp_code, value={'email': clean_data['email'], 'password': clean_data['password'],
                                           'fullname': clean_data['fullname']}, timeout=300)

            return Response({'email': clean_data['email'], 'result': 'email sent', 'success': True},
                            status=status.HTTP_202_ACCEPTED)
        return Response({'errors': serializer.errors, 'success': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
