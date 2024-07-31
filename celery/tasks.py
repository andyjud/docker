from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(name='count_to_10')     
def count_task():  
    logger.info("Task started: Count to 10")      
    for i in range(1, 11):
        logger.info(i)
        time.sleep(1)
    logger.info("Task completed!")
    return 'Task Done!'


@shared_task(name='send_newsletter')  
def send_newsletter():
    logger.info("Task started: Sending Newsletters")      
    for i in range(1, 11):
        logger.info(f'{i}. Newsletter')
        time.sleep(1)
    logger.info("All Newsletter sent!")       
    return 'Completed!'
