from django.db import models

class RADCHECK(models.Model):
     
     username = models.CharField(max_length=255,null=True)
     attribute = models.CharField(max_length=11,null=True)
     op = models.CharField(max_length=2,null=True,default='==')
     value = models.CharField(max_length=255,null=True)
     
    # username varchar(64) NOT NULL default '',
    # attribute varchar(64)  NOT NULL default '',
    # op char(2) NOT NULL DEFAULT '==',
    # value varchar(253) NOT NULL default '',
    # PRIMARY KEY  (id),
    # KEY username (username(32))
     
     class Meta:
        
        db_table = 'radcheck'

     def __str__(self):

          self.username
          self.attribute
          self.op
          self.value

          return self

class RADREPLY(models.Model):
     
     username = models.CharField(max_length=255,null=True)
     attribute = models.CharField(max_length=11,null=True)
     op = models.CharField(max_length=2,null=True,default='==')
     value = models.CharField(max_length=255,null=True)
     
    # id int(11) unsigned NOT NULL auto_increment,
    # username varchar(64) NOT NULL default '',
    # attribute varchar(64) NOT NULL default '',
    # op char(2) NOT NULL DEFAULT '=',
    # value varchar(253) NOT NULL default '',
    # PRIMARY KEY  (id),
    # KEY username (username(32))
     
     class Meta:
        
        db_table = 'radreply'

     def __str__(self):

          self.username
          self.attribute
          self.op
          self.value

          return self      