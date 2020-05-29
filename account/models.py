import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from account.managers import UserManager
from core.models import TimeStampModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    uid = models.UUIDField(verbose_name='사용자 UID', unique=True, default=uuid.uuid4, editable=False,
                           help_text='사용자 이메일을 대신해 사용자를 구분합니다.')
    email = models.EmailField(verbose_name='사용자 이메일', unique=True, db_index=True, blank=True, null=True)

    is_staff = models.BooleanField(verbose_name='사용자의 staff 여부', default=False)
    is_active = models.BooleanField(verbose_name='사용자의 활동 상태', default=True,
                                    help_text='사용자가 탈퇴할 경우 False로 변합니다.')

    objects = UserManager()
    USERNAME_FIELD = 'uid'

    def __str__(self):
        return f'({self.id}) User'
