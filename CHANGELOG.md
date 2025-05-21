# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

...

## [0.1.0] - 2025-05-21

### Added

- Direct inclusion of plantuml-mit-1.2025.2.jar within the repository for simplified execution.
- GitHub Actions workflow for automatic building and publishing of executable releases.

### Changed

- Transformed the project from a Python script-only repository to an executable application (bundled with plantuml-mit-1.2025.2.jar via PyInstaller).
- The primary method of use is now a standalone executable, simplifying user setup.

### Removed

- External dependency on a system-wide PlantUML installation for users.

[unreleased]: https://github.com/santosvilanculos/plantuml-to-drawio/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/santosvilanculos/plantuml-to-drawio/releases/tag/v0.1.0
