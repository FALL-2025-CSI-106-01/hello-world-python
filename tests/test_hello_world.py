import subprocess
import sys
import os

def test_hello_world_output():
    script_path = os.path.join(os.path.dirname(__file__), '..', 'hello_world_main.py')
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello World"