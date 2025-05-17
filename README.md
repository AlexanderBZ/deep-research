# Deep Research

A multi-agent AI research system that transforms user queries into structured research reports.

---

## Overview

**Deep Research** is a FastAPI-based application that uses a multi-agent approach to perform comprehensive research on user queries. The system consists of three specialized agents:

1. **Planner Agent**: Transforms user queries into structured research plans
2. **Researcher Agent**: Executes research tasks using web search tools
3. **Synthesizer Agent**: Compiles findings into a cohesive final report

---

## Features

- REST API for submitting research queries
- Multi-agent architecture for specialized task handling
- Integration with OpenAI's GPT models
- Web search capabilities via Tavily API
- Docker support for easy deployment

---

## Tech Stack

- Python 3.9+
- FastAPI
- LangChain & LangGraph
- OpenAI API
- Tavily Search API
- Poetry for dependency management
- Docker & Docker Compose

---

## Installation

### Prerequisites

- Python 3.9 or higher
- Poetry
- Docker & Docker Compose (optional)

### Local Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd deep-research
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Create a `.env` file with your API keys:

   ```env
   openai_api_key=your_openai_api_key
   tavily_api_key=your_tavily_api_key
   ```

4. Run the application:

   ```bash
   poetry run uvicorn src.main:app --host 0.0.0.0
   ```

---

### Docker Setup

1. Build and run with Docker Compose:

   ```bash
   docker-compose up --build
   ```

---

## API Usage

### Health Check

**GET** `/health`

**Response:**

```json
{
  "message": "running..."
}
```

---

### Submit Research Query

**POST** `/research`

**Request Body:**

```json
{
  "query": "What are the latest advancements in quantum computing?"
}
```

**Response:**

```json
{
  "plan": "...",
  "research": "...",
  "final_report": "...",
  "messages": [...]
}
```

---

## Project Structure

```
deep-research/
├── src/
│   ├── agents/        # Multi-agent system components
│   ├── api/           # FastAPI routes and schemas
│   ├── core/          # Core configuration and logic
│   ├── prompts/       # Agent prompt templates
│   ├── tools/         # Research tools
│   ├── utils/         # Utility functions
│   └── main.py        # Application entry point
├── tests/             # Test suite
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── pyproject.toml     # Poetry dependencies
└── README.md          # This file
```

---

## License

\[License information]

---

## Contributors

- Alexander Zwerner
