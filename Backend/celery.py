
# import os
# from celery import Celery
# from celery.schedules import crontab

  

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
  
# app = Celery('Backend')
# app.config_from_object('django.conf:settings',namespace='CELERY')
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'delete_activation_link': {
#         'task': 'Account.views.delete_activation_link',
#         'schedule': crontab(minute=1),  
#     },
# }