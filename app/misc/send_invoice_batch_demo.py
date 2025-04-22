#!/usr/bin/env python3

import requests
import json
import random
from pathlib import Path

def send_invoice_batch():
    current_dir = Path(__file__).parent
    clientes_file = current_dir / "clientes.txt"
    
    if not clientes_file.exists():
        print(f"Error: File {clientes_file} not found")
        return False
    
    try:
        with open(clientes_file, 'r') as file:
            all_lines = file.readlines()
        
        if not all_lines:
            print("Error: File is empty")
            return False
            
        num_lines_to_process = random.randint(8, 12)
        print(f"Processing {num_lines_to_process} random invoices...")
        selected_lines = random.sample(all_lines, min(num_lines_to_process, len(all_lines)))
        for line in selected_lines:
            try:
                cliente_data = json.loads(line.strip())
                
                response = requests.post(
                    'http://localhost:5000/api/invoice',
                    json=cliente_data,
                    headers={'Content-Type': 'application/json'}
                )
                if response.status_code == 200:
                    print(f"Successfully sent invoice for: {cliente_data.get('name', 'Unknown')}")
                else:
                    print(f"Failed to send invoice. Status code: {response.status_code}")
                    print(f"Response: {response.text}")
            
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
            except requests.RequestException as e:
                print(f"Request error: {e}")
        
        print(f"Invoice batch sending completed. Processed {len(selected_lines)} invoices.")
        return True
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    send_invoice_batch() 