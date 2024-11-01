from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, user_name, academic_email, academic_year, password=None):
        if not user_name:
            raise ValueError('Users must have a user name')
        if not academic_email:
            raise ValueError('Users must have an academic email')
        if not academic_year:
            raise ValueError('Users must have an academic year')

        user = self.model(
            user_name=user_name,
            academic_email=self.normalize_email(academic_email),
            academic_year=academic_year,
        )
        if password:
            user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, academic_email, academic_year, password=None):
        user = self.create_user(
            user_name,
            academic_email,
            academic_year,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    academic_email = models.EmailField(unique=True, null=False, blank=False)
    academic_year = models.IntegerField(choices=[
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ])
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['academic_email', 'academic_year']

    def __str__(self):
        return self.user_name

class Request(models.Model):
    class RequestState(models.TextChoices):
        OPEN = 'open', 'Open'
        CLOSE = 'close', 'Close'

    request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    request_description = models.TextField()
    request_current_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=6,
        choices=RequestState.choices,
        default=RequestState.OPEN
    )
    proofs = models.FileField(upload_to='proofs/', default='path/to/default/file.pdf')  # Keep this as a single FileField

    def __str__(self):
        return f"{self.request_description} - {self.state} by {self.user_id.user_name}"
