# $B \to bH(\gamma\gamma)$ analysis

$B \to bH(\gamma\gamma)$ selection

## Prerequisites

- Python ≥ 3.13
- [uv](https://docs.astral.sh/uv/) package manager
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rrabadan/b2bH-vlq.git
cd b2bH-vlq
```

### 2. Download Data Files (Git LFS)

The data files are stored using Git LFS. Make sure you have Git LFS installed and pull the data files:

```bash
# Install Git LFS (if not already installed)
# On Ubuntu/Debian: sudo apt install git-lfs
# On macOS: brew install git-lfs
# On Windows: Download from https://git-lfs.github.io/

# Initialize Git LFS and pull data files
git lfs install
git lfs pull
```

### 3. Install Dependencies with uv

Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install the project and all dependencies using uv:

```bash
# Install the project in development mode
uv sync --dev

# Or without dev dependencies
uv sync
```

This will:
- Create a virtual environment automatically
- Install the main package (`b2bH-vlq`) and its dependencies
- Install development tools (if using `--dev` flag)

## Usage

### Running the Notebooks

Jupyter notebooks are located in the `notebooks/` directory:

- `bdt-training.ipynb` - Boosted decision tree analysis


#### Option 1: Using Jupyter Lab/Notebook

```bash
# Activate the uv environment and start Jupyter
uv run jupyter lab
```

Then navigate to `notebooks/bdt-training.ipynb` in your browser.

#### Option 2: Using VS Code

If you're using VS Code with the Python extension:

1. Open the project folder in VS Code
2. Ensure the Python interpreter is set to the uv virtual environment
3. Open `notebooks/bdt-training.ipynb`
4. Run the cells interactively

### Data Files

The analysis uses ROOT files located in the `data/` directory:

**Signal files:**
- `BDT_tree_M800_14TeV.root` through `BDT_tree_M2200_14TeV.root` (various mass points)

**Background files:**
- `BKG_tree_tHq_14TeV.root`
- `BKG_tree_ttH_14TeV.root`
- `BKG_tree_VBF_14TeV.root`
- `BKG_tree_WH_14TeV.root`
- `BKG_tree_ZH_14TeV.root`

### Project Structure

```
├── src/b2bH_vlq/         # Main analysis package
├── notebooks/            # Jupyter notebooks for analysis
├── data/                 # ROOT data files
└── pyproject.toml        # Project configuration
```

## Development

### Setting up Development Environment

```bash
# Install with development dependencies
uv sync --dev

# Install pre-commit hooks (optional)
uv run pre-commit install
```

### Code Quality Tools

The project uses several code quality tools configured in `pyproject.toml`:

- **Black**: Code formatting
- **isort**: Import sorting
- **Ruff**: Fast Python linter
- **mypy**: Static type checking

Run them with:

```bash
uv run black .
uv run isort .
uv run ruff check .
uv run mypy src/
```
