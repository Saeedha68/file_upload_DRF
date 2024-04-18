from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .serializers import ImageSerialiser,DocumentSerialiser
from .models import document,Image
from rest_framework.permissions import IsAuthenticated,IsAdminUser
#----------------------------------------------------------------
#اجرای صفحه اصلی
def main(request):
    return render(request,'main.html')
#----------------------------------------------------------------
#کلاس آپلود عکس
class ImageUpload(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        ser_data = ImageSerialiser(data=request.data)
        print(ser_data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data ,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------------------------------------------------
#کلاس آپلود داکیومنت  شامل فایل های-txt and docx
class DocumentUpload(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        ser_data = DocumentSerialiser(data=request.data)
        print(ser_data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data ,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
#----------------------------------------------------------------
#در این کلاس اطلاعات متا دیتا را در غالب یه دیکشنری جدا به به همراه ریکوست به فراخوان ای پی آی فرستادم
class DocMetadata(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        documents = document.objects.all()
        ser_data= DocumentSerialiser(instance=documents,many=True)
        text=''
        postfix=''
        name=''
        my_list=[]
        my_dict = {}
        for i in range(len(documents)):
            with open(ser_data.data[i]['path'][1:], 'r') as file:
                text = file.read()
                postfix=file.name.split('/')[-1].split('.')[-1]
                name=file.name.split('/')[-1].split('.')[0]
            response_data = {
                'data': ser_data.data[i],
                'text': text,
                'name':name,
                'postfix':postfix

            }
            my_list.append(response_data)
            for index, d in enumerate(my_list):
                my_dict[index] = d             
        return Response(data=my_dict, status=status.HTTP_200_OK)
    

#----------------------------------------------------------------
#در این کلاس یک رکورد از جدول داکیومنت رو با استفاده از آی دی رکورد حذف می کنیم
class DeleteDocument(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request):
        id=request.GET['id']
        document.objects.filter(id=id).delete()
        documents = document.objects.all()
        ser_data= DocumentSerialiser(instance=documents,many=True)
        return Response(data = ser_data.data,status=status.HTTP_200_OK)
#----------------------------------------------------------------
#در این کلاس یک رکورد از جدول ایمیج رو با استفاده از آی دی رکورد حذف می کنیم
class DeleteImage(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request):
        id=request.GET['id']
        Image.objects.filter(id=id).delete()
        image = Image.objects.all()
        ser_data= ImageSerialiser(instance=image,many=True)
        return Response(data = ser_data.data,status=status.HTTP_200_OK)
    

#---------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

#پیاده سازی کلاس فکتوری،این کلاس رو با استفاده از رست فریمورک فراخوانی کردم و اطلاعات فراخوانی شده رو در کنسول چاپ کردم
class FileMetadata(ABC):
    @abstractmethod
    def extract_metadata(self, file_path):
        pass

    @abstractmethod
    def store_metadata(self, metadata):
        pass

class ImageMetadata(FileMetadata):
    def extract_metadata(self, item):
        metadata = {'name': item.name, 'postfix': item.postfix, 'register-date': item.register_date,'path': item.path}
        return metadata

    def store_metadata(self, metadata):
        print("--------------------------------")
        print("Storing image metadata:", metadata)
        print("--------------------------------")


class DocumentMetadata(FileMetadata):
    def extract_metadata(self, item):
        metadata = {'name': item.name, 'postfix': item.postfix, 'register-date': item.register_date,'path': item.path}
        return metadata

    def store_metadata(self, metadata):
        print("--------------------------------")
        print("Storing document metadata:", metadata)
        print("--------------------------------")


class MetadataFactory:
    def create_metadata(self, file_type):
        if file_type == 'image':
            return ImageMetadata()
        elif file_type == 'document':
            return DocumentMetadata()
        else:
            raise ValueError("Unsupported file type")


class Factory(APIView):
    def get(self,request):
        factory = MetadataFactory()

        image_metadata = factory.create_metadata('image')

        images= Image.objects.all()
        for item in images:
            image_data = image_metadata.extract_metadata(item)
            image_metadata.store_metadata(image_data)

        document_metadata = factory.create_metadata('document')
        
        documents=document.objects.all()
        for item in documents:
            document_data = document_metadata.extract_metadata(item)
            document_metadata.store_metadata(document_data)
        return Response({'نتیجه':'ذخیره سازی انجام شد'})
#قسمت های گوگل کلود و آمازون 3 با توجه به تحریم بودن ایران پیاده سازیشون امکان پذیر نیست 
#----------------------------------------------------------------
# استفاده از ماژول‌های مورد نیاز
# from storages.backends.s3boto3 import S3Boto3Storage
# from django.conf import settings
# # این بخش برای تنظیم کلاس‌های ذخیره‌سازی فایل است. برای مثال:
# class CustomS3Boto3Storage(S3Boto3Storage):
#     location = 'your-custom-location'

# # این بخش برای ادغام کلاس‌های ذخیره‌سازی فایل با نقاط پایانی بارگذاری فایل است. برای مثال:
# from django.core.files.storage import default_storage
# default_storage._wrapped = CustomS3Boto3Storage()