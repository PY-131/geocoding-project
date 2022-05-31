import pytest
import json

def __parse_json(req):
    try:
        data = json.loads(req.data.decode('utf8'))
    except Exception as e:
        raise e
    return data


@pytest.mark.index
def test_index_page_load(client):
    res = client.get('/')
    assert res.status_code == 200


@pytest.mark.index
def test_index_address_post(client):

    res = client.post('/', 
        data=dict(address="630 Ninth Ave, Unit 901, New York, NY 10036"),
        follow_redirects=True
    )

    assert res.status_code == 200
    assert b'630 Ninth Ave, Unit 901, New York, NY 10036' in res.data

@pytest.mark.iss
def test_iss_people(client):

    res = client.get('/iss_people')
    data = __parse_json(res)

    assert res.status_code == 200
    assert 'people' in data

@pytest.mark.iss
def test_iss_info(client):

    res = client.get('/iss_info')
    data = __parse_json(res)

    assert res.status_code == 200
    assert 'people' in data
    assert 'now' in data
    assert 'lat' in data
    assert 'lon' in data
    

@pytest.mark.iss
def test_iss_location(client):
    
    res = client.get('/iss_location')
    data = __parse_json(res)

    assert res.status_code == 200
    assert 'lat' in data
    assert 'lon' in data
