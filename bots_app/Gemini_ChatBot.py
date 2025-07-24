import streamlit as st
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from langchain.tools.arxiv.tool import ArxivQueryRun

import subprocess
import os
import pkg_resources
import re

# -------------------- Gemini LLM Setup -------------------- #
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="AIzaSyAs5PaZO4AklkRgzbS1VNlH9EQhS9JcAZM",
    convert_system_message_to_human=True,
    temperature=0.7
)

# -------------------- TOOL DEFINITIONS -------------------- #

# 🔢 Calculator Tool
def calculate(expression: str) -> str:
    try:
        return f"🧮 Result: {eval(expression)}"
    except Exception as e:
        return f"Calculation error: {e}"

calculator_tool = Tool.from_function(
    func=calculate,
    name="Calculator",
    description="Evaluates math expressions like '2 + 3 * (4/2)'"
)

# 📂 File Reader Tool
def read_file(filename: str) -> str:
    try:
        with open(filename, 'r') as f:
            return f"📄 File Preview:\n\n{f.read()[:300]}..."
    except Exception as e:
        return f"Error reading file: {e}"

file_reader_tool = Tool.from_function(
    func=read_file,
    name="FileReader",
    description="Reads content from a local .txt file"
)

# 🐍 Python Executor Tool
def execute_code(code: str) -> str:
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result", "✅ Code executed successfully"))
    except Exception as e:
        return f"Execution error: {e}"

code_executor_tool = Tool.from_function(
    func=execute_code,
    name="PythonExecutor",
    description="Executes basic Python code snippets"
)

# 📖 arXiv Research Tool
arxiv_tool = ArxivQueryRun()

# 📁 Folder Scanner Tool
def list_files(path: str) -> str:
    try:
        files = os.listdir(path)
        return f"📂 Files in '{path}':\n" + "\n".join(files)
    except Exception as e:
        return f"Error listing files: {e}"

folder_tool = Tool.from_function(
    func=list_files,
    name="FolderScanner",
    description="Lists all files in a specified folder"
)

# 📟 Shell Command Tool
def run_shell(command: str) -> str:
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return f"📟 Output:\n{result[:500]}..."
    except Exception as e:
        return f"Shell error: {e}"

shell_tool = Tool.from_function(
    func=run_shell,
    name="ShellRunner",
    description="Runs shell commands like 'ls', 'df -h', 'echo hello'"
)

# 📦 Dependency Analyzer
def show_dependencies(_: str = "") -> str:
    packages = sorted(["📦 " + str(p) for p in pkg_resources.working_set])
    return "\n".join(packages[:50]) + "\n...and more."

dependency_tool = Tool.from_function(
    func=show_dependencies,
    name="DependencyChecker",
    description="Lists installed Python packages and versions"
)

# 📊 Regex Extractor Tool
def extract_emails(text: str) -> str:
    matches = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
    return f"📧 Emails found: {matches}" if matches else "No emails found."

regex_tool = Tool.from_function(
    func=extract_emails,
    name="RegexExtractor",
    description="Extracts email addresses from text"
)

# 🧾 Markdown Generator Tool
def format_markdown(content: str) -> str:
    return f"# Title\n\n**Bold Section**\n\n- Item 1\n- Item 2\n\n{content}"

markdown_tool = Tool.from_function(
    func=format_markdown,
    name="MarkdownFormatter",
    description="Formats input into markdown structure"
)

# -------------------- Assemble All Tools -------------------- #
tools = [
    calculator_tool,
    file_reader_tool,
    code_executor_tool,
    arxiv_tool,
    folder_tool,
    shell_tool,
    dependency_tool,
    regex_tool,
    markdown_tool
]

agent = create_react_agent(llm, tools)

# -------------------- Streamlit UI -------------------- #
st.set_page_config(page_title="🔧 Gemini Agent", page_icon="🤖")
st.title("🧠 Gemini-Powered Super Assistant")

user_query = st.text_area("🔍 Type your query below:")

if st.button("Run Agent"):
    if not user_query.strip():
        st.warning("⚠️ Please enter a valid query.")
    else:
        input_msg = {"role": "user", "content": user_query}
        with st.spinner("Thinking..."):
            for step in agent.stream({"messages": [input_msg]}, stream_mode="values"):
                output = step["messages"][-1].content
                st.markdown(f"**🧠 Response:**\n\n{output}")
