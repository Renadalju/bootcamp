# CSV Profiler
---

## Installation

### Step 1: Set up a virtual environment
```
uv venv -p 3.11
```

### Step 2: Activate it

Activate On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Activate On Linux / Mac:

```bash
. .venv/bin/activate
```

---

## Usage(CLI)
use this command:

```bash 
uv run python -m src.csv_profiler.cli data/sample.csv
```

---

## Open Streamlit:

### Command: 
```bash
uv run streamlit run app.py
```