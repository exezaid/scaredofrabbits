from django.contrib import admin

from package.models import Category, Package, PackageExample, Repo, Commit

class PackageExampleInline(admin.TabularInline):
    model = PackageExample
    
class PackageAdmin(admin.ModelAdmin):
    
    save_on_top = True    
    search_fields = ('title',)
    list_filter = ('category','repo')    
    list_display = ('title', 'created', )
    date_hierarchy = 'created'    
    inlines = [
        PackageExampleInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'pypi_url', 'repo', 'repo_url', 'usage')
        }),
        ('Pulled data', {
            'classes': ('collapse',),
            'fields': ('repo_description', 'repo_watchers', 'repo_forks', 'repo_commits', 'pypi_version', 'pypi_downloads', 'participants')
        }),
    )    
    
class CommitAdmin(admin.ModelAdmin):
    list_filter = ('package',)
    

admin.site.register(Category)
admin.site.register(Package, PackageAdmin)
admin.site.register(Repo)
admin.site.register(Commit, CommitAdmin)