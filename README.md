# SOC Log Analysis Tool

This is a Python-based tool designed for SOC analysts to analyze log files efficiently. It scans a directory for log files, extracts log entries based on severity levels (CRITICAL, ERROR, WARNING, INFO, DEBUG), and generates a JSON report summarizing the findings.

---

## Features
- Scans a directory for `.log` files.
- Identifies log entries by severity levels.
- Generates a detailed JSON report of the log analysis.

---

## Prerequisites
- **Python 3.6+**
- Basic understanding of log file formats.

---

## Installation
1. Clone this repository or download the code.
   ```bash
   git clone https://github.com/username/SOC-Log-Analysis-Tool.git
   cd SOC-Log-Analysis-Tool
   ```
2. Ensure Python is installed. Verify with:
   ```bash
   python --version
   ```
3. Install any required Python libraries (if applicable).

---

## Usage
1. **Prepare your log files:**
   - Place your `.log` files in a directory.
   - Ensure logs contain entries with severities like `CRITICAL`, `ERROR`, `WARNING`, `INFO`, or `DEBUG`.

2. **Run the script:**
   - Open a terminal and navigate to the project directory.
   - Run the script:
     ```bash
     python log_analysis_tool.py
     ```

3. **Input the log directory path:**
   - When prompted, enter the full path to the directory containing your log files, e.g.:
     ```
     Enter the path to the log directory: /path/to/logs
     ```

4. **View the results:**
   - A file named `log_analysis_report.json` will be generated in the same directory as the script.
   - Open this file to review the summarized log analysis.

---

## Example
**Sample Log File (`example.log`):**
```
CRITICAL: Disk space critically low on server1.
ERROR: Failed to connect to database on server2.
WARNING: High memory usage detected on server3.
INFO: Daily backup completed successfully.
DEBUG: Debugging connection issue on port 8080.
```

**Run Command:**
```bash
python log_analysis_tool.py
```

**Generated Report (`log_analysis_report.json`):**
```json
{
    "CRITICAL": [
        {
            "timestamp": "2025-01-21T14:30:00",
            "file": "/path/to/logs/example.log",
            "message": "Disk space critically low on server1."
        }
    ],
    "ERROR": [
        {
            "timestamp": "2025-01-21T14:30:00",
            "file": "/path/to/logs/example.log",
            "message": "Failed to connect to database on server2."
        }
    ],
    ...
}
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Feel free to fork the repository, make improvements, and submit a pull request.

---

## Support
For any issues or questions, open an issue in the GitHub repository or contact the author.
