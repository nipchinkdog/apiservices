# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class CommAccounts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20L, blank=True)
    password = models.CharField(max_length=20L, blank=True)
    email = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'comm_accounts'

class CommComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accounts = models.ForeignKey(AuthUser, null=True, blank=True)
    posts = models.ForeignKey('CommPosts', null=True, blank=True)
    note = models.CharField(max_length=120L, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comm_comments'

class CommPosts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accounts = models.ForeignKey(AuthUser, null=True, blank=True)
    tags = models.TextField(blank=True)
    heroes = models.CharField(max_length=120L, blank=True)
    note = models.TextField(blank=True)
    type = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comm_posts'

class CommPostsChall(models.Model):
    id = models.BigIntegerField(primary_key=True)
    posts_origin = models.ForeignKey(CommPosts, null=True, blank=True)
    posts_chall = models.ForeignKey(CommPosts, null=True, blank=True)
    signs = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'comm_posts_chall'

class CommPostsHeroes(models.Model):
    id = models.IntegerField(primary_key=True)
    heroes_origin = models.CharField(max_length=50L, blank=True)
    heroes_chall = models.CharField(max_length=50L, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comm_posts_heroes'

class CommPostsInfos(models.Model):
    id = models.IntegerField(primary_key=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    heroes = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'comm_posts_infos'

class CommVotes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accounts = models.ForeignKey(AuthUser, null=True, blank=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    class Meta:
        db_table = 'comm_votes'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class SocialAuthAssociation(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=255L)
    handle = models.CharField(max_length=255L)
    secret = models.CharField(max_length=255L)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64L)
    class Meta:
        db_table = 'social_auth_association'

class SocialAuthNonce(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=255L)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40L)
    class Meta:
        db_table = 'social_auth_nonce'

class SocialAuthUsersocialauth(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    provider = models.CharField(max_length=32L)
    uid = models.CharField(max_length=255L)
    extra_data = models.TextField()
    class Meta:
        db_table = 'social_auth_usersocialauth'

