import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newscrapper.settings')

app = Celery('newscrapper')

app.conf.time_zone='UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every_1_hour':{
        'task':'scrapper.tasks.newsUpdate',
        'schedule':15,
        # 'schedule':crontab(hour='*', minute='1'),
    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')