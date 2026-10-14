# 🛡️ Website Defacement Detection Using Image and Text Recognition

### A Web-Based Cybersecurity System for Website Monitoring and Unauthorized Change Detection

## 📌 Project Overview

Website Defacement Detection Using Image and Text Recognition is a web-based cybersecurity project designed to monitor websites and detect suspicious or unauthorized modifications to their visual appearance and textual content.

The system captures website snapshots, compares the current website state with a previously stored baseline, and identifies potential changes using image and text comparison techniques. It provides a centralized interface for website monitoring, detection results, security alerts, incident management, and reporting.

The primary objective is to help website owners identify unexpected website modifications and respond to potential defacement incidents more effectively.

## 🎯 Project Objectives

- Monitor configured websites for unexpected changes.
- Capture website screenshots and content snapshots.
- Compare website images to identify visual differences.
- Extract and compare website text content to identify textual changes.
- Detect potential website defacement incidents.
- Generate security alerts when configured detection conditions are met.
- Maintain monitoring information and incident records.
- Provide a user-friendly dashboard for monitoring and reporting.

## ✨ Key Features

### 1. User and Access Management
- User authentication and protected application access.
- JWT-based authentication using the configured authentication components.
- Access to website monitoring and management features.

### 2. Website Monitoring and Snapshot Management
- Register and manage websites for monitoring.
- Fetch website content through HTTP requests.
- Capture website screenshots using browser automation.
- Store baseline and current snapshots for comparison.
- Schedule monitoring tasks using APScheduler.

### 3. Image Comparison and Defacement Detection
- Compare website screenshots against baseline images.
- Process images using OpenCV, Pillow, and NumPy.
- Identify visual differences between website snapshots.
- Evaluate image changes to help identify potential defacement.

### 4. Text Content Comparison
- Extract textual content from website HTML.
- Compare the current text content with previously stored content.
- Identify additions, removals, and modifications in website text.
- Use text changes as an additional signal for detecting suspicious modifications.

### 5. Security Alerts and Incident Management
- Present detected website changes to users.
- Maintain incident information for review.
- Support security alert workflows, including configured email notifications.
- Provide relevant information to help users investigate potential incidents.

### 6. Dashboard and Reporting
- Display website monitoring information and detection results.
- Provide access to incident and alert details.
- Organize monitoring records for review and reporting.
- Support centralized management of monitored websites.

### 7. System Configuration and Control
- Manage application settings and monitoring configurations.
- Configure website monitoring and detection workflows.
- Maintain application records required for monitoring and incident management.

## 🏗️ System Workflow

1. **Website Registration:** The user adds a website to the monitoring system.
2. **Initial Snapshot:** The system captures the website's initial screenshot and textual content as a baseline.
3. **Scheduled Monitoring:** The monitoring component periodically fetches the website and captures updated snapshots.
4. **Image Analysis:** The current screenshot is compared with the baseline image to identify visual differences.
5. **Text Analysis:** Extracted website text is compared with the previously stored textual content.
6. **Change Evaluation:** The detected differences are evaluated according to the application's detection logic.
7. **Alert and Incident Handling:** Potentially suspicious changes are recorded and presented through the configured alert workflow.
8. **Dashboard and Reporting:** Users review monitoring results, alerts, and incident information.

## 🧰 Technology Stack

### Frontend
- **React.js** — Building the user interface.
- **TypeScript** — Type-safe application development.
- **Tailwind CSS** — Styling and responsive layouts.
- **HTML5 and CSS3** — Web interface structure and presentation.

### Backend
- **Python** — Core application and monitoring logic.
- **Django** — Backend web framework.
- **Django REST Framework** — REST API development.
- **SimpleJWT** — JWT authentication integration.

### Website Monitoring and Automation
- **Playwright** — Browser automation and website screenshot capture.
- **curl_cffi** — HTTP request handling where configured.
- **APScheduler** — Scheduling periodic monitoring tasks.

### Image Processing and Analysis
- **OpenCV** — Image processing and comparison.
- **Pillow** — Image loading and manipulation.
- **NumPy** — Numerical operations on image data.

### Database and Development Tools
- **SQLite** — Application data storage.
- **Git** — Version control.
- **GitHub** — Source code hosting and project collaboration.
- **Visual Studio Code** — Development environment.

## 🗂️ Project Modules

| Module | Responsibility |
|---|---|
| User and Access Management | Authentication and protected access |
| Website Monitoring and Snapshot Module | Website fetching, screenshot capture, and snapshot management |
| Analysis and Detection Module | Image and text comparison and change evaluation |
| Incident and Alert Management Module | Incident records and configured security alerts |
| Reporting and System Control Module | Monitoring results, reporting, and configuration |

## 📁 Project Structure

The repository contains the frontend and backend components. The following is a simplified representation; the exact internal files may differ.

```text
Website-Defacement/
├── backend/
│   ├── Django application
│   ├── REST API
│   ├── Monitoring and analysis logic
│   └── Configuration and dependencies
├── watcher-grid/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

Install the following tools before running the application:

- Python
- Node.js and npm
- Git
- A modern web browser

### 1. Clone the Repository

```bash
git clone https://github.com/pragadesh2434/Website-Defacement.git
cd Website-Defacement
```

### 2. Configure the Backend

Open a terminal in the backend directory:

```bash
cd backend
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies if `requirements.txt` is present:

```bash
pip install -r requirements.txt
```

If the Django `manage.py` file is present in this directory, apply the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Follow the actual project configuration if the Django application or dependency file is located elsewhere.

### 3. Configure the Frontend

Open another terminal:

```bash
cd watcher-grid
npm install
npm run dev
```

Open the local URL displayed in the terminal to access the frontend.

### 4. Configure the Application

- Configure the frontend API URL according to the backend settings.
- Set the required environment variables.
- Configure the database and authentication settings.
- Configure monitoring intervals and website settings as supported by the application.
- Configure email settings if email alerts are enabled.

Refer to the actual configuration files for the correct variable names and values.

## 🔍 Image and Text Analysis

### Image Analysis

Website screenshots are processed and compared to identify visual changes between the baseline and current snapshots. OpenCV, Pillow, and NumPy support image processing and numerical comparison operations.

### Text Analysis

Textual content is extracted from website HTML and compared with previously stored content. This helps identify changes in page text, including inserted, removed, or modified content.

Image and text differences are indicators of potential modifications; not every change necessarily represents a malicious defacement.

## 🔐 Security Considerations

- Do not commit passwords, API keys, access tokens, or secret configuration files.
- Keep environment-specific settings out of version control.
- Protect API endpoints with appropriate authentication and authorization.
- Use secure configuration for email notifications.
- Review detected changes before classifying an incident as confirmed defacement.
- Monitor only websites that you own or are authorized to test.

## 🚀 Future Enhancements

- More advanced visual similarity analysis.
- Improved text-change classification.
- Configurable detection thresholds.
- Additional notification channels.
- Enhanced monitoring history and analytics.
- More detailed incident reporting.
- Automated testing and deployment.

## 🎓 Project Outcome

This project demonstrates the application of web development, browser automation, image processing, text comparison, scheduled monitoring, REST API development, authentication, and database management to a practical cybersecurity problem.

By combining image and textual change analysis, the system aims to help users identify suspicious website modifications and manage potential defacement incidents through a centralized application.

## 👨‍💻 Developer

**Pragadesh**

GitHub: [@pragadesh2434](https://github.com/pragadesh2434)

**Project Title:** Website Defacement Detection Using Image and Text Recognition

---

*Developed as a cybersecurity project focused on website monitoring, change detection, and incident management.*
