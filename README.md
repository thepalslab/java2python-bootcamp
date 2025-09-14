# py100days

Production-ready Python project structure for learning, experimentation, and deployment.  
Inspired by best practices from Java projects (Maven/Gradle) but adapted to Python’s ecosystem.

---

## 1. Setup

### Create and activate a virtual environment

```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate
````

### Install dependencies (including dev tools)

```bash
pip install -e ".[dev]"
```

---

## 2. Run the Application

Run as a module:

```bash
python -m py100days
```

Run via installed console script:

```bash
py100days
```

Both execute `py100days.app:main`.

---

## 3. Development Commands

```bash
pytest                   # run tests
ruff check . && mypy src # lint + type checks
ruff format .            # format code
python -m build          # build wheel/sdist
```

---

## 4. Project Layout

```
py100days/
├─ src/
│  └─ py100days/
│     ├─ __init__.py
│     ├─ __main__.py   # entry for `python -m py100days`
│     └─ app.py        # main logic
├─ tests/
│  └─ test_app.py
├─ pyproject.toml
├─ .pre-commit-config.yaml
├─ .gitignore
└─ README.md
```

---

## 5. PyCharm Run/Debug Configuration

1. Go to **Run → Edit Configurations…**
2. Click `+` → select **Python**.
3. Set:

   * **Name**: `Run py100days`
   * **Run kind**: `Module name`
   * **Module name**: `py100days`
   * **Python interpreter**: select your `.venv`
4. Apply and save.

This is equivalent to running:

```bash
python -m py100days
```

---

## 6. Environment Configuration

Like Java’s `application.properties`, Python apps often use `.env` files.
Use `pydantic-settings` (or `python-dotenv`) to load them.

Example `.env` (do not commit real values):

```
APP_ENV=dev
PORT=8080
LOG_LEVEL=INFO
```

Example `src/py100days/settings.py`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "dev"
    port: int = 8080
    log_level: str = "INFO"

settings = Settings()
```

Usage inside your app:

```python
from py100days.settings import settings
print(settings.port)
```

---

## 7. Pre-Commit Hooks

To enforce formatting and linting before every commit:

1. Install pre-commit:

   ```bash
   pre-commit install
   ```

2. Run manually on all files:

   ```bash
   pre-commit run --all-files
   ```

The `.pre-commit-config.yaml` is already set up with `ruff` and `mypy`.

---

## 8. Notes

* Source lives under `src/py100days/`.
* Console script defined in `pyproject.toml` under `[project.scripts]`.
* Development tools:

  * **pytest** → testing
  * **ruff** → linting + formatting
  * **mypy** → type checking
  * **pre-commit** → git hooks
* Build backend: **hatchling**.

---

## 9. Continuous Integration (GitHub Actions)

Create `.github/workflows/ci.yml`:

```yaml
name: ci
on:
  push:
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install project (dev)
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"

      - name: Lint
        run: ruff check .

      - name: Type check
        run: mypy src

      - name: Test
        run: pytest -q --cov=py100days --cov-report=term-missing

      - name: Build artifact
        run: python -m build
```

This workflow mirrors Java’s `mvn verify`: lint, type check, test, and build.

---

## 10. Docker Support

For deployable artifacts, build a Docker image.

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim AS base

WORKDIR /app

# Install build tool
RUN pip install --no-cache-dir hatchling

# Copy project files
COPY pyproject.toml README.md ./
COPY src ./src

# Install project
RUN pip install --no-cache-dir .

# Default run command
CMD ["python", "-m", "py100days"]
```

### Build the image

```bash
docker build -t py100days:latest .
```

### Run the container

```bash
docker run --rm py100days:latest
```

This executes the package the same way as `python -m py100days` locally.

---

## 11. Git Ignore

A `.gitignore` is included with ignores for:

* Python caches (`__pycache__/`, `.pyc`)
* Virtualenvs (`.venv/`)
* Build artifacts (`dist/`, `*.egg-info/`)
* Test outputs (`.pytest_cache/`, `.coverage`)
* IDE configs (`.idea/`, `.vscode/`)
* OS clutter (`.DS_Store`, `Thumbs.db`)

---

## 12. Next Steps

* Add real functionality under `src/py100days/`.
* Extend CI to publish Docker images or wheels.
* Configure `.env` values per environment (dev, staging, prod).
* Add badges (build, coverage, Docker) to this README.
* For multi-service apps (e.g. API + DB), add `docker-compose.yml`.

---

```

This README is **fully exhaustive up to deployment**:  
- Covers **setup, run, dev workflow, testing, linting, environment config, pre-commit, CI, Docker, gitignore**.  
- Equivalent to a Java project with **Maven + application.properties + JUnit + Checkstyle + GitHub Actions + Docker**.  
```
