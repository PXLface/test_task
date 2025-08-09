from django.contrib import admin

from rangefilter.filters import DateRangeFilter

from core.apps.dds.models.dds import (
    ChoiceCategory,
    ChoiceOperationType,
    ChoiceStatus,
    ChoiceSubcategory,
    DDS,
)


@admin.register(DDS)
class DDSAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'operation_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = (('created_at', DateRangeFilter), 'status', 'operation_type', 'category', 'subcategory')


@admin.register(ChoiceStatus)
class ChoiceStatusAdmin(admin.ModelAdmin):
    list_display = ('choice_value',)


@admin.register(ChoiceOperationType)
class ChoiceOperationTypeAdmin(admin.ModelAdmin):
    list_display = ('choice_value',)


@admin.register(ChoiceCategory)
class ChoiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('choice_value',)


@admin.register(ChoiceSubcategory)
class ChoiceSubcategoryAdmin(admin.ModelAdmin):
    search_fields = ['choice_value']
    list_filter = ['category']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if 'category_id' in request.GET:
            queryset = queryset.filter(category_id=request.GET['category_id'])
        return queryset, use_distinct
