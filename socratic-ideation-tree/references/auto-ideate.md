# Auto-Ideate: Autonomous Exploration

Autonomous Socratic exploration of ideation branches through self-directed questioning. Claude acts as both questioner and responder, exploring potential paths through simulated dialogue based on project context.

## Usage

```
/auto-ideate [options]
```

### Options

| Option                 | Default                                                             | Description                         |
| ---------------------- | ------------------------------------------------------------------- | ----------------------------------- |
| `--context <files>`    | INTENT.md + current branch + parent main context files (if present) | Context files to load               |
| `--depth <n>`          | 3                                                                   | Maximum exploration depth           |
| `--branches <n>`       | 3                                                                   | Number of parallel paths            |
| `--focus <phase>`      | auto-detect                                                         | Target: intent\|idea\|task\|subtask |
| `--strategy <type>`    | balanced                                                            | Strategy: breadth\|depth\|balanced  |
| `--max-iterations <n>` | 10                                                                  | Stop after n iterations             |

### Examples

```bash
# Basic exploration
/auto-ideate

# Deep dive into specific idea
/auto-ideate --context "INTENT.md,ideas/feature-x/IDEA.md" --depth 5

# Broad exploration of alternatives
/auto-ideate --branches 5 --strategy breadth

# Focus on task breakdown
/auto-ideate --focus task --context "ideas/auth-system/IDEA.md"
```

## Output Convention: Dot-Prefix

Auto-ideate creates suggestions **in the main tree** using `.` prefix to indicate pending review status.

### Structure

```
project-name/
├── INTENT.md
├── ideas/
│   ├── approved-idea/           # User-approved (no dot)
│   │   ├── IDEA.md
│   │   └── tasks/
│   ├── .suggested-idea-1/       # Auto-generated (dot prefix)
│   │   ├── .IDEA.md
│   │   └── .exploration.md      # Q&A trail
│   └── .suggested-idea-2/
│       └── .IDEA.md
├── .session-[timestamp].md      # Session summary
└── .feedback.md                 # Rejection patterns
```

### Promotion Workflow

To accept a suggestion:

```bash
# Rename to remove dot prefix
mv ideas/.suggested-idea/ ideas/suggested-idea/
mv ideas/suggested-idea/.IDEA.md ideas/suggested-idea/IDEA.md
```

To reject:

```bash
# Delete or document rejection pattern in .feedback.md
rm -rf ideas/.suggested-idea/
```

## Execution Protocol

### Phase 1: Context Analysis

1. **Load context files**

   - Parse INTENT.md for values, constraints, metrics
   - Identify current position in hierarchy
   - Extract patterns from existing ideas/tasks
   - Traverse parent directories and include the main context file (if present) from each level, stopping when `INTENT.md` is reached

2. **Determine exploration scope**
   - No ideas exist → generate ideas
   - Ideas lack tasks → decompose to tasks
   - Tasks lack subtasks → create subtasks
   - Structure complete → explore alternatives

### Phase 2: Simulated Socratic Dialogue

For each branch (up to `num_branches`):

1. Load context
2. For each iteration (up to `max_iterations`):
   - **Questioner**: Generate Socratic question based on context and phase
   - **Responder**: Simulate user response using intent values
   - **Analyzer**: Extract actionable insight
   - **Check convergence**: If insight concrete enough:
     - Create artifact with `.` prefix
     - Break loop
   - **Update context**: Append Q&A for next iteration

### Phase 3: Artifact Generation

Each successful exploration produces:

**Location**: `ideas/.idea-name/.IDEA.md` (or appropriate level)

**Exploration Trail**: `ideas/.idea-name/.exploration.md`

```markdown
# Exploration: [idea-name]

## Path

- Q1: [Question]
- A1: [Simulated response]
- I1: [Insight extracted]
- Q2: [Refined question]
- A2: [Deeper response]
- I2: [Refined insight]

## Confidence Score

- Alignment with intent: [0-100]
- Completeness: [0-100]
- Feasibility: [0-100]

## Recommendation

[Should user pursue? Why/why not?]
```

