import os
import subprocess
import sys

# Get the path to your Streamlit app
streamlit_script = os.path.abspath("newweather.py")

# Launch Streamlit using subprocess
subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_script])
