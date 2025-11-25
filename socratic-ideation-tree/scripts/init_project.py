#!/usr/bin/env python3
"""
Initialize a new Socratic Ideation Tree project structure.

Usage:
    python init_project.py <project-name> [--path <output-dir>]
    
Examples:
    python init_project.py my-app
    python init_project.py my-app --path /home/user/projects
"""

import argparse
import os
from pathlib import Path
from datetime import datetime


def create_intent_template(project_name: str) -> str:
    """Generate INTENT.md template content."""
    return f"""# Project Intent: {project_name}

## Vision

[What transformation are you trying to achieve? What does success look like?]

## Core Values

- **[Value 1]**: [Why it matters]
- **[Value 2]**: [Why it matters]

## Constraints

- **Time**: [Deadline or ongoing]
- **Resources**: [Budget, team, tools]
- **Scope**: [Boundaries, what's excluded]

## Success Metrics

- [ ] [Quantifiable outcome 1]
- [ ] [Qualitative outcome 2]

## Context

[Background, current state, relevant history]

## Decision Log

- {datetime.now().strftime('%Y-%m-%d')}: Project initialized
"""


def create_idea_template(idea_name: str) -> str:
    """Generate IDEA.md template content."""
    return f"""# Idea: {idea_name}

## Concept

[One paragraph description of this specific approach]

## Why This Approach

- Aligns with [value] because...
- Solves [problem] by...
- Fits within [constraint] via...

## Key Components

1. **[Component]**: [Purpose and description]
2. **[Component]**: [Purpose and description]

## Dependencies

- **Requires**: [Prerequisites, resources]
- **Assumes**: [Conditions that must be true]

## Risk Assessment

- **Primary risk**: [What could derail this]
- **Mitigation**: [How to prevent/handle]

## Next Steps

- [ ] Define [component] implementation
- [ ] Research [unknown area]
- [ ] Prototype [risky element]
"""


def create_task_template(task_name: str) -> str:
    """Generate TASK.md template content."""
    return f"""# Task: {task_name}

## Objective

[Single sentence describing what this task accomplishes]

## Acceptance Criteria

- [ ] Given [context], when [action], then [outcome]
- [ ] [Specific measurable result]

## Implementation Approach

[Paragraph describing the technical/practical approach]

## Dependencies

- **Blocked by**: [Previous tasks]
- **Blocks**: [Future tasks]
- **Requires**: [Resources, knowledge, tools]

## Estimated Effort

[Time estimate or complexity rating]

## Subtasks

1. [ ] [Atomic action 1]
2. [ ] [Atomic action 2]

## Notes

[Design decisions, alternatives considered, rationale]
"""


def init_project(project_name: str, base_path: Path) -> Path:
    """Initialize a new project with the Socratic Ideation Tree structure."""
    
    project_path = base_path / project_name
    
    # Create directory structure
    dirs = [
        project_path,
        project_path / "ideas",
        project_path / "ideas" / "example-idea" / "tasks" / "example-task" / "subtasks",
    ]
    
    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create INTENT.md
    intent_path = project_path / "INTENT.md"
    intent_path.write_text(create_intent_template(project_name))
    
    # Create example IDEA.md
    idea_path = project_path / "ideas" / "example-idea" / "IDEA.md"
    idea_path.write_text(create_idea_template("Example Idea"))
    
    # Create example TASK.md
    task_path = project_path / "ideas" / "example-idea" / "tasks" / "example-task" / "TASK.md"
    task_path.write_text(create_task_template("Example Task"))
    
    # Create example subtask
    subtask_path = project_path / "ideas" / "example-idea" / "tasks" / "example-task" / "subtasks" / "subtask-1.md"
    subtask_path.write_text("""# Subtask: Example Subtask

## Goal

[What this subtask accomplishes]

## Implementation

[Specific steps or code]

## Test Case

[How to verify completion]
""")
    
    return project_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a Socratic Ideation Tree project"
    )
    parser.add_argument("project_name", help="Name of the project")
    parser.add_argument(
        "--path",
        default=".",
        help="Base directory for project (default: current directory)"
    )
    
    args = parser.parse_args()
    base_path = Path(args.path).resolve()
    
    project_path = init_project(args.project_name, base_path)
    
    print(f"Initialized project at: {project_path}")
    print(f"""
Structure created:
{args.project_name}/
├── INTENT.md
└── ideas/
    └── example-idea/
        ├── IDEA.md
        └── tasks/
            └── example-task/
                ├── TASK.md
                └── subtasks/
                    └── subtask-1.md

Next steps:
1. Edit INTENT.md to define your project vision and constraints
2. Rename or delete example-idea/ and create your own ideas
3. Use '/auto-ideate' to explore branches automatically
""")


if __name__ == "__main__":
    main()
