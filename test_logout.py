#!/usr/bin/env python3
"""
Simple test script to verify logout functionality
"""
import requests
from requests.sessions import Session

def test_logout():
    base_url = "http://127.0.0.1:8000"
    
    # Create a session to maintain cookies
    session = Session()
    
    print("Testing logout functionality...")
    
    # Test 1: Check if admin logout page is accessible
    try:
        response = session.get(f"{base_url}/admin/logout/")
        print(f"Admin logout status: {response.status_code}")
        if "Successfully Logged Out" in response.text or "logged out" in response.text.lower():
            print("✓ Admin logout template is working")
        else:
            print("✗ Admin logout template might not be working properly")
    except Exception as e:
        print(f"✗ Error accessing admin logout: {e}")
    
    # Test 2: Check if accounts logout page is accessible
    try:
        response = session.get(f"{base_url}/accounts/logout/")
        print(f"Accounts logout status: {response.status_code}")
        if "Successfully Logged Out" in response.text or "logged out" in response.text.lower():
            print("✓ Accounts logout template is working")
        else:
            print("✗ Accounts logout template might not be working properly")
    except Exception as e:
        print(f"✗ Error accessing accounts logout: {e}")
    
    # Test 3: Check if templates are found
    print("\nTemplate locations:")
    print("- Admin logout: server/frontend/templates/admin/logged_out.html")
    print("- Registration logout: server/frontend/templates/registration/logged_out.html")

if __name__ == "__main__":
    test_logout()