import google.generativeai as genai
import os
import io
import contextlib
import sys
import traceback
import re
import subprocess
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
def generate_code(prompt: str) -> str:
    response = model.generate_content(prompt)
    raw_text = response.text
    return clean_code(raw_text)
def clean_code(generated: str) -> str:
    """
    Extracts Python code blocks from Gemini's response and returns only the code.
    If no fenced code blocks are found, returns the text as-is.
    """
    matches = re.findall(r"```python(.*?)```", generated, re.DOTALL)
    if matches:
        return matches[0].strip()
    return generated.strip()
def clean_code(text: str) -> str:
    """
    Takes Gemini's response and returns only the actual Python code.
    """
    # Case 1
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Case 2
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Case 3
    return text.strip()
def run_code(code: str) -> str:
    """
    Runs cleaned Python code and returns stdout/stderr.
    """
    try:
        clean = clean_code(code)
        result = subprocess.run(
            [sys.executable, "-c", clean],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout if result.returncode == 0 else "Error:\n" + result.stderr
    except subprocess.TimeoutExpired:
        return " Error: Code execution timed out."
    except Exception as e:
        return f" Error: {e}"


