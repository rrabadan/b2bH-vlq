# $B \to bH(\gamma\gamma)$ analysis

$B \to bH(\gamma\gamma)$ selection

## Prerequisites

- Python ≥ 3.13
- [uv](https://docs.astral.sh/uv/) package manager
- Git

## Installation

### 1. Clone the Repository with Submodules

This project uses submodules for the `anaheptools` package. Clone the repository with all submodules:

```bash
git clone --recursive https://github.com/rrabadan/b2bH-vlq.git
cd b2bH-vql
```

If you've already cloned the repository without submodules, initialize them:

```bash
git submodule update --init --recursive
```

### 2. Install Dependencies with uv

Install the project and all dependencies using uv:

```bash
# Install the project in development mode
uv sync --dev

# Or for production (without dev dependencies)
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
