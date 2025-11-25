# Output Patterns

Templates and examples for different output types across domains.

## Software Development

### Feature Specification

```markdown
# Feature: [Name]

## User Story
As a [user type]
I want to [action/goal]
So that [benefit/value]

## Acceptance Criteria
- [ ] Given [context], When [action], Then [outcome]
- [ ] Performance: [metric] < [threshold]
- [ ] Security: [requirement]
- [ ] Accessibility: [standard]

## Technical Specification

### API Changes
- Endpoint: `[METHOD] /api/[path]`
- Request: `{schema}`
- Response: `{schema}`

### Database Changes
- Table: [name]
- Migration: [description]

### UI Changes
- Component: [name]
- State Management: [approach]

## Testing Strategy
- Unit Tests: [coverage target]
- Integration Tests: [scenarios]
- E2E Tests: [user journeys]

## Rollout Plan
- [ ] Feature Flag: [name]
- [ ] Monitoring: [metrics]
- [ ] Rollback: [procedure]
```

### GitHub Issue Template

```markdown
## Description
[Clear problem statement]

## Current Behavior
[What happens now]

## Expected Behavior
[What should happen]

## Reproduction Steps
1. [Step one]
2. [Step two]

## Acceptance Criteria
- [ ] [Testable criterion]

## Technical Notes
[Implementation hints]

## Definition of Done
- [ ] Code complete
- [ ] Tests passing
- [ ] Documentation updated
- [ ] Code reviewed
```

## Research Projects

### Experiment Design

```markdown
# Experiment: [Name]

## Hypothesis
[If X then Y because Z]

## Variables
- Independent: [What we manipulate]
- Dependent: [What we measure]
- Controlled: [What we keep constant]

## Method

### Participants/Samples
[Description and N]

### Materials
- [Equipment/software needed]

### Procedure
1. [Step-by-step protocol]

## Analysis Plan
- Statistical Test: [name]
- Effect Size: [measure]
- Power Analysis: [calculation]

## Expected Outcomes
- Supporting Result: [what it looks like]
- Null Result: [interpretation]
- Contrary Result: [implications]

## Timeline
- Setup: [duration]
- Data Collection: [duration]
- Analysis: [duration]
```

## Business Strategy

### Initiative Proposal

```markdown
# Initiative: [Name]

## Executive Summary
[One paragraph overview]

## Business Case

### Problem
[Current pain point]

### Solution
[Proposed approach]

### Value Proposition
- Cost Savings: $[amount]
- Revenue Impact: $[amount]
- Efficiency Gain: [metric]

## Implementation Plan

### Phase 1: [Name] (Weeks 1-4)
- Deliverable: [what]
- Success Metric: [measure]

### Phase 2: [Name] (Weeks 5-8)
- Deliverable: [what]
- Success Metric: [measure]

## Resource Requirements
- Budget: $[amount]
- Team: [roles needed]
- Tools: [systems/software]

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |

## Success Metrics
- [ ] KPI 1: [target]
- [ ] KPI 2: [target]
```

## Personal Development

### Goal Achievement

```markdown
# Goal: [Name]

## Vision
[Detailed description of success]

## Why This Matters
- Personal Value: [alignment]
- Impact on Others: [benefit]
- Long-term Vision: [connection]

## Measurable Outcomes
- [ ] Quantitative: [number-based target]
- [ ] Qualitative: [experience-based target]

## Weekly Habits

| Habit | Frequency | Time | Trigger |
|-------|-----------|------|---------|
| [Action] | [N times] | [Duration] | [Cue] |

## Progress Tracking

### Week 1
- [ ] Completed: [what]
- Challenges: [what]
- Adjustments: [what]

## Accountability
- Partner: [who]
- Check-in: [frequency]
- Consequence/Reward: [what]
```

## Quality Standards

### Completeness Checklist

Every output should have:
- [ ] Clear objective/purpose statement
- [ ] Measurable success criteria
- [ ] Dependencies explicitly stated
- [ ] Time/effort estimation
- [ ] Next steps or subtasks defined

### Specificity Levels

| Level | Example |
|-------|---------|
| Too Vague | "Improve the system performance" |
| Better | "Reduce API response time" |
| Best | "Reduce API response time to <200ms for 95th percentile" |

### Testability Criteria

| Level | Example |
|-------|---------|
| Poor | "Make the UI more intuitive" |
| Good | "Users complete checkout in <3 clicks" |
| Best | "New users complete checkout in <3 clicks with <5% abandonment" |

## Anti-Pattern Examples

### Overloaded Task
```markdown
# Task: Build entire application
[Too broad, impossible to estimate]
```

### Vague Criteria
```markdown
## Acceptance Criteria
- [ ] Works well
- [ ] Users are happy
- [ ] Fast enough
```

### Missing Dependencies
```markdown
## Implementation
Just start coding the feature
[No mention of prerequisites]
```

### No Success Metrics
```markdown
## Outcome
The feature is implemented
[No way to measure success]
```

## Tool-Specific Formats

### Jira/Linear
- Use native fields for priority, assignee, labels
- Put detailed criteria in description
- Link dependencies using native linking

### GitHub Projects
- Use issue templates
- Leverage labels for categorization
- Use milestones for grouping

### Notion/Obsidian
- Use database properties for metadata
- Embed related documents
- Create views for different perspectives

### Plain Markdown
- Consistent heading hierarchy
- Include front matter for metadata
- Use checkboxes for trackable items
