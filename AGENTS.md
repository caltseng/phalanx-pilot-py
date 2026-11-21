# Agent instructions

- Python 3.12+, standard library only. Do not add dependencies.
- Code lives in `pilot/`; tests live in `tests/` and use `unittest`.
- Run the tests from the repo root before opening a PR:

  ```sh
  python -m unittest discover -s tests -v
  ```

- Add or update a test for every behavior change.
- CI (`.github/workflows/ci.yml`) runs the same command on Ubuntu and Windows;
  `test (ubuntu-latest)` and `test (windows-latest)` are required on `main`.
