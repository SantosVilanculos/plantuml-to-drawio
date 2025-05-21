# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2025-05-21

### Changed

- **Refactored CLI argument parsing to use the Click library**, replacing manual `sys.argv` handling. This significantly improves CLI robustness, user experience, and future extensibility.
  - The `--debug` option is now a **boolean flag** (`-d` or `--debug`). Its mere presence enables debug mode (`True`), while its absence disables it (`False`).
  - Improved **help text** for both the `path` argument (via the main command's docstring) and the `--output` option, including usage examples.

## [1.2.0] - 2025-05-21

### Added

- Direct inclusion of plantuml-mit-1.2025.2.jar within the repository for simplified execution.
- GitHub Actions workflow for automatic building and publishing of executable releases.

### Changed

- Transformed the project from a Python script-only repository to an executable application (bundled with plantuml-mit0.2025.2.jar via PyInstaller).
- The primary method of use is now a standalone executable, simplifying user setup.

### Removed

- External dependency on a system-wide PlantUML installation for users.

[unreleased]: https://github.com/santosvilanculos/plantuml-to-drawio/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/santosvilanculos/plantuml-to-drawio/releases/tag/v1.3.0
[1.2.0]: https://github.com/santosvilanculos/plantuml-to-drawio/releases/tag/v1.2.0
