import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

def main():
    print("LangChain environment test...")
    
    # Simple check to ensure imports work
    try:
        template = PromptTemplate.from_template("Hello {name}!")
        prompt = template.format(name="World")
        print(f"Prompt Template works: {prompt}")
        print("LangChain core libraries imported successfully.")
    except Exception as e:
        print(f"Error importing or using LangChain: {e}")

if __name__ == "__main__":
    main()
