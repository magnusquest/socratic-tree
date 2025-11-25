# 🌳 Socratic Ideation Tree

A Claude Code skill that transforms abstract goals into concrete, actionable tasks through systematic Socratic questioning and hierarchical decomposition.

## What It Does

The Socratic Ideation Tree guides you from vague intentions to executable plans through structured inquiry:

```
Abstract Goal → Specific Ideas → Implementation Plans → Concrete Tasks
```

It works for any domain:

| Domain | Flow |
|--------|------|
| **Software** | Project → Features → Architecture → Code Tasks |
| **Research** | Question → Hypotheses → Experiments → Procedures |
| **Business** | Strategy → Initiatives → Projects → Deliverables |
| **Personal** | Vision → Goals → Habits → Actions |

## Installation

### For Claude Code

1. Download or clone this repository
2. Place the `socratic-ideation-tree` folder in your Claude Code skills directory
3. The skill will automatically activate when you ask Claude to break down, plan, or structure projects

### Manual Usage

You can also use the framework manually by following the templates in `SKILL.md` and the reference files.

## Quick Start

### 1. Initialize a Project

```bash
python scripts/init_project.py my-project
cd my-project
```

This creates:
```
my-project/
├── INTENT.md           # Define your vision here
└── ideas/
    └── example-idea/   # Template to customize
        ├── IDEA.md
        └── tasks/
            └── example-task/
                ├── TASK.md
                └── subtasks/
```

### 2. Define Your Intent

Edit `INTENT.md` to capture your project's essence:

```markdown
# Project Intent: My App

## Vision
Create a simple task management app that feels faster than paper.

## Core Values
- **Simplicity**: Every feature must justify its complexity
- **Speed**: Instant response, no loading screens

## Constraints
- Time: 30 days to MVP
- Resources: Solo developer, $0 budget

## Success Metrics
- [ ] Tasks created in <3 clicks
- [ ] Page load <100ms
```

### 3. Generate Ideas

Either manually create ideas or use auto-ideation:

```
/auto-ideate --branches 3 --focus idea
```

### 4. Decompose to Tasks

Continue breaking down until tasks are atomic and actionable (2-4 hours each).

## Core Concepts

### The Four Phases

1. **Intent Crystallization**: Define vision, values, constraints, and success metrics
2. **Idea Generation**: Explore 3-5 different approaches with tradeoffs
3. **Task Decomposition**: Break ideas into specific, testable tasks
4. **Iterative Refinement**: Continue until tasks are atomic and assignable

### Socratic Questions

Each phase uses targeted questions:

| Phase | Example Questions |
|-------|-------------------|
| Intent | "What transformation are you achieving?" |
| Ideas | "What are 3-5 different ways to achieve this?" |
| Tasks | "What specific steps make this real?" |
| Refinement | "How will you know this is complete?" |

### Dot-Prefix Convention

Auto-generated suggestions use `.` prefix to indicate pending review:

```
ideas/
├── approved-idea/           # No dot = accepted
├── .suggested-idea-1/       # Dot = pending review
│   ├── .IDEA.md
│   └── .exploration.md
└── .suggested-idea-2/
```

**To accept**: Remove the `.` prefix
```bash
mv ideas/.suggested-idea ideas/suggested-idea
```

**To reject**: Delete or document in `.feedback.md`

## Project Structure

```
project-name/
├── INTENT.md              # Core values, constraints, success criteria
├── ideas/
│   ├── idea-1/
│   │   ├── IDEA.md        # Concept definition
│   │   └── tasks/
│   │       └── task-1/
│   │           ├── TASK.md
│   │           └── subtasks/
│   │               └── subtask-1.md
│   └── .idea-2/           # Auto-generated (pending review)
├── .session-xxx.md        # Auto-ideation session summaries
└── .feedback.md           # Track suggestion patterns
```

## Auto-Ideation

The `/auto-ideate` command enables autonomous exploration:

```bash
# Basic exploration
/auto-ideate

# Deep dive into specific idea
/auto-ideate --context "INTENT.md,ideas/feature-x/IDEA.md" --depth 5

# Broad exploration of alternatives  
/auto-ideate --branches 5 --strategy breadth

# Focus on task breakdown
/auto-ideate --focus task
```

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--context` | INTENT.md | Files to load for context |
| `--depth` | 3 | Maximum exploration depth |
| `--branches` | 3 | Number of parallel paths |
| `--focus` | auto | Target: intent\|idea\|task\|subtask |
| `--strategy` | balanced | Strategy: breadth\|depth\|balanced |
| `--max-iterations` | 10 | Stop after n iterations |

## Templates

### INTENT.md
```markdown
# Project Intent: [Name]

## Vision
[End state description]

## Core Values
- [Principle]: [Why it matters]

## Constraints
- Time: [Deadline]
- Resources: [Budget, team]
- Scope: [Boundaries]

## Success Metrics
- [ ] [Quantifiable outcome]

## Decision Log
- [Date]: [Decision and rationale]
```

### IDEA.md
```markdown
# Idea: [Name]

## Concept
[One paragraph description]

## Why This Approach
- Aligns with [value] because...

## Key Components
1. [Component]: [Purpose]

## Risk Assessment
- Primary risk: [Risk]
- Mitigation: [Strategy]
```

### TASK.md
```markdown
# Task: [Name]

## Objective
[Single sentence]

## Acceptance Criteria
- [ ] Given [context], when [action], then [outcome]

## Dependencies
- Blocked by: [Previous tasks]
- Blocks: [Future tasks]

## Estimated Effort
[Time estimate]

## Subtasks
1. [ ] [Atomic action]
```

## Reference Files

| File | Purpose |
|------|---------|
| `references/auto-ideate.md` | Detailed auto-ideation guide |
| `references/workflows.md` | Sequential, parallel, and conditional patterns |
| `references/output-patterns.md` | Domain-specific templates (software, research, business, personal) |

## Best Practices

1. **Start with Intent**: Spend time getting INTENT.md right—it guides everything
2. **Explore Before Committing**: Generate multiple ideas before choosing
3. **Go Deep Enough**: Break down until tasks are 2-4 hours max
4. **Document Decisions**: Keep a decision log in INTENT.md
5. **Review Suggestions**: Don't let `.` prefixed items accumulate

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Premature Specificity | Detailing before understanding | Complete intent phase first |
| Analysis Paralysis | Endless exploration | Limit to 3-5 options |
| Orphan Tasks | Tasks without context | Every task connects to intent |
| Vague Completion | No clear "done" criteria | Add measurable acceptance criteria |

## Integration

### With AI Coding Assistants
- Subtasks can reference `@copilot` for implementation
- TASK.md provides context for code generation
- Acceptance criteria become test cases

### With Project Management
- INTENT.md → Project Charter
- Ideas → Epics
- Tasks → Tickets/Cards
- Subtasks → Checklist items

### With Version Control
- Each phase → Git commit
- Each idea → Feature branch
- Task completion → Pull request

## License

MIT License - Feel free to adapt and use for any purpose.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Transform your ideas into action.** Start with why, explore what, then execute how. 🌳
