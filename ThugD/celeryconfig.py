#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Exchange, Queue

BROKER_URL = 'mongodb://ec2-72-44-33-186.compute-1.amazonaws.com:27017/thugd/'
BROKER_CONNECTION_TIMEOUT = 4  # Default Value
BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_MAX_RETRIES = 100	# Default Value
""" MongoDB as Broker """

# Time in Seconds
BROKER_HEARTBEAT = 4
# Rate
BROKER_HEARTBEAT_CHECKRATE = 2
""" Broker Heartbeat Settings => Time(sec.) = Broker_Heartbeat(sec.)/Rate """

CELERY_RESULT_BACKEND = 'mongodb://ec2-72-44-33-186.compute-1.amazonaws.com:27107/'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'thugd',
    'taskmeta_collection': 'thugd_taskmeta_collection',
}
CELERY_RESULT_EXCHANGE = 'thugresults'
CELERY_RESULT_EXCHANGE_TYPE = 'direct'

""" MongoDB as backend to store task state and results """

CELERY_RESULT_PERSISTENT = True
""" Msg will not be lost if broker restarts/shutdown """

CELERY_TASK_RESULT_EXPIRES = None		#Never Expires(eg. 24*3600->1 day)
""" Time after which task results would delete """

CELERY_DEFAULT_QUEUE = 'generic'
CELERY_DEFAULT_EXCHANGE = 'generic'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_BINDING = 'generic'
CELERY_DEFAULT_ROUTING_KEY = 'generic'
CELERY_DEFAULT_DELIVERY_MODE = 'persistent'
""" Default Queue Configuration """

CELERY_ACKS_LATE = True
""" ACKS_LATE means that tasks msgs will be acknowledged after task has been
    executed and then only it will be deleted from queue.
"""

CELERYD_PREFETCH_MULTIPLIER = 2
""" Giving each worker only TWO task at a time """

# No. of Concurrent worker processes/threads executing tasks
CELERYD_CONCURRENCY = 4
""" Concurrency Settings """

CELERY_MESSAGE_COMPRESSION = None
""" Message Settings """

# Task reports its status as "started" when task is executed on worker
CELERY_TRACK_STARTED = True
CELERY_TASK_PUBLISH_RETRY = True
""" Tasks Settings """
