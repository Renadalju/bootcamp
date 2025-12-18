# CSV Profiler
---

### Step 1: Set up a virtual environment
```
uv venv -p 3.11
```

### Step 2: Activate it

Activate On Windows (PowerShell):

```powershell
.\.venv\Scripts\activate
```

Activate On Linux / Mac:

```bash
. .venv/bin/activate
```

---

## Installation
```
uv pip install -r requirements.txt
```

---

## Usage(CLI)
use this command:

```bash 
uv run python -m csv_profiler.cli data/sample.csv
```
---

## Streamlit (GUI):

### Command: 
```bash
uv run streamlit run app.py
```
 ---

![CSV Profiler UI](/images/Screenshot.png)
