import pytest
import json
import sys, os
sys.path.append('../')

from Data4Tweets.app import app

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200
