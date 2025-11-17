# ImageHive 🖼️

Modern, modular image management and organization system with AI-powered features.

## Overview

ImageHive is a FastAPI-based backend with a TypeScript React frontend, designed for efficient image scanning, deduplication, tagging, and management. The architecture is built for maximal modularity and extensibility through a plugin system.

## Features (Planned)

- 📁 **Recursive Image Scanning** - Scan directories for images
- 🖼️ **Thumbnail Generation** - Auto-generate and cache thumbnails
- 🔍 **Duplicate Detection** - Find and manage duplicate images
- 🏷️ **Smart Tagging** - AI-powered image description and tagging
- 🔌 **Plugin System** - Extensible architecture for custom functionality
- 🌐 **Modern Web UI** - React-based interface for browsing and managing images

## Project Structure

```
/
├── backend/                 # FastAPI backend
│   ├── app/                # Core application logic
│   ├── plugins/            # Plugin system for extensions
│   ├── tests/              # Backend tests
│   ├── main.py             # FastAPI application entry point
│   └── requirements.txt    # Python dependencies
├── frontend/               # TypeScript React frontend
│   ├── src/
│   │   ├── components/    # Reusable React components
│   │   ├── pages/         # Page components
│   │   └── App.tsx        # Main application component
│   ├── public/            # Static assets
│   └── package.json       # Node dependencies
├── README.md              # This file
├── .gitignore            # Git ignore rules
└── pyproject.toml        # Poetry configuration (optional)
```

## Getting Started

### Prerequisites

- Python 3.11.4
- Node.js 18 or higher
- npm or yarn

### Backend Setup

#### Configuration

1. Install Python 3.11.4 using pyenv (if not already installed):
    ```shell
    # macOS: install pyenv (Homebrew)
    brew update
    brew install pyenv
    
    # Install Python 3.11.4
    pyenv install 3.11.4
    pyenv local 3.11.4
    pyenv rehash
    eval "$(pyenv init -)"
    ```

2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the development server:
   ```bash
   python main.py
   ```

   The API will be available at `http://localhost:8000`
   - API documentation: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

### Running Both Services

For development, run both the backend and frontend in separate terminal windows:

```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## API Endpoints

The backend provides the following placeholder endpoints (ready for implementation):

- `GET /` - API health check
- `POST /scan?path={path}` - Scan directory for images
- `GET /thumbnails/{image_id}?size={size}` - Get image thumbnail
- `POST /deduplicate` - Find duplicate images
- `GET /tags` - List all tags
- `POST /tags/{image_id}?tag={tag}` - Add tag to image

## Development

### Backend Testing

```bash
cd backend
pytest tests/
```

### Frontend Build

```bash
cd frontend
npm run build
```

The production build will be in `frontend/dist/`

### Code Style

Backend uses Python best practices. Frontend uses TypeScript with ESLint.

```bash
# Frontend linting
cd frontend
npm run lint
```

## Using Poetry (Optional)

If you prefer using Poetry for Python dependency management:

```bash
cd backend
poetry install
poetry run python main.py
```

## Plugin System

The `backend/plugins/` directory is designed for extensible functionality. Add custom plugins for:

- Image processing algorithms
- AI/ML models for analysis
- Custom storage backends
- Additional tagging systems

## Next Steps

1. Implement recursive image scanning in the `/scan` endpoint
2. Add thumbnail generation and caching
3. Integrate duplicate detection algorithms
4. Build out the frontend gallery and file tree components
5. Add AI-powered image description
6. Implement plugin loading system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]
