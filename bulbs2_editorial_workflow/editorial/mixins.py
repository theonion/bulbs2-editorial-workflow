from django.db import models
from django_fsm import FSMField, transition

from .models import State


class EditorialWorkflowMixin(models.Model):
    """
    provides controls for a publishing finite state machine - will throw errors if state is manipulated by any means
    other than the transition marked methods of the class

    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from bulbs2_editorial_workflow.editorial.mixins import EditorialWorkflowMixin
    >>> from bulbs2_editorial_workflow.editorial.models import State
    >>> class Article(PublishMixin, EditorialWorkflowMixin):
    ...     name = models.CharField(max_length=255)
    ...     editor_objects = WaitingForEditorManager()
    ...     draft_objects = DraftManager()
    ...     scheduled_objects = ScheduledManager()
    ...     published_objects = PublishedManager()
    ...
    ...     def send_to_editor(self):
    ...         super(Article, self).send_to_editor()
    ...         pass # include notification stuff here
    ...
    ...     def approve_draft(self):
    ...         super(Article, self).approve_draft()
    ...         pass  # include notification stuff here
    ...
    ...     def send_back_to_author(self):
    ...         super(Article, self).send_back_to_author()
    ...         pass  # include notification stuff here
    ...
    >>> article = Article.objects.create(name="Stuff about things")  # note, state is automatically set
    >>> assert article.state == State.draft
    """

    class Meta(object):
        abstract = True

    state = FSMField(default=State.draft, protected=True)

    @transition(field=state, source=State.draft, target=State.waiting_for_editor)
    def send_to_editor(self):
        """transitions the `state` value from 'draft' to 'waiting for editor'
        """
        pass

    @transition(field=state, source=State.waiting_for_editor, target=State.approved_for_publication)
    def approve_draft(self):
        """transitions the `state` value from 'waiting for editor' to 'approved for publication'
        """
        pass

    @transition(field=state, source=State.waiting_for_editor, target=State.draft)
    def send_back_to_author(self):
        """transitions the `state` value from 'waiting for editor' to 'draft'
        """
        pass
