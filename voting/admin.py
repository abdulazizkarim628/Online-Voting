from django.contrib import admin

# Register your models here.
from .models import Candidate, Position, Voter, Votes


admin.site.register(Candidate)

admin.site.register(Position)

admin.site.register(Voter)

admin.site.register(Votes)