"""
Created on 06.04.2018
:author Tatiana Korchuganova
Here are the models for runningprod views
"""


from __future__ import unicode_literals


from django.db import models
models.options.DEFAULT_NAMES += ('allColumns', 'orderColumns', \
                                 'primaryColumns', 'secondaryColumns', \
                                 'columnTitles', 'filterFields',)


class RunningMCProductionTasks(models.Model):
    campaign = models.CharField(max_length=72, db_column='CAMPAIGN', blank=True)
    reqid = models.IntegerField(null=True, db_column='REQID', blank=True)
    jeditaskid = models.BigIntegerField(db_column='JEDITASKID', primary_key=True)
    rjobs = models.IntegerField(null=True, db_column='RJOBS', blank=True)
    status = models.CharField(max_length=192, db_column='STATUS')
    totevrem = models.BigIntegerField(db_column='TOTEVREM')
    totev = models.BigIntegerField(db_column='TOTEV')
    nfilesfailed = models.IntegerField(null=True, db_column='NFILESFAILED', blank=True)
    workinggroup = models.CharField(max_length=96, db_column='WORKINGGROUP', blank=True)
    currentpriority = models.IntegerField(null=True, db_column='CURRENTPRIORITY', blank=True)
    processingtype = models.CharField(max_length=192, db_column='PROCESSINGTYPE', blank=True)
    corecount = models.IntegerField(null=True, db_column='CORECOUNT', blank=True)
    creationdate = models.DateTimeField(db_column='CREATIONDATE')
    taskname = models.CharField(max_length=384, db_column='TASKNAME', blank=True)
    splitrule = models.CharField(max_length=300, db_column='SPLITRULE', blank=True)
    username = models.CharField(max_length=384, db_column='USERNAME')
    cputime = models.IntegerField(null=True,db_column='CPUTIME', blank=True)
    site = models.CharField(max_length=384, db_column='SITE')
    class Meta:
        db_table = u'"ATLAS_PANDABIGMON"."RUNNINGMCPRODUCTIONTASKS"'

class RunningDPDProductionTasks(models.Model):
    campaign = models.CharField(max_length=72, db_column='CAMPAIGN', blank=True)
    reqid = models.IntegerField(null=True, db_column='REQID', blank=True)
    jeditaskid = models.BigIntegerField(db_column='JEDITASKID', primary_key=True)
    rjobs = models.IntegerField(null=True, db_column='RJOBS', blank=True)
    status = models.CharField(max_length=192, db_column='STATUS')
    totevrem = models.BigIntegerField(db_column='TOTEVREM')
    totev = models.BigIntegerField(db_column='TOTEV')
    nfilesfailed = models.IntegerField(null=True, db_column='NFILESFAILED', blank=True)
    workinggroup = models.CharField(max_length=96, db_column='WORKINGGROUP', blank=True)
    currentpriority = models.IntegerField(null=True, db_column='CURRENTPRIORITY', blank=True)
    processingtype = models.CharField(max_length=192, db_column='PROCESSINGTYPE', blank=True)
    corecount = models.IntegerField(null=True, db_column='CORECOUNT', blank=True)
    creationdate = models.DateTimeField(db_column='CREATIONDATE')
    taskname = models.CharField(max_length=384, db_column='TASKNAME', blank=True)
    splitrule = models.CharField(max_length=300, db_column='SPLITRULE', blank=True)
    username = models.CharField(max_length=384, db_column='USERNAME')
    outputtype = models.CharField(max_length=384, db_column='OUTPUTTYPE')
    cputime = models.IntegerField(null=True,db_column='CPUTIME', blank=True)
    class Meta:
        db_table = u'"ATLAS_PANDABIGMON"."RUNNINGDPDPRODUCTIONTASKS"'

