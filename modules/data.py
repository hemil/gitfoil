from datetime import datetime

from django.db import transaction

from wrapper.models import GithubUser
from wrapper.serializers import GithubUserSerializer


def insert_data_to_db(json_user_data):
    user_data = json_user_data.get("items", [])
    insertion_time = datetime.utcnow()
    with transaction.atomic():
        # assuming atomicity is needed. can be removed if not.
        for each_user_data in user_data:
            each_user_data["github_id"] = each_user_data.get("id")
            each_user_data.pop("id")
            each_user_data["api_call_at"] = insertion_time
            user = GithubUser.objects.filter(github_id=each_user_data["github_id"]).first()
            if not user:
                serializer = GithubUserSerializer(data=each_user_data)
            else:
                serializer = GithubUserSerializer(user, each_user_data, partial=True)

            if serializer.is_valid():
                serializer.save()
