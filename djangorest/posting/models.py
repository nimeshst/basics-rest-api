from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse as api_reverse
# Create your models here.


class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # means that when this user instance is deleted everything releated to this
    # is deleted
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud",
                           kwargs={'pk': self.pk},
                           request=request)
