from flask import Flask
import datetime
import subprocess
import os
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the htop endpoint app. Visit /htop to see system information."

@app.route('/htop')
def htop():
   
    name = "Pulimamidi Chandan"  
    
   
    username = os.getenv('USER', subprocess.getoutput('whoami'))
    
  
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    
    top_output = subprocess.getoutput('top -bn1')
    
   
    return f"""
    Name: {name}
    user: {username}
    Server Time (IST): {server_time}
    TOP output:
    {top_output}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)