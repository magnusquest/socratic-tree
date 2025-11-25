# Workflow Patterns

Patterns for structuring Socratic ideation across different project types.

## Sequential Workflows

### Linear Progression
Best for: Projects with clear dependencies and phases

```
Intent → Idea Selection → Sequential Tasks → Subtask Execution
```

**Guiding Questions:**
1. "What must be completed before anything else can begin?"
2. "What becomes possible only after X is done?"
3. "What's the critical path through this project?"

### Iterative Refinement
Best for: Projects requiring experimentation and learning

```
Intent → Prototype Idea → Test → Learn → Refined Idea → ...
```

**Guiding Questions:**
1. "What's the smallest experiment that validates this approach?"
2. "What did we learn that changes our assumptions?"
3. "How should the next iteration differ based on feedback?"

## Conditional Logic Patterns

### Decision Tree
Best for: Projects with multiple contingency paths

```
if (Condition A):
    → Idea Path 1 → Task Set Alpha
elif (Condition B):
    → Idea Path 2 → Task Set Beta
else:
    → Fallback Idea → Minimal Task Set
```

**In IDEA.md:**
```markdown
## Conditional Paths

### If [budget > $10k]:
- Full feature set
- Advanced analytics
- Custom UI design

### Else if [budget > $5k]:
- Core features only
- Basic analytics
- Template-based UI

### Else:
- Minimum viable product
- No analytics
- Stock UI components
```

### Risk Mitigation
Best for: High-uncertainty projects

```
Main Path: [Ideal approach]
├── Risk Point 1: [What could fail]
│   └── Mitigation: [Backup plan]
├── Risk Point 2: [What could fail]
│   └── Mitigation: [Backup plan]
```

**Guiding Questions:**
1. "What assumptions could be wrong?"
2. "What would we do if X doesn't work?"
3. "How would we know early if this is failing?"

## Parallel Execution Patterns

### Divide and Conquer
Best for: Large projects with independent workstreams

```
Intent
├── Workstream A (Independent)
│   ├── Idea A1
│   └── Tasks A1.1, A1.2
├── Workstream B (Independent)
│   ├── Idea B1
│   └── Tasks B1.1, B1.2
└── Integration Point
    └── Merge Tasks
```

**Guiding Questions:**
1. "Which parts can be developed independently?"
2. "What are the integration points?"
3. "How do we ensure consistency across workstreams?"

### Pipeline
Best for: Projects with staged processing

```
Stage 1: Input Processing
    ↓ (Output: Processed Data)
Stage 2: Transformation
    ↓ (Output: Transformed Data)
Stage 3: Output Generation
```

## Domain-Specific Patterns

### Software Development
```
Feature Request
→ User Story Definition
→ Technical Design
→ Implementation Tasks
→ Testing Tasks
→ Deployment Tasks
```

### Research
```
Research Question
→ Literature Review
→ Hypothesis Formation
→ Experiment Design
→ Data Collection
→ Analysis
→ Conclusion
```

### Business (OKR)
```
Objective
→ Key Result 1
    → Initiative A → Project Tasks
→ Key Result 2
    → Initiative B → Project Tasks
```

### Personal (Habit Stacking)
```
Goal
→ Keystone Habit
    → Trigger → Routine → Reward
→ Stacked Habit 1
→ Stacked Habit 2
```

## Meta-Workflow Patterns

### Exploration vs Exploitation

```python
if exploration_phase:
    generate_many_shallow_ideas()
    test_assumptions_quickly()
    eliminate_weak_paths()
else:  # exploitation_phase
    deep_dive_on_best_path()
    optimize_for_execution()
    measure_and_refine()
```

### Convergent-Divergent Thinking

**Divergent Phase:**
- "What are all possible approaches?"
- "What if we had no constraints?"
- "What would [other domain] do?"

**Convergent Phase:**
- "Which approach best fits constraints?"
- "What's the minimum viable solution?"
- "How do we start tomorrow?"

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Analysis Paralysis | Endless refinement | Set iteration limits, force decisions |
| Premature Convergence | Choosing before understanding | Mandatory exploration phase |
| Orphaned Tasks | Tasks without parent purpose | Every task traces to intent |
| Scope Creep | Expanding requirements | Lock intent before ideation |

## Optimization Techniques

### Critical Path Identification
1. Map all task dependencies
2. Calculate longest path
3. Focus resources on critical path
4. Parallelize non-critical tasks

### Bottleneck Analysis
1. Identify resource constraints
2. Find tasks competing for same resource
3. Serialize or find alternatives
4. Monitor and adjust

### Progressive Elaboration
1. Start with high-level tasks
2. Decompose only next sprint's work
3. Keep future tasks flexible
4. Refine as you learn
