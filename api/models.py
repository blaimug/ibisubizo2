from django.db import models

# Create your models here.
class users(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    dataFrom = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField()

# will work with users table
class verification(models.Model): 
    userId = models.IntegerField()
    reason = models.CharField(max_length=50) # can be forgotPassword, Activation, etc...
    method = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    initiated = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()

#  problems table
class problems(models.Model):
    title =  models.CharField(max_length=200)
    text = models.TextField()
    attachementsArray = models.CharField(max_length=200) # arrays
    public = models.BooleanField()
    userId = models.IntegerField()
    datePosted = models.DateTimeField(auto_now_add=True)
    canBeJoined = models.BooleanField()
    groupId = models.IntegerField()
    views = models.IntegerField()
    resolved = models.BooleanField()
    resolvedDateTime = models.DateTimeField()

class groups(models.Model):
    usersArray = models.CharField(max_length=200) #arrays
    problemId = models.IntegerField()

# will work with problems, and replies
class attachements(models.Model):
    name = models.CharField(max_length=200)
    path = models.FilePathField()
    attachementDate = models.DateTimeField(auto_now_add=True)
    attachementType = models.CharField(max_length=50)
    attachementSize = models.CharField(max_length=50)

class replies(models.Model):
    problemId = models.IntegerField()
    userId = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    attachementsArray = models.CharField(max_length=200) # arrays

# will work with replies and problems
class notifications(models.Model):
    notificationType = models.CharField(max_length=50) # can be email, or sms
    message = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField()
    recipient = models.CharField(max_length=200) #can be an array
    recipientName = models.CharField(max_length=50)

class replyReactions(models.Model):
    replyId = models.IntegerField()
    userId = models.IntegerField()
    reactionType = models.CharField(max_length=50) # can either be like, dislike, report
    reactionReason = models.TextField() # if type is report, give a reason
    dateTime = models.DateTimeField(auto_now_add=True)

class problemReactions(models.Model):
    problemId = models.IntegerField()
    userId = models.IntegerField()
    reactionType = models.CharField(max_length=50) # can either be like, dislike, report
    reactionReason = models.TextField() # if type is report, give a reason
    dateTime = models.DateTimeField(auto_now_add=True)
    