## Question Generation Strategies

### Convergent (narrow possibilities)

- "Given constraint X, which option remains viable?"
- "What's the simplest implementation satisfying Y?"
- "Which dependency must be resolved first?"

### Divergent (expand possibilities)

- "What alternative approaches haven't been considered?"
- "How might this work differently in context Z?"
- "What if constraint X were removed?"

### Clarifying (increase precision)

- "What specifically does 'success' mean here?"
- "How would you measure completion?"
- "What's the minimum viable version?"

## Exploration Strategies

### Breadth-First

Explore all options at current level before going deeper:

1. For each possible idea: generate shallow task list, score viability
2. Rank and filter all ideas

### Depth-First

Fully elaborate one path before trying others:

1. Select most promising idea
2. Decompose completely to subtasks
3. Validate against intent

### Balanced (Default)

Interleave based on confidence:

- High confidence (>80%): go deeper
- Low confidence (<80%): explore alternatives

## Convergence Criteria

Stop iterating when:

1. **Concrete Actions**: Can execute without further clarification
2. **Measurable Outcomes**: Has specific success criteria
3. **Resource Bounded**: Time/effort estimates provided
4. **Dependencies Clear**: Prerequisites explicitly stated
5. **Iteration Limit**: Max iterations reached

## Session Summary

After exploration, create `.session-[timestamp].md` at project root:

```markdown
# Exploration Session: [timestamp]

## Context

- Intent Focus: [Primary goals]
- Strategy: [breadth/depth/balanced]
- Branches Explored: [n]

## Discoveries

### High Confidence (>80%)

- **[idea-name]**: [Brief description]
  - Strength: [Why this works]
  - Location: `ideas/.idea-name/`

### Medium Confidence (50-80%)

- [Paths worth considering with caveats]

### Low Confidence (<50%)

- [Paths explored but not recommended]

## Recommended Next Steps

- Review: [Most promising path]
- Promote: [Which suggestion to integrate]
- Explore Further: [Gaps identified]

## Statistics

- Questions Generated: [n]
- Iterations: [n]
- Unique Paths: [n]
```

## Feedback Tracking

Track rejection patterns in `.feedback.md` at project root:

```markdown
# Suggestion Feedback

## Rejected Patterns

- Over-emphasizes: [aspect]
- Under-considers: [constraint]
- Misunderstands: [intent element]

## Successful Patterns

- Well-aligned: [aspect]
- Good balance of: [tradeoff]
- Clever solution for: [problem]
```

## User Response Simulation

Base simulated responses on INTENT.md:

- **Values**: Core values from intent
- **Constraints**: Project constraints
- **Style**: Detected communication style
- **Domain**: Inferred domain knowledge
- **Preferences**: Patterns from existing choices

## Advanced Features

### Multi-Agent Simulation

Simulate stakeholder perspectives:

| Agent     | Focus          | Concerns                    |
| --------- | -------------- | --------------------------- |
| Developer | Implementation | Complexity, maintainability |
| User      | Experience     | Simplicity, value           |
| Manager   | Delivery       | Timeline, resources         |
| Architect | Design         | Scalability, patterns       |

### Parallel Universe Exploration

Explore "what-if" scenarios:

- **Unlimited Resources**: Remove budget constraint
- **Tight Deadline**: Amplify time constraint
- **Different Tech**: Swap tech stack
- **Pivot Market**: Change target user

## Best Practices

1. **Start Small**: Focused explorations before broad searches
2. **Iterate on Intent**: Refine INTENT.md based on discoveries
3. **Review Regularly**: Don't let `.` prefixed items accumulate
4. **Learn from Patterns**: Update based on successful paths
5. **Maintain Coherence**: All artifacts connect back to intent

## Limitations

- User simulation is approximation based on context
- May generate plausible but unworkable paths
- Should not replace human judgment for critical decisions
- Best used for exploration, not final decision making
