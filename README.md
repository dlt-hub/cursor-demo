# Cursor.ai DLT Development Assistant

This is a POC to setup up a locally optimal, AI-powered development environment that streamlines the creation and maintenance of dlt pipelines using Cursor.ai and Claude 3.5 Sonnet.

## Overview

This project combines:
- Cursor.ai's intelligent code editing capabilities
- Claude 3.5 Sonnet's advanced language understanding
- dlt's robust data pipeline framework

to create a seamless development experience for data engineers and developers working with dlt.

## Project Structure

```
.
├── .cursorrules           # AI instruction rules for dlt development
├── dlt/                  # dlt codebase
├── prompts/              # Optimized prompts for common tasks
├── templates/            # Pipeline and source templates
└── docs/                # Documentation
```

## Setup

1. Clone this repository:
```bash
git clone --recursive https://github.com/your-org/cursor-dlt-assistant.git
```

2. Clone dlt for AI context:
```bash
git clone --recursive https://github.com/dlt-hub/dlt.git .dlt
```

3. Install Cursor.ai and configure Claude 3.5 Sonnet
4. Copy the `.cursorrules` file to your project root

## Difficulty Tiers



**Tier 2: Advanced Verified Pipeline (70% Success Rate)**
- Multiple resources with verified sources
- Support for incremental loading and hints
- Minor code modifications expected
- May require minimal troubleshooting
- Ideal for production-ready data pipelines

**Tier 3: Experimental Custom Sources (35-55% Success Rate)**
- Custom source development
- Experimental features
- Significant code modifications likely
- Multiple iterations may be needed
- Best for advanced users and testing

## Features

**AI-Assisted Development**
- Optimized prompts for common dlt operations
- Single-shot code generation for basic pipelines
- Context-aware documentation assistance
- Full dlt codebase context for accurate assistance

**Development Focus**
- Verified sources only
- Emphasis on simple, working solutions
- Comprehensive AI context through dlt codebase

## Usage Guidelines

**For Best Results**
- Start with Tier 1 pipelines
- Use verified sources whenever possible
- Expect single-shot success for basic pipelines
- Plan for iterations with advanced features

**Limitations**
- Custom destinations are out of scope
- Complex pipelines may require manual adjustments
- Experimental features have lower success rates

## Getting Started

1. Choose your pipeline tier based on requirements
2. Follow the provided templates
3. Use AI assistance for code generation
4. Test and iterate as needed