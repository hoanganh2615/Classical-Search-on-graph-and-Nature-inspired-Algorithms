## Setup

All commands are run from the `src/` directory.

```bash
git clone https://github.com/longhuynhdev/Search-and-Nature-inspired-Algorithms.git
cd Search-and-Nature-inspired-Algorithms/src
```

---

### Option A — uv (recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package manager. Install it once:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then create the environment and install dependencies:

```bash
uv venv
uv pip install -r requirements.txt
```

Run the comparison runner:

```bash
uv run python main.py
```

---

### Option B — pip + venv

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the comparison runner:

```bash
python main.py
```

Algorithms that are not yet implemented print `pending` and do not crash the run.
