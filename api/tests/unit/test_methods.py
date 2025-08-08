from main import app

def test_list_route():
    with app.test_client() as client:
        resp = client.get('/list')
        assert resp.status_code == 200
        assert resp.is_json
        assert isinstance(resp.get_json(), list)
