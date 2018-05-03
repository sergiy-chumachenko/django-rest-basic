from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('url', 'name', 'paradigm')
        view_name = 'languages:language-detail'