from src.utils.llm_client import LLMClient

class CodeAnalyzer:
    def __init__(self):
        self.llm = LLMClient()

    def analyze(self, file_path: str, code_content: str) -> dict:
        prompt = f"""Analyze the following code file: {file_path}

