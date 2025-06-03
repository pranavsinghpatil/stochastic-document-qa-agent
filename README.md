# Stochastic Document QA Agent

A lightweight Document Question Answering AI Agent that enables natural language queries over documents using state-of-the-art language models.

## Features

- **Document Processing**: Extract and process text from PDFs and other document formats
- **Efficient Chunking**: Smart text splitting for optimal context management
- **RESTful API**: Easy integration with web applications
- **Scalable Architecture**: Modular design for easy extension
- **Enterprise Ready**: Built with security and scalability in mind

## Project Structure

```
/stochastic-document-qa-agent
├── data/                 # Sample PDFs and test files
├── ingestion/            # Code for parsing and structuring documents
│   ├── pdf_loader.py
│   └── text_extractor.py
├── qa_interface/         # Code for user interface and API endpoints
│   ├── main.py
│   └── api_utils.py
├── utils/                # Utility functions
├── tests/                # Unit tests
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stochastic-document-qa-agent.git
   cd stochastic-document-qa-agent
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the API server:
   ```bash
   cd qa_interface
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`

3. Try it out:
   ```bash
   curl "http://localhost:8000/ask?question=What%20is%20this%20document%20about?"
   ```

## API Documentation

Once the server is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Testing

Run the test suite with:

```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
