from bulbs2.publishing.mixins import PublishMixin
from bulbs2_editorial_workflow.editorial.managers import (
    WaitingForEditorManager, DraftManager, ScheduledManager, PublishedManager)
from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
from django.db import models


class Article(PublishMixin, EditorialWorkflowMixin):
    name = models.CharField(max_length=255)
    editor_objects = WaitingForEditorManager()
    draft_objects = DraftManager()
    scheduled_objects = ScheduledManager()
    published_objects = PublishedManager()

    def send_to_editor(self):
        super(Article, self).send_to_editor()
        self.save()

    def approve_draft(self):
        super(Article, self).approve_draft()
        self.save()

    def send_back_to_author(self):
        super(Article, self).send_back_to_author()
        self.save()
