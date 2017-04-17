from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger


from .utils import (
    send_sms_notification,
    send_email_notification
)


logger = get_task_logger(__name__)


@task(name = "task_new_merchant_sms_notification", bind=True)
def task_new_merchant_sms_notification(phone, msg):
    """ Send Sms Notification """
    send_sms_notification(phone, msg)
    logger.info("SMS SENT")


@task(name = "task_email_notification", bind=True)
def task_email_notification(self, email, msg):
    send_email_notification(email, msg)
    logger.info("SENT")
