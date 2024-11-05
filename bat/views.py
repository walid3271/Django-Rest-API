# List Create Api View
from .models import user_model
from .sterilizers import user_model_serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class user_all_view_create(ListCreateAPIView):
    queryset = user_model.objects.all()
    serializer_class = user_model_serializers
    
class user_all_id_update_delete(RetrieveUpdateDestroyAPIView):
    queryset = user_model.objects.all()
    serializer_class = user_model_serializers


















# Model Mixins
# from .models import user_model
# from .sterilizers import user_model_serializers
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# class user_all_view(GenericAPIView, ListModelMixin):
#     queryset = user_model.objects.all()
#     serializer_class = user_model_serializers
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
# class user_id_view(GenericAPIView, RetrieveModelMixin):
#     queryset = user_model.objects.all()
#     serializer_class = user_model_serializers
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class user_create_view(GenericAPIView, CreateModelMixin):
#     queryset = user_model.objects.all()
#     serializer_class = user_model_serializers
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class user_update_view(GenericAPIView, UpdateModelMixin):
#     queryset = user_model.objects.all()
#     serializer_class = user_model_serializers
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class user_delete_view(GenericAPIView, DestroyModelMixin):
#     queryset = user_model.objects.all()
#     serializer_class = user_model_serializers
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

































#Class Base View
# from django.shortcuts import render
# from .models import user_model
# from .sterilizers import user_model_serializers
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class user_all(APIView):
#     def get(self, request, pk=None, format=None):
#         id=pk
#         if id is not None:
#             user = user_model.objects.get(id=id)
#             serializer = user_model_serializers(user)
#             return Response(serializer.data)
#         else:
#             user = user_model.objects.all()
#             serializer = user_model_serializers(user, many=True)
#             return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = user_model_serializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Insert Data'})
#         else:
#             return Response(serializer.errors, status=400)
    
#     def put(self, request, pk, format=None):
#         id = pk
#         user = user_model.objects.get(pk=id)
#         serializer = user_model_serializers(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Update Data'})
#         else:
#             return Response(serializer.errors, status=400)
    
#     def patch(self, request, pk, format=None):
#         id = pk
#         user = user_model.objects.get(pk=id)
#         serializer = user_model_serializers(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Partial Data Update'})
#         else:
#             return Response(serializer.errors, status=400)
    
#     def delete(self, request, pk, format=None):
#         id = pk
#         user = user_model.objects.get(pk=id)
#         user.delete()
#         return Response({'Msg': 'Successfully Delete Data'})
    
    
    
    
#Function Base View
# from django.shortcuts import render
# from .models import user_model
# from .sterilizers import user_model_serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
# def user_all(request,pk=None):
#     if request.method == 'GET':
#         id=pk
#         if id is not None:
#             user = user_model.objects.get(id=id)
#             serializer = user_model_serializers(user)
#             return Response(serializer.data)
        
#         user = user_model.objects.all()
#         serializer = user_model_serializers(user, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = user_model_serializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Insert Data'})
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'PUT':
#         id = pk
#         user = user_model.objects.get(pk=id)
#         serializer = user_model_serializers(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Update Data'})
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'PATCH':
#         id = pk
#         user = user_model.objects.get(pk=id)
#         serializer = user_model_serializers(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Msg': 'Successfully Partial Data Update'})
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'DELETE':
#         id = pk
#         user = user_model.objects.get(pk=id)
#         user.delete()
#         return Response({'Msg': 'Successfully Delete Data'})