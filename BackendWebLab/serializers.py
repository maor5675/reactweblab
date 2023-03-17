from rest_framework import serializers
from .models import Phone,Phonetype,Phonebrand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonebrand
        fields = '__all__'

         
class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(source='type.brand')
    type = PhoneTypeSerializer()

    class Meta:
        model = Phone
        fields = '__all__'
        

## i think i do all the serilizer and i do ot correctly leave it alone if you dont get any bugs        