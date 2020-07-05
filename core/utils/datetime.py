from datetime import datetime
from typing import Tuple

from django.utils import timezone

from core.utils.typing import typechecking


@typechecking
def default_start_end_date() -> Tuple[datetime, datetime]:
    """
    기본적인 start_date(시작 시간)와 end_date(종료 시간)을 반환합니다.
    - start_date : 1970년 01월 01일 00시 00분
    - end_date   : 2099년 12월 31일 23시 59분
    """
    start_date = timezone.datetime(year=1970, month=1, day=1)
    end_date = timezone.datetime(year=2100, month=1, day=1) - timezone.timedelta(seconds=1)

    return start_date, end_date
