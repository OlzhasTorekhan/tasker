from django.db.models import Model,AutoField,TextField,CASCADE,BooleanField,DateTimeField,SmallIntegerField,ManyToOneRel,ForeignKey
from django.conf import settings
# Create your models here.


class Project(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    name = TextField('name',null=False,blank=False)
    favorite = BooleanField('favorite',default=False)
    own_user = ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)

class ToDoItem(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    title = TextField('title',null=False,blank=False)
    complete = BooleanField('complete',default=False)
    project = ForeignKey(Project,on_delete=CASCADE)

class SubTasks(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    title = TextField('title',null=False,blank=False)
    description = TextField('description')
    deadline = DateTimeField('deadline')
    do_notify = BooleanField('do_notify',default=False)
    notify_period = DateTimeField('notify_period',null=True)
    priority = SmallIntegerField('priority')
    todositem = ForeignKey(ToDoItem,on_delete=CASCADE)


