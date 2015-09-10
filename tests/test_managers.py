from datetime import timedelta

from bulbs2_editorial_workflow.editorial.models import State
from django.utils import timezone
from example.app.models import Article
from model_mommy import mommy
import pytest


@pytest.mark.django_db
def test_draft_manager():
    article = mommy.make(Article)
    assert article.state == State.draft
    assert article in Article.draft_objects.all()
    _ = article.send_to_editor()
    assert article not in Article.draft_objects.all()
    _ = article.send_back_to_author()
    assert article.state == State.draft
    assert article in Article.draft_objects.all()


@pytest.mark.django_db
def test_editor_manager():
    article = mommy.make(Article)
    assert article.state == State.draft
    assert article in Article.draft_objects.all()
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    assert article in Article.editor_objects.all()


@pytest.mark.django_db
def test_scheduled_manager():
    article = mommy.make(Article)
    assert article.state == State.draft
    assert article in Article.draft_objects.all()
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    assert article in Article.editor_objects.all()
    _ = article.approve_draft()
    assert article.state == State.approved_for_publication
    assert article not in Article.scheduled_objects.all()
    article.published = timezone.now() + timedelta(days=1)
    article.save()
    assert article in Article.scheduled_objects.all()


@pytest.mark.django_db
def test_published_manager():
    article = mommy.make(Article)
    assert article.state == State.draft
    assert article in Article.draft_objects.all()
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    assert article in Article.editor_objects.all()
    _ = article.approve_draft()
    assert article.state == State.approved_for_publication
    assert article not in Article.published_objects.all()
    article.published = timezone.now() - timedelta(days=1)
    article.save()
    assert article in Article.published_objects.all()
