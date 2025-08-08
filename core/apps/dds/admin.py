from django.contrib import admin

from core.apps.dds.models.dds import DDS, ChoiceCategory, ChoiceOperationType, ChoiceStatus, ChoiceSubcategory



@admin.register(DDS)
class DDSAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'operation_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('created_at', 'status', 'operation_type', 'category', 'subcategory')
    class Media:
        css = {
            'all': (
                'smart-selects/admin/css/chained.css',
            )
        }
        js = (
            'admin/js/vendor/jquery/jquery.min.js',
            'smart-selects/admin/js/chained.js',
        )

@admin.register(ChoiceStatus)
class ChoiceStatusAdmin(admin.ModelAdmin):
    list_display = ('status_choice',)


@admin.register(ChoiceOperationType)
class ChoiceOperationTypeAdmin(admin.ModelAdmin):
    list_display = ('operation_type_choice',)


@admin.register(ChoiceCategory)
class ChoiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_choice',)



@admin.register(ChoiceSubcategory)
class ChoiceSubcategoryAdmin(admin.ModelAdmin):
    search_fields = ['subcategory_choice']
    list_filter = ['category']
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if 'category_id' in request.GET:
            queryset = queryset.filter(category_id=request.GET['category_id'])
        return queryset, use_distinct

    