# celeryconfig.py
# coding=utf-8


BROKER_URL = 'redis://172.16.203.129:6379/8'
CELERY_RESULT_BACKEND = 'redis://172.16.203.129:6379/9'

# Tasks 位于 worker.py 中
CELERY_IMPORTS = ('wvs_tasks', )

# 默认为1次/秒的任务
CELERY_ANNOTATIONS = {'wvs_tasks.wvs_spider_dispatch': {'rate_limit': '1/s'}}

CELERY_ROUTES = {'wvs_tasks.wvs_spider_dispatch': {'queue': 'add'},
                 'wvs_tasks.error_handler': {'queue': 'error'}}

# 默认所有格式为 json
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
