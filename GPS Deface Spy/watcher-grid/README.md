# Website Defacement Detection — Frontend

## Overview

The frontend of the Website Defacement Detection System is a web application that helps users monitor websites, view website changes, identify potential defacement incidents, and manage security alerts through a user-friendly dashboard.

## Features

- **Dashboard:** View website monitoring information and security status.
- **Website Monitoring:** Manage monitored websites and view monitoring results.
- **Defacement Detection:** Display detected website changes and potential security incidents.
- **Security Alerts:** View alerts and incident details.
- **Incident Management:** Review and track reported website modifications.
- **Reports:** Access monitoring and detection reports.
- **Authentication:** User login and access to authorized application features.

## Technology Stack

- React.js
- TypeScript
- Vite
- Tailwind CSS
- HTML5
- CSS3
- JavaScript

## Project Structure

```text
watcher-grid/
├── public/
├── src/
├── index.html
├── package.json
├── package-lock.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

*The actual project structure may differ depending on the files present in the repository.*

## Prerequisites

- Node.js
- npm
- A modern web browser
- The backend API configured and running, if required

## Installation

Open a terminal in the `watcher-grid` directory and run:

```bash
npm install
```

## Environment Configuration

Configure the frontend environment variables according to the project's API setup.

For example, if the application uses a Vite API URL variable, configure the appropriate variable in a local `.env` file:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Use the actual API URL and variable name expected by the source code. Do not commit `.env` files or secrets to GitHub.

## Run the Development Server

```bash
npm run dev
```

Open the local URL printed in the terminal, usually:

```text
http://localhost:5173
```

## Build for Production

```bash
npm run build
```

To preview the production build locally, run:

```bash
npm run preview
```

## Backend Integration

The frontend communicates with the backend API to retrieve website monitoring data, detection results, security alerts, and incident information.

Ensure that the backend is running and that API endpoints, authentication settings, and CORS configuration match the frontend implementation.

## Security Best Practices

- Never expose passwords, API keys, access tokens, or other credentials.
- Keep environment-specific configuration out of version control.
- Validate API responses and handle errors appropriately.
- Use authenticated API requests for protected resources.

## Project Purpose

This frontend is part of a cybersecurity project designed to help identify unauthorized website modifications and improve website monitoring and incident response.
