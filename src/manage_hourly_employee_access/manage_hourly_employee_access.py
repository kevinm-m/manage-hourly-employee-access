import os
import requests
from datetime import datetime

def get_access_token(client_id, client_secret, tenant_id):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

def get_hourly_employees(token, group_id):
    url = f"https://graph.microsoft.com/v1.0/groups/{group_id}/members"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [member['id'] for member in response.json()['value']]

def check_employee_hours(employee_id, token):
    # Hypothetical API or logic for checking clock-in/clock-out status
    # Replace this with real integration as needed
    return "clocking_in"  # Or "clocking_out"

def manage_ms_teams_chat(employee_id, status, token):
    url = f"https://graph.microsoft.com/v1.0/users/{employee_id}/presence"
    headers = {"Authorization": f"Bearer {token}"}

    if status == "clocking_in":
        data = {"availability": "Available"}
    else:
        data = {"availability": "Offline"}

    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()

def main():
    client_id = os.getenv("AD_CLIENT_ID")
    client_secret = os.getenv("AD_CLIENT_SECRET")
    tenant_id = os.getenv("AD_TENANT_ID")
    group_id = os.getenv("HOURLY_EMPLOYEES_GROUP_ID")

    if not all([client_id, client_secret, tenant_id, group_id]):
        raise ValueError("Missing required environment variables.")

    token = get_access_token(client_id, client_secret, tenant_id)

    employees = get_hourly_employees(token, group_id)
    for employee_id in employees:
        status = check_employee_hours(employee_id, token)
        manage_ms_teams_chat(employee_id, status, token)

if __name__ == "__main__":
    main()
