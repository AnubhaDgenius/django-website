from rest_framework import serializers, permissions
from gallery.models import Notice, Owner,Ques
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes

class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = ('url', 'subject', 'message', 'cr_date','notice_details')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('url', 'name','myimg',' name_pet','type', 'breed','age_pet', 'myimg_pet', 'user')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class QuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ques
        fields = ('url', 'question', 'answer', 'user', 'notice')