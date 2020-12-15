from django.contrib import admin
from django.contrib.auth.models import User, Group

from worker.models import Position, Level, Tax, Worker, Premium

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Position)
admin.site.register(Level)
admin.site.register(Premium)
admin.site.register(Tax)
admin.site.register(Worker)
