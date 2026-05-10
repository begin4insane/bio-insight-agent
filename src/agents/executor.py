python
# executor.py: Programmer Agent with Self-Reflection Capabilities
import subprocess
import logging

logger = logging.getLogger(__name__)

class ProgrammerAgent:
    def __init__(self, llm_client, max_retries=3):
        self.llm = llm_client
        self.max_retries = max_retries

    def run_script(self, code: str, language: str = "python") -> str:
        """Executes generated code in a sandbox and reflects on errors."""
        current_code = code
        
        for attempt in range(self.max_retries):
            try:
                # Mock execution sandbox for R/Python
                logger.info(f"Execution attempt {attempt + 1}/{self.max_retries}")
                result = subprocess.run(
                    [language, "-c", current_code], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                return result.stdout
                
            except subprocess.CalledProcessError as e:
                error_trace = e.stderr
                logger.warning(f"Execution failed. Error traceback captured.")
                
                if attempt == self.max_retries - 1:
                    raise Exception("Max retries reached. Agent could not resolve the error.")
                
                # LLM Self-Reflection to patch code
                current_code = self._reflect_and_fix(current_code, error_trace)

    def _reflect_and_fix(self, bad_code: str, error_trace: str) -> str:
        """Calls the LLM to analyze the traceback and fix the code."""
        prompt = f"""
        Analyze the following traceback and fix the code. Pay attention to common bioinformatics errors 
        (e.g., Pandas DataFrame index mismatch, missing R packages like WGCNA, or Scikit-learn dimension errors).
        
        [TRACEBACK]
        {error_trace}
        
        [CODE]
        {bad_code}
        """
        # Return patched code
        return self.llm.generate(prompt)
