import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newscrapper.settings')

app = Celery('newscrapper')

app.config_from_object('django.conf:settings')

app.conf.schedule_beat = {
    'every_1_hour':{
        'task':'scrapper.tasks.newsUpdate',
        'schedule':crontab(hour='*', minute='1'),
        'args':()
    }
}

app.conf.time_zone='UTC'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')