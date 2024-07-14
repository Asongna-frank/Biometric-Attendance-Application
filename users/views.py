# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from api.serializers.users import AuthTokenSerializer, UserSerializer  # Make sure to define these serializers
#
# class ObtainTokenPairWithEmailView(APIView):
#     permission_classes = ()
#     authentication_classes = ()
#
#     def post(self, request, *args, **kwargs):
#         serializer = AuthTokenSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             refresh = RefreshToken.for_user(user)
#
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
