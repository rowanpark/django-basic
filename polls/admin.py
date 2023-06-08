from django.contrib import admin
from polls.models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 필드 순서 변경하기
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]  # 각 필드를 분리해서 보여주기
    inlines = [ChoiceInline]  # Question 및 Choice 한 화면에서 같이 보기
    list_display = ('question_text', 'pub_date')  # 레코드 리스트 컬럼 항목 지정 (각 레코드의 제목 정하기)
    list_filter = ['pub_date']  # 필터 사이드 바 추가
    search_fields = ['question_text']  # 검색 박스 추가


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
