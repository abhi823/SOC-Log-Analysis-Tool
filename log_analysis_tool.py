import os
import re
import json
from datetime import datetime

# Define log patterns and severities
LOG_PATTERNS = {
    "CRITICAL": re.compile(r"CRITICAL: (.+)"),
    "ERROR": re.compile(r"ERROR: (.+)"),
    "WARNING": re.compile(r"WARNING: (.+)"),
    "INFO": re.compile(r"INFO: (.+)"),
    "DEBUG": re.compile(r"DEBUG: (.+)"),
}

class LogAnalysisTool:
    def __init__(self, log_directory):
        self.log_directory = log_directory
        self.analysis_results = {}

    def analyze_logs(self):
        """Analyze all logs in the specified directory."""
        if not os.path.exists(self.log_directory):
            print(f"Directory '{self.log_directory}' does not exist.")
            return

        for root, _, files in os.walk(self.log_directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(".log"):
                    self._analyze_file(file_path)

    def _analyze_file(self, file_path):
        """Analyze a single log file."""
        with open(file_path, "r") as log_file:
            for line in log_file:
                self._process_log_line(file_path, line)

    def _process_log_line(self, file_path, line):
        """Process an individual log line."""
        timestamp = datetime.now().isoformat()

        for severity, pattern in LOG_PATTERNS.items():
            match = pattern.search(line)
            if match:
                log_message = match.group(1)
                if severity not in self.analysis_results:
                    self.analysis_results[severity] = []

                self.analysis_results[severity].append({
                    "timestamp": timestamp,
                    "file": file_path,
                    "message": log_message.strip(),
                })

    def generate_report(self, output_file):
        """Generate a JSON report of the analysis results."""
        with open(output_file, "w") as report_file:
            json.dump(self.analysis_results, report_file, indent=4)
        print(f"Report generated: {output_file}")

if __name__ == "__main__":
    # Configuration
    log_directory = input("Enter the path to the log directory: ").strip()
    output_file = "log_analysis_report.json"

    # Initialize and run the log analysis tool
    analyzer = LogAnalysisTool(log_directory)
    analyzer.analyze_logs()
    analyzer.generate_report(output_file)
