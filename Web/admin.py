from django.contrib import admin

from .models import *


# ModelAdmins
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["Name",]

    def Name(self, instance):
        return instance.user.username


class PetStatusAdmin(admin.ModelAdmin):
    # list_display = ["狀態名稱", "狀態描述", "無法攻擊機率", "攻擊同隊機率", "攻擊自己機率", "攻擊修正", "防禦修正"]
    list_display = ["Name", ]

    def Name(self, instance):
        return instance.name


class PetSkillAdmin(admin.ModelAdmin):
    # list_display = ["技能名稱", "技能描述", "血量修正", "攻擊修正", "防禦修正", "直接攻擊值", "直接攻擊機率"]
    list_display = ["Name", ]

    def Name(self, instance):
        return instance.name


class PetPrototypeAdmin(admin.ModelAdmin):
    # list_display = ["原型名稱", "故事", "最大血量", "最大攻擊", "最大防禦", "基礎血量", "基礎攻擊", "基礎防禦", "可習得技能", "最大等級"]
    list_display = ["Name", ]

    def Name(self, instance):
        return instance.name

class PetAdmin(admin.ModelAdmin):
    # list_display = ["擁有者", "寵物原型", "等級", "狀態"]
    list_display = ["Name", ]

    def Name(self, instance):
        return instance.name

# Register your models here.
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(PetStatus, PetStatusAdmin)
# admin.site.register(PetSkill, PetSkillAdmin)
# admin.site.register(PetPrototype, PetPrototypeAdmin)
# admin.site.register(Pet, PetAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(PetStatus, PetStatusAdmin)
admin.site.register(PetSkill, PetSkillAdmin)
admin.site.register(PetPrototype)
admin.site.register(Pet)
