from django.contrib import admin
from .models import Document, Tag, DocumentTag, Borrowing, Reservation

admin.site.register(Document)
admin.site.register(Tag)
admin.site.register(DocumentTag)
admin.site.register(Borrowing)
admin.site.register(Reservation)