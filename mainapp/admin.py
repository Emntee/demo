from django.contrib import admin
from .models import (
    Entry,
    GreignYarnRecord,
    GreignYarnSummury,
    PaintingRecord,
    PaintingSummury,
    Supplier 
    ) 

# Register your models here.
admin.site.register(Entry)
admin.site.register(Supplier)
admin.site.register(GreignYarnRecord)
admin.site.register(GreignYarnSummury)
admin.site.register(PaintingRecord)
admin.site.register(PaintingSummury)