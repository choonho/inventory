from mongoengine import *
from datetime import datetime
from spaceone.core.model.mongo_model import MongoModel
from spaceone.inventory.model.job_model import Job

class Error(EmbeddedDocument):
    error_code = StringField(max_length=128)
    message = StringField(max_length=2048)
    additional = DictField()

class JobTask(MongoModel):
    job_task_id = StringField(max_length=40, generate_id='job_task', unique=True)
    state = StringField(max_length=20, default='PENDING',
                        choices=('PENDING', 'IN_PROGRESS', 'SUCCESS', 'FAILURE'))
    created_count = IntField()
    updated_count = IntField()
    failure_count = IntField()
    errors = ListField(EmbeddedDocumentField(Error, default=None, null=True))
    job_id = StringField(max_length=40)
    secret_id = StringField(max_length=40)
    provider = StringField(max_length=40, default=None, null=True)
    service_account_id = StringField(max_length=40, default=None, null=True)
    project_id = StringField(max_length=255, default=None, null=True)
    domain_id = StringField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    started_at = DateTimeField(default=None, null=True)
    finished_at = DateTimeField(default=None, null=True)

    meta = {
        'updatable_fields': [
            'state',
            'secret_id',
            'provider',
            'service_account_id',
            'project_id',
            'created_count',
            'updated_count',
            'failure_count',
            'errors',
            'started_at',
            'finished_at'
        ],
        'exact_fields': [
            'job_task_id',
            'state',
            'job_id',
            'secret_id',
            'provider',
            'service_account_id',
            'project_id',
            'domain_id',
        ],
        'minimal_fields': [
            'job_task_id',
            'state',
            'created_count',
            'updated_count',
            'failure_count',
            'job_id',
            'created_at',
            'started_at',
            'finished_at',
        ],
        'ordering': [
            '-created_at'
        ],
        'indexes': [
            'job_task_id',
            'state',
            'job_id',
            'secret_id',
            'provider',
            'service_account_id',
            'project_id',
            'domain_id',
        ]
    }