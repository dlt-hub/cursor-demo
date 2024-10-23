# dlt + Cursor.ai 🖱️: A Practical Approach

A research project exploring how effectively novice users can create working dlt pipelines using AI assistance. The core hypothesis is that with proper AI guidance, even users new to dlt can successfully build and maintain data pipelines, and potentially develop basic custom sources.

## Development Tiers

**Tier 1: Basic Pipeline Development (90%+ Success Rate)**
- Single verified source usage
- Minimal configuration required
- Single-shot success highly likely
- Perfect for users new to dlt

**Tier 2: Advanced Pipeline Development (70% Success Rate)**
- Hacked sources, custom sources, multiple resources
- Incremental loading support
- Transformations
- Some iteration expected
- Suitable for users with basic dlt experience

**Tier 3: Experimental Development (35-55% Success Rate)**
- Custom source creation
- Advanced transformations
- Complex error handling
- Multiple iterations likely
- For users ready to dive deeper

## Research Goals

This project specifically examines:
- How effectively can AI assist novice users in creating working pipelines?
- What is the feasibility of guided custom source development?
- Where do users typically need the most assistance?
- What patterns lead to successful first-time implementations?

## Development Pattern

The approach leverages:
- Thoughtful prompts that tap into Cursor.ai's understanding of dlt
- Strategic model selection between deepseek-chat and claude-3.5-sonnet
- Intelligent use of Cursor's reranking and codebase search

## Model Selection

| Model | Best For | Notes |
|-------|----------|--------|
| deepseek-chat | Quick answers, basic pipelines | Free, fast responses |
| claude-3.5-sonnet-200k | Complex reasoning, source development | Paid, deeper understanding |

This isn't just about code generation - it's about understanding how effectively AI can bridge the gap between dlt's capabilities and novice users' needs. The tiered approach provides a clear progression path while setting realistic expectations for success at each level.