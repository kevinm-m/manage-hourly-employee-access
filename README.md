# manage-employee-hourly-access

[![PyPI - Version](https://img.shields.io/pypi/v/manage-employee-hourly-access.svg)](https://pypi.org/project/manage-employee-hourly-access)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/manage-employee-hourly-access.svg)](https://pypi.org/project/manage-employee-hourly-access)

-----

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Development](#development)
  - [Running Tests](#running-tests)
  - [Deployment](#deployment)
- [License](#license)

## Overview

This project automates employee hour tracking and integrates with Microsoft Teams to manage chat availability.

## Features

- Fetches hourly employees from Microsoft Active Directory via the Microsoft Graph API.
- Updates Microsoft Teams chat availability based on clock-in/clock-out status.
- Managed using Hatch for modern dependency and environment management.

## Directory Structure

```bash
project_name/
├── src/
│   ├── manage_hourly_employee_access.py   # Main Python script
├── tests/
│   ├── test_manage_hourly_employee_access.py  # Unit tests
├── pyproject.toml                         # Project and environment configuration
├── README.md                              # Project documentation
├── LICENSE                                # License file
```

## Installation

```console
pip install manage-employee-hourly-access
```

## Development

1. Install Hatch:

   ```console
   pip install hatch
   ```

2. Create the development environment:

   ```console
   hatch env create
   hatch env use
   ```

3. Install the production environment (optional):

   ```console
   hatch env create production
   ```

### Running Tests

1. Run all tests:

   ```console
   hatch run pytest
   ```

2. Run tests with coverage:

   ```console
   hatch run pytest --cov=src
   ```

### Deployment

Use the `ansible/deploy_timer.yml` playbook to deploy the script and configure the systemd timer.

## License

`manage-employee-hourly-access` is distributed under the terms of the [0BSD](https://spdx.org/licenses/0BSD.html) license.
