from attachments.models import Attachment
from django.contrib.contenttypes import generic

class AttachmentInlines(generic.GenericStackedInline):
    model = Attachment
    extra = 1
    prepopulated_fields = {"title": ("attachment_file",)}
    