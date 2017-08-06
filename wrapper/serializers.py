from .models import GithubUser
from rest_framework.serializers import ModelSerializer


class GithubUserSerializer(ModelSerializer):
    class Meta:
        model = GithubUser
