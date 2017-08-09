from shreableUrl.apps.snippet.models import Snippet
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('data',)