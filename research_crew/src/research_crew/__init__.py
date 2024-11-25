import os

from dotenv import load_dotenv
from langtrace_python_sdk import langtrace

# Load environment variables
load_dotenv()

langtrace.init(api_key=os.environ["LANGTRACE_API_KEY"])