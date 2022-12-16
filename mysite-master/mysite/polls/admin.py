from django.contrib import admin
from .models import Question, Choice, User, Vote
from .forms import RequiredInlineFormSet

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    formset = RequiredInlineFormSet
    fields = ('choice_text',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'surname', 'avatar', 'email')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    model = Vote

