from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(verbose_name='생성 시간', auto_now_add=True, db_index=True, help_text='생성 시간')
    updated_at = models.DateTimeField(verbose_name='수정 시간', auto_now=True, db_index=True, help_text='수정 시간')

    class Meta:
        abstract = True
