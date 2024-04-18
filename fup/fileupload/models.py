from django.db import models
from django.core.files.storage import FileSystemStorage

#پیاده سازی مدل با استفاده از  نام پسوند تاریخ درج و مسیر ذخیره عکس
class Image(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    postfix = models.CharField(max_length=20,blank=True,null=True)
    register_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    path = models.ImageField(upload_to='path/images',default="path/images/nophoto.png")
    
    def __str__(self) -> str:
        return f"{self.name}"
    
#پیاده سازی مدل با استفاده از  نام پسوند تاریخ درج و مسیر ذخیره داکیومنت
class document(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    postfix = models.CharField(max_length=20,blank=True,null=True)
    register_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    path = models.FileField(upload_to='path/documents', max_length=100,blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"

#ساخت یک نمونه از کلاس با توجه سیستم فایل سیستم استوریج    
class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/', storage=FileSystemStorage())

