from unittest.mock import patch
from services.starkbank_api_service import generate_invoices

def test_service_exists():
    try:
        from services import starkbank_api_service
        assert True
    except ImportError:
        assert False, "Could not import starkbank_api_service"

@patch('starkbank.invoice.create')
def test_generate_invoices(mock_create):
    test_invoice = {
        'amount': 1000,
        'tax_id': '012.345.678-90',
        'name': 'Test Customer',
        'due': '2024-12-31',
        'expiration': 123456,
        'fine': 2.5,
        'interest': 1.0
    }
    
    mock_create.return_value = [{
        'id': '123',
        'amount': 1000,
        'status': 'created'
    }]
    
    result = generate_invoices(test_invoice)
    
    assert result is not None 