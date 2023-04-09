import time

from celery import shared_task
from . import models


@shared_task()
def add(x, y):
    result = x + y
    print(result)
    return result


@shared_task()
def create_data(title: str):

    data = []
    for i in title:
        data.append(i)
    for data_row in data:
        time.sleep(5)
        models.Data.objects.create(title=data_row)
    print("ALL data was created")
