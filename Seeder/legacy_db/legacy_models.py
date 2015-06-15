# Legacy model for extracting data from old system
#
# from __future__ import unicode_literals
#
# from django.db import models
#
#
#
#
#

# class Correspondence(models.Model):
#     resource_id = models.IntegerField()
#     correspondence_type_id = models.IntegerField(blank=True, null=True)
#     date = models.DateTimeField()
#     result = models.SmallIntegerField(blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'correspondence'
#
#
# class CorrespondenceType(models.Model):
#     type = models.CharField(unique=True, max_length=45)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'correspondence_type'
#
#
# class Keywords(models.Model):
#     id = models.IntegerField(primary_key=True)
#     keyword = models.CharField(max_length=100)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'keywords'
#
#
# class KeywordsResources(models.Model):
#     resource_id = models.IntegerField()
#     keyword = models.ForeignKey(Keywords)
#
#     class Meta:
#         managed = False
#         db_table = 'keywords_resources'
#         unique_together = (('resource_id', 'keyword_id'),)
#
#
# class QaChecks(models.Model):
#     resource = models.ForeignKey('Resources')
#     curator = models.ForeignKey(Curators)
#     date_checked = models.DateTimeField()
#     date_crawled = models.DateField(blank=True, null=True)
#     result = models.SmallIntegerField(blank=True, null=True)
#     solution = models.SmallIntegerField(blank=True, null=True)
#     solution_date = models.DateField(blank=True, null=True)
#     solution_user = models.IntegerField(blank=True, null=True)
#     proxy_problems = models.TextField(blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
#     image = models.CharField(max_length=255, blank=True, null=True)
#     ticket_no = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'qa_checks'
#
#
# class QaChecksQaProblems(models.Model):
#     qa_check = models.ForeignKey(QaChecks)
#     qa_problem = models.ForeignKey('QaProblems')
#     url = models.CharField(max_length=255, blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'qa_checks_qa_problems'
#
#
# class QaProblems(models.Model):
#     problem = models.CharField(max_length=45)
#     description = models.CharField(max_length=255)
#     question = models.CharField(max_length=255)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'qa_problems'
#
#
# class ResourceStatus(models.Model):
#     status = models.CharField(max_length=45)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'resource_status'
#
#
# class Roles(models.Model):
#     name = models.CharField(unique=True, max_length=45)
#     description = models.CharField(max_length=255)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'roles'
#
#
# class SeedStatus(models.Model):
#     status = models.CharField(unique=True, max_length=45)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'seed_status'
#
#
# class Subcontracts(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent = models.ForeignKey(Contracts)
#     date_signed = models.DateTimeField()
#     blanco = models.IntegerField(blank=True, null=True)
#     addendum = models.IntegerField(blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'subcontracts'
#
#
# class SuggestedBy(models.Model):
#     proposer = models.CharField(unique=True, max_length=45)
#     comments = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'suggested_by'