from bulbs2_editorial_workflow.editorial.models import State
from django_fsm import TransitionNotAllowed
from example.app.models import Article
from model_mommy import mommy
import pytest


@pytest.mark.django_db
def test_init_state_is_draft():
    article = mommy.make(Article)
    assert article.state == State.draft


@pytest.mark.django_db
def test_direct_state_change_raises_error():
    article = mommy.make(Article)
    assert article.state == State.draft
    with pytest.raises(AttributeError):
        article.state = State.approved_for_publication


@pytest.mark.django_db
def test_send_to_editor():
    article = mommy.make(Article)
    assert article.state == State.draft
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor


@pytest.mark.django_db
def test_approve_draft():
    article = mommy.make(Article)
    assert article.state == State.draft
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    _ = article.approve_draft()
    assert article.state == State.approved_for_publication


@pytest.mark.django_db
def test_send_back_to_author():
    article = mommy.make(Article)
    assert article.state == State.draft
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    _ = article.send_back_to_author()
    assert article.state == State.draft


@pytest.mark.django_db
def test_cannot_approve_draft_state():
    """must be State.waiting_for_editor to be approved
    """
    article = mommy.make(Article)
    assert article.state == State.draft
    _ = article.send_to_editor()
    assert article.state == State.waiting_for_editor
    _ = article.send_back_to_author()
    assert article.state == State.draft
    with pytest.raises(TransitionNotAllowed):
        _ = article.approve_draft()
