from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Full Name
    name = "Kotapati Yamini"  
    
    # System Username
    username = os.getlogin()
    
    # Server Time in IST (Indian Standard Time)
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Run top command and get the output
    top_output = subprocess.getoutput("top -b -n 1")
    
    # Format the response as plain text
    response = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {server_time}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    
    return response

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
