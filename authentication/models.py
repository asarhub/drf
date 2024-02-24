from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
print(User)
