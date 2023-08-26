from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=True)
    objects = UserManager()#This will hold all the value of usemanger file as object
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    
    @property#this decorator allow to get the balance of the account
    def balance(self):
        if hasattr(self,'account'):
            return self.account.balance
        return 0
    
    