class RunningProdTasksModel(models.Model):
    campaign = models.CharField(max_length=72, db_column='CAMPAIGN', blank=True)
    reqid = models.IntegerField(null=True, db_column='REQID', blank=True)
    runnumber = models.IntegerField(null=True, db_column='RUNNUMBER', blank=True)
    jeditaskid = models.BigIntegerField(db_column='JEDITASKID', primary_key=True)
    rjobs = models.IntegerField(null=True, db_column='RJOBS', blank=True)
    slots = models.IntegerField(null=True, db_column='SLOTS', blank=True)
    aslots = models.IntegerField(null=True, db_column='ASLOTS', blank=True)
    status = models.CharField(max_length=192, db_column='STATUS')
    superstatus = models.CharField(max_length=192, db_column='SUPERSTATUS')
    neventstobeused = models.BigIntegerField(db_column='NEVENTSTOBEUSED')
    neventsused = models.BigIntegerField(db_column='NEVENTSUSED')
    nevents = models.BigIntegerField(db_column='NEVENTS')
    percentage = models.BigIntegerField(db_column='PERCENTAGE')
    nfilesfailed = models.IntegerField(null=True, db_column='NFILESFAILED', blank=True)
    workinggroup = models.CharField(max_length=96, db_column='WORKINGGROUP', blank=True)
    priority = models.IntegerField(null=True, db_column='CURRENTPRIORITY', blank=True)
    processingtype = models.CharField(max_length=192, db_column='PROCESSINGTYPE', blank=True)
    corecount = models.IntegerField(null=True, db_column='CORECOUNT', blank=True)
    age = models.IntegerField(db_column='AGE', blank=True)
    creationdate = models.DateTimeField(db_column='CREATIONDATE')
    username = models.CharField(max_length=384, db_column='USERNAME')
    cputime = models.IntegerField(null=True,db_column='CPUTIME', blank=True)
    site = models.CharField(max_length=384, db_column='SITE', blank=True)
    outputdatasettype = models.CharField(max_length=384, db_column='OUTPUTDATASETTYPE')
    ptag = models.CharField(max_length=72, db_column='PTAG', blank=True)
    simtype = models.CharField(max_length=72, db_column='SIMTYPE', blank=True)
    gshare = models.CharField(max_length=72, db_column='GSHARE', blank=True)
    hashtags = models.CharField(max_length=400, db_column='HASHTAGS', blank=True)
    eventservice = models.IntegerField(null=True, db_column='EVENTSERVICE', blank=True)
    neventsrunning = models.BigIntegerField(db_column='NRUNNINGEVENTS')
    class Meta:
        db_table = u'"ATLAS_PANDABIGMON"."RUNNINGPRODTASKS"'

class RunningProdRequestsModel(models.Model):
    reqid = models.IntegerField(db_column='REQID', primary_key=True)
    ntasks = models.IntegerField(null=True, db_column='NTASKS', blank=True)
    rjobs = models.IntegerField(null=True, db_column='RJOBS', blank=True)
    slots = models.IntegerField(null=True, db_column='SLOTS', blank=True)
    aslots = models.IntegerField(null=True, db_column='ASLOTS', blank=True)
    neventstobeused = models.BigIntegerField(db_column='NEVENTSTOBEUSED')
    neventsused = models.BigIntegerField(db_column='NEVENTSUSED')
    nevents = models.BigIntegerField(db_column='NEVENTS')
    percentage = models.BigIntegerField(db_column='PERCENTAGE')
    nfilesfailed = models.IntegerField(null=True, db_column='NFILESFAILED', blank=True)
    avgpriority = models.IntegerField(null=True, db_column='AVGPRIORITY', blank=True)
    corecount = models.IntegerField(null=True, db_column='CORECOUNT', blank=True)
    creationdate = models.DateTimeField(db_column='CREATIONDATE')
    cputime = models.IntegerField(null=True,db_column='CPUTIME', blank=True)
    class Meta:
        db_table = u'"ATLAS_PANDABIGMON"."RUNNING_PROD_REQUESTS"'
