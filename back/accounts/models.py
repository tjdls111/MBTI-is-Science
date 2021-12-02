from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, mbti, poster_number, password=None, ):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            mbti = mbti,
            poster_number = poster_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, mbti,  password):
        user = self.create_user(
            username= username,          
            mbti = mbti,
            password=password    
        )

        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True 
        
        user.save(using=self._db)
        return user



class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    
    MBTI_CHOICES = (
        ('ENTJ', 'ENTJ'),
        ('ENTP', 'ENTP'),
        ('ENFJ', 'ENFJ'),
        ('ENFP', 'ENFP'),
        ('ESTJ', 'ESTJ'),
        ('ESTP', 'ESTP'),
        ('ESFJ', 'ESFJ'),
        ('ESFP', 'ESFP'),
        ('INTJ', 'INTJ'),
        ('INTP', 'INTP'),
        ('INFJ', 'INFJ'),
        ('INFP', 'INFP'),
        ('ISTJ', 'ISTJ'),
        ('ISTP', 'ISTP'),
        ('ISFJ', 'ISFJ'),
        ('ISFP', 'ISFP'),
        ('IDKW',"I Don't know")
    )
    mbti = models.CharField(max_length=5, choices=MBTI_CHOICES)
    poster_number = models.IntegerField(default=0)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['mbti',]

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username

