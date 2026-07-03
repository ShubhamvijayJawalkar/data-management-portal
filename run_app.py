import sys
sys.path.insert(0, r'C:\Users\CW230503\Desktop\flask_app')
from app import app
app.run(host='127.0.0.1', port=5008, debug=False, threaded=True)
