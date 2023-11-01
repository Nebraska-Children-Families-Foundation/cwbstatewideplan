from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    ActivityStatus, NCFFTeam, CommunityCollaborative, ChangeIndicator,
    PerformanceMeasure, DHHPriority, Goal, Objective, Strategy,
    CommunityActivity, StrategyActivity, StrategyPriority
)

class ActivityStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)

class NCFFTeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CommunityCollaborativeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ChangeIndicatorAdmin(admin.ModelAdmin):
    list_display = ('related_goal', 'indicator')

class PerformanceMeasureAdmin(admin.ModelAdmin):
    list_display = ('related_goal', 'measure')

class DHHPriorityAdmin(admin.ModelAdmin):
    list_display = ('related_goal', 'priority_description')

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_number', 'goal_name')

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('objective_number', 'objective_name', 'related_goal')

class StrategyAdmin(admin.ModelAdmin):
    list_display = ('strategy_number', 'strategy_name', 'related_goal', 'related_objective')

class CommunityActivityAdmin(admin.ModelAdmin):
    list_display = ('status', 'related_goal', 'related_strategy', 'related_objective')

class StrategyActivityAdmin(admin.ModelAdmin):
    list_display = ('status', 'related_goal', 'related_strategy', 'related_objective')

class StrategyPriorityAdmin(admin.ModelAdmin):
    list_display = ('strategy', 'community_collab')

# Register your models here.
admin.site.register(ActivityStatus, ActivityStatusAdmin)
admin.site.register(NCFFTeam, NCFFTeamAdmin)
admin.site.register(CommunityCollaborative, CommunityCollaborativeAdmin)
admin.site.register(ChangeIndicator, ChangeIndicatorAdmin)
admin.site.register(PerformanceMeasure, PerformanceMeasureAdmin)
admin.site.register(DHHPriority, DHHPriorityAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(CommunityActivity, CommunityActivityAdmin)
admin.site.register(StrategyActivity, StrategyActivityAdmin)
admin.site.register(StrategyPriority, StrategyPriorityAdmin)
