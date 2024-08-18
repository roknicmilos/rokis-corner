from django.contrib import admin

from cv.admin import (
    EmploymentInline,
    LinkInline,
    SkillInline,
    LanguageInline,
    InternshipInline,
)
from cv.models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    inlines = [
        LinkInline,
        SkillInline,
        LanguageInline,
        EmploymentInline,
        InternshipInline,
    ]
