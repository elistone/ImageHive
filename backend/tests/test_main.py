"""
ImageHive Tests
Test suite for backend functionality.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns correct information."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "ImageHive API"
    assert data["status"] == "running"
    assert "version" in data


def test_scan_endpoint():
    """Test the scan endpoint placeholder."""
    response = client.post("/scan?path=/test/path")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_implemented"
    assert data["path"] == "/test/path"


def test_thumbnails_endpoint():
    """Test the thumbnails endpoint placeholder."""
    response = client.get("/thumbnails/test123")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_implemented"
    assert data["image_id"] == "test123"


def test_deduplicate_endpoint():
    """Test the deduplicate endpoint placeholder."""
    response = client.post("/deduplicate")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_implemented"


def test_tags_get_endpoint():
    """Test the tags GET endpoint placeholder."""
    response = client.get("/tags")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_implemented"


def test_tags_post_endpoint():
    """Test the tags POST endpoint placeholder."""
    response = client.post("/tags/test123?tag=nature")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_implemented"
    assert data["image_id"] == "test123"
    assert data["tag"] == "nature"
