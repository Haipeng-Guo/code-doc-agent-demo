import argparse
from src.agents.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Code Documentation AI Agent")
    parser.add_argument("--path", required=True, help="Path to source code directory")
    parser.add_argument("--output", default="./docs/API_Documentation.md", help="Output Markdown file")
    args = parser.parse_args()

    orchestrator = Orchestrator()
    orchestrator.run(args.path, args.output)

if __name__ == "__main__":
    main()