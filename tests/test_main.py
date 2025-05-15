import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_create_short_url():
    # Use ASGITransport for FastAPI app
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/shorten", json={"original_url": "https://example.com"})
    assert response.status_code == 200  # Ensure the status code matches your app's response
    data = response.json()
    assert "short_code" in data
    assert data["original_url"] == "https://example.com"

@pytest.mark.asyncio
async def test_redirect_to_target_url():
    # First, create a shortened URL
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/shorten", json={"original_url": "https://example.com"})
        assert response.status_code == 200  # Ensure the status code matches your app's response
        short_code = response.json()["short_code"]

        # Then test redirect
        redirect_response = await ac.get(f"/{short_code}", follow_redirects=False)
        assert redirect_response.status_code in [301, 302, 307]  # Include 307 as valid
        assert redirect_response.headers["location"] == "https://example.com"