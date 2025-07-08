# Helix – Recruiting Assistant  
### SAGEBOT - THE FUTURE OF AI AGENTS

## Overview

**Helix** is an AI-powered recruiting assistant designed to streamline and elevate candidate outreach for busy recruiters at fast-growing companies. Built for the 2025 SAGEBOT Inaugural Hackathon, Helix leverages natural language generation and smart candidate management tools to help recruiters save time and maintain high standards in every candidate interaction.

## Key Features

- **Polished Outreach Drafts:**  
  Generates complete, human-sounding outreach messages tailored to each candidate and role, ready for quick review and minor edits.

- **Minimal Input, Maximum Output:**  
  Requires only essential details (role, qualities, candidate name, resume, or special notes) to craft compelling messages—no lengthy instructions needed.

- **Professional & Persuasive Tone:**  
  Ensures every message is warm, professional, and tailored to recruiting best practices.

- **Smart Candidate Management:**  
  Integrates with three core tools:
  1. **retrieve_candidate:** Fetches details for any existing candidate using their unique ID.
  2. **insert_candidate:** Adds new candidates with just a name and description.
  3. **delete_candidate:** Removes candidates from the system by ID.

- **Intent Awareness:**  
  Tracks recruiter intent to automate candidate management actions and message generation, reducing repetitive tasks.

- **Focused Communication:**  
  Keeps questions to a minimum, assumes sensible defaults, and clarifies only when necessary.

## How It Works

1. **Input:**  
   Recruiter provides minimal information about the role or candidate (e.g., “Reach out to Jane Smith for the Senior Data Scientist role”).

2. **Processing:**  
   - If candidate details are missing, Helix uses available tools to retrieve or insert candidate information as needed.
   - Generates a complete, grammatically correct outreach message draft, ready for recruiter review.

3. **Output:**  
   - Delivers a polished outreach draft, optionally confirming candidate actions (retrieval, insertion, deletion) as required.

## Example Usage

**Adding a New Candidate:**  
- Recruiter: “Add John Doe, Senior Backend Engineer, 7 years at SaaS startups.”  
- Helix:  
  - `insert_candidate(first_name='John', last_name='Doe', description='Senior Backend Engineer, 7 years at SaaS startups')`

**Retrieving Candidate Details:**  
- Recruiter: “Show me details for candidate ID 1023.”  
- Helix:  
  - “Sure, give me a second while I retrieve the information.”  
  - *(retrieves and displays candidate info)*

**Crafting Outreach:**  
- Recruiter: “Draft a message to Jane Smith for the Product Manager role. She’s detail-oriented and has fintech experience.”  
- Helix:  
  - *(Generates a complete, professional outreach message ready for review.)*

## Core Principles

- **Save Recruiters Time:**  
  Helix acts as a trusted extension of the recruiter, handling the heavy lifting while preserving intent and standards.

- **Maintain Professionalism:**  
  All communications are polished, persuasive, and tailored to the recruiting context.

- **Seamless Integration:**  
  Candidate management and messaging are unified in a single workflow, powered by simple, minimal inputs.

## Project Context

Helix was created for the **2025 SAGEBOT Inaugural STATE**, with a focus on AI-driven productivity in HR and talent acquisition. The project demonstrates how AI can empower recruiters to operate at scale without sacrificing personalization or quality.

## Getting Started

1. **Provide candidate or role details.**
2. **Review the outreach draft or candidate action confirmation.**
3. **Edit if needed, then send!**

*For more information or integration support, contact the Helix project team or refer to the API documentation.*
