"""
ImageHive Backend - FastAPI Application
Main entry point for the ImageHive API server.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ImageHive API",
    description="API for image scanning, deduplication, tagging, and management",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API health check."""
    return {
        "name": "ImageHive API",
        "version": "0.1.0",
        "status": "running",
    }


@app.post("/scan")
async def scan_images(path: str):
    """
    Scan a directory recursively for images.
    
    Args:
        path: Directory path to scan for images
        
    Returns:
        List of discovered image files
    """
    return {
        "status": "not_implemented",
        "message": "Image scanning endpoint - to be implemented",
        "path": path,
    }


@app.get("/thumbnails/{image_id}")
async def get_thumbnail(image_id: str, size: int = 200):
    """
    Get thumbnail for a specific image.
    
    Args:
        image_id: Unique identifier for the image
        size: Thumbnail size in pixels (default: 200)
        
    Returns:
        Thumbnail image
    """
    return {
        "status": "not_implemented",
        "message": "Thumbnail generation endpoint - to be implemented",
        "image_id": image_id,
        "size": size,
    }


@app.post("/deduplicate")
async def deduplicate_images():
    """
    Find and report duplicate images.
    
    Returns:
        List of duplicate image groups
    """
    return {
        "status": "not_implemented",
        "message": "Deduplication endpoint - to be implemented",
    }


@app.get("/tags")
async def get_tags():
    """
    Get all available image tags.
    
    Returns:
        List of tags
    """
    return {
        "status": "not_implemented",
        "message": "Tags listing endpoint - to be implemented",
    }


@app.post("/tags/{image_id}")
async def add_tag(image_id: str, tag: str):
    """
    Add a tag to an image.
    
    Args:
        image_id: Unique identifier for the image
        tag: Tag to add to the image
        
    Returns:
        Updated tag list for the image
    """
    return {
        "status": "not_implemented",
        "message": "Tag addition endpoint - to be implemented",
        "image_id": image_id,
        "tag": tag,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
