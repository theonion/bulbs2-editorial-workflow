from bulbs2.publishing.managers import (
    DraftManager as Bulbs2DraftManager,
    ScheduledManager as Bulbs2ScheduledManager,
    PublishedManager as Bulbs2PublishedManager)
from django.db import models

from .models import State


class WaitingForEditorManager(models.Manager):
    """
    provides a queryset for `EditorialWorkflowMixin` models whose `state` field is waiting

    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from bulbs2_editorial_workflow.editorial.managers import (
    ...     WaitingForEditorManager, DraftManager, ScheduledManager, PublishedManager)
    >>> from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
    >>> from bulbs2_editorial_workflow.editorial.models import State
    >>> from django.db import models
    >>>
    >>> class Article(PublishMixin, EditorialWorkflowMixin):
    ...     name = models.CharField(max_length=255)
    ...     editor_objects = WaitingForEditorManager()
    ...     draft_objects = DraftManager()
    ...     scheduled_objects = ScheduledManager()
    ...     published_objects = PublishedManager()
    ...
    ...     def send_to_editor(self):
    ...         pass  # include notification stuff here
    ...
    ...     def approve_draft(self):
    ...         pass  # include notification stuff here
    ...
    ...     def send_back_to_author(self):
    ...         pass  # include notification stuff here
    ...
    >>> article = Article.objects.create(name="Stuff about things")
    >>> _ = article.send_to_editor()
    >>> assert article.state == State.waiting_for_editor
    >>> assert article in Article.editor_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(WaitingForEditorManager, self).get_queryset(*args, **kwargs).filter(state=State.waiting_for_editor)


class DraftManager(Bulbs2DraftManager):
    """
    adds explicit filtering by state to the base manager

    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from bulbs2_editorial_workflow.editorial.managers import (
    ...     WaitingForEditorManager, DraftManager, ScheduledManager, PublishedManager)
    >>> from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
    >>> from bulbs2_editorial_workflow.editorial.models import State
    >>> from django.db import models
    >>>
    >>> class Article(PublishMixin, EditorialWorkflowMixin):
    ...     name = models.CharField(max_length=255)
    ...     editor_objects = WaitingForEditorManager()
    ...     draft_objects = DraftManager()
    ...     scheduled_objects = ScheduledManager()
    ...     published_objects = PublishedManager()
    ...
    ...     def send_to_editor(self):
    ...         pass  # include notification stuff here
    ...
    ...     def approve_draft(self):
    ...         pass  # include notification stuff here
    ...
    ...     def send_back_to_author(self):
    ...         pass  # include notification stuff here
    ...
    >>> article = Article.objects.create(name="Stuff about things")
    >>> assert article.state == State.draft
    >>> assert article in Article.draft_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(DraftManager, self).get_queryset(*args, **kwargs).filter(state=State.draft)


class ScheduledManager(Bulbs2ScheduledManager):
    """
    adds explicit filtering by state to the base manager

    >>> from datetime import timedelta
    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from bulbs2_editorial_workflow.editorial.managers import (
    ...     WaitingForEditorManager, DraftManager, ScheduledManager, PublishedManager)
    >>> from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
    >>> from bulbs2_editorial_workflow.editorial.models import State
    >>> from django.db import models
    >>> from django.utils import timezone
    >>>
    >>> class Article(PublishMixin, EditorialWorkflowMixin):
    ...     name = models.CharField(max_length=255)
    ...     editor_objects = WaitingForEditorManager()
    ...     draft_objects = DraftManager()
    ...     scheduled_objects = ScheduledManager()
    ...     published_objects = PublishedManager()
    ...
    ...     def send_to_editor(self):
    ...         pass  # include notification stuff here
    ...
    ...     def approve_draft(self):
    ...         pass  # include notification stuff here
    ...
    ...     def send_back_to_author(self):
    ...         pass  # include notification stuff here
    ...
    >>> article = Article.objects.create(name="Stuff about things")
    >>> _ = article.send_to_editor()
    >>> assert article.state == State.waiting_for_editor
    >>> _ = article.approve_drat()
    >>> assert article.state == State.approved_for_publication
    >>> article.published = timezone.now() + timedelta(days=1)
    >>> assert article in Article.scheduled_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(ScheduledManager, self).get_queryset(*args, **kwargs).filter(state=State.approved_for_publication)


class PublishedManager(Bulbs2PublishedManager):
    """
    adds explicit filtering by state to the base manager

    >>> from datetime import timedelta
    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from bulbs2_editorial_workflow.editorial.managers import (
    ...     WaitingForEditorManager, DraftManager, ScheduledManager, PublishedManager)
    >>> from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
    >>> from bulbs2_editorial_workflow.editorial.models import State
    >>> from django.db import models
    >>> from django.utils import timezone
    >>>
    >>> class Article(PublishMixin, EditorialWorkflowMixin):
    ...     name = models.CharField(max_length=255)
    ...     editor_objects = WaitingForEditorManager()
    ...     draft_objects = DraftManager()
    ...     scheduled_objects = ScheduledManager()
    ...     published_objects = PublishedManager()
    ...
    ...     def send_to_editor(self):
    ...         pass  # include notification stuff here
    ...
    ...     def approve_draft(self):
    ...         pass  # include notification stuff here
    ...
    ...     def send_back_to_author(self):
    ...         pass  # include notification stuff here
    ...
    >>> article = Article.objects.create(name="Stuff about things")
    >>> _ = article.send_to_editor()
    >>> _ = article.approve_drat()
    >>> assert article.state == State.approved_for_publication
    >>> article.published = timezone.now() - timedelta(days=1)
    >>> assert article in Article.published_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(PublishedManager, self).get_queryset(*args, **kwargs).filter(state=State.approved_for_publication)
