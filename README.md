# Business Listings Dashboard

A full-stack Business Listings Dashboard built using React.js, FastAPI (Python), SQLite(SQL), and dynamic chart visualizations.

## Features

- City-wise business count visualization
- Category-wise analytics
- Source-wise analytics
- Dynamic API integration
- SQLite database integration
- Interactive charts using Recharts

## Tech Stack

### Frontend
- React.js
- TypeScript
- Recharts

### Backend
- FastAPI
- Python
- SQLite

## APIs

- `/city-count`
- `/category-count`
- `/source-count`

## Database

SQLite database used for storing and querying 500+ generated business records.

## Setup Instructions

1. Install Python and required libraries
2. Run FastAPI backend using:
uvicorn main:app --reload
3. Open React frontend in CodeSandbox
4. APIs will connect with backend and display charts

## Challenges Faced

- Windows 7 compatibility limitations
- MySQL setup issues on legacy environment
- Cross-origin API integration between local backend and online frontend

## Scraping Approach

Due to scraping restrictions and local environment limitations, dynamically generated structured business listing data was used to simulate real business records for dashboard analytics.

## Project Flow

Database → FastAPI APIs → React Frontend → Charts Dashboard

## Author

Shruti Chaurasia
