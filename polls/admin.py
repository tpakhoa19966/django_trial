from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,       {'fields': ['question_text']}),
		('Datetime', {'fields': ['pub_date'], 'classes':'colappse'}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# Register your models here.
