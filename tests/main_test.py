"""Tests for ping views."""
from http import HTTPStatus

from flask import url_for


def test_ping(client):
    """Test for ping endpoint."""
    response = client.get(url_for("ping.main"))
    assert response.status_code == HTTPStatus.OK

def test_get_person(client):
    response = client.get(url_for("conhece.doc"))
    result = response.json
    assert ("maria" in result) == True