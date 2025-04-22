import starkbank
import os
from datetime import date, datetime, timedelta
from dateutil.parser import parse


def starkbank_transfer(webhook_data):
    try:

        invoice = webhook_data["event"]["log"]["invoice"]

        transfers = starkbank.transfer.create([
            starkbank.Transfer(
                amount= (invoice["amount"] - invoice["fee"]),
                bank_code= os.getenv('STARBANK_TRANSFER_BANK_CODE'),
                branch_code= os.getenv('STARBANK_TRANSFER_BRANCH_CODE'),
                account_number= os.getenv('STARBANK_TRANSFER_ACCOUNT'),
                account_type= os.getenv('STARBANK_TRANSFER_ACC_TYPE'),
                tax_id= os.getenv('STARBANK_TRANSFER_TAX_ID'),
                name= os.getenv('STARBANK_TRANSFER_NAME'),
                rules=[
                    starkbank.transfer.Rule(
                    key="resendingLimit", 
                    value=10               
                    ) 
                ] 
            )
        ])

    except Exception as e:
        return {
            'status_code': 500,
            'content': {'error': str(e)},
            'success': False
        }
