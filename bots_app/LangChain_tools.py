import streamlit as st
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from langchain.tools.arxiv.tool import ArxivQueryRun

import subprocess
import os
import pkg_resources
import re

# ---------------- Gemini Setup ---------------- #
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="YOUR_GEMINI_API_KEY",  # Replace with your key
    convert_system_message_to_human=True,
    temperature=0.7
)

# ---------------- Tool Functions ---------------- #

def calculate(expression: str) -> str:
    try:
        return f"🧮 Result: {eval(expression)}"
    except Exception as e:
        return f"Calculation error: {e}"

def read_file(filename: str) -> str:
    try:
        with open(filename, 'r') as f:
            return f"📄 Preview:\n\n{f.read()[:300]}..."
    except Exception as e:
        return f"File error: {e}"

def execute_code(code: str) -> str:
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result", "✅ Code executed"))
    except Exception as e:
        return f"Execution error: {e}"

def list_files(path: str) -> str:
    try:
        return "\n".join(os.listdir(path))
    except Exception as e:
        return f"Folder error: {e}"

def run_cmd(command: str) -> str:
    try:
        result = subprocess.run(["cmd.exe", "/c", command], capture_output=True, text=True)
        return result.stdout[:500] or result.stderr
    except Exception as e:
        return f"Command error: {e}"

def show_dependencies(_: str = "") -> str:
    return "\n".join(["📦 " + str(p) for p in pkg_resources.working_set][:50]) + "\n...and more."

def extract_emails(text: str) -> str:
    matches = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
    return "\n".join(matches) if matches else "No emails found."

def format_markdown(content: str) -> str:
    return f"# Heading\n\n**Bold Section**\n\n- Item 1\n- Item 2\n\n{content}"

# ---------------- Gemini Agent ---------------- #
tools = [
    Tool.from_function(calculate, name="Calculator", description="Math evaluator"),
    Tool.from_function(read_file, name="FileReader", description="Reads local text file"),
    Tool.from_function(execute_code, name="PythonExecutor", description="Executes Python code"),
    ArxivQueryRun(),
    Tool.from_function(list_files, name="FolderScanner", description="Lists folder contents"),
    Tool.from_function(run_cmd, name="CommandPromptRunner", description="Runs Windows CMD commands"),
    Tool.from_function(show_dependencies, name="DependencyChecker", description="Lists installed packages"),
    Tool.from_function(extract_emails, name="RegexExtractor", description="Extracts email addresses"),
    Tool.from_function(format_markdown, name="MarkdownFormatter", description="Formats text into markdown")
]

agent = create_react_agent(llm, tools)

# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="Gemini Dashboard", page_icon="🧠")

st.title("🧠 Gemini Multi-Tool Assistant")

tabs = st.tabs([
    "🔍 General Agent",
    "➕ Calculator",
    "📂 File Reader",
    "🐍 Python Executor",
    "📖 arXiv Search",
    "📁 Folder Scanner",
    "🖥️ CMD Runner",
    "📦 Dependency Checker",
    "📊 Email Extractor",
    "📝 Markdown Formatter"
])

# General Agent
with tabs[0]:
    query = st.text_area("Type your query")
    if st.button("Run Agent"):
        if query.strip():
            input_msg = {"role": "user", "content": query}
            with st.spinner("Processing..."):
                for step in agent.stream({"messages": [input_msg]}, stream_mode="values"):
                    output = step["messages"][-1].content
                    st.markdown(f"**Response:**\n\n{output}")
        else:
            st.warning("Enter something first!")

# Tool Panels
with tabs[1]:
    expr = st.text_input("Math Expression")
    if st.button("Calculate"):
        st.success(calculate(expr))

with tabs[2]:
    file = st.text_input("Filename (e.g., sample.txt)")
    if st.button("Read File"):
        st.code(read_file(file))

with tabs[3]:
    code = st.text_area("Python Code")
    if st.button("Run Code"):
        st.code(execute_code(code))

with tabs[4]:
    paper = st.text_input("Search arXiv")
    if st.button("Find Papers"):
        st.code(ArxivQueryRun().run(paper))

with tabs[5]:
    path = st.text_input("Folder path (e.g., C:\\Users\\Pankaj\\Projects)")
    if st.button("Scan Folder"):
        st.code(list_files(path))

with tabs[6]:
    cmd = st.text_input("CMD Command")
    if st.button("Run CMD"):
        st.code(run_cmd(cmd))

with tabs[7]:
    if st.button("List Installed Packages"):
        st.code(show_dependencies())

with tabs[8]:
    text = st.text_area("Paste text with emails")
    if st.button("Extract Emails"):
        st.code(extract_emails(text))

with tabs[9]:
    raw = st.text_area("Text to format")
    if st.button("Generate Markdown"):
        st.markdown(format_markdown(raw))
