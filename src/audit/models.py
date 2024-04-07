# from django.db import models

# from django.db import models

# class ProcedureAud(models.Model):
#     procedureAudID = models.AutoField(primary_key=True)
#     UserID = models.IntegerField()
#     ContractID = models.IntegerField()
#     ProcedureName = models.CharField(max_length=255)
#     Timestamp = models.DateTimeField(default=models.DateTimeField)

# class ActionAudit(models.Model):
#     AuditID = models.AutoField(primary_key=True)
#     UserID = models.IntegerField()
#     ActionID = models.IntegerField()
#     Sign = models.CharField(max_length=1)
#     OperationID = models.IntegerField()
#     OperDate = models.DateField()
#     ContractID = models.IntegerField()
#     AmountTypeID = models.IntegerField()
#     ActionTypeID = models.IntegerField()
#     PaymentTypeID = models.IntegerField()
#     IssueDate = models.DateField()
#     RepaymentDate = models.DateField()
#     IsOutBalance = models.BooleanField()
#     AmountLocalCur = models.DecimalField(max_digits=10, decimal_places=2)
#     AmountForeignCur = models.DecimalField(max_digits=10, decimal_places=2)
#     AuditDate = models.DateTimeField(auto_now_add=True)
#     procedureAudID = models.IntegerField()

# class OperationAudit(models.Model):
#     AuditID = models.AutoField(primary_key=True)
#     UserID = models.IntegerField()
#     OperationID = models.IntegerField()
#     Type = models.CharField(max_length=255)
#     Version = models.IntegerField()
#     OperDate = models.DateField()
#     TimeInMillis = models.BigIntegerField()
#     ContractID = models.IntegerField()
#     DocumentID = models.IntegerField()
#     AmountTypeID = models.IntegerField()
#     ActionTypeID = models.IntegerField()
#     PaymentTypeID = models.IntegerField()
#     IsOutBalance = models.BooleanField()
#     FundTransactionID = models.IntegerField()
#     TotalLocalCur = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalForeignCur = models.DecimalField(max_digits=10, decimal_places=2)
#     RealDate = models.DateField()
#     IsAutoAccept = models.BooleanField()
#     CollateralID = models.IntegerField()
#     CollateralActionTypeID = models.IntegerField()
#     StoringPlaceID = models.IntegerField()
#     AuditDate = models.DateTimeField(auto_now_add=True)

# class TrancheAudit(models.Model):
#     AuditID = models.AutoField(primary_key=True)
#     TrancheID = models.IntegerField()
#     UserID = models.IntegerField()
#     Version = models.IntegerField()
#     ScheduleID = models.IntegerField()
#     IssueDate = models.DateField()
#     RepaymentDate = models.DateField()
#     Principal = models.DecimalField(max_digits=10, decimal_places=2)
#     Interest = models.DecimalField(max_digits=10, decimal_places=2)
#     IsLgot = models.CharField(max_length=1)
#     AuditDate = models.DateTimeField(auto_now_add=True)
#     procedureAudID = models.IntegerField()

# Create your models here.
