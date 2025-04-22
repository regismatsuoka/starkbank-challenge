def test_webhook_controller_exists():
    try:
        from controllers import webhook_controller
        assert True
    except ImportError:
        assert False, "Could not import webhook_controller"

def test_webhook_endpoint(client):
    response = client.post('/api/webhook', json={"event": {"subscription": "invoice", "log": {"type": "invoice", "invoice": {"id": "123", "status": "paid"}}}})
    assert response is not None 