from rest_framework import serializers
from .models import Image,document

class ImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
    #validation error
    def validate_name(self, name):
        if len(name) < 2:
            raise serializers.ValidationError('نام عکس باید بیشتر از 1 کاراکتر باشد')
        return name
    
    #validation error
    def validate(self,data):
        if data['postfix'] != 'jpg' and data['postfix'] != 'png':
            raise serializers.ValidationError("پسوند عکس حتما باید jpg یا png باشد ...")
        return data

class DocumentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = document
        fields = '__all__'

    #validation error
    def validate_name(self, name):
        if len(name) < 3:
            raise serializers.ValidationError('نام عکس باید بیشتر از 2 کاراکتر باشد')
        return name
    
    #validation error
    def validate(self,data):
        if data['postfix'] != 'docx':
            raise serializers.ValidationError("نام فایل باید با پسوند docx باشد ...")
        return data
