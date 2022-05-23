from django.db.models import Model,AutoField,ForeignObject,TextField,CASCADE,BooleanField,DateTimeField,SmallIntegerField

# Create your models here.
class SubTasks(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    title = TextField('title',null=False,blank=False)
    description = TextField('description')
    deadline = DateTimeField('deadline')
    do_notify = BooleanField('do_notify',default=False)
    notify_period = DateTimeField('notify_period',null=True)
    priority = SmallIntegerField('priority')

class ToDoItem(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    title = TextField('title',null=False,blank=False)
    complete = BooleanField('complete',default=False)
    sub_tasks = ForeignObject()

class Project(Model):
    id = AutoField('id',primary_key=True,null=False,blank=False)
    name = TextField('name',null=False,blank=False)
    favorite = BooleanField('favorite',default=False)
    items = ForeignObject(ToDoItem,on_delete=CASCADE)

