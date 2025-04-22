import starkbank
from datetime import date, datetime, timedelta
from dateutil.parser import parse


def generate_invoices(invoice_data):
    try:

       return starkbank.invoice.create([
            starkbank.Invoice(amount=invoice_data["amount"],
                              tax_id=invoice_data["tax_id"],
                              name=invoice_data["name"],
                              due=parse(invoice_data["due"]),
                              expiration=invoice_data["expiration"],
                              fine=invoice_data["fine"],
                              interest=invoice_data["interest"])
        ])
    
    except Exception as e:
        return {
            'status_code': 500,
            'content': {'error': str(e)},
            'success': False
        }
