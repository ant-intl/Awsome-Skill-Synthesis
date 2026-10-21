<h1 align="center">Awesome-Skill-Synthesis</h1>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies **From Heterogeneous Evidence to Reusable Procedures: A Survey of Agent Skill Synthesis** and organizes research on agent skill synthesis and reuse.

## Contents

| Part | Overview | Paper Count |
| --- | --- | ---: |
| [1. Skill Sources](#sources) | Sources provide the evidence used to synthesize skills. | 114 |
| [2. Skill Synthesis Methods](#synthesis) | Methods transform source evidence into reusable skills. | 125 |
| [3. Skill Representations](#representations) | Representations define how skills are stored and accessed. | 131 |
| [4. Skill Utilization](#utilization) | Agents select, execute, and compose skills to solve tasks. | 80 |
| [5. Skill Evaluation](#evaluation) | Evaluation measures skill quality and effects on task performance. | 51 |
| [6. Skill Evolution](#evolution) | Evolution updates skills and maintains their libraries. | 59 |

<a id="sources"></a>

## 1. Skill Sources

Skills draw on human supervision, external knowledge, and agent experience.

- **[Human Supervision](#sources-human-supervision)**
  - [Behavioral Demonstrations](#sources-human-supervision-behavioral-demonstrations)
  - [Corrective Feedback](#sources-human-supervision-corrective-feedback)
- **[External Knowledge](#sources-external-knowledge)**
  - [Documentary Artifacts](#sources-external-knowledge-documentary-artifacts)
  - [Software Artifacts](#sources-external-knowledge-software-artifacts)
  - [Multimodal Artifacts](#sources-external-knowledge-multimodal-artifacts)
- **[Agent Experience](#sources-agent-experience)**
  - [Execution Trajectories](#sources-agent-experience-execution-trajectories)
  - [Exploratory Practice](#sources-agent-experience-exploratory-practice)
  - [Deployment Experience](#sources-agent-experience-deployment-experience)

<a id="sources-human-supervision"></a>

### Human Supervision

<a id="sources-human-supervision-behavioral-demonstrations"></a>

#### Behavioral Demonstrations

<!-- paper:e05 -->
- (*2025*) **ALLOY: Generating Reusable Agent Workflows from User Demonstration** [[📝 Paper](https://arxiv.org/abs/2510.10049)]  
  → ALLOY converts user demonstrations into editable workflows that agents can reuse across related web tasks.

<!-- paper:shen2019skillbot -->
- (*2019*) **SkillBot: Towards automatic skill development via user demonstration** [[📝 Paper](https://aclanthology.org/N19-4018/)]  
  → SkillBot converts on-screen user demonstrations into personal-assistant skills with natural-language understanding and executable actions.

<!-- paper:wang2023demo2code -->
- (*2023*) **Demo2Code: From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought** [[📝 Paper](https://arxiv.org/abs/2305.16744)] [[💻 Code](https://github.com/portal-cornell/demo2code)]  
  → Demo2Code summarizes demonstrations into task specifications and expands those specifications into executable robot programs.

<!-- paper:yin2025hybridrobotskill -->
- (*2025*) **An LLM-enabled human demonstration-assisted hybrid robot skill synthesis approach for human-robot collaborative assembly** [[📝 Paper](https://www.sciencedirect.com/science/article/pii/S0007850625000630)]  
  → This approach combines human demonstrations, a mixed-reality interface, and LLM reasoning to synthesize robot skills for collaborative assembly.

<!-- paper:gu2025colada -->
- (*2024*) **Continual Robot Skill and Task Learning via Dialogue** [[📝 Paper](https://arxiv.org/abs/2409.03166)]  
  → CoLaDA uses dialogue to acquire and confirm robot skills and task knowledge for continual learning.

<!-- paper:xgarrett2024skillmimicgen -->
- (*2024*) **SkillMimicGen: Automated Demonstration Generation for Efficient Skill Learning and Deployment** [[📝 Paper](https://arxiv.org/abs/2410.18907)] [[🌐 Project](https://skillgen.github.io/)]  
  → SkillMimicGen expands demonstrated robot skills into additional training demonstrations for efficient acquisition and deployment.

<!-- paper:xzhao2025generalizable -->
- (*2026*) **Generalizable Hierarchical Skill Learning via Object-Centric Representation** [[📝 Paper](https://arxiv.org/abs/2510.21121)]  
  → This method learns object-centric skill representations that connect high-level vision-language planning with low-level robot control.

<!-- paper:xfu2024language -->
- (*2024*) **Language-guided Skill Learning with Temporal Variational Inference** [[📝 Paper](https://arxiv.org/abs/2402.16354)]  
  → This method uses temporal variational inference to learn language-grounded skills from behavioral sequences.

<!-- paper:xingelhag2024robotic -->
- (*2024*) **A Robotic Skill Learning System Built Upon Diffusion Policies and Foundation Models** [[📝 Paper](https://arxiv.org/abs/2403.16730)]  
  → This system learns diffusion-policy skills from demonstrations and uses foundation models to select and coordinate them for robot tasks.

<!-- paper:xli2025atomic -->
- (*2025*) **An Atomic Skill Library Construction Method for Data-Efficient Embodied Manipulation** [[📝 Paper](https://arxiv.org/abs/2501.15068)]  
  → This method decomposes manipulation tasks into subtasks and builds an expanding atomic skill library through data collection and vision-language-action fine-tuning.

<!-- paper:xsi2026vla -->
- (*2026*) **VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models** [[📝 Paper](https://arxiv.org/abs/2605.29562)]  
  → VLA-Pro transfers procedural memory across tasks through skill modules for vision-language-action models.

<!-- paper:xju2024rethinking -->
- (*2024*) **Rethinking Mutual Information for Language Conditioned Skill Discovery on Imitation Learning** [[📝 Paper](https://arxiv.org/abs/2402.17511)]  
  → LCSD uses mutual-information objectives to learn discrete language-conditioned skills from multitask demonstrations.

<a id="sources-human-supervision-corrective-feedback"></a>

#### Corrective Feedback

<!-- paper:castelli2007augmentation -->
- (*2007*) **Augmentation-Based Learning combining observations and user edits for Programming-by-Demonstration** [[📝 Paper](https://doi.org/10.1016/j.knosys.2007.04.007)]  
  → Augmentation-Based Learning combines task demonstrations with direct user edits to incrementally construct executable procedure models.

<!-- paper:mericli2011taskrefinement -->
- (*2011*) **Task refinement for autonomous robots using complementary corrective human feedback** [[📝 Paper](https://www.cs.cmu.edu/~mmv/papers/11ijars-cetin.pdf)]  
  → This robot-learning method uses corrective human feedback to refine task behavior beyond the coverage of initial demonstrations.

<!-- paper:xchen2026few -->
- (*2026*) **A Few Words Go a Long Way: Language Guided Robot Policy Synthesis** [[📝 Paper](https://arxiv.org/abs/2607.23784)]  
  → This approach synthesizes robot policy programs from language guidance, turning human instructions into executable control procedures.

<a id="sources-external-knowledge"></a>

### External Knowledge

<a id="sources-external-knowledge-documentary-artifacts"></a>

#### Documentary Artifacts

<!-- paper:c51 -->
- (*2025*) **SOP-Agent: Empower General Purpose AI Agent with Domain-Specific SOPs** [[📝 Paper](https://arxiv.org/abs/2501.09316)]  
  → SOP-Agent converts domain-specific standard operating procedures into structured guidance for general-purpose agents.

<!-- paper:c12 -->
- (*2026*) **SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources** [[📝 Paper](https://arxiv.org/abs/2604.03964)] [[💻 Code](https://github.com/ma-compbio-lab/SkillFoundry)]  
  → SkillFoundry mines heterogeneous scientific resources, extracts operational contracts, and validates executable skill packages in an evolving library.

<!-- paper:c14 -->
- (*2026*) **Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents** [[📝 Paper](https://arxiv.org/abs/2606.09316)]  
  → Anything2Skill extracts evidence-grounded procedures from external knowledge and compiles them into structured contracts maintained in a persistent SkillBank.

<!-- paper:e06 -->
- (*2025*) **LLM Agents Making Agent Tools** [[📝 Paper](https://arxiv.org/abs/2502.11705)] [[💻 Code](https://github.com/KatherLab/ToolMaker)]  
  → ToolMaker converts scientific papers and their code into reusable tools that LLM agents can invoke.

<!-- paper:shen2026skillalpha -->
- (*2026*) **Progressive Agent Skill Generation via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2608.01678)] [[💻 Code](https://github.com/ejhshen/skill-alpha)]  
  → SkillAlpha progressively generates reusable agent skills through reinforcement learning and task feedback.

<!-- paper:xsha2026skillcenter -->
- (*2026*) **SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents** [[📝 Paper](https://arxiv.org/abs/2607.07676)] [[💻 Code](https://github.com/LabRAI/SkillCenter)]  
  → SkillCenter builds a large source-grounded library by extracting and organizing reusable procedures from external resources.

<!-- paper:xcao2026guideskill -->
- (*2026*) **GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning** [[📝 Paper](https://arxiv.org/abs/2607.26160)]  
  → GuideSkill converts clinical guidelines into executable skills and evolves them using execution feedback for grounded clinical reasoning.

<!-- paper:xzhou2026skillgenbench -->
- (*2026*) **SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.18693)] [[💻 Code](https://github.com/QuantaAlpha/SkillGenBench)]  
  → SkillGenBench evaluates skill-generation pipelines under controlled execution conditions and distinguishes task-conditioned synthesis from reusable library construction.

<!-- paper:e32 -->
- (*2026*) **Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality** [[📝 Paper](https://arxiv.org/abs/2602.08004)]  
  → This empirical study characterizes public Claude skill artifacts, including their structure, redundancy, usage patterns, and security risks.

<!-- paper:c45 -->
- (*2026*) **SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.15557)] [[💻 Code](https://github.com/EverMind-AI/SkillCorpus)]  
  → SkillCorpus consolidates public skill packages and evaluates their organization, quality, and usefulness for real-world agents.

<a id="sources-external-knowledge-software-artifacts"></a>

#### Software Artifacts

<!-- paper:e03 -->
- (*2026*) **Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction** [[📝 Paper](https://arxiv.org/abs/2603.11808)]  
  → This repository-mining framework extracts reusable procedural knowledge from open-source agentic codebases and assesses candidate skill quality.

<!-- paper:tong2026code2skill -->
- (*2026*) **Grounded Skill Synthesis from Code at Scale for Agentic Intelligence** [[📝 Paper](https://arxiv.org/abs/2609.05571)] [[💻 Code](https://github.com/ant-intl/Code2Skill)]  
  → Code2Skill extracts reusable procedural skills from source repositories with code-grounded workflow context, applicability boundaries, and source evidence.

<!-- paper:e06 -->
- (*2025*) **LLM Agents Making Agent Tools** [[📝 Paper](https://arxiv.org/abs/2502.11705)] [[💻 Code](https://github.com/KatherLab/ToolMaker)]  
  → ToolMaker converts scientific papers and their code into reusable tools that LLM agents can invoke.

<!-- paper:f07 -->
- (*2018*) **Learning Libraries of Subroutines for Neurally-Guided Bayesian Program Induction** [[📝 Paper](https://people.csail.mit.edu/asolar/papers/EllisMSST18.pdf)]  
  → This library-learning method discovers reusable subroutines while training a neural guide to search programs expressed in the evolving library.

<!-- paper:f08 -->
- (*2021*) **DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning** [[📝 Paper](https://doi.org/10.1145/3453483.3454080)] [[💻 Code](https://github.com/ellisk42/ec)]  
  → DreamCoder alternates program synthesis and abstraction learning to grow a library of reusable computational concepts.

<!-- paper:f10 -->
- (*2024*) **LILO: Learning Interpretable Libraries by Compressing and Documenting Code** [[📝 Paper](https://arxiv.org/abs/2310.19791)] [[💻 Code](https://github.com/gabegrand/lilo)]  
  → LILO compresses synthesized programs into reusable library functions and documents the abstractions with natural language.

<!-- paper:f11 -->
- (*2024*) **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** [[📝 Paper](https://arxiv.org/abs/2401.16467)] [[💻 Code](https://github.com/esteng/regal_program_learning)]  
  → ReGAL refactors task programs into shared abstractions that can be reused during subsequent program generation.

<!-- paper:xwang2026effiskill -->
- (*2026*) **EffiSkill: Agent Skill Based Automated Code Efficiency Optimization** [[📝 Paper](https://arxiv.org/abs/2603.27850)]  
  → EffiSkill constructs and applies reusable optimization skills to improve the execution efficiency of generated code.

<!-- paper:xlou2026lego -->
- (*2026*) **LEGO: An LLM Skill-Based Front-End Design Generation Platform** [[📝 Paper](https://arxiv.org/abs/2604.23355)] [[🌐 Project](https://github.com/loujc/LEGO-An-LLM-Skill-Based-Front-End-Design-Generation-Platform)]  
  → LEGO packages frontend implementation knowledge as reusable skills that guide LLM-based interface generation.

<!-- paper:xgaurav2025codemem -->
- (*2025*) **CodeMem: Architecting Reproducible Agents via Dynamic MCP and Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2512.15813)]  
  → CodeMem stores reusable executable procedures behind dynamic MCP interfaces to support reproducible agent execution.

<!-- paper:xgaurav2025synthesizing -->
- (*2025*) **Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation** [[📝 Paper](https://arxiv.org/abs/2512.20278)]  
  → This work examines architectures and challenges for generating reusable procedural memory from automated workflows.

<!-- paper:xhuang2025cascade -->
- (*2025*) **CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution** [[📝 Paper](https://arxiv.org/abs/2512.23880)]  
  → CASCADE builds a cumulative library of executable capabilities through autonomous development, testing, and skill evolution.

<!-- paper:xli2026human -->
- (*2026*) **From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs** [[📝 Paper](https://arxiv.org/abs/2606.07586)]  
  → This system packages expert knowledge and implementation resources into reusable skills for end-to-end LLM deployment on spatial NPUs.

<a id="sources-external-knowledge-multimodal-artifacts"></a>

#### Multimodal Artifacts

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:c12 -->
- (*2026*) **SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources** [[📝 Paper](https://arxiv.org/abs/2604.03964)] [[💻 Code](https://github.com/ma-compbio-lab/SkillFoundry)]  
  → SkillFoundry mines heterogeneous scientific resources, extracts operational contracts, and validates executable skill packages in an evolving library.

<!-- paper:c14 -->
- (*2026*) **Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents** [[📝 Paper](https://arxiv.org/abs/2606.09316)]  
  → Anything2Skill extracts evidence-grounded procedures from external knowledge and compiles them into structured contracts maintained in a persistent SkillBank.

<!-- paper:e04 -->
- (*2026*) **CUA-Skill: Develop Skills for Computer Using Agent** [[📝 Paper](https://arxiv.org/abs/2601.21123)] [[💻 Code](https://github.com/microsoft/cua_skill)] [[🌐 Project](https://microsoft.github.io/cua_skill/)]  
  → CUA-Skill organizes computer-use procedures in a skill library that combines operational guidance with resources for visual interaction.

<!-- paper:xche2026mmg2skill -->
- (*2026*) **MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?** [[📝 Paper](https://arxiv.org/abs/2606.01993)] [[💻 Code](https://github.com/NJU-LINK/MMG2Skill)]  
  → MMG2Skill distills real-world multimodal guides into reusable skills and improves them through subsequent agent interaction.

<!-- paper:xliu2026skilllens -->
- (*2026*) **SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation** [[📝 Paper](https://arxiv.org/abs/2608.10775)]  
  → SkillLens constructs visual skill cards for GUI-action retrieval and distills their guidance into an agent policy.

<!-- paper:xdeng2025open -->
- (*2025*) **Open-World Skill Discovery from Unsegmented Demonstrations** [[📝 Paper](https://arxiv.org/abs/2503.10684)] [[💻 Code](https://github.com/CraftJarvis/SkillDiscovery)]  
  → This method detects skill boundaries in unsegmented demonstration videos and learns reusable behaviors from the resulting clips.

<a id="sources-agent-experience"></a>

### Agent Experience

<a id="sources-agent-experience-execution-trajectories"></a>

#### Execution Trajectories

<!-- paper:c01 -->
- (*2024*) **ExpeL: LLM Agents Are Experiential Learners** [[📝 Paper](https://arxiv.org/abs/2308.10144)] [[💻 Code](https://github.com/LeapLabTHU/ExpeL)]  
  → ExpeL extracts reusable natural-language insights from successful and failed task experiences and retrieves them to guide subsequent agent decisions.

<!-- paper:e16 -->
- (*2026*) **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** [[📝 Paper](https://arxiv.org/abs/2603.25158)] [[💻 Code](https://github.com/Qwen-Applications/Trace2Skill)]  
  → Trace2Skill consolidates lessons from execution trajectories into transferable procedural skills with explicit applicability guidance.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:e13 -->
- (*2025*) **Inducing Programmatic Skills for Agentic Tasks** [[📝 Paper](https://arxiv.org/abs/2504.06821)] [[💻 Code](https://github.com/zorazrw/agent-skill-induction)]  
  → This framework induces executable programmatic skills from agent task experience and verifies them before reuse.

<!-- paper:c15 -->
- (*2026*) **SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2606.26669)]  
  → SkillDisCo distills shared control-flow structures from successful agent traces and compiles them into parameterized, callable procedural skills.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:xwu2025evolver -->
- (*2025*) **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle** [[📝 Paper](https://arxiv.org/abs/2510.16079)] [[💻 Code](https://github.com/KnowledgeXLab/EvolveR)]  
  → EvolveR connects experience collection, procedural abstraction, execution, and revision in an experience-driven agent lifecycle.

<!-- paper:xcao2025remember -->
- (*2026*) **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** [[📝 Paper](https://arxiv.org/abs/2512.10696)] [[💻 Code](https://github.com/agentscope-ai/ReMe)]  
  → ReMe extracts, retrieves, and refines procedural memories from agent experience to support adaptation across tasks.

<!-- paper:xforouzandeh2025learning -->
- (*2025*) **Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement** [[📝 Paper](https://arxiv.org/abs/2512.18950)] [[💻 Code](https://github.com/S-Forouzandeh/MACLA-LLM-Agents-AAMAS-2026-Conference)]  
  → MACLA maintains hierarchical procedural memories using Bayesian selection and contrastive refinement from task experience.

<!-- paper:xzhou2026wise -->
- (*2026*) **WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents** [[📝 Paper](https://arxiv.org/abs/2601.08158)]  
  → WISE-Flow turns service-agent trajectories into structured workflow experience that supports reusable procedural guidance and self-evolution.

<!-- paper:xli2026online -->
- (*2026*) **Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval** [[📝 Paper](https://arxiv.org/abs/2606.04391)] [[💻 Code](https://github.com/plusnli/online-skill-learning)]  
  → This web-agent framework learns skills online and retrieves them using the current environment state to improve applicability.

<!-- paper:xwang2026webxskill -->
- (*2026*) **WebXSkill: Skill Learning for Autonomous Web Agents** [[📝 Paper](https://arxiv.org/abs/2604.13318)] [[🌐 Project](https://github.com/aiming-lab/WebXSkill)]  
  → WebXSkill learns reusable web-interaction procedures from experience and combines procedural guidance with executable resources.

<!-- paper:xliu2026drive -->
- (*2026*) **DRIVE: Modeling Skills at the Reasoning and Interaction Levels for Web Agents under Continual Learning** [[📝 Paper](https://arxiv.org/abs/2605.23939)]  
  → DRIVE maintains reusable web-agent skills at both reasoning and interaction levels for continual task learning.

<!-- paper:xhan2025legomem -->
- (*2025*) **LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation** [[📝 Paper](https://arxiv.org/abs/2510.04851)]  
  → LEGOMem decomposes execution experience into modular procedural memories that multi-agent systems reuse for workflow automation.

<!-- paper:xhao2026automating -->
- (*2026*) **Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining** [[📝 Paper](https://arxiv.org/abs/2606.20363)] [[💻 Code](https://anonymous.4open.science/r/CUA-1680)]  
  → This method mines computer-use interaction trajectories to generate reusable SKILL.md instructions automatically.

<!-- paper:e21 -->
- (*2026*) **Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery** [[📝 Paper](https://arxiv.org/abs/2603.05860)]  
  → MACRO discovers recurring tool-use patterns in medical-imaging experience and turns them into reusable composite skills.

<!-- paper:e22 -->
- (*2026*) **Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory** [[📝 Paper](https://arxiv.org/abs/2606.09365)] [[💻 Code](https://github.com/manglu097/SkeMex)]  
  → This medical-agent framework distills clinical task experience into an evolving skill memory for transferable reasoning.

<!-- paper:e23 -->
- (*2026*) **ASPIRE: Agentic /Skills Discovery for Robotics** [[📝 Paper](https://arxiv.org/abs/2607.00272)]  
  → ASPIRE constructs and repairs reusable robot skills from multimodal execution traces and failure analysis.

<!-- paper:xwang2025integrating -->
- (*2025*) **Integrating failures in robot skill acquisition with offline action-sequence diffusion rl** [[📝 Paper](https://ieeexplore.ieee.org/document/10889202/)]  
  → This method learns robot skills from successful and failed offline action sequences using diffusion-based reinforcement learning.

<!-- paper:xliu2026procedural -->
- (*2026*) **Procedural Memory Distillation: Online Reflection for Self-Improving Language Models** [[📝 Paper](https://arxiv.org/abs/2607.01480)]  
  → Procedural Memory Distillation uses online reflection to convert execution experience into procedural knowledge internalized by a language model.

<!-- paper:xhe2026siri -->
- (*2026*) **SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training** [[📝 Paper](https://arxiv.org/abs/2606.02355)]  
  → SIRI derives intrinsic skills during reinforcement learning and internalizes their guidance in the agent policy.

<!-- paper:xzhang2026spyce -->
- (*2026*) **SPyCE: Skill-Policy Co-evolution for Multimodal Agents** [[📝 Paper](https://arxiv.org/abs/2607.13854)]  
  → SPyCE co-evolves reusable skills and multimodal agent policies using interaction experience.

<!-- paper:xli2026arise -->
- (*2026*) **ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2603.16060)] [[💻 Code](https://github.com/Skylanding/ARISE)]  
  → ARISE co-evolves intrinsic skills and agent reasoning through a hierarchical reinforcement-learning framework.

<a id="sources-agent-experience-exploratory-practice"></a>

#### Exploratory Practice

<!-- paper:e01 -->
- (*2023*) **Voyager: An Open-Ended Embodied Agent with Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.16291)] [[💻 Code](https://github.com/MineDojo/Voyager)] [[🌐 Project](https://voyager.minedojo.org/)]  
  → Voyager learns executable skills through Minecraft exploration, execution feedback, and iterative code refinement, then reuses them from a growing library.

<!-- paper:e07 -->
- (*2026*) **Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs** [[📝 Paper](https://arxiv.org/abs/2504.20406)]  
  → This approach discovers and verifies reusable software-scripting skills through offline simulations of API interactions.

<!-- paper:e09 -->
- (*2025*) **Automated Skill Discovery for Language Agents through Exploration and Iterative Feedback** [[📝 Paper](https://arxiv.org/abs/2506.04287)]  
  → This framework discovers agent skills through environment exploration and iterative feedback, producing reusable experience for subsequent learning.

<!-- paper:e12 -->
- (*2025*) **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[📝 Paper](https://arxiv.org/abs/2504.07079)] [[💻 Code](https://github.com/OSU-NLP-Group/SkillWeaver)]  
  → SkillWeaver explores websites, synthesizes reusable APIs, and improves them through execution-based practice.

<!-- paper:e14 -->
- (*2026*) **OSExpert: Computer-Use Agents Learning Professional Skills via Exploration** [[📝 Paper](https://arxiv.org/abs/2603.07978)] [[💻 Code](https://github.com/Lumos-Jiateng/OSExpert)]  
  → OSExpert discovers elementary software functions through exploration and composes them into higher-level computer-use skills.

<!-- paper:e23 -->
- (*2026*) **ASPIRE: Agentic /Skills Discovery for Robotics** [[📝 Paper](https://arxiv.org/abs/2607.00272)]  
  → ASPIRE constructs and repairs reusable robot skills from multimodal execution traces and failure analysis.

<!-- paper:c11 -->
- (*2026*) **OpenSkill: Open-World Self-Evolution for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.06741)] [[💻 Code](https://github.com/OpenLAIR/OpenSkill)]  
  → OpenSkill expands an agent's skill repertoire through autonomous exploration and self-evolution in open-world environments.

<!-- paper:f04 -->
- (*2018*) **Diversity is All You Need: Learning Skills without a Reward Function** [[📝 Paper](https://arxiv.org/abs/1802.06070)] [[💻 Code](https://github.com/ben-eysenbach/sac/blob/master/DIAYN.md)]  
  → DIAYN discovers diverse, distinguishable behaviors without task rewards, providing a reusable repertoire for downstream control.

<!-- paper:xzhao2024agentic -->
- (*2025*) **Agentic Skill Discovery** [[📝 Paper](https://arxiv.org/abs/2405.15019)] [[💻 Code](https://github.com/xf-zhao/Agentic-Skill-Discovery)]  
  → Agentic Skill Discovery uses language-model reasoning to propose meaningful robot behaviors and autonomously acquire the corresponding skills.

<!-- paper:xzhou2024proposer -->
- (*2025*) **Proposer-Agent-Evaluator(PAE): Autonomous Skill Discovery For Foundation Model Internet Agents** [[📝 Paper](https://arxiv.org/abs/2412.13194)]  
  → PAE combines a task proposer, acting agent, and evaluator to autonomously discover and learn internet-interaction skills.

<!-- paper:xtziafas2024lifelong -->
- (*2024*) **Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models** [[📝 Paper](https://arxiv.org/abs/2406.18746)] [[🌐 Project](https://gtziafas.github.io/LRLL_project/)]  
  → LRLL autonomously grows a robot's executable skill library through task proposals, interaction, and validation of reusable programs.

<!-- paper:xwu2025ascent -->
- (*2025*) **ASCENT: Autonomous Skill Learning Toward Complex Embodied Tasks With Foundation Models** [[📝 Paper](https://ieeexplore.ieee.org/document/11127927/)]  
  → ASCENT autonomously acquires robot skills through foundation-model-guided interaction and skill composition for complex embodied tasks.

<!-- paper:xyang2025self -->
- (*2026*) **Self-guided hierarchical exploration for generalist foundation model web agents** [[📝 Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2852977ade3d2a70eceb78cdef91f4b3-Abstract-Conference.html)]  
  → This SAGE framework uses hierarchical, self-guided web exploration to generate training tasks and acquire reusable interaction skills.

<!-- paper:xjansonnie2024unsupervised -->
- (*2024*) **Unsupervised Skill Discovery for Robotic Manipulation through Automatic Task Generation** [[📝 Paper](https://arxiv.org/abs/2410.04855)]  
  → This method automatically generates manipulation tasks to discover reusable object-interaction skills without manual task labels.

<!-- paper:xhe2026ee -->
- (*2026*) **EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning** [[📝 Paper](https://arxiv.org/abs/2604.09815)]  
  → EE-MCP generates environments and learns from interaction to discover and evolve GUI-agent skills.

<!-- paper:c31 -->
- (*2026*) **Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills** [[📝 Paper](https://arxiv.org/abs/2607.22529)] [[💻 Code](https://github.com/Qwen-Applications/skill-self-play)]  
  → Skill Self-Play co-evolves tasks and reusable skills to expand the capability frontier of LLM agents.

<!-- paper:c32 -->
- (*2026*) **Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember** [[📝 Paper](https://arxiv.org/abs/2607.29468)] [[💻 Code](https://github.com/Zenghuang-Fu/SESA-Self-Evolving-Search-Agents)]  
  → This self-play framework trains search agents to generate tasks, solve them, and retain reusable skills from the resulting experience.

<!-- paper:e08 -->
- (*2026*) **SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2602.08234)] [[💻 Code](https://github.com/aiming-lab/SkillRL)]  
  → SkillRL distills rollout experience into a hierarchical skill library and recursively evolves the library during reinforcement learning.

<!-- paper:e11 -->
- (*2026*) **Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2605.06130)] [[💻 Code](https://github.com/AlphaLab-USTC/Skill1)]  
  → Skill1 jointly optimizes skill selection, utilization, and experience distillation within a unified reinforcement-learning process.

<!-- paper:c05 -->
- (*2026*) **Reinforcement Learning for Self-Improving Agent with Skill Library** [[📝 Paper](https://arxiv.org/abs/2512.17102)] [[💻 Code](https://github.com/amazon-science/SAGE)]  
  → SAGE trains agents to generate and use a growing skill library across sequential tasks through skill-augmented reinforcement learning.

<!-- paper:c10 -->
- (*2026*) **Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks** [[📝 Paper](https://arxiv.org/abs/2604.20987)] [[💻 Code](https://github.com/wuxiyang1996/COS-PLAY)]  
  → This framework jointly evolves an LLM decision agent and its skill-bank agent to improve coordination on long-horizon tasks.

<!-- paper:c29 -->
- (*2026*) **Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting** [[📝 Paper](https://arxiv.org/abs/2607.26643)] [[💻 Code](https://github.com/HQ-Lin/SkillBoost/tree/main)]  
  → SkillBoost localizes failures, explores repair candidates, and accepts skill updates under regression bounds to reduce overfitting.

<!-- paper:feng2026skillhex -->
- (*2026*) **SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation** [[📝 Paper](https://arxiv.org/abs/2608.05628)]  
  → SkillHEX generates hypotheses about skill failures and tests targeted revisions through autonomous exploration and exploitation.

<!-- paper:xqiu2026unsupervised -->
- (*2026*) **Unsupervised Skill Discovery for Agentic Data Analysis** [[📝 Paper](https://arxiv.org/abs/2606.06416)]  
  → DataCOPE discovers reusable data-analysis skills from autonomous task experience without manually specified skill labels.

<!-- paper:xhuang2025automated -->
- (*2025*) **Automated Hybrid Reward Scheduling via Large Language Models for Robotic Skill Learning** [[📝 Paper](https://arxiv.org/abs/2505.02483)]  
  → Automated Hybrid Reward Scheduling uses language models to adapt reward combinations during robot skill learning.

<!-- paper:c07 -->
- (*2026*) **CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification** [[📝 Paper](https://arxiv.org/abs/2604.01687)] [[💻 Code](https://github.com/Zhang-Henry/CoEvoSkills)]  
  → CoEvoSkills co-evolves skill candidates and their verification procedures to support continued improvement of reusable agent capabilities.

<!-- paper:e20 -->
- (*2025*) **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** [[📝 Paper](https://arxiv.org/abs/2512.23760)]  
  → This framework organizes synthesized experience in an auditable skill graph and uses verifiable rewards and contract checks to govern updates.

<a id="sources-agent-experience-deployment-experience"></a>

#### Deployment Experience

<!-- paper:e02 -->
- (*2026*) **AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** [[📝 Paper](https://arxiv.org/abs/2603.01145)] [[💻 Code](https://github.com/ECNU-ICALK/AutoSkill)]  
  → AutoSkill distills conversational experience into reusable skills and updates them as new interactions accumulate.

<!-- paper:e19 -->
- (*2026*) **Memento-Skills: Let Agents Design Agents** [[📝 Paper](https://arxiv.org/abs/2603.18743)] [[💻 Code](https://github.com/Memento-Teams/Memento-Skills)]  
  → Memento-Skills lets deployed agents create, revise, and expand external skill libraries using execution feedback.

<!-- paper:e18 -->
- (*2026*) **MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild** [[📝 Paper](https://arxiv.org/abs/2603.17187)] [[💻 Code](https://github.com/aiming-lab/MetaClaw)]  
  → MetaClaw converts deployment conversations and failures into skills while updating the agent policy through experience-driven learning.

<!-- paper:e17 -->
- (*2026*) **SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems** [[📝 Paper](https://arxiv.org/abs/2606.01314)]  
  → SkillSmith co-evolves skills and the tools they call through coordinated proposals informed by execution traces and failure patterns.

<!-- paper:c06 -->
- (*2026*) **SkillClaw: Let Skills Evolve Collectively with Agentic Evolver** [[📝 Paper](https://arxiv.org/abs/2604.08377)] [[💻 Code](https://github.com/AMAP-ML/SkillClaw)]  
  → SkillClaw aggregates experience across deployed agents and evolves shared skills through an agentic maintenance process.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:e22 -->
- (*2026*) **Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory** [[📝 Paper](https://arxiv.org/abs/2606.09365)] [[💻 Code](https://github.com/manglu097/SkeMex)]  
  → This medical-agent framework distills clinical task experience into an evolving skill memory for transferable reasoning.

<!-- paper:c08 -->
- (*2026*) **XSkill: Continual Learning from Experience and Skills in Multimodal Agents** [[📝 Paper](https://arxiv.org/abs/2603.12056)] [[💻 Code](https://github.com/XSkill-Agent/XSkill)]  
  → XSkill accumulates multimodal execution experience and reusable skills to support continual adaptation across agent tasks.

<!-- paper:wang2026atlasva -->
- (*2026*) **AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.17933)]  
  → AtlasVA accumulates visual skill memory from teacher-free interaction and retrieves it to guide subsequent visual-agent decisions.

<!-- paper:jiang2026skillsmithlocal -->
- (*2026*) **SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution** [[📝 Paper](https://arxiv.org/abs/2608.08037)]  
  → This SkillSmith framework automatically constructs and evolves textual skills to improve locally deployed agents.

<!-- paper:lu2026skillsentry -->
- (*2026*) **SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance** [[📝 Paper](https://arxiv.org/abs/2608.09253)]  
  → SkillSentry checks skill steps and constraints during execution and returns targeted guidance when runtime behavior deviates from the procedure.

<!-- paper:yang2026gse -->
- (*2026*) **Learning Globally Reusable Skills for Coding Agents** [[📝 Paper](https://arxiv.org/abs/2608.06153)]  
  → GSE clusters local coding-agent improvement proposals into shared skill abstractions and checks them against historical task experience.

<!-- paper:yao2026mera -->
- (*2026*) **MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale** [[📝 Paper](https://arxiv.org/abs/2608.10333)]  
  → MERA distills recurring procedures into a SkillBook and adapts a small model through verified demonstrations, skill-guided training, and cost-aware routing.

<!-- paper:liu2026rethinking -->
- (*2026*) **Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds** [[📝 Paper](https://arxiv.org/abs/2608.02636)] [[💻 Code](https://github.com/HKUST-KnowComp/rethinkskill)]  
  → This study analyzes how feedback quality and repeated revision shape skill improvement and degradation over multiple evolution rounds.

<!-- paper:xwu2025evolver -->
- (*2025*) **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle** [[📝 Paper](https://arxiv.org/abs/2510.16079)] [[💻 Code](https://github.com/KnowledgeXLab/EvolveR)]  
  → EvolveR connects experience collection, procedural abstraction, execution, and revision in an experience-driven agent lifecycle.

<!-- paper:xcheng2026mem2evolve -->
- (*2026*) **Mem²Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation** [[📝 Paper](https://arxiv.org/abs/2604.10923)]  
  → Mem2Evolve co-evolves experience memory and reusable assets so that accumulated lessons guide capability expansion.

<!-- paper:xyang2026federatedskill -->
- (*2026*) **FederatedSkill: Federated Learning for Agentic Skill Evolution** [[📝 Paper](https://arxiv.org/abs/2606.03143)] [[💻 Code](https://github.com/UCSB-NLP-Chang/FederatedSkill)]  
  → FederatedSkill shares and evolves procedural skills across distributed agents while evaluating transfer across deployment sites.

<!-- paper:xwu2026bayesian -->
- (*2026*) **Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses** [[📝 Paper](https://arxiv.org/abs/2606.08348)] [[💻 Code](https://github.com/DataArcTech/Bayesian-Agent)]  
  → Bayesian-Agent uses posterior estimates from execution evidence to guide skill selection and evolution within agent harnesses.

<!-- paper:xpan2026skillmas -->
- (*2026*) **SkillMAS: Skill Co-Evolution with LLM-based Multi-Agent System** [[📝 Paper](https://arxiv.org/abs/2605.09341)]  
  → SkillMAS lets multiple LLM agents share experience and co-evolve reusable skills through collaboration.

<!-- paper:xouyang2026skillos -->
- (*2026*) **SkillOS: Learning Skill Curation for Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2605.06614)]  
  → SkillOS learns to insert, update, and delete library entries according to their effect on future agent performance.

<!-- paper:xwang2026continual -->
- (*2026*) **Continual Quadruped Robots Coordination via Semantic Skill Discovery** [[📝 Paper](https://arxiv.org/abs/2606.08102)]  
  → This framework discovers semantically grounded coordination skills for continual learning by quadruped robots.

<!-- paper:xcheng2026continual -->
- (*2025*) **Continual Robot Learning via Language-Guided Skill Acquisition** [[📝 Paper](https://openreview.net/forum?id=dVMqrppXOR)]  
  → LG-SAIL combines language-guided skill acquisition and continued robot interaction to expand a reusable control repertoire.

<!-- paper:c43 -->
- (*2026*) **SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks** [[📝 Paper](https://arxiv.org/abs/2604.20087)] [[💻 Code](https://github.com/cxcscmu/SkillLearnBench)]  
  → SkillLearnBench evaluates continual skill generation through complementary measures of skill quality, execution trajectories, and task outcomes.

<!-- paper:c44 -->
- (*2026*) **SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents** [[📝 Paper](https://arxiv.org/abs/2604.17308)] [[💻 Code](https://github.com/ZhangZi-a/SkillFlow)]  
  → SkillFlow evaluates lifelong skill discovery and evolution by carrying an agent's revised library across sequences of related tasks.

<!-- paper:c46 -->
- (*2026*) **Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2606.23127)]  
  → AFTER evaluates procedural-memory improvement and transfer across tasks, professional roles, and model backbones.

<!-- paper:c33 -->
- (*2026*) **Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.10990)]  
  → This work models skill drift as contract violations and supports proactive maintenance when dependencies or execution conditions change.

[↑ Contents](#contents)

<a id="synthesis"></a>

## 2. Skill Synthesis Methods

Four construction operations turn source evidence into reusable procedures: procedural distillation, contrastive induction, constructive compilation, and objective optimization.

- **[Procedural Distillation](#synthesis-procedural-distillation)**
- **[Contrastive Induction](#synthesis-contrastive-induction)**
- **[Constructive Compilation](#synthesis-constructive-compilation)**
- **[Objective Optimization](#synthesis-objective-optimization)**

<a id="synthesis-procedural-distillation"></a>

### Procedural Distillation

<!-- paper:e02 -->
- (*2026*) **AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** [[📝 Paper](https://arxiv.org/abs/2603.01145)] [[💻 Code](https://github.com/ECNU-ICALK/AutoSkill)]  
  → AutoSkill distills conversational experience into reusable skills and updates them as new interactions accumulate.

<!-- paper:c01 -->
- (*2024*) **ExpeL: LLM Agents Are Experiential Learners** [[📝 Paper](https://arxiv.org/abs/2308.10144)] [[💻 Code](https://github.com/LeapLabTHU/ExpeL)]  
  → ExpeL extracts reusable natural-language insights from successful and failed task experiences and retrieves them to guide subsequent agent decisions.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:e05 -->
- (*2025*) **ALLOY: Generating Reusable Agent Workflows from User Demonstration** [[📝 Paper](https://arxiv.org/abs/2510.10049)]  
  → ALLOY converts user demonstrations into editable workflows that agents can reuse across related web tasks.

<!-- paper:c02 -->
- (*2024*) **Agent Workflow Memory** [[📝 Paper](https://arxiv.org/abs/2409.07429)] [[💻 Code](https://github.com/zorazrw/agent-workflow-memory)]  
  → Agent Workflow Memory induces reusable workflows from interaction histories and retrieves them as procedural guidance for web tasks.

<!-- paper:e13 -->
- (*2025*) **Inducing Programmatic Skills for Agentic Tasks** [[📝 Paper](https://arxiv.org/abs/2504.06821)] [[💻 Code](https://github.com/zorazrw/agent-skill-induction)]  
  → This framework induces executable programmatic skills from agent task experience and verifies them before reuse.

<!-- paper:e16 -->
- (*2026*) **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** [[📝 Paper](https://arxiv.org/abs/2603.25158)] [[💻 Code](https://github.com/Qwen-Applications/Trace2Skill)]  
  → Trace2Skill consolidates lessons from execution trajectories into transferable procedural skills with explicit applicability guidance.

<!-- paper:c15 -->
- (*2026*) **SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2606.26669)]  
  → SkillDisCo distills shared control-flow structures from successful agent traces and compiles them into parameterized, callable procedural skills.

<!-- paper:e03 -->
- (*2026*) **Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction** [[📝 Paper](https://arxiv.org/abs/2603.11808)]  
  → This repository-mining framework extracts reusable procedural knowledge from open-source agentic codebases and assesses candidate skill quality.

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:tong2026code2skill -->
- (*2026*) **Grounded Skill Synthesis from Code at Scale for Agentic Intelligence** [[📝 Paper](https://arxiv.org/abs/2609.05571)] [[💻 Code](https://github.com/ant-intl/Code2Skill)]  
  → Code2Skill extracts reusable procedural skills from source repositories with code-grounded workflow context, applicability boundaries, and source evidence.

<!-- paper:xwu2025evolver -->
- (*2025*) **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle** [[📝 Paper](https://arxiv.org/abs/2510.16079)] [[💻 Code](https://github.com/KnowledgeXLab/EvolveR)]  
  → EvolveR connects experience collection, procedural abstraction, execution, and revision in an experience-driven agent lifecycle.

<!-- paper:xzhou2026wise -->
- (*2026*) **WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents** [[📝 Paper](https://arxiv.org/abs/2601.08158)]  
  → WISE-Flow turns service-agent trajectories into structured workflow experience that supports reusable procedural guidance and self-evolution.

<!-- paper:xwang2026webxskill -->
- (*2026*) **WebXSkill: Skill Learning for Autonomous Web Agents** [[📝 Paper](https://arxiv.org/abs/2604.13318)] [[🌐 Project](https://github.com/aiming-lab/WebXSkill)]  
  → WebXSkill learns reusable web-interaction procedures from experience and combines procedural guidance with executable resources.

<!-- paper:xli2026online -->
- (*2026*) **Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval** [[📝 Paper](https://arxiv.org/abs/2606.04391)] [[💻 Code](https://github.com/plusnli/online-skill-learning)]  
  → This web-agent framework learns skills online and retrieves them using the current environment state to improve applicability.

<!-- paper:xyuan2026clawtrace -->
- (*2026*) **ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation** [[📝 Paper](https://arxiv.org/abs/2604.23853)] [[💻 Code](https://github.com/epsilla-cloud/clawtrace)]  
  → ClawTrace attributes execution costs to skill components and converts traces into preservation, pruning, and repair proposals.

<!-- paper:xliu2026skilllens -->
- (*2026*) **SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation** [[📝 Paper](https://arxiv.org/abs/2608.10775)]  
  → SkillLens constructs visual skill cards for GUI-action retrieval and distills their guidance into an agent policy.

<!-- paper:xli2026codeskill -->
- (*2026*) **CODESKILL: Learning Self-Evolving Skills for Coding Agents** [[📝 Paper](https://arxiv.org/abs/2605.25430)]  
  → CODESKILL trains a management policy to extract multigranularity skills from coding traces and maintain them using quality and execution rewards.

<!-- paper:e21 -->
- (*2026*) **Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery** [[📝 Paper](https://arxiv.org/abs/2603.05860)]  
  → MACRO discovers recurring tool-use patterns in medical-imaging experience and turns them into reusable composite skills.

<!-- paper:e22 -->
- (*2026*) **Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory** [[📝 Paper](https://arxiv.org/abs/2606.09365)] [[💻 Code](https://github.com/manglu097/SkeMex)]  
  → This medical-agent framework distills clinical task experience into an evolving skill memory for transferable reasoning.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:e10 -->
- (*2026*) **SkillX: Automatically Constructing Skill Knowledge Bases for Agents** [[📝 Paper](https://arxiv.org/abs/2604.04804)] [[💻 Code](https://github.com/zjunlp/SkillX)]  
  → SkillX constructs a hierarchical skill knowledge base through multilevel design, iterative refinement, and exploratory expansion.

<!-- paper:f07 -->
- (*2018*) **Learning Libraries of Subroutines for Neurally-Guided Bayesian Program Induction** [[📝 Paper](https://people.csail.mit.edu/asolar/papers/EllisMSST18.pdf)]  
  → This library-learning method discovers reusable subroutines while training a neural guide to search programs expressed in the evolving library.

<!-- paper:f08 -->
- (*2021*) **DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning** [[📝 Paper](https://doi.org/10.1145/3453483.3454080)] [[💻 Code](https://github.com/ellisk42/ec)]  
  → DreamCoder alternates program synthesis and abstraction learning to grow a library of reusable computational concepts.

<!-- paper:f09 -->
- (*2023*) **Top-Down Synthesis for Library Learning** [[📝 Paper](http://dx.doi.org/10.1145/3571234)] [[💻 Code](https://github.com/mlb2251/stitch)]  
  → Top-down library learning discovers reusable program abstractions by searching over candidate library functions and their compressive value.

<!-- paper:f10 -->
- (*2024*) **LILO: Learning Interpretable Libraries by Compressing and Documenting Code** [[📝 Paper](https://arxiv.org/abs/2310.19791)] [[💻 Code](https://github.com/gabegrand/lilo)]  
  → LILO compresses synthesized programs into reusable library functions and documents the abstractions with natural language.

<!-- paper:f11 -->
- (*2024*) **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** [[📝 Paper](https://arxiv.org/abs/2401.16467)] [[💻 Code](https://github.com/esteng/regal_program_learning)]  
  → ReGAL refactors task programs into shared abstractions that can be reused during subsequent program generation.

<!-- paper:f12 -->
- (*2022*) **Leveraging Language to Learn Program Abstractions and Search Heuristics** [[📝 Paper](https://arxiv.org/abs/2106.11053)]  
  → This work uses language to guide the acquisition of program abstractions and search heuristics for reusable computational procedures.

<!-- paper:c55 -->
- (*2026*) **Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories** [[📝 Paper](https://arxiv.org/abs/2607.25560)] [[💻 Code](https://anonymous.4open.science/r/SigLeak-D1DB)]  
  → SigLeak reconstructs proprietary skill procedures from observable execution trajectories, exposing a behavioral channel for skill leakage.

<!-- paper:xdeng2025open -->
- (*2025*) **Open-World Skill Discovery from Unsegmented Demonstrations** [[📝 Paper](https://arxiv.org/abs/2503.10684)] [[💻 Code](https://github.com/CraftJarvis/SkillDiscovery)]  
  → This method detects skill boundaries in unsegmented demonstration videos and learns reusable behaviors from the resulting clips.

<!-- paper:xju2024rethinking -->
- (*2024*) **Rethinking Mutual Information for Language Conditioned Skill Discovery on Imitation Learning** [[📝 Paper](https://arxiv.org/abs/2402.17511)]  
  → LCSD uses mutual-information objectives to learn discrete language-conditioned skills from multitask demonstrations.

<!-- paper:xhe2025goal -->
- (*2025*) **Goal-Oriented Skill Abstraction for Offline Multi-Task Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2507.06628)]  
  → GO-Skill abstracts goal-oriented behaviors from offline multitask experience for reusable downstream control.

<!-- paper:xliu2025learning -->
- (*2025*) **Learning Generalizable Skills from Offline Multi-Task Data for Multi-Agent Cooperation** [[📝 Paper](https://arxiv.org/abs/2503.21200)] [[💻 Code](https://github.com/mooricAnna/HiSSD)]  
  → HiSSD learns shared and task-specific skills from offline multitask data to support generalizable multi-agent cooperation.

<!-- paper:xxiao2026offline -->
- (*2026*) **Offline Multi-agent Continual Cooperation via Skill Partition and Reuse** [[📝 Paper](https://arxiv.org/abs/2606.25389)] [[💻 Code](https://github.com/yuchen2003/comad-icml26)]  
  → COMAD partitions offline multi-agent experience into reusable skills to support continual cooperation across tasks.

<!-- paper:xliu2026procedural -->
- (*2026*) **Procedural Memory Distillation: Online Reflection for Self-Improving Language Models** [[📝 Paper](https://arxiv.org/abs/2607.01480)]  
  → Procedural Memory Distillation uses online reflection to convert execution experience into procedural knowledge internalized by a language model.

<!-- paper:xhe2026siri -->
- (*2026*) **SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training** [[📝 Paper](https://arxiv.org/abs/2606.02355)]  
  → SIRI derives intrinsic skills during reinforcement learning and internalizes their guidance in the agent policy.

<!-- paper:xzhang2026spyce -->
- (*2026*) **SPyCE: Skill-Policy Co-evolution for Multimodal Agents** [[📝 Paper](https://arxiv.org/abs/2607.13854)]  
  → SPyCE co-evolves reusable skills and multimodal agent policies using interaction experience.

<!-- paper:xli2026arise -->
- (*2026*) **ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2603.16060)] [[💻 Code](https://github.com/Skylanding/ARISE)]  
  → ARISE co-evolves intrinsic skills and agent reasoning through a hierarchical reinforcement-learning framework.

<a id="synthesis-contrastive-induction"></a>

### Contrastive Induction

<!-- paper:f14 -->
- (*2023*) **Reflexion: Language Agents with Verbal Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2303.11366)] [[💻 Code](https://github.com/noahshinn/reflexion)]  
  → Reflexion converts execution feedback into verbal reflections that guide later attempts, providing a foundation for experience-based procedural improvement.

<!-- paper:f15 -->
- (*2023*) **Self-Refine: Iterative Refinement with Self-Feedback** [[📝 Paper](https://arxiv.org/abs/2303.17651)] [[💻 Code](https://github.com/madaan/self-refine)]  
  → Self-Refine iteratively critiques and revises model outputs, supplying a reusable refinement pattern for skill-generation pipelines.

<!-- paper:f16 -->
- (*2024*) **CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing** [[📝 Paper](https://arxiv.org/abs/2305.11738)] [[💻 Code](https://github.com/microsoft/ProphetNet/tree/master/CRITIC)]  
  → CRITIC uses external tools to verify and critique generated outputs, grounding iterative procedural correction in execution evidence.

<!-- paper:wang2026reflex -->
- (*2026*) **REFLEX: Reflective Evolution from LLM Experience** [[📝 Paper](https://arxiv.org/abs/2606.16496)] [[💻 Code](https://github.com/wangpan-ustc/REFLEX)]  
  → REFLEX derives procedural improvements from reflective analysis of LLM execution experience.

<!-- paper:c01 -->
- (*2024*) **ExpeL: LLM Agents Are Experiential Learners** [[📝 Paper](https://arxiv.org/abs/2308.10144)] [[💻 Code](https://github.com/LeapLabTHU/ExpeL)]  
  → ExpeL extracts reusable natural-language insights from successful and failed task experiences and retrieves them to guide subsequent agent decisions.

<!-- paper:e24 -->
- (*2026*) **SkillGen: Verified Inference-Time Agent Skill Synthesis** [[📝 Paper](https://arxiv.org/abs/2605.10999)] [[💻 Code](https://github.com/yccm/SkillGen)]  
  → SkillGen synthesizes skills at inference time through contrastive trajectory analysis, iterative refinement, and paired performance verification.

<!-- paper:c28 -->
- (*2026*) **SKILL-KD: Contrastive Skill Distillation for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.28048)]  
  → SKILL-KD contrasts student failures with teacher trajectories to produce skill patches, then validates and consolidates them through student re-execution.

<!-- paper:xcao2025remember -->
- (*2026*) **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** [[📝 Paper](https://arxiv.org/abs/2512.10696)] [[💻 Code](https://github.com/agentscope-ai/ReMe)]  
  → ReMe extracts, retrieves, and refines procedural memories from agent experience to support adaptation across tasks.

<!-- paper:xforouzandeh2025learning -->
- (*2025*) **Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement** [[📝 Paper](https://arxiv.org/abs/2512.18950)] [[💻 Code](https://github.com/S-Forouzandeh/MACLA-LLM-Agents-AAMAS-2026-Conference)]  
  → MACLA maintains hierarchical procedural memories using Bayesian selection and contrastive refinement from task experience.

<!-- paper:xju2026embodiskill -->
- (*2026*) **EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents** [[📝 Paper](https://arxiv.org/abs/2605.10332)] [[💻 Code](https://github.com/air-embodied-brain/EmbodiSkill)]  
  → EmbodiSkill reflects on embodied task execution with explicit skill awareness to improve subsequent skill construction and use.

<!-- paper:xqiu2026unsupervised -->
- (*2026*) **Unsupervised Skill Discovery for Agentic Data Analysis** [[📝 Paper](https://arxiv.org/abs/2606.06416)]  
  → DataCOPE discovers reusable data-analysis skills from autonomous task experience without manually specified skill labels.

<!-- paper:e09 -->
- (*2025*) **Automated Skill Discovery for Language Agents through Exploration and Iterative Feedback** [[📝 Paper](https://arxiv.org/abs/2506.04287)]  
  → This framework discovers agent skills through environment exploration and iterative feedback, producing reusable experience for subsequent learning.

<!-- paper:e15 -->
- (*2026*) **EvoSkill: Automated Skill Discovery for Multi-Agent Systems** [[📝 Paper](https://arxiv.org/abs/2603.02766)] [[💻 Code](https://github.com/sentient-agi/EvoSkill)]  
  → EvoSkill analyzes execution failures and iteratively proposes reusable skills for multi-agent task solving.

<!-- paper:e18 -->
- (*2026*) **MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild** [[📝 Paper](https://arxiv.org/abs/2603.17187)] [[💻 Code](https://github.com/aiming-lab/MetaClaw)]  
  → MetaClaw converts deployment conversations and failures into skills while updating the agent policy through experience-driven learning.

<!-- paper:c26 -->
- (*2026*) **SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision** [[📝 Paper](https://arxiv.org/abs/2606.01139)] [[💻 Code](https://github.com/HKUST-KnowComp/skillrevise)]  
  → SkillRevise uses execution traces to locate and revise weaknesses in LLM-authored skill instructions.

<!-- paper:feng2026skillhex -->
- (*2026*) **SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation** [[📝 Paper](https://arxiv.org/abs/2608.05628)]  
  → SkillHEX generates hypotheses about skill failures and tests targeted revisions through autonomous exploration and exploitation.

<!-- paper:liu2026rethinking -->
- (*2026*) **Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds** [[📝 Paper](https://arxiv.org/abs/2608.02636)] [[💻 Code](https://github.com/HKUST-KnowComp/rethinkskill)]  
  → This study analyzes how feedback quality and repeated revision shape skill improvement and degradation over multiple evolution rounds.

<!-- paper:xmoll2026grasp -->
- (*2026*) **GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.29668)] [[💻 Code](https://github.com/jomoll/GRASP)]  
  → GRASP proposes skill revisions and gates acceptance with regression checks on previously successful and failed cases.

<!-- paper:c07 -->
- (*2026*) **CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification** [[📝 Paper](https://arxiv.org/abs/2604.01687)] [[💻 Code](https://github.com/Zhang-Henry/CoEvoSkills)]  
  → CoEvoSkills co-evolves skill candidates and their verification procedures to support continued improvement of reusable agent capabilities.

<!-- paper:f24 -->
- (*2026*) **GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2507.19457)] [[💻 Code](https://github.com/gepa-ai/gepa)]  
  → GEPA uses execution traces and reflective feedback to evolve reusable prompts and program components.

<!-- paper:e25 -->
- (*2026*) **Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.16986)]  
  → SkillTTA synthesizes temporary skills from retrieved trajectories and optimizes the prompt that generates them for test-time adaptation.

<a id="synthesis-constructive-compilation"></a>

### Constructive Compilation

<!-- paper:e01 -->
- (*2023*) **Voyager: An Open-Ended Embodied Agent with Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.16291)] [[💻 Code](https://github.com/MineDojo/Voyager)] [[🌐 Project](https://voyager.minedojo.org/)]  
  → Voyager learns executable skills through Minecraft exploration, execution feedback, and iterative code refinement, then reuses them from a growing library.

<!-- paper:e07 -->
- (*2026*) **Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs** [[📝 Paper](https://arxiv.org/abs/2504.20406)]  
  → This approach discovers and verifies reusable software-scripting skills through offline simulations of API interactions.

<!-- paper:e12 -->
- (*2025*) **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[📝 Paper](https://arxiv.org/abs/2504.07079)] [[💻 Code](https://github.com/OSU-NLP-Group/SkillWeaver)]  
  → SkillWeaver explores websites, synthesizes reusable APIs, and improves them through execution-based practice.

<!-- paper:e14 -->
- (*2026*) **OSExpert: Computer-Use Agents Learning Professional Skills via Exploration** [[📝 Paper](https://arxiv.org/abs/2603.07978)] [[💻 Code](https://github.com/Lumos-Jiateng/OSExpert)]  
  → OSExpert discovers elementary software functions through exploration and composes them into higher-level computer-use skills.

<!-- paper:e23 -->
- (*2026*) **ASPIRE: Agentic /Skills Discovery for Robotics** [[📝 Paper](https://arxiv.org/abs/2607.00272)]  
  → ASPIRE constructs and repairs reusable robot skills from multimodal execution traces and failure analysis.

<!-- paper:xcheng2026continual -->
- (*2025*) **Continual Robot Learning via Language-Guided Skill Acquisition** [[📝 Paper](https://openreview.net/forum?id=dVMqrppXOR)]  
  → LG-SAIL combines language-guided skill acquisition and continued robot interaction to expand a reusable control repertoire.

<!-- paper:e06 -->
- (*2025*) **LLM Agents Making Agent Tools** [[📝 Paper](https://arxiv.org/abs/2502.11705)] [[💻 Code](https://github.com/KatherLab/ToolMaker)]  
  → ToolMaker converts scientific papers and their code into reusable tools that LLM agents can invoke.

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:c14 -->
- (*2026*) **Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents** [[📝 Paper](https://arxiv.org/abs/2606.09316)]  
  → Anything2Skill extracts evidence-grounded procedures from external knowledge and compiles them into structured contracts maintained in a persistent SkillBank.

<!-- paper:e17 -->
- (*2026*) **SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems** [[📝 Paper](https://arxiv.org/abs/2606.01314)]  
  → SkillSmith co-evolves skills and the tools they call through coordinated proposals informed by execution traces and failure patterns.

<!-- paper:e19 -->
- (*2026*) **Memento-Skills: Let Agents Design Agents** [[📝 Paper](https://arxiv.org/abs/2603.18743)] [[💻 Code](https://github.com/Memento-Teams/Memento-Skills)]  
  → Memento-Skills lets deployed agents create, revise, and expand external skill libraries using execution feedback.

<!-- paper:jiang2026skillsmithlocal -->
- (*2026*) **SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution** [[📝 Paper](https://arxiv.org/abs/2608.08037)]  
  → This SkillSmith framework automatically constructs and evolves textual skills to improve locally deployed agents.

<!-- paper:xyang2026evods -->
- (*2026*) **EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management** [[📝 Paper](https://arxiv.org/abs/2606.03841)] [[💻 Code](https://github.com/usail-hkust/EvoDS)]  
  → EvoDS learns reusable data-science skills and manages task context to improve autonomous analysis through experience.

<!-- paper:xchen2026few -->
- (*2026*) **A Few Words Go a Long Way: Language Guided Robot Policy Synthesis** [[📝 Paper](https://arxiv.org/abs/2607.23784)]  
  → This approach synthesizes robot policy programs from language guidance, turning human instructions into executable control procedures.

<!-- paper:xxiao2026s -->
- (*2026*) **S³: Improving Agent Safety through Multi-Stage Defense** [[📝 Paper](https://arxiv.org/abs/2608.02683)]  
  → S3 converts safety designs into reusable stage-specific skills and orchestrates them to detect and mitigate risks throughout agent workflows.

<!-- paper:xsha2026skillcenter -->
- (*2026*) **SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents** [[📝 Paper](https://arxiv.org/abs/2607.07676)] [[💻 Code](https://github.com/LabRAI/SkillCenter)]  
  → SkillCenter builds a large source-grounded library by extracting and organizing reusable procedures from external resources.

<!-- paper:xgaurav2025codemem -->
- (*2025*) **CodeMem: Architecting Reproducible Agents via Dynamic MCP and Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2512.15813)]  
  → CodeMem stores reusable executable procedures behind dynamic MCP interfaces to support reproducible agent execution.

<!-- paper:xlou2026lego -->
- (*2026*) **LEGO: An LLM Skill-Based Front-End Design Generation Platform** [[📝 Paper](https://arxiv.org/abs/2604.23355)] [[🌐 Project](https://github.com/loujc/LEGO-An-LLM-Skill-Based-Front-End-Design-Generation-Platform)]  
  → LEGO packages frontend implementation knowledge as reusable skills that guide LLM-based interface generation.

<!-- paper:xcao2026guideskill -->
- (*2026*) **GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning** [[📝 Paper](https://arxiv.org/abs/2607.26160)]  
  → GuideSkill converts clinical guidelines into executable skills and evolves them using execution feedback for grounded clinical reasoning.

<!-- paper:xche2026mmg2skill -->
- (*2026*) **MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?** [[📝 Paper](https://arxiv.org/abs/2606.01993)] [[💻 Code](https://github.com/NJU-LINK/MMG2Skill)]  
  → MMG2Skill distills real-world multimodal guides into reusable skills and improves them through subsequent agent interaction.

<!-- paper:xblumenfeld2026aip -->
- (*2026*) **AIP: A Graph Representation for Learning and Governing Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.04781)] [[💻 Code](https://github.com/zach-blumenfeld/aip-skillbench)]  
  → AIP represents skills as typed execution graphs with procedural descriptions and executable nodes for learning and governance.

<!-- paper:xlin2026muse -->
- (*2026*) **MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2605.27366)]  
  → MUSE-Autoskill connects skill creation, memory, management, and evaluation in a continuous agent self-evolution process.

<!-- paper:e26 -->
- (*2026*) **From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills** [[📝 Paper](https://arxiv.org/abs/2604.24026)] [[💻 Code](https://github.com/COOLPKU/SSL)]  
  → This work represents skill procedures through scheduling, structural, and logical constraints to support reliable composition.

<!-- paper:e27 -->
- (*2026*) **SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses** [[📝 Paper](https://arxiv.org/abs/2604.03088)]  
  → SkVM compiles skill procedures into a language-virtual-machine representation for execution across models and agent harnesses.

<!-- paper:e28 -->
- (*2026*) **SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces** [[📝 Paper](https://arxiv.org/abs/2605.15215)] [[💻 Code](https://github.com/AetherHeart-AI/Aeloon)]  
  → Boundary-guided SkillSmith compiles skill packages into minimal runtime interfaces that expose the operations needed for execution.

<!-- paper:e30 -->
- (*2026*) **SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.03353)] [[💻 Code](https://github.com/Nexa-Language/Skill-Compiler)]  
  → SkCC uses a typed intermediate representation to compile portable skill artifacts and check cross-framework execution constraints.

<!-- paper:c17 -->
- (*2026*) **SIGIL: Skill Compilation for Reliable and Efficient Agent Execution** [[📝 Paper](https://arxiv.org/abs/2607.27309)]  
  → SIGIL translates authored skills into a validated typed intermediate representation and generates executable harnesses that enforce prescribed procedures.

<!-- paper:c24 -->
- (*2026*) **SkillDroid: Compile Once, Reuse Forever** [[📝 Paper](https://arxiv.org/abs/2604.14872)]  
  → SkillDroid compiles successful mobile interaction trajectories into parameterized templates that can be replayed and recompiled after execution failures.

<!-- paper:c18 -->
- (*2026*) **Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.19604)] [[💻 Code](https://github.com/PKU-LLM-DS-LAB/FairyClaw)]  
  → Formal Skill combines typed metadata, executable state machines, and runtime hooks to make reusable agent procedures observable and enforceable.

<!-- paper:c15 -->
- (*2026*) **SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2606.26669)]  
  → SkillDisCo distills shared control-flow structures from successful agent traces and compiles them into parameterized, callable procedural skills.

<!-- paper:c16 -->
- (*2026*) **Harnessing LLM Agents with Skill Programs** [[📝 Paper](https://arxiv.org/abs/2605.17734)] [[💻 Code](https://github.com/HolaYan/ExecutableSkills-HASP)]  
  → HASP represents reusable skills as executable program functions that intervene in agent loops by modifying actions or supplying corrective context.

<!-- paper:f25 -->
- (*2024*) **DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines** [[📝 Paper](https://arxiv.org/abs/2310.03714)] [[💻 Code](https://github.com/stanfordnlp/dspy)]  
  → DSPy compiles declarative language-model programs by optimizing instructions and demonstrations for their constituent modules.

<!-- paper:f28 -->
- (*2025*) **AFlow: Automating Agentic Workflow Generation** [[📝 Paper](https://arxiv.org/abs/2410.10762)] [[💻 Code](https://github.com/FoundationAgents/AFlow)]  
  → AFlow searches over executable agent workflows and uses evaluation feedback to improve their reusable control structure.

<!-- paper:f29 -->
- (*2025*) **Automated Design of Agentic Systems** [[📝 Paper](https://arxiv.org/abs/2408.08435)] [[💻 Code](https://github.com/ShengranHu/ADAS)]  
  → Automated Design of Agentic Systems searches an archive of agent programs to construct and evaluate new task-solving procedures.

<!-- paper:f19 -->
- (*2022*) **Large Language Models Are Human-Level Prompt Engineers** [[📝 Paper](https://arxiv.org/abs/2211.01910)] [[💻 Code](https://github.com/keirp/automatic_prompt_engineer)]  
  → Automatic Prompt Engineer generates and scores candidate instructions to discover reusable prompts for specified tasks.

<!-- paper:f33 -->
- (*2024*) **Large Language Models as Tool Makers** [[📝 Paper](https://arxiv.org/abs/2305.17126)] [[💻 Code](https://github.com/ctlllll/LLM-ToolMaker)]  
  → This framework lets a language model create reusable tools that other model instances invoke during downstream task solving.

<!-- paper:f34 -->
- (*2023*) **CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.14318)] [[💻 Code](https://github.com/qiancheng0/CREATOR)]  
  → CREATOR separates abstract reasoning from executable tool creation and reuses generated tools to solve related problems.

<a id="synthesis-objective-optimization"></a>

### Objective Optimization

<!-- paper:c25 -->
- (*2026*) **SkillOpt: Executive Strategy for Self-Evolving Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.23904)] [[💻 Code](https://github.com/microsoft/SkillOpt)] [[🌐 Project](https://microsoft.github.io/SkillOpt/)]  
  → SkillOpt optimizes external skill documents through bounded edits generated from scored rollouts and selected using held-out validation.

<!-- paper:c27 -->
- (*2026*) **Self-Supervised Skill Optimization** [[📝 Paper](https://arxiv.org/abs/2607.28777)]  
  → Self-Supervised Skill Optimization uses unlabeled executions and comparative skill probes to improve reusable procedural guidance without task labels or rewards.

<!-- paper:c29 -->
- (*2026*) **Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting** [[📝 Paper](https://arxiv.org/abs/2607.26643)] [[💻 Code](https://github.com/HQ-Lin/SkillBoost/tree/main)]  
  → SkillBoost localizes failures, explores repair candidates, and accepts skill updates under regression bounds to reduce overfitting.

<!-- paper:c30 -->
- (*2026*) **Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills** [[📝 Paper](https://arxiv.org/abs/2607.20999)] [[💻 Code](https://github.com/xiaolin9595/workflow-localized-mechanism-learning)]  
  → Workflow-localized mechanism learning attributes failures to specific workflow components and repairs structured skills using reusable mechanism knowledge.

<!-- paper:shen2026skillalpha -->
- (*2026*) **Progressive Agent Skill Generation via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2608.01678)] [[💻 Code](https://github.com/ejhshen/skill-alpha)]  
  → SkillAlpha progressively generates reusable agent skills through reinforcement learning and task feedback.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:xvishe2026skill -->
- (*2026*) **Skill-R1: Agent Skill Evolution via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2605.09359)]  
  → Skill-R1 uses reinforcement learning to evolve reusable agent skills from task outcomes.

<!-- paper:e25 -->
- (*2026*) **Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.16986)]  
  → SkillTTA synthesizes temporary skills from retrieved trajectories and optimizes the prompt that generates them for test-time adaptation.

<!-- paper:f18 -->
- (*2022*) **RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2205.12548)] [[💻 Code](https://github.com/mingkaid/rl-prompt)]  
  → RLPrompt learns discrete prompts through reinforcement learning, providing a foundation for optimizing reusable instruction artifacts.

<!-- paper:f20 -->
- (*2023*) **Automatic Prompt Optimization with "Gradient Descent" and Beam Search** [[📝 Paper](https://arxiv.org/abs/2305.03495)] [[💻 Code](https://github.com/microsoft/LMOps/tree/main/prompt_optimization)]  
  → This prompt optimizer uses natural-language error feedback as textual gradients and beam search to improve reusable instructions.

<!-- paper:f21 -->
- (*2024*) **Large Language Models as Optimizers** [[📝 Paper](https://arxiv.org/abs/2309.03409)] [[💻 Code](https://github.com/google-deepmind/opro)]  
  → OPRO uses language models to propose and evaluate candidate solutions, including reusable task instructions, within an iterative optimization loop.

<!-- paper:f22 -->
- (*2023*) **Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution** [[📝 Paper](https://arxiv.org/abs/2309.16797)]  
  → Promptbreeder evolves task prompts and the prompts that mutate them to improve reusable instructions through self-referential search.

<!-- paper:f23 -->
- (*2023*) **EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers** [[📝 Paper](https://arxiv.org/abs/2309.08532)] [[💻 Code](https://github.com/beeevita/EvoPrompt)]  
  → EvoPrompt combines language models with evolutionary search to optimize discrete prompts for downstream tasks.

<!-- paper:f26 -->
- (*2024*) **Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** [[📝 Paper](https://arxiv.org/abs/2406.11695)]  
  → MIPRO optimizes instructions and demonstrations jointly across multistage language-model programs to improve reusable workflow components.

<!-- paper:f27 -->
- (*2024*) **Language Agents as Optimizable Graphs** [[📝 Paper](https://arxiv.org/abs/2402.16823)] [[💻 Code](https://github.com/metauto-ai/gptswarm)]  
  → GPTSwarm represents agent systems as graphs whose prompts and connections can be optimized for task execution.

<!-- paper:f28 -->
- (*2025*) **AFlow: Automating Agentic Workflow Generation** [[📝 Paper](https://arxiv.org/abs/2410.10762)] [[💻 Code](https://github.com/FoundationAgents/AFlow)]  
  → AFlow searches over executable agent workflows and uses evaluation feedback to improve their reusable control structure.

<!-- paper:f29 -->
- (*2025*) **Automated Design of Agentic Systems** [[📝 Paper](https://arxiv.org/abs/2408.08435)] [[💻 Code](https://github.com/ShengranHu/ADAS)]  
  → Automated Design of Agentic Systems searches an archive of agent programs to construct and evaluate new task-solving procedures.

<!-- paper:f30 -->
- (*2025*) **AgentSquare: Automatic LLM Agent Search in Modular Design Space** [[📝 Paper](https://arxiv.org/abs/2410.06153)] [[💻 Code](https://github.com/tsinghua-fib-lab/AgentSquare)]  
  → AgentSquare searches a modular agent-design space and recombines components into reusable agent architectures.

<!-- paper:e08 -->
- (*2026*) **SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2602.08234)] [[💻 Code](https://github.com/aiming-lab/SkillRL)]  
  → SkillRL distills rollout experience into a hierarchical skill library and recursively evolves the library during reinforcement learning.

<!-- paper:e11 -->
- (*2026*) **Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2605.06130)] [[💻 Code](https://github.com/AlphaLab-USTC/Skill1)]  
  → Skill1 jointly optimizes skill selection, utilization, and experience distillation within a unified reinforcement-learning process.

<!-- paper:e20 -->
- (*2025*) **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** [[📝 Paper](https://arxiv.org/abs/2512.23760)]  
  → This framework organizes synthesized experience in an auditable skill graph and uses verifiable rewards and contract checks to govern updates.

<!-- paper:c05 -->
- (*2026*) **Reinforcement Learning for Self-Improving Agent with Skill Library** [[📝 Paper](https://arxiv.org/abs/2512.17102)] [[💻 Code](https://github.com/amazon-science/SAGE)]  
  → SAGE trains agents to generate and use a growing skill library across sequential tasks through skill-augmented reinforcement learning.

<!-- paper:c09 -->
- (*2026*) **Dynamic Dual-Granularity Skill Bank for Agentic RL** [[📝 Paper](https://arxiv.org/abs/2603.28716)] [[💻 Code](https://github.com/TU2021/D2Skill-AgenticRL)]  
  → D2Skill maintains a dual-granularity skill bank and uses utility signals to select, update, and prune skills during agentic reinforcement learning.

<!-- paper:c10 -->
- (*2026*) **Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks** [[📝 Paper](https://arxiv.org/abs/2604.20987)] [[💻 Code](https://github.com/wuxiyang1996/COS-PLAY)]  
  → This framework jointly evolves an LLM decision agent and its skill-bank agent to improve coordination on long-horizon tasks.

<!-- paper:xyue2025real -->
- (*2025*) **Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition** [[📝 Paper](https://arxiv.org/abs/2505.11175)]  
  → VERGSA verifies embodied reasoning and generates dense reward signals to guide the acquisition of reusable control skills.

<!-- paper:f03 -->
- (*2016*) **The Option-Critic Architecture** [[📝 Paper](https://arxiv.org/abs/1609.05140)] [[💻 Code](https://github.com/jeanharb/option_critic)]  
  → Option-Critic jointly learns option policies and termination conditions to acquire temporally extended skills from reward feedback.

<!-- paper:f04 -->
- (*2018*) **Diversity is All You Need: Learning Skills without a Reward Function** [[📝 Paper](https://arxiv.org/abs/1802.06070)] [[💻 Code](https://github.com/ben-eysenbach/sac/blob/master/DIAYN.md)]  
  → DIAYN discovers diverse, distinguishable behaviors without task rewards, providing a reusable repertoire for downstream control.

<!-- paper:xkuroki2024agent -->
- (*2025*) **Agent Skill Acquisition for Large Language Models via CycleQD** [[📝 Paper](https://arxiv.org/abs/2410.14735)]  
  → CycleQD uses quality-diversity search and model merging to acquire and combine agent capabilities across tasks.

<!-- paper:xliu2025skill -->
- (*2025*) **Skill Expansion and Composition in Parameter Space** [[📝 Paper](https://arxiv.org/abs/2502.05932)] [[💻 Code](https://github.com/ltlhuuu/PSEC)]  
  → PSEC expands a library of compact skill modules and composes them in parameter space to address new control tasks.

<!-- paper:yao2026mera -->
- (*2026*) **MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale** [[📝 Paper](https://arxiv.org/abs/2608.10333)]  
  → MERA distills recurring procedures into a SkillBook and adapts a small model through verified demonstrations, skill-guided training, and cost-aware routing.

<!-- paper:xzhang2026skillflow -->
- (*2026*) **SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration** [[📝 Paper](https://arxiv.org/abs/2605.14089)] [[💻 Code](https://anonymous.4open.science/r/SkillFlow-E850)]  
  → This SkillFlow framework recursively evolves skills through flow-based agent orchestration and execution feedback.

<!-- paper:xouyang2026skillos -->
- (*2026*) **SkillOS: Learning Skill Curation for Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2605.06614)]  
  → SkillOS learns to insert, update, and delete library entries according to their effect on future agent performance.

<!-- paper:xxiao2026socratic -->
- (*2026*) **Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.07412)]  
  → Socratic-SWE distills coding traces into reusable agent skills and iteratively improves them through task feedback.

<!-- paper:c31 -->
- (*2026*) **Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills** [[📝 Paper](https://arxiv.org/abs/2607.22529)] [[💻 Code](https://github.com/Qwen-Applications/skill-self-play)]  
  → Skill Self-Play co-evolves tasks and reusable skills to expand the capability frontier of LLM agents.

<!-- paper:c32 -->
- (*2026*) **Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember** [[📝 Paper](https://arxiv.org/abs/2607.29468)] [[💻 Code](https://github.com/Zenghuang-Fu/SESA-Self-Evolving-Search-Agents)]  
  → This self-play framework trains search agents to generate tasks, solve them, and retain reusable skills from the resulting experience.

<!-- paper:xfu2026davinci -->
- (*2026*) **daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization** [[📝 Paper](https://arxiv.org/abs/2606.16497)] [[💻 Code](https://github.com/GAIR-NLP/daVinci-kernel)]  
  → DaVinci-kernel jointly evolves skill selection, summarization, and use through reinforcement learning for GPU kernel optimization.

[↑ Contents](#contents)

<a id="representations"></a>

## 3. Skill Representations

Retained procedures take textual, structured, executable, internalized, or hybrid forms.

- **[Textual Skills](#representations-textual-skills)**
- **[Structured Skills](#representations-structured-skills)**
  - [Sequential Workflows](#representations-structured-skills-sequential-workflows)
  - [Graph-Based Representations](#representations-structured-skills-graph-based-representations)
  - [Typed Specifications and Intermediate Representations](#representations-structured-skills-typed-specifications-and-intermediate-representations)
- **[Executable Skills](#representations-executable-skills)**
  - [Functions, Scripts, and Executable Modules](#representations-executable-skills-functions-scripts-and-executable-modules)
  - [Compiled Runtime Interfaces and Harnesses](#representations-executable-skills-compiled-runtime-interfaces-and-harnesses)
- **[Internalized Skills](#representations-internalized-skills)**
  - [Adapter- and LoRA-based Skills](#representations-internalized-skills-adapter-and-lora-based-skills)
  - [Learned Policies and Controllers](#representations-internalized-skills-learned-policies-and-controllers)
- **[Hybrid Skills](#representations-hybrid-skills)**

<a id="representations-textual-skills"></a>

### Textual Skills

<!-- paper:c01 -->
- (*2024*) **ExpeL: LLM Agents Are Experiential Learners** [[📝 Paper](https://arxiv.org/abs/2308.10144)] [[💻 Code](https://github.com/LeapLabTHU/ExpeL)]  
  → ExpeL extracts reusable natural-language insights from successful and failed task experiences and retrieves them to guide subsequent agent decisions.

<!-- paper:e02 -->
- (*2026*) **AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** [[📝 Paper](https://arxiv.org/abs/2603.01145)] [[💻 Code](https://github.com/ECNU-ICALK/AutoSkill)]  
  → AutoSkill distills conversational experience into reusable skills and updates them as new interactions accumulate.

<!-- paper:e16 -->
- (*2026*) **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** [[📝 Paper](https://arxiv.org/abs/2603.25158)] [[💻 Code](https://github.com/Qwen-Applications/Trace2Skill)]  
  → Trace2Skill consolidates lessons from execution trajectories into transferable procedural skills with explicit applicability guidance.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:c52 -->
- (*2024*) **SkillAct: Using Skill Abstractions Improves LLM Agents** [[📝 Paper](https://openreview.net/forum?id=6LG3cIRrF4)]  
  → SkillAct uses reusable skill abstractions to supply procedural guidance for LLM-agent task execution.

<!-- paper:e24 -->
- (*2026*) **SkillGen: Verified Inference-Time Agent Skill Synthesis** [[📝 Paper](https://arxiv.org/abs/2605.10999)] [[💻 Code](https://github.com/yccm/SkillGen)]  
  → SkillGen synthesizes skills at inference time through contrastive trajectory analysis, iterative refinement, and paired performance verification.

<!-- paper:shen2026skillalpha -->
- (*2026*) **Progressive Agent Skill Generation via Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2608.01678)] [[💻 Code](https://github.com/ejhshen/skill-alpha)]  
  → SkillAlpha progressively generates reusable agent skills through reinforcement learning and task feedback.

<!-- paper:yao2026mera -->
- (*2026*) **MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale** [[📝 Paper](https://arxiv.org/abs/2608.10333)]  
  → MERA distills recurring procedures into a SkillBook and adapts a small model through verified demonstrations, skill-guided training, and cost-aware routing.

<!-- paper:c26 -->
- (*2026*) **SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision** [[📝 Paper](https://arxiv.org/abs/2606.01139)] [[💻 Code](https://github.com/HKUST-KnowComp/skillrevise)]  
  → SkillRevise uses execution traces to locate and revise weaknesses in LLM-authored skill instructions.

<!-- paper:c28 -->
- (*2026*) **SKILL-KD: Contrastive Skill Distillation for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.28048)]  
  → SKILL-KD contrasts student failures with teacher trajectories to produce skill patches, then validates and consolidates them through student re-execution.

<!-- paper:xyu2026skill -->
- (*2026*) **Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.30723)] [[💻 Code](https://github.com/jianxiangyu/MASA_)]  
  → Model-aware skill alignment adapts reusable instructions to the capabilities and execution behavior of different language-model backbones.

<!-- paper:xnguyen2026recursive -->
- (*2026*) **Recursive Self-Evolving Agents via Held-Out Selection** [[📝 Paper](https://arxiv.org/abs/2606.28374)]  
  → This framework uses held-out evaluation to select recursive skill updates and measure their transfer beyond the experience used for revision.

<!-- paper:c46 -->
- (*2026*) **Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2606.23127)]  
  → AFTER evaluates procedural-memory improvement and transfer across tasks, professional roles, and model backbones.

<!-- paper:f17 -->
- (*2020*) **AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts** [[📝 Paper](https://arxiv.org/abs/2010.15980)] [[💻 Code](https://github.com/ucinlp/autoprompt)]  
  → AutoPrompt searches for discrete prompt tokens that elicit desired model behavior, illustrating an optimization approach to retained textual guidance.

<!-- paper:f18 -->
- (*2022*) **RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2205.12548)] [[💻 Code](https://github.com/mingkaid/rl-prompt)]  
  → RLPrompt learns discrete prompts through reinforcement learning, providing a foundation for optimizing reusable instruction artifacts.

<!-- paper:f19 -->
- (*2022*) **Large Language Models Are Human-Level Prompt Engineers** [[📝 Paper](https://arxiv.org/abs/2211.01910)] [[💻 Code](https://github.com/keirp/automatic_prompt_engineer)]  
  → Automatic Prompt Engineer generates and scores candidate instructions to discover reusable prompts for specified tasks.

<!-- paper:f20 -->
- (*2023*) **Automatic Prompt Optimization with "Gradient Descent" and Beam Search** [[📝 Paper](https://arxiv.org/abs/2305.03495)] [[💻 Code](https://github.com/microsoft/LMOps/tree/main/prompt_optimization)]  
  → This prompt optimizer uses natural-language error feedback as textual gradients and beam search to improve reusable instructions.

<!-- paper:f21 -->
- (*2024*) **Large Language Models as Optimizers** [[📝 Paper](https://arxiv.org/abs/2309.03409)] [[💻 Code](https://github.com/google-deepmind/opro)]  
  → OPRO uses language models to propose and evaluate candidate solutions, including reusable task instructions, within an iterative optimization loop.

<!-- paper:f22 -->
- (*2023*) **Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution** [[📝 Paper](https://arxiv.org/abs/2309.16797)]  
  → Promptbreeder evolves task prompts and the prompts that mutate them to improve reusable instructions through self-referential search.

<!-- paper:f23 -->
- (*2023*) **EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers** [[📝 Paper](https://arxiv.org/abs/2309.08532)] [[💻 Code](https://github.com/beeevita/EvoPrompt)]  
  → EvoPrompt combines language models with evolutionary search to optimize discrete prompts for downstream tasks.

<!-- paper:f24 -->
- (*2026*) **GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2507.19457)] [[💻 Code](https://github.com/gepa-ai/gepa)]  
  → GEPA uses execution traces and reflective feedback to evolve reusable prompts and program components.

<!-- paper:c34 -->
- (*2026*) **SkillReducer: Optimizing LLM Agent Skills for Token Efficiency** [[📝 Paper](https://arxiv.org/abs/2603.29919)]  
  → SkillReducer compresses skill instructions to reduce context costs while preserving the information needed to select and execute the procedure.

<!-- paper:jiang2026skillsmithlocal -->
- (*2026*) **SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution** [[📝 Paper](https://arxiv.org/abs/2608.08037)]  
  → This SkillSmith framework automatically constructs and evolves textual skills to improve locally deployed agents.

<!-- paper:xai2026scivisagentskills -->
- (*2026*) **SciVisAgentSkills: Design and Evaluation of Agent Skills for Scientific Data Analysis and Visualization** [[📝 Paper](https://arxiv.org/abs/2606.05525)] [[💻 Code](https://github.com/KuangshiAi/SciVisAgentSkills)]  
  → SciVisAgentSkills designs and evaluates reusable instructions for scientific data analysis and visualization workflows.

<!-- paper:e30 -->
- (*2026*) **SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.03353)] [[💻 Code](https://github.com/Nexa-Language/Skill-Compiler)]  
  → SkCC uses a typed intermediate representation to compile portable skill artifacts and check cross-framework execution constraints.

<!-- paper:xwen2026toward -->
- (*2026*) **Toward User Comprehension Supports for LLM Agent Skill Specifications** [[📝 Paper](https://arxiv.org/abs/2605.19362)] [[💻 Code](https://github.com/zikaiwen/cyber-skill-comprehension)]  
  → This work studies how users understand skill specifications and develops support for inspecting reusable agent procedures.

<!-- paper:e32 -->
- (*2026*) **Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality** [[📝 Paper](https://arxiv.org/abs/2602.08004)]  
  → This empirical study characterizes public Claude skill artifacts, including their structure, redundancy, usage patterns, and security risks.

<!-- paper:c45 -->
- (*2026*) **SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.15557)] [[💻 Code](https://github.com/EverMind-AI/SkillCorpus)]  
  → SkillCorpus consolidates public skill packages and evaluates their organization, quality, and usefulness for real-world agents.

<!-- paper:zhang2026skillreuse -->
- (*2026*) **What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files** [[📝 Paper](https://arxiv.org/abs/2608.08453)]  
  → This empirical study identifies specification, organization, and portability defects that prevent public SKILL.md artifacts from being reused effectively.

<!-- paper:destefanis2026gitskills -->
- (*2026*) **GitSkills: A Dataset of Agent Skills on GitHub** [[📝 Paper](https://arxiv.org/abs/2608.10906)] [[📦 Data](https://huggingface.co/datasets/mvaccargiu/gitskills)]  
  → GitSkills collects public GitHub skill artifacts to support empirical study of skill structure, distribution, and maintenance.

<a id="representations-structured-skills"></a>

### Structured Skills

<a id="representations-structured-skills-sequential-workflows"></a>

#### Sequential Workflows

<!-- paper:e05 -->
- (*2025*) **ALLOY: Generating Reusable Agent Workflows from User Demonstration** [[📝 Paper](https://arxiv.org/abs/2510.10049)]  
  → ALLOY converts user demonstrations into editable workflows that agents can reuse across related web tasks.

<!-- paper:c02 -->
- (*2024*) **Agent Workflow Memory** [[📝 Paper](https://arxiv.org/abs/2409.07429)] [[💻 Code](https://github.com/zorazrw/agent-workflow-memory)]  
  → Agent Workflow Memory induces reusable workflows from interaction histories and retrieves them as procedural guidance for web tasks.

<!-- paper:c30 -->
- (*2026*) **Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills** [[📝 Paper](https://arxiv.org/abs/2607.20999)] [[💻 Code](https://github.com/xiaolin9595/workflow-localized-mechanism-learning)]  
  → Workflow-localized mechanism learning attributes failures to specific workflow components and repairs structured skills using reusable mechanism knowledge.

<!-- paper:xzhou2026wise -->
- (*2026*) **WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents** [[📝 Paper](https://arxiv.org/abs/2601.08158)]  
  → WISE-Flow turns service-agent trajectories into structured workflow experience that supports reusable procedural guidance and self-evolution.

<!-- paper:xhan2025legomem -->
- (*2025*) **LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation** [[📝 Paper](https://arxiv.org/abs/2510.04851)]  
  → LEGOMem decomposes execution experience into modular procedural memories that multi-agent systems reuse for workflow automation.

<!-- paper:f26 -->
- (*2024*) **Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** [[📝 Paper](https://arxiv.org/abs/2406.11695)]  
  → MIPRO optimizes instructions and demonstrations jointly across multistage language-model programs to improve reusable workflow components.

<!-- paper:f28 -->
- (*2025*) **AFlow: Automating Agentic Workflow Generation** [[📝 Paper](https://arxiv.org/abs/2410.10762)] [[💻 Code](https://github.com/FoundationAgents/AFlow)]  
  → AFlow searches over executable agent workflows and uses evaluation feedback to improve their reusable control structure.

<!-- paper:f31 -->
- (*2025*) **WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2411.05451)] [[💻 Code](https://github.com/OpenBMB/WorkflowLLM)]  
  → WorkflowLLM learns to construct structured workflows that coordinate reusable actions and tool interfaces.

<!-- paper:f32 -->
- (*2026*) **Generalizing experience for language agents with hierarchical metaflows** [[📝 Paper](https://papers.nips.cc/paper_files/paper/2025/hash/5c882988ce5fac487974ee4f415b96a9-Abstract-Conference.html)] [[💻 Code](https://github.com/RUCBM/MetaFlowLLM)]  
  → MetaFlows organizes completed task experience in a hierarchy of reusable workflow patterns for generalization across agent tasks.

<a id="representations-structured-skills-graph-based-representations"></a>

#### Graph-Based Representations

<!-- paper:c51 -->
- (*2025*) **SOP-Agent: Empower General Purpose AI Agent with Domain-Specific SOPs** [[📝 Paper](https://arxiv.org/abs/2501.09316)]  
  → SOP-Agent converts domain-specific standard operating procedures into structured guidance for general-purpose agents.

<!-- paper:xblumenfeld2026aip -->
- (*2026*) **AIP: A Graph Representation for Learning and Governing Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.04781)] [[💻 Code](https://github.com/zach-blumenfeld/aip-skillbench)]  
  → AIP represents skills as typed execution graphs with procedural descriptions and executable nodes for learning and governance.

<!-- paper:e04 -->
- (*2026*) **CUA-Skill: Develop Skills for Computer Using Agent** [[📝 Paper](https://arxiv.org/abs/2601.21123)] [[💻 Code](https://github.com/microsoft/cua_skill)] [[🌐 Project](https://microsoft.github.io/cua_skill/)]  
  → CUA-Skill organizes computer-use procedures in a skill library that combines operational guidance with resources for visual interaction.

<!-- paper:e10 -->
- (*2026*) **SkillX: Automatically Constructing Skill Knowledge Bases for Agents** [[📝 Paper](https://arxiv.org/abs/2604.04804)] [[💻 Code](https://github.com/zjunlp/SkillX)]  
  → SkillX constructs a hierarchical skill knowledge base through multilevel design, iterative refinement, and exploratory expansion.

<!-- paper:c20 -->
- (*2026*) **Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills** [[📝 Paper](https://arxiv.org/abs/2604.05333)] [[💻 Code](https://github.com/davidliuk/graph-of-skills)]  
  → Graph-of-Skills retrieves dependency-aware skill bundles from a graph so that selected procedures include the prerequisites needed for execution.

<!-- paper:c21 -->
- (*2026*) **GraSP: Graph-Structured Skill Compositions for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2604.17870)]  
  → GraSP compiles selected skills into typed dependency graphs with node-level verification and local repair for multi-skill execution.

<!-- paper:c22 -->
- (*2026*) **SkillNet: Create, Evaluate, and Connect AI Skills** [[📝 Paper](https://arxiv.org/abs/2603.04448)] [[💻 Code](https://github.com/zjunlp/SkillNet)]  
  → SkillNet organizes reusable skills in a shared ontology with explicit relationships, creation tools, and multidimensional evaluation.

<!-- paper:e20 -->
- (*2025*) **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** [[📝 Paper](https://arxiv.org/abs/2512.23760)]  
  → This framework organizes synthesized experience in an auditable skill graph and uses verifiable rewards and contract checks to govern updates.

<!-- paper:xmeng2026skillrae -->
- (*2026*) **SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution** [[📝 Paper](https://arxiv.org/abs/2605.10114)]  
  → SkillRAE compiles retrieved skill knowledge into structured execution context to support efficient multi-skill use.

<!-- paper:xyao2026skilltrace -->
- (*2026*) **SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents** [[📝 Paper](https://arxiv.org/abs/2608.02356)]  
  → This SkillTrace framework traverses a query-skill graph to retrieve and compose procedures for complex agent requests.

<!-- paper:xli2026skillgraph -->
- (*2026*) **SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs** [[📝 Paper](https://arxiv.org/abs/2605.12039)]  
  → SkillGraph evolves a graph of reusable skills through reinforcement learning, including merging, splitting, and deprecating skill nodes.

<!-- paper:xli2025experience -->
- (*2025*) **Experience-Evolving Multi-Turn Tool-Use Agent with Hybrid Episodic-Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2512.07287)] [[💻 Code](https://github.com/LISijia-dev/H-EPM)]  
  → This agent combines episodic records with reusable procedural knowledge to improve multistep tool use through experience.

<!-- paper:xqi2024semantic -->
- (*2025*) **Semantic-Geometric-Physical-Driven Robot Manipulation Skill Transfer via Skill Library and Tactile Representation** [[📝 Paper](https://arxiv.org/abs/2411.11714)] [[💻 Code](https://github.com/MingchaoQi/skill_transfer)]  
  → This robot framework combines skill libraries, task and scene graphs, and tactile representations to transfer manipulation procedures.

<!-- paper:c48 -->
- (*2026*) **Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale** [[📝 Paper](https://arxiv.org/abs/2603.02176)] [[💻 Code](https://github.com/ynulihao/AgentSkillOS)]  
  → AgentSkillOS organizes skills in a capability tree and retrieves and orchestrates them through dependency-aware task pipelines.

<!-- paper:e29 -->
- (*2026*) **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems** [[📝 Paper](https://arxiv.org/abs/2605.13716)] [[💻 Code](https://github.com/Hik289/SkillOps)]  
  → SkillOps maintains skill libraries using typed contracts, dependency relationships, utility assessment, and lifecycle operations.

<!-- paper:yang2026gse -->
- (*2026*) **Learning Globally Reusable Skills for Coding Agents** [[📝 Paper](https://arxiv.org/abs/2608.06153)]  
  → GSE clusters local coding-agent improvement proposals into shared skill abstractions and checks them against historical task experience.

<a id="representations-structured-skills-typed-specifications-and-intermediate-representations"></a>

#### Typed Specifications and Intermediate Representations

<!-- paper:e26 -->
- (*2026*) **From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills** [[📝 Paper](https://arxiv.org/abs/2604.24026)] [[💻 Code](https://github.com/COOLPKU/SSL)]  
  → This work represents skill procedures through scheduling, structural, and logical constraints to support reliable composition.

<!-- paper:c14 -->
- (*2026*) **Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents** [[📝 Paper](https://arxiv.org/abs/2606.09316)]  
  → Anything2Skill extracts evidence-grounded procedures from external knowledge and compiles them into structured contracts maintained in a persistent SkillBank.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:e30 -->
- (*2026*) **SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.03353)] [[💻 Code](https://github.com/Nexa-Language/Skill-Compiler)]  
  → SkCC uses a typed intermediate representation to compile portable skill artifacts and check cross-framework execution constraints.

<!-- paper:c17 -->
- (*2026*) **SIGIL: Skill Compilation for Reliable and Efficient Agent Execution** [[📝 Paper](https://arxiv.org/abs/2607.27309)]  
  → SIGIL translates authored skills into a validated typed intermediate representation and generates executable harnesses that enforce prescribed procedures.

<!-- paper:c23 -->
- (*2026*) **ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents** [[📝 Paper](https://arxiv.org/abs/2603.20340)] [[💻 Code](https://github.com/underfitting-lu/contractskill)]  
  → ContractSkill turns web-agent skills into executable contracts that support verification, fault localization, and targeted procedural repairs.

<!-- paper:c33 -->
- (*2026*) **Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.10990)]  
  → This work models skill drift as contract violations and supports proactive maintenance when dependencies or execution conditions change.

<!-- paper:c35 -->
- (*2026*) **Skillware: A Software Ontology and Engineering Lifecycle for Persistent Behavioral Artifacts** [[📝 Paper](https://arxiv.org/abs/2607.18970)] [[💻 Code](https://github.com/MetaInFLow/skillware-patterns)]  
  → Skillware treats persistent skills as software artifacts with explicit interfaces, versions, dependencies, and lifecycle operations.

<!-- paper:lu2026skillsentry -->
- (*2026*) **SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance** [[📝 Paper](https://arxiv.org/abs/2608.09253)]  
  → SkillSentry checks skill steps and constraints during execution and returns targeted guidance when runtime behavior deviates from the procedure.

<!-- paper:xli2026skill -->
- (*2026*) **Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.27955)] [[💻 Code](https://github.com/InternLM/Skill-as-Pseudocode)]  
  → Skill-as-Pseudocode converts skill documents into typed contracts and explicit action templates for more structured agent execution.

<!-- paper:xblumenfeld2026aip -->
- (*2026*) **AIP: A Graph Representation for Learning and Governing Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.04781)] [[💻 Code](https://github.com/zach-blumenfeld/aip-skillbench)]  
  → AIP represents skills as typed execution graphs with procedural descriptions and executable nodes for learning and governance.

<!-- paper:xliu2026embodied -->
- (*2026*) **Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling** [[📝 Paper](https://arxiv.org/abs/2606.31252)]  
  → Embodied CAD grounds reusable modeling procedures in geometric solvers and executable constraints for parametric assembly tasks.

<!-- paper:c40 -->
- (*2026*) **Behavioral Integrity Verification for AI Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.11770)]  
  → Behavioral Integrity Verification compares declared skill capabilities with behavior inferred from instructions and code to detect integrity violations.

<!-- paper:xchen2026slbench -->
- (*2026*) **SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills** [[📝 Paper](https://arxiv.org/abs/2607.09016)]  
  → SLBench measures whether agents obey logical relationships and constraints encoded in reusable skill procedures.

<a id="representations-executable-skills"></a>

### Executable Skills

<a id="representations-executable-skills-functions-scripts-and-executable-modules"></a>

#### Functions, Scripts, and Executable Modules

<!-- paper:e01 -->
- (*2023*) **Voyager: An Open-Ended Embodied Agent with Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.16291)] [[💻 Code](https://github.com/MineDojo/Voyager)] [[🌐 Project](https://voyager.minedojo.org/)]  
  → Voyager learns executable skills through Minecraft exploration, execution feedback, and iterative code refinement, then reuses them from a growing library.

<!-- paper:e06 -->
- (*2025*) **LLM Agents Making Agent Tools** [[📝 Paper](https://arxiv.org/abs/2502.11705)] [[💻 Code](https://github.com/KatherLab/ToolMaker)]  
  → ToolMaker converts scientific papers and their code into reusable tools that LLM agents can invoke.

<!-- paper:e12 -->
- (*2025*) **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[📝 Paper](https://arxiv.org/abs/2504.07079)] [[💻 Code](https://github.com/OSU-NLP-Group/SkillWeaver)]  
  → SkillWeaver explores websites, synthesizes reusable APIs, and improves them through execution-based practice.

<!-- paper:e07 -->
- (*2026*) **Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs** [[📝 Paper](https://arxiv.org/abs/2504.20406)]  
  → This approach discovers and verifies reusable software-scripting skills through offline simulations of API interactions.

<!-- paper:e13 -->
- (*2025*) **Inducing Programmatic Skills for Agentic Tasks** [[📝 Paper](https://arxiv.org/abs/2504.06821)] [[💻 Code](https://github.com/zorazrw/agent-skill-induction)]  
  → This framework induces executable programmatic skills from agent task experience and verifies them before reuse.

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:c15 -->
- (*2026*) **SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2606.26669)]  
  → SkillDisCo distills shared control-flow structures from successful agent traces and compiles them into parameterized, callable procedural skills.

<!-- paper:c16 -->
- (*2026*) **Harnessing LLM Agents with Skill Programs** [[📝 Paper](https://arxiv.org/abs/2605.17734)] [[💻 Code](https://github.com/HolaYan/ExecutableSkills-HASP)]  
  → HASP represents reusable skills as executable program functions that intervene in agent loops by modifying actions or supplying corrective context.

<!-- paper:e23 -->
- (*2026*) **ASPIRE: Agentic /Skills Discovery for Robotics** [[📝 Paper](https://arxiv.org/abs/2607.00272)]  
  → ASPIRE constructs and repairs reusable robot skills from multimodal execution traces and failure analysis.

<!-- paper:xgaurav2025codemem -->
- (*2025*) **CodeMem: Architecting Reproducible Agents via Dynamic MCP and Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2512.15813)]  
  → CodeMem stores reusable executable procedures behind dynamic MCP interfaces to support reproducible agent execution.

<!-- paper:xwang2026effiskill -->
- (*2026*) **EffiSkill: Agent Skill Based Automated Code Efficiency Optimization** [[📝 Paper](https://arxiv.org/abs/2603.27850)]  
  → EffiSkill constructs and applies reusable optimization skills to improve the execution efficiency of generated code.

<!-- paper:xlou2026lego -->
- (*2026*) **LEGO: An LLM Skill-Based Front-End Design Generation Platform** [[📝 Paper](https://arxiv.org/abs/2604.23355)] [[🌐 Project](https://github.com/loujc/LEGO-An-LLM-Skill-Based-Front-End-Design-Generation-Platform)]  
  → LEGO packages frontend implementation knowledge as reusable skills that guide LLM-based interface generation.

<!-- paper:xyang2026evods -->
- (*2026*) **EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management** [[📝 Paper](https://arxiv.org/abs/2606.03841)] [[💻 Code](https://github.com/usail-hkust/EvoDS)]  
  → EvoDS learns reusable data-science skills and manages task context to improve autonomous analysis through experience.

<!-- paper:xhuang2025cascade -->
- (*2025*) **CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution** [[📝 Paper](https://arxiv.org/abs/2512.23880)]  
  → CASCADE builds a cumulative library of executable capabilities through autonomous development, testing, and skill evolution.

<!-- paper:xcao2026guideskill -->
- (*2026*) **GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning** [[📝 Paper](https://arxiv.org/abs/2607.26160)]  
  → GuideSkill converts clinical guidelines into executable skills and evolves them using execution feedback for grounded clinical reasoning.

<!-- paper:xgaurav2025synthesizing -->
- (*2025*) **Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation** [[📝 Paper](https://arxiv.org/abs/2512.20278)]  
  → This work examines architectures and challenges for generating reusable procedural memory from automated workflows.

<!-- paper:f07 -->
- (*2018*) **Learning Libraries of Subroutines for Neurally-Guided Bayesian Program Induction** [[📝 Paper](https://people.csail.mit.edu/asolar/papers/EllisMSST18.pdf)]  
  → This library-learning method discovers reusable subroutines while training a neural guide to search programs expressed in the evolving library.

<!-- paper:f08 -->
- (*2021*) **DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning** [[📝 Paper](https://doi.org/10.1145/3453483.3454080)] [[💻 Code](https://github.com/ellisk42/ec)]  
  → DreamCoder alternates program synthesis and abstraction learning to grow a library of reusable computational concepts.

<!-- paper:f09 -->
- (*2023*) **Top-Down Synthesis for Library Learning** [[📝 Paper](http://dx.doi.org/10.1145/3571234)] [[💻 Code](https://github.com/mlb2251/stitch)]  
  → Top-down library learning discovers reusable program abstractions by searching over candidate library functions and their compressive value.

<!-- paper:f10 -->
- (*2024*) **LILO: Learning Interpretable Libraries by Compressing and Documenting Code** [[📝 Paper](https://arxiv.org/abs/2310.19791)] [[💻 Code](https://github.com/gabegrand/lilo)]  
  → LILO compresses synthesized programs into reusable library functions and documents the abstractions with natural language.

<!-- paper:f11 -->
- (*2024*) **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** [[📝 Paper](https://arxiv.org/abs/2401.16467)] [[💻 Code](https://github.com/esteng/regal_program_learning)]  
  → ReGAL refactors task programs into shared abstractions that can be reused during subsequent program generation.

<!-- paper:f12 -->
- (*2022*) **Leveraging Language to Learn Program Abstractions and Search Heuristics** [[📝 Paper](https://arxiv.org/abs/2106.11053)]  
  → This work uses language to guide the acquisition of program abstractions and search heuristics for reusable computational procedures.

<!-- paper:f13 -->
- (*2018*) **HOUDINI: Lifelong Learning as Program Synthesis** [[📝 Paper](https://arxiv.org/abs/1804.00218)] [[💻 Code](https://github.com/trishullab/houdini)]  
  → HOUDINI synthesizes typed differentiable programs from reusable neural modules and expands its library through lifelong learning.

<!-- paper:f33 -->
- (*2024*) **Large Language Models as Tool Makers** [[📝 Paper](https://arxiv.org/abs/2305.17126)] [[💻 Code](https://github.com/ctlllll/LLM-ToolMaker)]  
  → This framework lets a language model create reusable tools that other model instances invoke during downstream task solving.

<!-- paper:f34 -->
- (*2023*) **CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.14318)] [[💻 Code](https://github.com/qiancheng0/CREATOR)]  
  → CREATOR separates abstract reasoning from executable tool creation and reuses generated tools to solve related problems.

<!-- paper:f35 -->
- (*2023*) **Toolformer: Language Models Can Teach Themselves to Use Tools** [[📝 Paper](https://arxiv.org/abs/2302.04761)]  
  → Toolformer learns when and how to invoke external tools, providing an interface-learning foundation for executable skill use.

<a id="representations-executable-skills-compiled-runtime-interfaces-and-harnesses"></a>

#### Compiled Runtime Interfaces and Harnesses

<!-- paper:e27 -->
- (*2026*) **SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses** [[📝 Paper](https://arxiv.org/abs/2604.03088)]  
  → SkVM compiles skill procedures into a language-virtual-machine representation for execution across models and agent harnesses.

<!-- paper:e28 -->
- (*2026*) **SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces** [[📝 Paper](https://arxiv.org/abs/2605.15215)] [[💻 Code](https://github.com/AetherHeart-AI/Aeloon)]  
  → Boundary-guided SkillSmith compiles skill packages into minimal runtime interfaces that expose the operations needed for execution.

<!-- paper:c17 -->
- (*2026*) **SIGIL: Skill Compilation for Reliable and Efficient Agent Execution** [[📝 Paper](https://arxiv.org/abs/2607.27309)]  
  → SIGIL translates authored skills into a validated typed intermediate representation and generates executable harnesses that enforce prescribed procedures.

<!-- paper:c18 -->
- (*2026*) **Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.19604)] [[💻 Code](https://github.com/PKU-LLM-DS-LAB/FairyClaw)]  
  → Formal Skill combines typed metadata, executable state machines, and runtime hooks to make reusable agent procedures observable and enforceable.

<!-- paper:c24 -->
- (*2026*) **SkillDroid: Compile Once, Reuse Forever** [[📝 Paper](https://arxiv.org/abs/2604.14872)]  
  → SkillDroid compiles successful mobile interaction trajectories into parameterized templates that can be replayed and recompiled after execution failures.

<!-- paper:f38 -->
- (*2024*) **SGLang: Efficient Execution of Structured Language Model Programs** [[📝 Paper](https://arxiv.org/abs/2312.07104)] [[💻 Code](https://github.com/sgl-project/sglang)]  
  → SGLang provides structured language-model programs and an efficient runtime for executing reusable control and generation patterns.

<!-- paper:f39 -->
- (*2023*) **An LLM Compiler for Parallel Function Calling** [[📝 Paper](https://arxiv.org/abs/2312.04511)] [[💻 Code](https://github.com/SqueezeAILab/LLMCompiler)]  
  → LLMCompiler plans and schedules parallel function calls, supporting efficient orchestration of reusable executable components.

<!-- paper:f41 -->
- (*2024*) **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** [[📝 Paper](https://arxiv.org/abs/2405.15793)] [[💻 Code](https://github.com/SWE-agent/SWE-agent)]  
  → SWE-agent designs agent-computer interfaces for repository interaction, providing an execution environment for reusable software-engineering procedures.

<!-- paper:f40 -->
- (*2024*) **Executable Code Actions Elicit Better LLM Agents** [[📝 Paper](https://arxiv.org/abs/2402.01030)] [[💻 Code](https://github.com/xingyaoww/code-act)]  
  → CodeAct represents agent actions as executable code, enabling the composition and reuse of tool operations through a common interface.

<a id="representations-internalized-skills"></a>

### Internalized Skills

<a id="representations-internalized-skills-adapter-and-lora-based-skills"></a>

#### Adapter- and LoRA-based Skills

<!-- paper:c56 -->
- (*2026*) **Parametric Skills** [[📝 Paper](https://arxiv.org/abs/2606.30015)]  
  → Parametric Skills uses a hypernetwork to convert textual skills into LoRA adapters for context-free procedural reuse.

<!-- paper:c57 -->
- (*2026*) **Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.16769)]  
  → Skill-to-LoRA synthesizes demonstrations from skill documents and trains skill-specific adapters that replace repeated runtime instruction loading.

<!-- paper:xliu2025skill -->
- (*2025*) **Skill Expansion and Composition in Parameter Space** [[📝 Paper](https://arxiv.org/abs/2502.05932)] [[💻 Code](https://github.com/ltlhuuu/PSEC)]  
  → PSEC expands a library of compact skill modules and composes them in parameter space to address new control tasks.

<!-- paper:xsi2026vla -->
- (*2026*) **VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models** [[📝 Paper](https://arxiv.org/abs/2605.29562)]  
  → VLA-Pro transfers procedural memory across tasks through skill modules for vision-language-action models.

<!-- paper:f55 -->
- (*2019*) **Parameter-Efficient Transfer Learning for NLP** [[📝 Paper](https://arxiv.org/abs/1902.00751)] [[💻 Code](https://github.com/google-research/adapter-bert)]  
  → Adapters store task-specific behavior in compact trainable modules, providing a parameter-efficient carrier for internalized skills.

<!-- paper:f56 -->
- (*2021*) **AdapterFusion: Non-Destructive Task Composition for Transfer Learning** [[📝 Paper](https://arxiv.org/abs/2005.00247)] [[💻 Code](https://github.com/Adapter-Hub/adapters)]  
  → AdapterFusion combines pretrained task adapters to transfer and compose capabilities while preserving the underlying modules.

<!-- paper:f57 -->
- (*2021*) **LoRA: Low-Rank Adaptation of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2106.09685)] [[💻 Code](https://github.com/microsoft/LoRA)]  
  → LoRA represents adaptation through low-rank parameter updates, enabling compact and interchangeable modules for learned skills.

<!-- paper:f58 -->
- (*2024*) **Instance-Level Dynamic LoRAs Composition for Cross-Task Generalization** [[📝 Paper](https://aclanthology.org/2024.findings-emnlp.326/)] [[💻 Code](https://github.com/noname822/iLoraComp)]  
  → This method selects and weights multiple LoRA modules for each input to compose task expertise for unseen tasks.

<!-- paper:xwu2025tokmem -->
- (*2026*) **TokMem: One-Token Procedural Memory for Large Language Models** [[📝 Paper](https://arxiv.org/abs/2510.00444)] [[💻 Code](https://github.com/MANGA-UOFA/TokMem)]  
  → TokMem distills procedural instructions into trainable memory tokens that activate reusable behavior in a frozen language model.

<!-- paper:han2026kvskill -->
- (*2026*) **KV-Skill: Forging Expertise in the Model's Native Language** [[📝 Paper](https://arxiv.org/abs/2608.05475)] [[💻 Code](https://github.com/shawnzhg/KV-Skill)]  
  → KV-Skill converts expertise into external latent operators accessed through a model-side interface during inference.

<a id="representations-internalized-skills-learned-policies-and-controllers"></a>

#### Learned Policies and Controllers

<!-- paper:gu2025colada -->
- (*2024*) **Continual Robot Skill and Task Learning via Dialogue** [[📝 Paper](https://arxiv.org/abs/2409.03166)]  
  → CoLaDA uses dialogue to acquire and confirm robot skills and task knowledge for continual learning.

<!-- paper:xju2024rethinking -->
- (*2024*) **Rethinking Mutual Information for Language Conditioned Skill Discovery on Imitation Learning** [[📝 Paper](https://arxiv.org/abs/2402.17511)]  
  → LCSD uses mutual-information objectives to learn discrete language-conditioned skills from multitask demonstrations.

<!-- paper:xhe2025goal -->
- (*2025*) **Goal-Oriented Skill Abstraction for Offline Multi-Task Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2507.06628)]  
  → GO-Skill abstracts goal-oriented behaviors from offline multitask experience for reusable downstream control.

<!-- paper:xingelhag2024robotic -->
- (*2024*) **A Robotic Skill Learning System Built Upon Diffusion Policies and Foundation Models** [[📝 Paper](https://arxiv.org/abs/2403.16730)]  
  → This system learns diffusion-policy skills from demonstrations and uses foundation models to select and coordinate them for robot tasks.

<!-- paper:xhu2025sample -->
- (*2026*) **Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model** [[📝 Paper](https://arxiv.org/abs/2512.14031)]  
  → This benchmark compares hierarchical reinforcement learning and vision-language-action models for sample-efficient acquisition of construction robot skills.

<!-- paper:xli2024skill -->
- (*2025*) **Skill matters: Dynamic skill learning for multi-agent cooperative reinforcement learning** [[📝 Paper](https://www.sciencedirect.com/science/article/pii/S0893608024007767)]  
  → Dynamic Skill Learning discovers diverse multi-agent behaviors and assigns skills to agents according to their evolving task context.

<!-- paper:xliu2025learning -->
- (*2025*) **Learning Generalizable Skills from Offline Multi-Task Data for Multi-Agent Cooperation** [[📝 Paper](https://arxiv.org/abs/2503.21200)] [[💻 Code](https://github.com/mooricAnna/HiSSD)]  
  → HiSSD learns shared and task-specific skills from offline multitask data to support generalizable multi-agent cooperation.

<!-- paper:f01 -->
- (*1998*) **Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning** [[📝 Paper](https://www.sciencedirect.com/science/article/pii/S0004370299000521)]  
  → The options framework formalizes temporally extended actions through initiation conditions, internal policies, and termination rules, providing a foundation for reusable skills.

<!-- paper:f03 -->
- (*2016*) **The Option-Critic Architecture** [[📝 Paper](https://arxiv.org/abs/1609.05140)] [[💻 Code](https://github.com/jeanharb/option_critic)]  
  → Option-Critic jointly learns option policies and termination conditions to acquire temporally extended skills from reward feedback.

<!-- paper:f02 -->
- (*2000*) **Hierarchical reinforcement learning with the MAXQ value function decomposition** [[📝 Paper](https://arxiv.org/abs/cs/9905014)]  
  → MAXQ decomposes reinforcement-learning tasks into reusable subtasks and their value functions, supporting hierarchical skill construction.

<!-- paper:f06 -->
- (*2019*) **MCP: Learning Composable Hierarchical Control with Multiplicative Compositional Policies** [[📝 Paper](https://arxiv.org/abs/1905.09808)] [[🌐 Project](https://xbpeng.github.io/projects/MCP/index.html)]  
  → Multiplicative Compositional Policies combine learned control primitives to construct reusable hierarchical behaviors.

<!-- paper:f04 -->
- (*2018*) **Diversity is All You Need: Learning Skills without a Reward Function** [[📝 Paper](https://arxiv.org/abs/1802.06070)] [[💻 Code](https://github.com/ben-eysenbach/sac/blob/master/DIAYN.md)]  
  → DIAYN discovers diverse, distinguishable behaviors without task rewards, providing a reusable repertoire for downstream control.

<!-- paper:f05 -->
- (*2020*) **Accelerating Reinforcement Learning with Learned Skill Priors** [[📝 Paper](https://arxiv.org/abs/2010.11944)] [[💻 Code](https://github.com/clvrai/spirl)]  
  → This approach learns a prior over behavioral skills from offline experience and uses it to accelerate downstream reinforcement learning.

<a id="representations-hybrid-skills"></a>

### Hybrid Skills

<!-- paper:c07 -->
- (*2026*) **CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification** [[📝 Paper](https://arxiv.org/abs/2604.01687)] [[💻 Code](https://github.com/Zhang-Henry/CoEvoSkills)]  
  → CoEvoSkills co-evolves skill candidates and their verification procedures to support continued improvement of reusable agent capabilities.

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:c12 -->
- (*2026*) **SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources** [[📝 Paper](https://arxiv.org/abs/2604.03964)] [[💻 Code](https://github.com/ma-compbio-lab/SkillFoundry)]  
  → SkillFoundry mines heterogeneous scientific resources, extracts operational contracts, and validates executable skill packages in an evolving library.

<!-- paper:c35 -->
- (*2026*) **Skillware: A Software Ontology and Engineering Lifecycle for Persistent Behavioral Artifacts** [[📝 Paper](https://arxiv.org/abs/2607.18970)] [[💻 Code](https://github.com/MetaInFLow/skillware-patterns)]  
  → Skillware treats persistent skills as software artifacts with explicit interfaces, versions, dependencies, and lifecycle operations.

<!-- paper:e04 -->
- (*2026*) **CUA-Skill: Develop Skills for Computer Using Agent** [[📝 Paper](https://arxiv.org/abs/2601.21123)] [[💻 Code](https://github.com/microsoft/cua_skill)] [[🌐 Project](https://microsoft.github.io/cua_skill/)]  
  → CUA-Skill organizes computer-use procedures in a skill library that combines operational guidance with resources for visual interaction.

<!-- paper:xchen2026skilltrace -->
- (*2026*) **SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse** [[📝 Paper](https://arxiv.org/abs/2608.05204)]  
  → SkillTrace audits provenance across descriptions, implementations, and execution traces to make skill reuse relationships inspectable.

<!-- paper:xwang2026webxskill -->
- (*2026*) **WebXSkill: Skill Learning for Autonomous Web Agents** [[📝 Paper](https://arxiv.org/abs/2604.13318)] [[🌐 Project](https://github.com/aiming-lab/WebXSkill)]  
  → WebXSkill learns reusable web-interaction procedures from experience and combines procedural guidance with executable resources.

<!-- paper:xliu2026drive -->
- (*2026*) **DRIVE: Modeling Skills at the Reasoning and Interaction Levels for Web Agents under Continual Learning** [[📝 Paper](https://arxiv.org/abs/2605.23939)]  
  → DRIVE maintains reusable web-agent skills at both reasoning and interaction levels for continual task learning.

<!-- paper:xliu2026skilllens -->
- (*2026*) **SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation** [[📝 Paper](https://arxiv.org/abs/2608.10775)]  
  → SkillLens constructs visual skill cards for GUI-action retrieval and distills their guidance into an agent policy.

<!-- paper:xcheng2026continual -->
- (*2025*) **Continual Robot Learning via Language-Guided Skill Acquisition** [[📝 Paper](https://openreview.net/forum?id=dVMqrppXOR)]  
  → LG-SAIL combines language-guided skill acquisition and continued robot interaction to expand a reusable control repertoire.

[↑ Contents](#contents)

<a id="utilization"></a>

## 4. Skill Utilization

Agents use skills through context injection, runtime invocation, and model activation, with multi-skill orchestration coordinating their use.

- **[Context Injection](#utilization-context-injection)**
- **[Runtime Invocation](#utilization-runtime-invocation)**
- **[Model Activation](#utilization-model-activation)**
- **[Multi-Skill Orchestration](#utilization-multi-skill-orchestration)**

<a id="utilization-context-injection"></a>

### Context Injection

<!-- paper:c01 -->
- (*2024*) **ExpeL: LLM Agents Are Experiential Learners** [[📝 Paper](https://arxiv.org/abs/2308.10144)] [[💻 Code](https://github.com/LeapLabTHU/ExpeL)]  
  → ExpeL extracts reusable natural-language insights from successful and failed task experiences and retrieves them to guide subsequent agent decisions.

<!-- paper:e02 -->
- (*2026*) **AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** [[📝 Paper](https://arxiv.org/abs/2603.01145)] [[💻 Code](https://github.com/ECNU-ICALK/AutoSkill)]  
  → AutoSkill distills conversational experience into reusable skills and updates them as new interactions accumulate.

<!-- paper:e16 -->
- (*2026*) **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** [[📝 Paper](https://arxiv.org/abs/2603.25158)] [[💻 Code](https://github.com/Qwen-Applications/Trace2Skill)]  
  → Trace2Skill consolidates lessons from execution trajectories into transferable procedural skills with explicit applicability guidance.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:e10 -->
- (*2026*) **SkillX: Automatically Constructing Skill Knowledge Bases for Agents** [[📝 Paper](https://arxiv.org/abs/2604.04804)] [[💻 Code](https://github.com/zjunlp/SkillX)]  
  → SkillX constructs a hierarchical skill knowledge base through multilevel design, iterative refinement, and exploratory expansion.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:c52 -->
- (*2024*) **SkillAct: Using Skill Abstractions Improves LLM Agents** [[📝 Paper](https://openreview.net/forum?id=6LG3cIRrF4)]  
  → SkillAct uses reusable skill abstractions to supply procedural guidance for LLM-agent task execution.

<!-- paper:e04 -->
- (*2026*) **CUA-Skill: Develop Skills for Computer Using Agent** [[📝 Paper](https://arxiv.org/abs/2601.21123)] [[💻 Code](https://github.com/microsoft/cua_skill)] [[🌐 Project](https://microsoft.github.io/cua_skill/)]  
  → CUA-Skill organizes computer-use procedures in a skill library that combines operational guidance with resources for visual interaction.

<!-- paper:e24 -->
- (*2026*) **SkillGen: Verified Inference-Time Agent Skill Synthesis** [[📝 Paper](https://arxiv.org/abs/2605.10999)] [[💻 Code](https://github.com/yccm/SkillGen)]  
  → SkillGen synthesizes skills at inference time through contrastive trajectory analysis, iterative refinement, and paired performance verification.

<!-- paper:wang2026atlasva -->
- (*2026*) **AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.17933)]  
  → AtlasVA accumulates visual skill memory from teacher-free interaction and retrieves it to guide subsequent visual-agent decisions.

<!-- paper:c34 -->
- (*2026*) **SkillReducer: Optimizing LLM Agent Skills for Token Efficiency** [[📝 Paper](https://arxiv.org/abs/2603.29919)]  
  → SkillReducer compresses skill instructions to reduce context costs while preserving the information needed to select and execute the procedure.

<!-- paper:xli2026online -->
- (*2026*) **Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval** [[📝 Paper](https://arxiv.org/abs/2606.04391)] [[💻 Code](https://github.com/plusnli/online-skill-learning)]  
  → This web-agent framework learns skills online and retrieves them using the current environment state to improve applicability.

<!-- paper:xmeng2026skillrae -->
- (*2026*) **SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution** [[📝 Paper](https://arxiv.org/abs/2605.10114)]  
  → SkillRAE compiles retrieved skill knowledge into structured execution context to support efficient multi-skill use.

<!-- paper:xlin2026emotion2skill -->
- (*2026*) **Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution** [[📝 Paper](https://arxiv.org/abs/2608.09248)] [[💻 Code](https://github.com/BoHan-LIN04/Emotion2Skill)]  
  → Emotion2Skill uses model-internal emotion signals to adapt skill selection and guide subsequent skill evolution.

<!-- paper:e30 -->
- (*2026*) **SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.03353)] [[💻 Code](https://github.com/Nexa-Language/Skill-Compiler)]  
  → SkCC uses a typed intermediate representation to compile portable skill artifacts and check cross-framework execution constraints.

<!-- paper:xyu2026skill -->
- (*2026*) **Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.30723)] [[💻 Code](https://github.com/jianxiangyu/MASA_)]  
  → Model-aware skill alignment adapts reusable instructions to the capabilities and execution behavior of different language-model backbones.

<!-- paper:c42 -->
- (*2026*) **How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings** [[📝 Paper](https://arxiv.org/abs/2604.04323)] [[💻 Code](https://github.com/UCSB-NLP-Chang/Skill-Usage)]  
  → The Skill-Usage study evaluates autonomous skill discovery, loading, and execution under realistic access to a large skill collection.

<!-- paper:c45 -->
- (*2026*) **SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.15557)] [[💻 Code](https://github.com/EverMind-AI/SkillCorpus)]  
  → SkillCorpus consolidates public skill packages and evaluates their organization, quality, and usefulness for real-world agents.

<!-- paper:c19 -->
- (*2026*) **Skill Retrieval Augmentation for Agentic AI** [[📝 Paper](https://arxiv.org/abs/2604.24594)] [[💻 Code](https://github.com/oneal2000/SR-Agents)]  
  → Skill Retrieval Augmentation retrieves procedural skills on demand and evaluates retrieval, incorporation, and downstream execution as distinct stages.

<!-- paper:c47 -->
- (*2026*) **SkillRouter: Skill Routing for LLM Agents at Scale** [[📝 Paper](https://arxiv.org/abs/2603.22455)]  
  → SkillRouter studies scalable routing from task requests to reusable agent skills and measures retrieval and execution performance.

<!-- paper:xli2025skillflow -->
- (*2025*) **SkillFlow: Scalable and Efficient Agent Skill Retrieval System** [[📝 Paper](https://arxiv.org/abs/2504.06188)] [[💻 Code](https://github.com/IBPA/skill-flow)]  
  → SkillFlow provides scalable retrieval and indexing of agent skills to support efficient access to large procedural libraries.

<!-- paper:xjiang2026skillreason -->
- (*2026*) **SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests** [[📝 Paper](https://arxiv.org/abs/2608.08640)]  
  → SkillReason uses reasoning about implicit user intent to improve retrieval of suitable procedural skills.

<a id="utilization-runtime-invocation"></a>

### Runtime Invocation

<!-- paper:e01 -->
- (*2023*) **Voyager: An Open-Ended Embodied Agent with Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.16291)] [[💻 Code](https://github.com/MineDojo/Voyager)] [[🌐 Project](https://voyager.minedojo.org/)]  
  → Voyager learns executable skills through Minecraft exploration, execution feedback, and iterative code refinement, then reuses them from a growing library.

<!-- paper:e12 -->
- (*2025*) **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[📝 Paper](https://arxiv.org/abs/2504.07079)] [[💻 Code](https://github.com/OSU-NLP-Group/SkillWeaver)]  
  → SkillWeaver explores websites, synthesizes reusable APIs, and improves them through execution-based practice.

<!-- paper:e07 -->
- (*2026*) **Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs** [[📝 Paper](https://arxiv.org/abs/2504.20406)]  
  → This approach discovers and verifies reusable software-scripting skills through offline simulations of API interactions.

<!-- paper:e13 -->
- (*2025*) **Inducing Programmatic Skills for Agentic Tasks** [[📝 Paper](https://arxiv.org/abs/2504.06821)] [[💻 Code](https://github.com/zorazrw/agent-skill-induction)]  
  → This framework induces executable programmatic skills from agent task experience and verifies them before reuse.

<!-- paper:c16 -->
- (*2026*) **Harnessing LLM Agents with Skill Programs** [[📝 Paper](https://arxiv.org/abs/2605.17734)] [[💻 Code](https://github.com/HolaYan/ExecutableSkills-HASP)]  
  → HASP represents reusable skills as executable program functions that intervene in agent loops by modifying actions or supplying corrective context.

<!-- paper:f36 -->
- (*2023*) **ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings** [[📝 Paper](https://arxiv.org/abs/2305.11554)] [[💻 Code](https://github.com/Ber666/ToolkenGPT)]  
  → ToolkenGPT represents callable tools as learned embeddings that let a frozen language model select and invoke external capabilities.

<!-- paper:e27 -->
- (*2026*) **SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses** [[📝 Paper](https://arxiv.org/abs/2604.03088)]  
  → SkVM compiles skill procedures into a language-virtual-machine representation for execution across models and agent harnesses.

<!-- paper:e28 -->
- (*2026*) **SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces** [[📝 Paper](https://arxiv.org/abs/2605.15215)] [[💻 Code](https://github.com/AetherHeart-AI/Aeloon)]  
  → Boundary-guided SkillSmith compiles skill packages into minimal runtime interfaces that expose the operations needed for execution.

<!-- paper:c17 -->
- (*2026*) **SIGIL: Skill Compilation for Reliable and Efficient Agent Execution** [[📝 Paper](https://arxiv.org/abs/2607.27309)]  
  → SIGIL translates authored skills into a validated typed intermediate representation and generates executable harnesses that enforce prescribed procedures.

<!-- paper:c18 -->
- (*2026*) **Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.19604)] [[💻 Code](https://github.com/PKU-LLM-DS-LAB/FairyClaw)]  
  → Formal Skill combines typed metadata, executable state machines, and runtime hooks to make reusable agent procedures observable and enforceable.

<!-- paper:c24 -->
- (*2026*) **SkillDroid: Compile Once, Reuse Forever** [[📝 Paper](https://arxiv.org/abs/2604.14872)]  
  → SkillDroid compiles successful mobile interaction trajectories into parameterized templates that can be replayed and recompiled after execution failures.

<!-- paper:xwang2026webxskill -->
- (*2026*) **WebXSkill: Skill Learning for Autonomous Web Agents** [[📝 Paper](https://arxiv.org/abs/2604.13318)] [[🌐 Project](https://github.com/aiming-lab/WebXSkill)]  
  → WebXSkill learns reusable web-interaction procedures from experience and combines procedural guidance with executable resources.

<!-- paper:xgaurav2025codemem -->
- (*2025*) **CodeMem: Architecting Reproducible Agents via Dynamic MCP and Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2512.15813)]  
  → CodeMem stores reusable executable procedures behind dynamic MCP interfaces to support reproducible agent execution.

<!-- paper:xliu2026embodied -->
- (*2026*) **Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling** [[📝 Paper](https://arxiv.org/abs/2606.31252)]  
  → Embodied CAD grounds reusable modeling procedures in geometric solvers and executable constraints for parametric assembly tasks.

<!-- paper:f33 -->
- (*2024*) **Large Language Models as Tool Makers** [[📝 Paper](https://arxiv.org/abs/2305.17126)] [[💻 Code](https://github.com/ctlllll/LLM-ToolMaker)]  
  → This framework lets a language model create reusable tools that other model instances invoke during downstream task solving.

<!-- paper:f34 -->
- (*2023*) **CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2305.14318)] [[💻 Code](https://github.com/qiancheng0/CREATOR)]  
  → CREATOR separates abstract reasoning from executable tool creation and reuses generated tools to solve related problems.

<!-- paper:f38 -->
- (*2024*) **SGLang: Efficient Execution of Structured Language Model Programs** [[📝 Paper](https://arxiv.org/abs/2312.07104)] [[💻 Code](https://github.com/sgl-project/sglang)]  
  → SGLang provides structured language-model programs and an efficient runtime for executing reusable control and generation patterns.

<!-- paper:f40 -->
- (*2024*) **Executable Code Actions Elicit Better LLM Agents** [[📝 Paper](https://arxiv.org/abs/2402.01030)] [[💻 Code](https://github.com/xingyaoww/code-act)]  
  → CodeAct represents agent actions as executable code, enabling the composition and reuse of tool operations through a common interface.

<!-- paper:f41 -->
- (*2024*) **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** [[📝 Paper](https://arxiv.org/abs/2405.15793)] [[💻 Code](https://github.com/SWE-agent/SWE-agent)]  
  → SWE-agent designs agent-computer interfaces for repository interaction, providing an execution environment for reusable software-engineering procedures.

<!-- paper:lu2026skillsentry -->
- (*2026*) **SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance** [[📝 Paper](https://arxiv.org/abs/2608.09253)]  
  → SkillSentry checks skill steps and constraints during execution and returns targeted guidance when runtime behavior deviates from the procedure.

<!-- paper:xchen2026skillharness -->
- (*2026*) **SkillHarness: Harnessing Safe Skills for Computer-Use Agents** [[📝 Paper](https://arxiv.org/abs/2606.20636)]  
  → SkillHarness combines skill constraints, execution permissions, and context-dependent selection to support safe computer-use behavior.

<!-- paper:c50 -->
- (*2026*) **SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?** [[📝 Paper](https://arxiv.org/abs/2603.00718)] [[💻 Code](https://github.com/shiqichen17/SkillCraft)]  
  → SkillCraft evaluates whether agents can acquire and apply reusable tool-use skills across tasks.

<!-- paper:c53 -->
- (*2026*) **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** [[📝 Paper](https://arxiv.org/abs/2603.15401)] [[📦 Data](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)]  
  → SWE-Skills-Bench compares software-engineering agents with and without supplied skills on real repository tasks.

<a id="utilization-model-activation"></a>

### Model Activation

<!-- paper:c56 -->
- (*2026*) **Parametric Skills** [[📝 Paper](https://arxiv.org/abs/2606.30015)]  
  → Parametric Skills uses a hypernetwork to convert textual skills into LoRA adapters for context-free procedural reuse.

<!-- paper:c57 -->
- (*2026*) **Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.16769)]  
  → Skill-to-LoRA synthesizes demonstrations from skill documents and trains skill-specific adapters that replace repeated runtime instruction loading.

<!-- paper:xwu2025tokmem -->
- (*2026*) **TokMem: One-Token Procedural Memory for Large Language Models** [[📝 Paper](https://arxiv.org/abs/2510.00444)] [[💻 Code](https://github.com/MANGA-UOFA/TokMem)]  
  → TokMem distills procedural instructions into trainable memory tokens that activate reusable behavior in a frozen language model.

<!-- paper:xxie2026history -->
- (*2026*) **From History to State: Constant-Context Skill Learning for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.05413)]  
  → This method compresses accumulated interaction history into persistent skill state and compact modules for constant-context agent execution.

<!-- paper:f55 -->
- (*2019*) **Parameter-Efficient Transfer Learning for NLP** [[📝 Paper](https://arxiv.org/abs/1902.00751)] [[💻 Code](https://github.com/google-research/adapter-bert)]  
  → Adapters store task-specific behavior in compact trainable modules, providing a parameter-efficient carrier for internalized skills.

<!-- paper:f57 -->
- (*2021*) **LoRA: Low-Rank Adaptation of Large Language Models** [[📝 Paper](https://arxiv.org/abs/2106.09685)] [[💻 Code](https://github.com/microsoft/LoRA)]  
  → LoRA represents adaptation through low-rank parameter updates, enabling compact and interchangeable modules for learned skills.

<!-- paper:han2026kvskill -->
- (*2026*) **KV-Skill: Forging Expertise in the Model's Native Language** [[📝 Paper](https://arxiv.org/abs/2608.05475)] [[💻 Code](https://github.com/shawnzhg/KV-Skill)]  
  → KV-Skill converts expertise into external latent operators accessed through a model-side interface during inference.

<!-- paper:c36 -->
- (*2026*) **Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering** [[📝 Paper](https://arxiv.org/abs/2606.29824)]  
  → Neural Procedural Memory distills contrastive execution experience into activation-steering vectors that guide agent behavior.

<!-- paper:xingelhag2024robotic -->
- (*2024*) **A Robotic Skill Learning System Built Upon Diffusion Policies and Foundation Models** [[📝 Paper](https://arxiv.org/abs/2403.16730)]  
  → This system learns diffusion-policy skills from demonstrations and uses foundation models to select and coordinate them for robot tasks.

<!-- paper:xju2024rethinking -->
- (*2024*) **Rethinking Mutual Information for Language Conditioned Skill Discovery on Imitation Learning** [[📝 Paper](https://arxiv.org/abs/2402.17511)]  
  → LCSD uses mutual-information objectives to learn discrete language-conditioned skills from multitask demonstrations.

<!-- paper:xhe2025goal -->
- (*2025*) **Goal-Oriented Skill Abstraction for Offline Multi-Task Reinforcement Learning** [[📝 Paper](https://arxiv.org/abs/2507.06628)]  
  → GO-Skill abstracts goal-oriented behaviors from offline multitask experience for reusable downstream control.

<!-- paper:f03 -->
- (*2016*) **The Option-Critic Architecture** [[📝 Paper](https://arxiv.org/abs/1609.05140)] [[💻 Code](https://github.com/jeanharb/option_critic)]  
  → Option-Critic jointly learns option policies and termination conditions to acquire temporally extended skills from reward feedback.

<!-- paper:f05 -->
- (*2020*) **Accelerating Reinforcement Learning with Learned Skill Priors** [[📝 Paper](https://arxiv.org/abs/2010.11944)] [[💻 Code](https://github.com/clvrai/spirl)]  
  → This approach learns a prior over behavioral skills from offline experience and uses it to accelerate downstream reinforcement learning.

<!-- paper:c37 -->
- (*2026*) **SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization** [[📝 Paper](https://arxiv.org/abs/2604.02268)] [[💻 Code](https://github.com/ZJU-REAL/SkillZero)]  
  → SKILL0 progressively withdraws skill context during reinforcement learning so that agents internalize procedural guidance in their parameters.

<!-- paper:c38 -->
- (*2026*) **Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents** [[📝 Paper](https://arxiv.org/abs/2604.10674)]  
  → Skill-SD summarizes completed trajectories into skills that condition a training-time teacher and distills the resulting behavior into a skill-free student.

<!-- paper:xhe2026siri -->
- (*2026*) **SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training** [[📝 Paper](https://arxiv.org/abs/2606.02355)]  
  → SIRI derives intrinsic skills during reinforcement learning and internalizes their guidance in the agent policy.

<!-- paper:xliu2026procedural -->
- (*2026*) **Procedural Memory Distillation: Online Reflection for Self-Improving Language Models** [[📝 Paper](https://arxiv.org/abs/2607.01480)]  
  → Procedural Memory Distillation uses online reflection to convert execution experience into procedural knowledge internalized by a language model.

<a id="utilization-multi-skill-orchestration"></a>

### Multi-Skill Orchestration

<!-- paper:c20 -->
- (*2026*) **Graph-of-Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills** [[📝 Paper](https://arxiv.org/abs/2604.05333)] [[💻 Code](https://github.com/davidliuk/graph-of-skills)]  
  → Graph-of-Skills retrieves dependency-aware skill bundles from a graph so that selected procedures include the prerequisites needed for execution.

<!-- paper:c21 -->
- (*2026*) **GraSP: Graph-Structured Skill Compositions for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2604.17870)]  
  → GraSP compiles selected skills into typed dependency graphs with node-level verification and local repair for multi-skill execution.

<!-- paper:c22 -->
- (*2026*) **SkillNet: Create, Evaluate, and Connect AI Skills** [[📝 Paper](https://arxiv.org/abs/2603.04448)] [[💻 Code](https://github.com/zjunlp/SkillNet)]  
  → SkillNet organizes reusable skills in a shared ontology with explicit relationships, creation tools, and multidimensional evaluation.

<!-- paper:c16 -->
- (*2026*) **Harnessing LLM Agents with Skill Programs** [[📝 Paper](https://arxiv.org/abs/2605.17734)] [[💻 Code](https://github.com/HolaYan/ExecutableSkills-HASP)]  
  → HASP represents reusable skills as executable program functions that intervene in agent loops by modifying actions or supplying corrective context.

<!-- paper:c18 -->
- (*2026*) **Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.19604)] [[💻 Code](https://github.com/PKU-LLM-DS-LAB/FairyClaw)]  
  → Formal Skill combines typed metadata, executable state machines, and runtime hooks to make reusable agent procedures observable and enforceable.

<!-- paper:e29 -->
- (*2026*) **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems** [[📝 Paper](https://arxiv.org/abs/2605.13716)] [[💻 Code](https://github.com/Hik289/SkillOps)]  
  → SkillOps maintains skill libraries using typed contracts, dependency relationships, utility assessment, and lifecycle operations.

<!-- paper:xyao2026skilltrace -->
- (*2026*) **SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents** [[📝 Paper](https://arxiv.org/abs/2608.02356)]  
  → This SkillTrace framework traverses a query-skill graph to retrieve and compose procedures for complex agent requests.

<!-- paper:xmeng2026skillrae -->
- (*2026*) **SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution** [[📝 Paper](https://arxiv.org/abs/2605.10114)]  
  → SkillRAE compiles retrieved skill knowledge into structured execution context to support efficient multi-skill use.

<!-- paper:xli2026skillgraph -->
- (*2026*) **SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs** [[📝 Paper](https://arxiv.org/abs/2605.12039)]  
  → SkillGraph evolves a graph of reusable skills through reinforcement learning, including merging, splitting, and deprecating skill nodes.

<!-- paper:xzhao2026generative -->
- (*2026*) **Generative Skill Composition for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.32025)]  
  → SkillComposer generates task-adapted compositions of reusable skills for LLM-agent execution.

<!-- paper:xgao2026compositional -->
- (*2026*) **Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose** [[📝 Paper](https://arxiv.org/abs/2606.18051)]  
  → Compositional Skill Routing decomposes task requests, retrieves relevant skills, and composes them into task-solving procedures.

<!-- paper:xmeng2026constraint -->
- (*2026*) **Constraint-consistent skill composition for reliable zero-shot task generalization in LLM agents** [[📝 Paper](https://ieeexplore.ieee.org/document/11484408/)]  
  → This approach composes skills using explicit interfaces, preconditions, and effects to preserve consistency across task execution steps.

<!-- paper:f39 -->
- (*2023*) **An LLM Compiler for Parallel Function Calling** [[📝 Paper](https://arxiv.org/abs/2312.04511)] [[💻 Code](https://github.com/SqueezeAILab/LLMCompiler)]  
  → LLMCompiler plans and schedules parallel function calls, supporting efficient orchestration of reusable executable components.

<!-- paper:xli2024skill -->
- (*2025*) **Skill matters: Dynamic skill learning for multi-agent cooperative reinforcement learning** [[📝 Paper](https://www.sciencedirect.com/science/article/pii/S0893608024007767)]  
  → Dynamic Skill Learning discovers diverse multi-agent behaviors and assigns skills to agents according to their evolving task context.

<!-- paper:xliu2025learning -->
- (*2025*) **Learning Generalizable Skills from Offline Multi-Task Data for Multi-Agent Cooperation** [[📝 Paper](https://arxiv.org/abs/2503.21200)] [[💻 Code](https://github.com/mooricAnna/HiSSD)]  
  → HiSSD learns shared and task-specific skills from offline multitask data to support generalizable multi-agent cooperation.

<!-- paper:xliu2025skill -->
- (*2025*) **Skill Expansion and Composition in Parameter Space** [[📝 Paper](https://arxiv.org/abs/2502.05932)] [[💻 Code](https://github.com/ltlhuuu/PSEC)]  
  → PSEC expands a library of compact skill modules and composes them in parameter space to address new control tasks.

<!-- paper:xsi2026vla -->
- (*2026*) **VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models** [[📝 Paper](https://arxiv.org/abs/2605.29562)]  
  → VLA-Pro transfers procedural memory across tasks through skill modules for vision-language-action models.

<!-- paper:f56 -->
- (*2021*) **AdapterFusion: Non-Destructive Task Composition for Transfer Learning** [[📝 Paper](https://arxiv.org/abs/2005.00247)] [[💻 Code](https://github.com/Adapter-Hub/adapters)]  
  → AdapterFusion combines pretrained task adapters to transfer and compose capabilities while preserving the underlying modules.

<!-- paper:f58 -->
- (*2024*) **Instance-Level Dynamic LoRAs Composition for Cross-Task Generalization** [[📝 Paper](https://aclanthology.org/2024.findings-emnlp.326/)] [[💻 Code](https://github.com/noname822/iLoraComp)]  
  → This method selects and weights multiple LoRA modules for each input to compose task expertise for unseen tasks.

<!-- paper:xwang2026skill -->
- (*2026*) **Skill Is Not Document: Query-Conditioned Compatibility for LLM Agent Skill Routing** [[📝 Paper](https://arxiv.org/abs/2606.03565)]  
  → This routing method assesses query-conditioned skill compatibility so that retrieval accounts for procedural applicability.

<!-- paper:xhe2026relevance -->
- (*2026*) **From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents** [[📝 Paper](https://arxiv.org/abs/2608.09168)]  
  → Reward-aware execution gating estimates the utility of invoking a skill to guide selection beyond semantic relevance.

[↑ Contents](#contents)

<a id="evaluation"></a>

## 5. Skill Evaluation

Evaluation covers five quality dimensions and benchmarks for synthesis, utilization, evolution, and security.

- **[Metrics](#evaluation-metrics)**
  - [Fidelity](#evaluation-metrics-fidelity)
  - [Utility](#evaluation-metrics-utility)
  - [Transferability](#evaluation-metrics-transferability)
  - [Efficiency](#evaluation-metrics-efficiency)
  - [Safety](#evaluation-metrics-safety)
- **[Benchmarks](#evaluation-benchmarks)**
  - [Synthesis](#evaluation-benchmarks-synthesis)
  - [Utilization](#evaluation-benchmarks-utilization)
  - [Evolution](#evaluation-benchmarks-evolution)
  - [Security](#evaluation-benchmarks-security)

<a id="evaluation-metrics"></a>

### Metrics

<a id="evaluation-metrics-fidelity"></a>

#### Fidelity

<!-- paper:c23 -->
- (*2026*) **ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents** [[📝 Paper](https://arxiv.org/abs/2603.20340)] [[💻 Code](https://github.com/underfitting-lu/contractskill)]  
  → ContractSkill turns web-agent skills into executable contracts that support verification, fault localization, and targeted procedural repairs.

<!-- paper:c13 -->
- (*2026*) **RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources** [[📝 Paper](https://arxiv.org/abs/2606.29538)] [[💻 Code](https://github.com/microsoft/Resource2Skill)] [[📦 Data](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL)]  
  → RESOURCE2SKILL distills videos, repositories, and other human-created resources into a hierarchical skill wiki combining instructions, code, visual examples, and provenance.

<!-- paper:xzhang2026cross -->
- (*2026*) **Cross-Layer Misalignment Detection in Agent Skills: A Progressive Loading-Aware Contrastive Learning Approach** [[📝 Paper](https://arxiv.org/abs/2607.10534)]  
  → This method detects inconsistencies across skill descriptions, instructions, and implementations using loading-aware contrastive learning.

<!-- paper:c40 -->
- (*2026*) **Behavioral Integrity Verification for AI Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.11770)]  
  → Behavioral Integrity Verification compares declared skill capabilities with behavior inferred from instructions and code to detect integrity violations.

<!-- paper:xchen2026slbench -->
- (*2026*) **SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills** [[📝 Paper](https://arxiv.org/abs/2607.09016)]  
  → SLBench measures whether agents obey logical relationships and constraints encoded in reusable skill procedures.

<!-- paper:lu2026skillsentry -->
- (*2026*) **SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance** [[📝 Paper](https://arxiv.org/abs/2608.09253)]  
  → SkillSentry checks skill steps and constraints during execution and returns targeted guidance when runtime behavior deviates from the procedure.

<!-- paper:c39 -->
- (*2026*) **AEVAL: From Anecdotal to Deterministic Testing for Agentic Skill Workflows** [[📝 Paper](https://arxiv.org/abs/2607.16345)]  
  → AEVAL tests skill workflows with declared evaluation contracts, separate executors and graders, and explicit first-attempt scoring.

<!-- paper:xchen2026skilltrace -->
- (*2026*) **SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse** [[📝 Paper](https://arxiv.org/abs/2608.05204)]  
  → SkillTrace audits provenance across descriptions, implementations, and execution traces to make skill reuse relationships inspectable.

<a id="evaluation-metrics-utility"></a>

#### Utility

<!-- paper:e31 -->
- (*2026*) **SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks** [[📝 Paper](https://arxiv.org/abs/2602.12670)] [[💻 Code](https://github.com/benchflow-ai/skillsbench)] [[🌐 Project](https://www.skillsbench.ai/)]  
  → SkillsBench evaluates how supplied and generated skills affect agent performance across diverse tasks under controlled execution settings.

<!-- paper:c53 -->
- (*2026*) **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** [[📝 Paper](https://arxiv.org/abs/2603.15401)] [[📦 Data](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)]  
  → SWE-Skills-Bench compares software-engineering agents with and without supplied skills on real repository tasks.

<!-- paper:c41 -->
- (*2026*) **A Framework for Evaluating Agentic Skills at Scale** [[📝 Paper](https://arxiv.org/abs/2606.17819)]  
  → This evaluation framework generates realistic tasks and scoring rubrics to measure skill utility across agent-model configurations.

<!-- paper:c42 -->
- (*2026*) **How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings** [[📝 Paper](https://arxiv.org/abs/2604.04323)] [[💻 Code](https://github.com/UCSB-NLP-Chang/Skill-Usage)]  
  → The Skill-Usage study evaluates autonomous skill discovery, loading, and execution under realistic access to a large skill collection.

<!-- paper:xcho2026skillret -->
- (*2026*) **SkillRet: A Large-Scale Benchmark for Skill Retrieval in LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.05726)] [[💻 Code](https://github.com/ThakiCloud/SKILLRET)]  
  → SkillRet benchmarks retrieval of relevant skills from a large collection of procedural resources for LLM agents.

<!-- paper:c47 -->
- (*2026*) **SkillRouter: Skill Routing for LLM Agents at Scale** [[📝 Paper](https://arxiv.org/abs/2603.22455)]  
  → SkillRouter studies scalable routing from task requests to reusable agent skills and measures retrieval and execution performance.

<!-- paper:xzhou2026counterfactual -->
- (*2026*) **Counterfactual Trace Auditing of LLM Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.11946)] [[💻 Code](https://github.com/WillChow66/CTA)]  
  → Counterfactual Trace Auditing compares paired executions to identify how a supplied skill changes agent decisions and task outcomes.

<!-- paper:xdong2026agent -->
- (*2026*) **Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents** [[📝 Paper](https://arxiv.org/abs/2608.11888)]  
  → This study analyzes skill-induced failures by comparing agent behavior and outcomes with and without supplied skills.

<a id="evaluation-metrics-transferability"></a>

#### Transferability

<!-- paper:c46 -->
- (*2026*) **Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2606.23127)]  
  → AFTER evaluates procedural-memory improvement and transfer across tasks, professional roles, and model backbones.

<!-- paper:c43 -->
- (*2026*) **SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks** [[📝 Paper](https://arxiv.org/abs/2604.20087)] [[💻 Code](https://github.com/cxcscmu/SkillLearnBench)]  
  → SkillLearnBench evaluates continual skill generation through complementary measures of skill quality, execution trajectories, and task outcomes.

<!-- paper:c44 -->
- (*2026*) **SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents** [[📝 Paper](https://arxiv.org/abs/2604.17308)] [[💻 Code](https://github.com/ZhangZi-a/SkillFlow)]  
  → SkillFlow evaluates lifelong skill discovery and evolution by carrying an agent's revised library across sequences of related tasks.

<!-- paper:xlei2026skillevolbench -->
- (*2026*) **SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2605.24117)]  
  → SkillEvolBench separates experience acquisition from held-out deployment to evaluate transfer and composition of synthesized procedural skills.

<!-- paper:xguan2026continualskillbench -->
- (*2026*) **ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?** [[📝 Paper](https://arxiv.org/abs/2608.03874)] [[💻 Code](https://github.com/gtynnn060110-hash/continual-skill-bench-final)]  
  → ContinualSkillBench evaluates whether maintained skills improve capabilities beyond continued access to accumulated task experience.

<!-- paper:xyu2026skill -->
- (*2026*) **Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.30723)] [[💻 Code](https://github.com/jianxiangyu/MASA_)]  
  → Model-aware skill alignment adapts reusable instructions to the capabilities and execution behavior of different language-model backbones.

<!-- paper:xyang2026federatedskill -->
- (*2026*) **FederatedSkill: Federated Learning for Agentic Skill Evolution** [[📝 Paper](https://arxiv.org/abs/2606.03143)] [[💻 Code](https://github.com/UCSB-NLP-Chang/FederatedSkill)]  
  → FederatedSkill shares and evolves procedural skills across distributed agents while evaluating transfer across deployment sites.

<a id="evaluation-metrics-efficiency"></a>

#### Efficiency

<!-- paper:c34 -->
- (*2026*) **SkillReducer: Optimizing LLM Agent Skills for Token Efficiency** [[📝 Paper](https://arxiv.org/abs/2603.29919)]  
  → SkillReducer compresses skill instructions to reduce context costs while preserving the information needed to select and execute the procedure.

<!-- paper:c47 -->
- (*2026*) **SkillRouter: Skill Routing for LLM Agents at Scale** [[📝 Paper](https://arxiv.org/abs/2603.22455)]  
  → SkillRouter studies scalable routing from task requests to reusable agent skills and measures retrieval and execution performance.

<!-- paper:c48 -->
- (*2026*) **Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale** [[📝 Paper](https://arxiv.org/abs/2603.02176)] [[💻 Code](https://github.com/ynulihao/AgentSkillOS)]  
  → AgentSkillOS organizes skills in a capability tree and retrieves and orchestrates them through dependency-aware task pipelines.

<!-- paper:e31 -->
- (*2026*) **SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks** [[📝 Paper](https://arxiv.org/abs/2602.12670)] [[💻 Code](https://github.com/benchflow-ai/skillsbench)] [[🌐 Project](https://www.skillsbench.ai/)]  
  → SkillsBench evaluates how supplied and generated skills affect agent performance across diverse tasks under controlled execution settings.

<!-- paper:c53 -->
- (*2026*) **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** [[📝 Paper](https://arxiv.org/abs/2603.15401)] [[📦 Data](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)]  
  → SWE-Skills-Bench compares software-engineering agents with and without supplied skills on real repository tasks.

<!-- paper:xli2026pando -->
- (*2026*) **PANDO: Efficient Multimodal AI Agents via Online Skill Distillation** [[📝 Paper](https://arxiv.org/abs/2605.24785)]  
  → PANDO distills reusable skills during multimodal interaction to reduce repeated actions and execution overhead.

<!-- paper:xli2025skillflow -->
- (*2025*) **SkillFlow: Scalable and Efficient Agent Skill Retrieval System** [[📝 Paper](https://arxiv.org/abs/2504.06188)] [[💻 Code](https://github.com/IBPA/skill-flow)]  
  → SkillFlow provides scalable retrieval and indexing of agent skills to support efficient access to large procedural libraries.

<!-- paper:xmeng2026skillrae -->
- (*2026*) **SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution** [[📝 Paper](https://arxiv.org/abs/2605.10114)]  
  → SkillRAE compiles retrieved skill knowledge into structured execution context to support efficient multi-skill use.

<!-- paper:xzhang2026library -->
- (*2026*) **Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.19576)] [[💻 Code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)]  
  → Library Drift diagnoses performance changes caused by interactions among evolving skill entries and proposes library-level repairs.

<!-- paper:xsong2026more -->
- (*2026*) **More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.24050)]  
  → This study identifies skill shadowing, where expanding a library changes selection behavior and reduces the usefulness of existing skills.

<!-- paper:zhang2026skillreuse -->
- (*2026*) **What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files** [[📝 Paper](https://arxiv.org/abs/2608.08453)]  
  → This empirical study identifies specification, organization, and portability defects that prevent public SKILL.md artifacts from being reused effectively.

<!-- paper:destefanis2026gitskills -->
- (*2026*) **GitSkills: A Dataset of Agent Skills on GitHub** [[📝 Paper](https://arxiv.org/abs/2608.10906)] [[📦 Data](https://huggingface.co/datasets/mvaccargiu/gitskills)]  
  → GitSkills collects public GitHub skill artifacts to support empirical study of skill structure, distribution, and maintenance.

<a id="evaluation-metrics-safety"></a>

#### Safety

<!-- paper:c54 -->
- (*2026*) **Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2607.13987)]  
  → SkillSec-Eval organizes threats and evaluates security across skill admission, retrieval, planning, execution, and evolution.

<!-- paper:c40 -->
- (*2026*) **Behavioral Integrity Verification for AI Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.11770)]  
  → Behavioral Integrity Verification compares declared skill capabilities with behavior inferred from instructions and code to detect integrity violations.

<!-- paper:xhossain2026skillvetbench -->
- (*2026*) **SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.15899)]  
  → SkillVetBench evaluates LLM-based judges on multiple security-risk dimensions of open-source agent skill packages.

<!-- paper:xzhuang2026agenttrap -->
- (*2026*) **AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.13940)] [[💻 Code](https://github.com/zhmzm/AgentTrap)]  
  → AgentTrap evaluates runtime trust failures caused by third-party skills while tracking completion of legitimate tasks.

<!-- paper:xschmotz2026skillinject -->
- (*2026*) **Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks** [[📝 Paper](https://arxiv.org/abs/2602.20156)] [[💻 Code](https://github.com/aisa-group/skill-inject)]  
  → Skill-Inject evaluates agent vulnerability to malicious instructions embedded in skill files.

<!-- paper:e33 -->
- (*2025*) **Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections** [[📝 Paper](https://arxiv.org/abs/2510.26328)] [[💻 Code](https://github.com/aisa-group/promptinject-agent-skills)]  
  → This work demonstrates prompt-injection attacks embedded in skill instructions and associated scripts used by coding agents.

<!-- paper:xsaha2026under -->
- (*2026*) **Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry** [[📝 Paper](https://arxiv.org/abs/2605.11418)] [[💻 Code](https://github.com/ShoumikSaha/agent-skill-security)]  
  → This study examines semantic supply-chain attacks that exploit skill descriptions and registry content to influence agent behavior.

<!-- paper:xqu2026supply -->
- (*2026*) **Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems** [[📝 Paper](https://arxiv.org/abs/2604.03081)]  
  → This work studies how poisoned skill supply chains can compromise coding agents when contaminated procedures are retrieved and executed.

<!-- paper:xchen2026how -->
- (*2026*) **How Your Credentials Are Leaked by LLM Agent Skills: An Empirical Study** [[📝 Paper](https://arxiv.org/abs/2604.03070)]  
  → This empirical study traces how instructions and code in agent skills expose credentials, informing security checks before skill reuse.

<!-- paper:xsui2026elasticback -->
- (*2026*) **ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization** [[📝 Paper](https://arxiv.org/abs/2608.09577)]  
  → ElasticBack studies conditional backdoors in skill documents using jointly optimized triggers and behavioral rules.

<!-- paper:c55 -->
- (*2026*) **Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories** [[📝 Paper](https://arxiv.org/abs/2607.25560)] [[💻 Code](https://anonymous.4open.science/r/SigLeak-D1DB)]  
  → SigLeak reconstructs proprietary skill procedures from observable execution trajectories, exposing a behavioral channel for skill leakage.

<!-- paper:xhua2026behavioral -->
- (*2026*) **Behavioral Skill Reconstruction: Reconstructing Hidden Functionality from LLM Agent Skills** [[📝 Paper](https://arxiv.org/abs/2608.04192)]  
  → Behavioral Skill Reconstruction infers hidden skill functionality from observable agent responses and execution behavior.

<!-- paper:xshao2025your -->
- (*2026*) **Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents** [[📝 Paper](https://arxiv.org/abs/2509.26354)] [[💻 Code](https://github.com/ShaoShuai0605/Misevolution)]  
  → This study examines unsafe behavioral changes that can emerge when agents evolve their own skills and memories.

<!-- paper:xzhao2026safety -->
- (*2026*) **On Safety Risks in Experience-Driven Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2604.16968)]  
  → This study measures how experience-driven skill updates can weaken agent safety even when collected experience comes from benign tasks.

<a id="evaluation-benchmarks"></a>

### Benchmarks

<a id="evaluation-benchmarks-synthesis"></a>

#### Synthesis

<!-- paper:xzhou2026skillgenbench -->
- (*2026*) **SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.18693)] [[💻 Code](https://github.com/QuantaAlpha/SkillGenBench)]  
  → SkillGenBench evaluates skill-generation pipelines under controlled execution conditions and distinguishes task-conditioned synthesis from reusable library construction.

<!-- paper:c43 -->
- (*2026*) **SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks** [[📝 Paper](https://arxiv.org/abs/2604.20087)] [[💻 Code](https://github.com/cxcscmu/SkillLearnBench)]  
  → SkillLearnBench evaluates continual skill generation through complementary measures of skill quality, execution trajectories, and task outcomes.

<a id="evaluation-benchmarks-utilization"></a>

#### Utilization

<!-- paper:e31 -->
- (*2026*) **SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks** [[📝 Paper](https://arxiv.org/abs/2602.12670)] [[💻 Code](https://github.com/benchflow-ai/skillsbench)] [[🌐 Project](https://www.skillsbench.ai/)]  
  → SkillsBench evaluates how supplied and generated skills affect agent performance across diverse tasks under controlled execution settings.

<!-- paper:c53 -->
- (*2026*) **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** [[📝 Paper](https://arxiv.org/abs/2603.15401)] [[📦 Data](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)]  
  → SWE-Skills-Bench compares software-engineering agents with and without supplied skills on real repository tasks.

<!-- paper:xcho2026skillret -->
- (*2026*) **SkillRet: A Large-Scale Benchmark for Skill Retrieval in LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.05726)] [[💻 Code](https://github.com/ThakiCloud/SKILLRET)]  
  → SkillRet benchmarks retrieval of relevant skills from a large collection of procedural resources for LLM agents.

<!-- paper:c47 -->
- (*2026*) **SkillRouter: Skill Routing for LLM Agents at Scale** [[📝 Paper](https://arxiv.org/abs/2603.22455)]  
  → SkillRouter studies scalable routing from task requests to reusable agent skills and measures retrieval and execution performance.

<!-- paper:c42 -->
- (*2026*) **How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings** [[📝 Paper](https://arxiv.org/abs/2604.04323)] [[💻 Code](https://github.com/UCSB-NLP-Chang/Skill-Usage)]  
  → The Skill-Usage study evaluates autonomous skill discovery, loading, and execution under realistic access to a large skill collection.

<!-- paper:c48 -->
- (*2026*) **Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale** [[📝 Paper](https://arxiv.org/abs/2603.02176)] [[💻 Code](https://github.com/ynulihao/AgentSkillOS)]  
  → AgentSkillOS organizes skills in a capability tree and retrieves and orchestrates them through dependency-aware task pipelines.

<!-- paper:xchen2026slbench -->
- (*2026*) **SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills** [[📝 Paper](https://arxiv.org/abs/2607.09016)]  
  → SLBench measures whether agents obey logical relationships and constraints encoded in reusable skill procedures.

<a id="evaluation-benchmarks-evolution"></a>

#### Evolution

<!-- paper:c44 -->
- (*2026*) **SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents** [[📝 Paper](https://arxiv.org/abs/2604.17308)] [[💻 Code](https://github.com/ZhangZi-a/SkillFlow)]  
  → SkillFlow evaluates lifelong skill discovery and evolution by carrying an agent's revised library across sequences of related tasks.

<!-- paper:xlei2026skillevolbench -->
- (*2026*) **SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills** [[📝 Paper](https://arxiv.org/abs/2605.24117)]  
  → SkillEvolBench separates experience acquisition from held-out deployment to evaluate transfer and composition of synthesized procedural skills.

<!-- paper:xguan2026continualskillbench -->
- (*2026*) **ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?** [[📝 Paper](https://arxiv.org/abs/2608.03874)] [[💻 Code](https://github.com/gtynnn060110-hash/continual-skill-bench-final)]  
  → ContinualSkillBench evaluates whether maintained skills improve capabilities beyond continued access to accumulated task experience.

<!-- paper:xnguyen2026recursive -->
- (*2026*) **Recursive Self-Evolving Agents via Held-Out Selection** [[📝 Paper](https://arxiv.org/abs/2606.28374)]  
  → This framework uses held-out evaluation to select recursive skill updates and measure their transfer beyond the experience used for revision.

<!-- paper:xyang2026federatedskill -->
- (*2026*) **FederatedSkill: Federated Learning for Agentic Skill Evolution** [[📝 Paper](https://arxiv.org/abs/2606.03143)] [[💻 Code](https://github.com/UCSB-NLP-Chang/FederatedSkill)]  
  → FederatedSkill shares and evolves procedural skills across distributed agents while evaluating transfer across deployment sites.

<!-- paper:xouyang2026skillos -->
- (*2026*) **SkillOS: Learning Skill Curation for Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2605.06614)]  
  → SkillOS learns to insert, update, and delete library entries according to their effect on future agent performance.

<a id="evaluation-benchmarks-security"></a>

#### Security

<!-- paper:c40 -->
- (*2026*) **Behavioral Integrity Verification for AI Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.11770)]  
  → Behavioral Integrity Verification compares declared skill capabilities with behavior inferred from instructions and code to detect integrity violations.

<!-- paper:xkim2026skillmutator -->
- (*2026*) **SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.14154)] [[💻 Code](https://anonymous.4open.science/r/SkillMutator-B200)]  
  → SkillMutator benchmarks coordinated attacks across skill instructions and code and evaluates defenses against these cross-modal threats.

<!-- paper:xhossain2026skillvetbench -->
- (*2026*) **SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.15899)]  
  → SkillVetBench evaluates LLM-based judges on multiple security-risk dimensions of open-source agent skill packages.

<!-- paper:xliu2026maliciousskills -->
- (*2026*) **"Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild** [[📝 Paper](https://arxiv.org/abs/2602.06547)]  
  → This study audits malicious public skill packages and characterizes attacks carried by their instructions, code, and supporting resources.

<!-- paper:xzhuang2026agenttrap -->
- (*2026*) **AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.13940)] [[💻 Code](https://github.com/zhmzm/AgentTrap)]  
  → AgentTrap evaluates runtime trust failures caused by third-party skills while tracking completion of legitimate tasks.

<!-- paper:xschmotz2026skillinject -->
- (*2026*) **Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks** [[📝 Paper](https://arxiv.org/abs/2602.20156)] [[💻 Code](https://github.com/aisa-group/skill-inject)]  
  → Skill-Inject evaluates agent vulnerability to malicious instructions embedded in skill files.

<!-- paper:xjiang2026harmfulskillbench -->
- (*2026*) **HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?** [[📝 Paper](https://arxiv.org/abs/2604.15415)] [[💻 Code](https://github.com/TrustAIRLab/HarmfulSkillBench)]  
  → HarmfulSkillBench measures how installed harmful skills change an agent's behavior on unsafe requests.

[↑ Contents](#contents)

<a id="evolution"></a>

## 6. Skill Evolution

Skills and their libraries evolve through refinement, reorganization, migration, and reduction.

- **[Refinement](#evolution-refinement)**
- **[Reorganization](#evolution-reorganization)**
  - [Consolidation](#evolution-reorganization-consolidation)
  - [Specialization](#evolution-reorganization-specialization)
- **[Migration](#evolution-migration)**
- **[Reduction](#evolution-reduction)**

<a id="evolution-refinement"></a>

### Refinement

<!-- paper:e12 -->
- (*2025*) **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[📝 Paper](https://arxiv.org/abs/2504.07079)] [[💻 Code](https://github.com/OSU-NLP-Group/SkillWeaver)]  
  → SkillWeaver explores websites, synthesizes reusable APIs, and improves them through execution-based practice.

<!-- paper:c26 -->
- (*2026*) **SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision** [[📝 Paper](https://arxiv.org/abs/2606.01139)] [[💻 Code](https://github.com/HKUST-KnowComp/skillrevise)]  
  → SkillRevise uses execution traces to locate and revise weaknesses in LLM-authored skill instructions.

<!-- paper:c23 -->
- (*2026*) **ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents** [[📝 Paper](https://arxiv.org/abs/2603.20340)] [[💻 Code](https://github.com/underfitting-lu/contractskill)]  
  → ContractSkill turns web-agent skills into executable contracts that support verification, fault localization, and targeted procedural repairs.

<!-- paper:c30 -->
- (*2026*) **Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills** [[📝 Paper](https://arxiv.org/abs/2607.20999)] [[💻 Code](https://github.com/xiaolin9595/workflow-localized-mechanism-learning)]  
  → Workflow-localized mechanism learning attributes failures to specific workflow components and repairs structured skills using reusable mechanism knowledge.

<!-- paper:c03 -->
- (*2026*) **Memp: Exploring Agent Procedural Memory** [[📝 Paper](https://arxiv.org/abs/2508.06433)] [[💻 Code](https://github.com/zjunlp/MemP)]  
  → MEMP distills agent trajectories into procedural instructions and abstractions that are retrieved, revised, and maintained as experience accumulates.

<!-- paper:xcao2025remember -->
- (*2026*) **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** [[📝 Paper](https://arxiv.org/abs/2512.10696)] [[💻 Code](https://github.com/agentscope-ai/ReMe)]  
  → ReMe extracts, retrieves, and refines procedural memories from agent experience to support adaptation across tasks.

<!-- paper:lu2026skillsentry -->
- (*2026*) **SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance** [[📝 Paper](https://arxiv.org/abs/2608.09253)]  
  → SkillSentry checks skill steps and constraints during execution and returns targeted guidance when runtime behavior deviates from the procedure.

<!-- paper:c33 -->
- (*2026*) **Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.10990)]  
  → This work models skill drift as contract violations and supports proactive maintenance when dependencies or execution conditions change.

<!-- paper:c25 -->
- (*2026*) **SkillOpt: Executive Strategy for Self-Evolving Agent Skills** [[📝 Paper](https://arxiv.org/abs/2605.23904)] [[💻 Code](https://github.com/microsoft/SkillOpt)] [[🌐 Project](https://microsoft.github.io/SkillOpt/)]  
  → SkillOpt optimizes external skill documents through bounded edits generated from scored rollouts and selected using held-out validation.

<!-- paper:feng2026skillhex -->
- (*2026*) **SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation** [[📝 Paper](https://arxiv.org/abs/2608.05628)]  
  → SkillHEX generates hypotheses about skill failures and tests targeted revisions through autonomous exploration and exploitation.

<!-- paper:xmoll2026grasp -->
- (*2026*) **GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.29668)] [[💻 Code](https://github.com/jomoll/GRASP)]  
  → GRASP proposes skill revisions and gates acceptance with regression checks on previously successful and failed cases.

<!-- paper:xgautam2026skillaxe -->
- (*2026*) **SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement** [[📝 Paper](https://arxiv.org/abs/2606.10546)]  
  → SkillAxe uses evaluation feedback to guide iterative self-refinement of LLM-authored agent skills.

<!-- paper:xzhu2026skillcoach -->
- (*2026*) **SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use** [[📝 Paper](https://arxiv.org/abs/2607.01874)]  
  → SkillCoach evolves evaluation rubrics alongside agent skill use to provide targeted feedback for improvement.

<!-- paper:liu2026rethinking -->
- (*2026*) **Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds** [[📝 Paper](https://arxiv.org/abs/2608.02636)] [[💻 Code](https://github.com/HKUST-KnowComp/rethinkskill)]  
  → This study analyzes how feedback quality and repeated revision shape skill improvement and degradation over multiple evolution rounds.

<!-- paper:xwang2025alignevoskill -->
- (*2025*) **AlignEvoSkill: Towards Knowledge-Aware and Task-Aligned Agent Skill Evolution** [[📝 Paper](https://arxiv.org/abs/2506.23149)]  
  → AlignEvoSkill retrieves relevant knowledge and revises existing skills to address task-specific capability gaps.

<!-- paper:xwei2026elite -->
- (*2026*) **ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents** [[📝 Paper](https://arxiv.org/abs/2603.24018)]  
  → ELITE maintains and refines an experiential skill pool to support intent-aware transfer across embodied tasks.

<!-- paper:xzhang2026memskill -->
- (*2026*) **MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2602.02474)] [[💻 Code](https://github.com/ViktorAxelsen/MemSkill)]  
  → MemSkill learns reusable memory-construction procedures and revises them using feedback from failed memory operations.

<!-- paper:f37 -->
- (*2024*) **Offline Training of Language Model Agents with Functions as Learnable Weights** [[📝 Paper](https://arxiv.org/abs/2402.11359)] [[💻 Code](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentoptimizer.ipynb)]  
  → AgentOptimizer improves an agent by editing its external callable functions using task execution feedback.

<!-- paper:xwang2026self -->
- (*2026*) **Self-Evolving Embodied Agents via Skill-Harness Evolution** [[📝 Paper](https://arxiv.org/abs/2608.11350)]  
  → SHAPER jointly evolves embodied skills and their context-code harness using environment rollouts with frozen model parameters.

<!-- paper:e17 -->
- (*2026*) **SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems** [[📝 Paper](https://arxiv.org/abs/2606.01314)]  
  → SkillSmith co-evolves skills and the tools they call through coordinated proposals informed by execution traces and failure patterns.

<!-- paper:xwu2025evolver -->
- (*2025*) **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle** [[📝 Paper](https://arxiv.org/abs/2510.16079)] [[💻 Code](https://github.com/KnowledgeXLab/EvolveR)]  
  → EvolveR connects experience collection, procedural abstraction, execution, and revision in an experience-driven agent lifecycle.

<!-- paper:xlin2026muse -->
- (*2026*) **MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation** [[📝 Paper](https://arxiv.org/abs/2605.27366)]  
  → MUSE-Autoskill connects skill creation, memory, management, and evaluation in a continuous agent self-evolution process.

<!-- paper:xliu2026skillsvote -->
- (*2026*) **SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution** [[📝 Paper](https://arxiv.org/abs/2605.18401)] [[💻 Code](https://github.com/MemTensor/skills-vote)]  
  → SkillsVote governs the collection, recommendation, and evolution of reusable skills across their lifecycle.

<!-- paper:xxia2026harnessing -->
- (*2026*) **Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.20631)]  
  → This work identifies architectural patterns and a reference architecture for integrating skills into LLM-agent execution and maintenance.

<!-- paper:f42 -->
- (*2017*) **Gradient Episodic Memory for Continual Learning** [[📝 Paper](https://arxiv.org/abs/1706.08840)] [[💻 Code](https://github.com/facebookresearch/GradientEpisodicMemory)]  
  → Gradient Episodic Memory constrains learning with stored examples to retain previous capabilities during subsequent updates.

<!-- paper:f43 -->
- (*2018*) **Efficient Lifelong Learning with A-GEM** [[📝 Paper](https://arxiv.org/abs/1812.00420)] [[💻 Code](https://github.com/facebookresearch/agem)]  
  → A-GEM uses an averaged replay constraint to reduce forgetting during continual acquisition of new capabilities.

<!-- paper:f44 -->
- (*2018*) **Progress &amp; Compress: A scalable framework for continual learning** [[📝 Paper](https://arxiv.org/abs/1805.06370)]  
  → Progress and Compress alternates task acquisition and knowledge consolidation to retain capabilities in a bounded model.

<!-- paper:f45 -->
- (*2020*) **Dark Experience for General Continual Learning: a Strong, Simple Baseline** [[📝 Paper](https://arxiv.org/abs/2004.07211)] [[💻 Code](https://github.com/aimagelab/mammoth)]  
  → Dark Experience Replay combines replayed examples and previous model outputs to preserve learned behavior during continual updates.

<!-- paper:xyu2026do -->
- (*2026*) **Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation** [[📝 Paper](https://arxiv.org/abs/2605.09315)]  
  → This study measures degradation of previously acquired capabilities during skill, workflow, memory, and model updates in self-evolving agents.

<a id="evolution-reorganization"></a>

### Reorganization

<a id="evolution-reorganization-consolidation"></a>

#### Consolidation

<!-- paper:xli2026skillgraph -->
- (*2026*) **SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs** [[📝 Paper](https://arxiv.org/abs/2605.12039)]  
  → SkillGraph evolves a graph of reusable skills through reinforcement learning, including merging, splitting, and deprecating skill nodes.

<!-- paper:yang2026gse -->
- (*2026*) **Learning Globally Reusable Skills for Coding Agents** [[📝 Paper](https://arxiv.org/abs/2608.06153)]  
  → GSE clusters local coding-agent improvement proposals into shared skill abstractions and checks them against historical task experience.

<!-- paper:f07 -->
- (*2018*) **Learning Libraries of Subroutines for Neurally-Guided Bayesian Program Induction** [[📝 Paper](https://people.csail.mit.edu/asolar/papers/EllisMSST18.pdf)]  
  → This library-learning method discovers reusable subroutines while training a neural guide to search programs expressed in the evolving library.

<!-- paper:f08 -->
- (*2021*) **DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning** [[📝 Paper](https://doi.org/10.1145/3453483.3454080)] [[💻 Code](https://github.com/ellisk42/ec)]  
  → DreamCoder alternates program synthesis and abstraction learning to grow a library of reusable computational concepts.

<!-- paper:f09 -->
- (*2023*) **Top-Down Synthesis for Library Learning** [[📝 Paper](http://dx.doi.org/10.1145/3571234)] [[💻 Code](https://github.com/mlb2251/stitch)]  
  → Top-down library learning discovers reusable program abstractions by searching over candidate library functions and their compressive value.

<!-- paper:f10 -->
- (*2024*) **LILO: Learning Interpretable Libraries by Compressing and Documenting Code** [[📝 Paper](https://arxiv.org/abs/2310.19791)] [[💻 Code](https://github.com/gabegrand/lilo)]  
  → LILO compresses synthesized programs into reusable library functions and documents the abstractions with natural language.

<!-- paper:f11 -->
- (*2024*) **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** [[📝 Paper](https://arxiv.org/abs/2401.16467)] [[💻 Code](https://github.com/esteng/regal_program_learning)]  
  → ReGAL refactors task programs into shared abstractions that can be reused during subsequent program generation.

<a id="evolution-reorganization-specialization"></a>

#### Specialization

<!-- paper:xli2026skillgraph -->
- (*2026*) **SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs** [[📝 Paper](https://arxiv.org/abs/2605.12039)]  
  → SkillGraph evolves a graph of reusable skills through reinforcement learning, including merging, splitting, and deprecating skill nodes.

<!-- paper:c49 -->
- (*2026*) **PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction** [[📝 Paper](https://arxiv.org/abs/2510.15863)] [[💻 Code](https://github.com/simonucl/PolySkill)]  
  → PolySkill separates a skill's abstract goal from site-specific implementations to support compositional reuse and continual web-agent learning.

<!-- paper:e17 -->
- (*2026*) **SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems** [[📝 Paper](https://arxiv.org/abs/2606.01314)]  
  → SkillSmith co-evolves skills and the tools they call through coordinated proposals informed by execution traces and failure patterns.

<a id="evolution-migration"></a>

### Migration

<!-- paper:xblumenfeld2026aip -->
- (*2026*) **AIP: A Graph Representation for Learning and Governing Agent Skills** [[📝 Paper](https://arxiv.org/abs/2606.04781)] [[💻 Code](https://github.com/zach-blumenfeld/aip-skillbench)]  
  → AIP represents skills as typed execution graphs with procedural descriptions and executable nodes for learning and governance.

<!-- paper:xli2026skill -->
- (*2026*) **Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.27955)] [[💻 Code](https://github.com/InternLM/Skill-as-Pseudocode)]  
  → Skill-as-Pseudocode converts skill documents into typed contracts and explicit action templates for more structured agent execution.

<!-- paper:e28 -->
- (*2026*) **SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces** [[📝 Paper](https://arxiv.org/abs/2605.15215)] [[💻 Code](https://github.com/AetherHeart-AI/Aeloon)]  
  → Boundary-guided SkillSmith compiles skill packages into minimal runtime interfaces that expose the operations needed for execution.

<!-- paper:c17 -->
- (*2026*) **SIGIL: Skill Compilation for Reliable and Efficient Agent Execution** [[📝 Paper](https://arxiv.org/abs/2607.27309)]  
  → SIGIL translates authored skills into a validated typed intermediate representation and generates executable harnesses that enforce prescribed procedures.

<!-- paper:e30 -->
- (*2026*) **SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents** [[📝 Paper](https://arxiv.org/abs/2605.03353)] [[💻 Code](https://github.com/Nexa-Language/Skill-Compiler)]  
  → SkCC uses a typed intermediate representation to compile portable skill artifacts and check cross-framework execution constraints.

<!-- paper:c56 -->
- (*2026*) **Parametric Skills** [[📝 Paper](https://arxiv.org/abs/2606.30015)]  
  → Parametric Skills uses a hypernetwork to convert textual skills into LoRA adapters for context-free procedural reuse.

<!-- paper:c57 -->
- (*2026*) **Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents** [[📝 Paper](https://arxiv.org/abs/2606.16769)]  
  → Skill-to-LoRA synthesizes demonstrations from skill documents and trains skill-specific adapters that replace repeated runtime instruction loading.

<!-- paper:han2026kvskill -->
- (*2026*) **KV-Skill: Forging Expertise in the Model's Native Language** [[📝 Paper](https://arxiv.org/abs/2608.05475)] [[💻 Code](https://github.com/shawnzhg/KV-Skill)]  
  → KV-Skill converts expertise into external latent operators accessed through a model-side interface during inference.

<!-- paper:xwu2025tokmem -->
- (*2026*) **TokMem: One-Token Procedural Memory for Large Language Models** [[📝 Paper](https://arxiv.org/abs/2510.00444)] [[💻 Code](https://github.com/MANGA-UOFA/TokMem)]  
  → TokMem distills procedural instructions into trainable memory tokens that activate reusable behavior in a frozen language model.

<a id="evolution-reduction"></a>

### Reduction

<!-- paper:c34 -->
- (*2026*) **SkillReducer: Optimizing LLM Agent Skills for Token Efficiency** [[📝 Paper](https://arxiv.org/abs/2603.29919)]  
  → SkillReducer compresses skill instructions to reduce context costs while preserving the information needed to select and execute the procedure.

<!-- paper:xyuan2026clawtrace -->
- (*2026*) **ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation** [[📝 Paper](https://arxiv.org/abs/2604.23853)] [[💻 Code](https://github.com/epsilla-cloud/clawtrace)]  
  → ClawTrace attributes execution costs to skill components and converts traces into preservation, pruning, and repair proposals.

<!-- paper:c09 -->
- (*2026*) **Dynamic Dual-Granularity Skill Bank for Agentic RL** [[📝 Paper](https://arxiv.org/abs/2603.28716)] [[💻 Code](https://github.com/TU2021/D2Skill-AgenticRL)]  
  → D2Skill maintains a dual-granularity skill bank and uses utility signals to select, update, and prune skills during agentic reinforcement learning.

<!-- paper:c04 -->
- (*2026*) **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** [[📝 Paper](https://arxiv.org/abs/2602.01869)] [[💻 Code](https://github.com/Miracle1207/Skill-Pro)]  
  → Skill-Pro learns reusable skills from execution experience with non-parametric PPO and manages their contribution to a bounded skill library.

<!-- paper:e29 -->
- (*2026*) **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems** [[📝 Paper](https://arxiv.org/abs/2605.13716)] [[💻 Code](https://github.com/Hik289/SkillOps)]  
  → SkillOps maintains skill libraries using typed contracts, dependency relationships, utility assessment, and lifecycle operations.

<!-- paper:xouyang2026skillos -->
- (*2026*) **SkillOS: Learning Skill Curation for Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2605.06614)]  
  → SkillOS learns to insert, update, and delete library entries according to their effect on future agent performance.

<!-- paper:xli2026skillgraph -->
- (*2026*) **SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs** [[📝 Paper](https://arxiv.org/abs/2605.12039)]  
  → SkillGraph evolves a graph of reusable skills through reinforcement learning, including merging, splitting, and deprecating skill nodes.

<!-- paper:c35 -->
- (*2026*) **Skillware: A Software Ontology and Engineering Lifecycle for Persistent Behavioral Artifacts** [[📝 Paper](https://arxiv.org/abs/2607.18970)] [[💻 Code](https://github.com/MetaInFLow/skillware-patterns)]  
  → Skillware treats persistent skills as software artifacts with explicit interfaces, versions, dependencies, and lifecycle operations.

<!-- paper:xzhang2026blind -->
- (*2026*) **The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents** [[📝 Paper](https://arxiv.org/abs/2607.07436)]  
  → The Blind Curator analyzes how biased evaluation suppresses failure-based skill retirement in evolving libraries.

<!-- paper:xzhang2026library -->
- (*2026*) **Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.19576)] [[💻 Code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)]  
  → Library Drift diagnoses performance changes caused by interactions among evolving skill entries and proposes library-level repairs.

<!-- paper:xsong2026more -->
- (*2026*) **More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill Libraries** [[📝 Paper](https://arxiv.org/abs/2605.24050)]  
  → This study identifies skill shadowing, where expanding a library changes selection behavior and reduces the usefulness of existing skills.

<!-- paper:c45 -->
- (*2026*) **SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents** [[📝 Paper](https://arxiv.org/abs/2607.15557)] [[💻 Code](https://github.com/EverMind-AI/SkillCorpus)]  
  → SkillCorpus consolidates public skill packages and evaluates their organization, quality, and usefulness for real-world agents.

<!-- paper:zhang2026skillreuse -->
- (*2026*) **What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files** [[📝 Paper](https://arxiv.org/abs/2608.08453)]  
  → This empirical study identifies specification, organization, and portability defects that prevent public SKILL.md artifacts from being reused effectively.

<!-- paper:destefanis2026gitskills -->
- (*2026*) **GitSkills: A Dataset of Agent Skills on GitHub** [[📝 Paper](https://arxiv.org/abs/2608.10906)] [[📦 Data](https://huggingface.co/datasets/mvaccargiu/gitskills)]  
  → GitSkills collects public GitHub skill artifacts to support empirical study of skill structure, distribution, and maintenance.

[↑ Contents](#contents)

## Contributing

Contributions are welcome. Please provide the paper, its appropriate taxonomy category, a concise description of its role in skill synthesis or reuse, and an author-released implementation when available. See [MAINTENANCE.md](MAINTENANCE.md) for the update workflow.

## Acknowledgments

The catalogue format is inspired by [takeshiww/Awsome-Skill-Synthesis](https://github.com/takeshiww/Awsome-Skill-Synthesis). The categories and literature mappings follow the accompanying survey.

## License

This repository uses the [MIT License](LICENSE). Linked papers, datasets, and software retain their respective licenses.
