from django.db import models

# Create your models here.
from django.db import models

# Enum Fields
ACTIVITY_STATUS_CHOICES = [
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Ongoing', 'Ongoing'),
]

QUARTERS_CHOICES = [
    ('Q1', 'Q1'),
    ('Q2', 'Q2'),
    ('Q3', 'Q3'),
    ('Q4', 'Q4'),
]

# Tables from cwb_choice schema
class ActivityStatus(models.Model):
    status = models.CharField(max_length=25, choices=ACTIVITY_STATUS_CHOICES)

class NCFFTeam(models.Model):
    name = models.CharField(max_length=50)

class CommunityCollaborative(models.Model):
    name = models.CharField(max_length=100)

# Tables from cwb_supp schema
class ChangeIndicator(models.Model):
    related_goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    indicator = models.CharField(max_length=255)

class PerformanceMeasure(models.Model):
    related_goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    measure = models.CharField(max_length=255)

class DHHPriority(models.Model):
    related_goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    priority_description = models.CharField(max_length=255)

# Tables from cwb_core schema
class Goal(models.Model):
    goal_number = models.IntegerField()
    goal_name = models.CharField(max_length=255)

class Objective(models.Model):
    objective_number = models.IntegerField()
    objective_name = models.CharField(max_length=255)
    related_goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

class Strategy(models.Model):
    strategy_number = models.CharField(max_length=9)
    strategy_name = models.CharField(max_length=255)
    related_goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    related_objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

# Activity tables
class CommunityActivity(models.Model):
    # Your other fields here
    status = models.CharField(
        max_length=25,
        choices=[
            ('Not Started', 'Not Started'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed'),
            ('Ongoing', 'Ongoing')
        ],
    )
    related_goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    related_strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    related_objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

class StrategyActivity(models.Model):
    # Your other fields here
    status = models.CharField(
        max_length=25,
        choices=[
            ('Not Started', 'Not Started'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed'),
            ('Ongoing', 'Ongoing')
        ],
    )
    related_goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    related_strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    related_objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

# Junction table
class StrategyPriority(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    community_collab = models.ForeignKey(CommunityCollaborative, on_delete=models.CASCADE)
