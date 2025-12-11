# Design Document: Multi-Agent News Analyzer

## Project Overview
This project implements a three-agent system that fetches news articles, analyzes them using AI, and generates social media posts.

## Architecture

### Agent 1: News Fetcher (Non-AI Agent)
- **Purpose**: Fetch latest news articles based on keywords
- **Technology**: NewsAPI REST API
- **Input**: Keyword string (e.g., "artificial intelligence")
- **Output**: Article object containing:
  - `title`: Article headline
  - `content`: Article body text
  - `url`: Source URL
  - `source`: Publisher name
- **Communication**: Passes article data to Agent 2

### Agent 2: Article Analyzer (AI Agent)
- **Purpose**: Analyze article content using natural language processing
- **Technology**: OpenAI GPT-4
- **Input**: Article object from Agent 1
- **Output**: Analysis object containing:
  - `summary`: 2-3 sentence summary
  - `key_points`: List of 3-5 important points
  - `sentiment`: Overall sentiment (positive/negative/neutral)
- **Communication**: Passes analysis data to Agent 3

### Agent 3: Social Formatter (AI Agent)
- **Purpose**: Generate engaging social media posts
- **Technology**: OpenAI GPT-4
- **Input**: Analysis from Agent 2 + original article data
- **Output**: Formatted social media post (max 280 characters)
- **Communication**: Returns final output to orchestrator

## Data Flow Diagram