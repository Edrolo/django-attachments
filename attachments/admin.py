from attachments.models import Attachment
from django.contrib.contenttypes import admin


class AttachmentInlines(admin.GenericStackedInline):
    model = Attachment
    extra = 1
    prepopulated_fields = {"title": ("attachment_file",)}
