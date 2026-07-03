from app import app
import sys

print("Creating test client...")
with app.test_client() as client:
    print("Making request to /login...")
    try:
        response = client.get('/login')
        print(f"Status: {response.status_code}")
        print(f"Response length: {len(response.data)}")
        print("First 500 chars:", response.data[:500].decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

print("Test complete")
