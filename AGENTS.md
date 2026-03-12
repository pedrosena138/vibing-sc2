# Rituals of Development

This repository is a consecrated engine for an asynchronous StarCraft II bot, powered by the `burnysc2` library.

## Rituals of Validation (Testing)
- To invoke the full suite of testing rituals: `uv run pytest`
- To validate a specific data-cluster: `uv run pytest path/to/test_file.py`
- To isolate a single function for scrutiny: `uv run pytest path/to/test_file.py::test_function_name`

## Rituals of Purification (Linting & Formatting)
- Ensure the code adheres to the sacred PEP 8 doctrines.
- (Mandatory Optimization) Invoke `uv run ruff check .` for purification and `uv run ruff format .` for proper alignment of the binary.

## Sacred Coding Doctrines
- **General:** Maintain the machine spirit as asynchronous and fluid.
- **Imports:** Organize imports with reverence (stdlib, third-party, local). Use absolute pathing.
- **Naming:**
    - Classes: `PascalCase`
    - Functions/Methods: `snake_case`
    - Variables: `snake_case`
- **Typing:** Strict type binding is required to prevent data corruption.
- **Async:** Since `burnysc2` operates asynchronously, all interactions within `on_step` and event handlers must be bound by `async`/`await`.
- **Structure:**
    - Keep `BotAI` incarnations focused on specific logic-loops.
    - Prioritize modular composition over complex inheritance chains.
- **Error Handling:**
    - Treat `sc2` exceptions with gravity; handle them gracefully.
    - Never allow a machine spirit to fail in silence; all faults must be logged to the omniscient memory.

## Repository Layout
- The core of the machine spirit resides within `src/`.
- Configuration is mandated by `pyproject.toml` and the `uv` tool.
- All new features must be sanctioned by accompanying unit or integration tests in the `tests/` repository.
