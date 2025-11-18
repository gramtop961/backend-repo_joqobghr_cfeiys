"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Event planning app schemas

class Event(BaseModel):
    """
    Event collection schema
    Collection name: "event"
    """
    title: str = Field(..., min_length=3, max_length=120, description="Event title")
    description: Optional[str] = Field(None, max_length=2000, description="Event description")
    date: datetime = Field(..., description="Event date and time (ISO 8601)")
    location: str = Field(..., min_length=2, max_length=200, description="Event location")
    organizer: Optional[str] = Field(None, max_length=120, description="Organizer name")
    capacity: Optional[int] = Field(None, ge=1, description="Max attendees if limited")

class RSVP(BaseModel):
    """
    RSVP collection schema
    Collection name: "rsvp"
    """
    event_id: str = Field(..., description="Related event ID")
    name: str = Field(..., min_length=2, max_length=120, description="Attendee name")
    email: EmailStr = Field(..., description="Attendee email")
    guests: int = Field(1, ge=1, le=10, description="Number of guests including self")
    message: Optional[str] = Field(None, max_length=500, description="Optional note")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
