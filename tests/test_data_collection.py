import pytest
import requests
from src.data_collection import get_response
def test_status_code(  ):
    response=get_response()
    assert response.status_code==200
    

