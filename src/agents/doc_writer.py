from src.utils.llm_client import LLMClient

class DocWriter:
    def __init__(self):
        self.llm = LLMClient()

    def write(self, file_path: str, analysis: dict) -> str:
        prompt = f"""You are a technical writer. Turn the following code analysis into a clear Markdown section for file `{file_path}`.

Analysis:
{analysis}

Generate a section with:
- **File**: {file_path}
- **Purpose**:
- **Input/Output**:
- **Dependencies**:
- **Notes**:

Use proper Markdown formatting.
"""
        return self.llm.generate(prompt)