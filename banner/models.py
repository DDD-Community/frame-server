from django.db import models
from django.utils import timezone

from core.utils.datetime import default_start_end_date


class Banner(models.Model):
    class BannerType(models.IntegerChoices):
        MAIN = 1
        STORY = 2
        EVENT = 3

    type = models.IntegerField(verbose_name='배너 종류', choices=BannerType.choices)

    title = models.CharField(max_length=100, verbose_name='배너 제목')
    description = models.TextField(verbose_name='배너 내용', blank=True)
    image = models.ImageField(upload_to='banner', verbose_name='배너 배경 이미지', blank=True, null=True)

    start_at = models.DateTimeField(verbose_name='앱 노출 시작 시간', default=default_start_end_date()[0])
    end_at = models.DateTimeField(verbose_name='앱 노출 종료 시간', default=default_start_end_date()[1])
    visible = models.BooleanField(verbose_name='앱 노출 여부', default=False,
                                  help_text='True로 설정하여 앱에 노출시킬 수 있습니다.')

    class Meta:
        index_together = (
            ('visible', 'start_at', 'end_at',),
        )
