from celery import shared_task
import time

import flask_excel
from backend.models import Blog

@shared_task(ignore_result = False)
def add(x,y):
    time.sleep(10)
    return x+y
    

@shared_task(bind = True, ignore_result = False)
def create_csv(self):
    resource = Blog.query.all()

    task_id = self.request.id
    filename = f'blog_data_{task_id}.csv'
    column_names = [column.name for column in Blog.__table__.columns]
    print(column_names)
    csv_out = flask_excel.make_response_from_query_sets(resource, column_names = column_names, file_type='csv' )

    with open(f'./backend/celery/user-downloads/{filename}', 'wb') as file:
        file.write(csv_out.data)
    
    return filename