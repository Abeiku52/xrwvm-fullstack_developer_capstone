# fullstack_developer_capstone

A comprehensive full-stack web application for a car dealership built with Django, React components, and modern web technologies.

## 🚀 Project Overview

**Project Name**: fullstack_developer_capstone

This is a capstone project for a national car retailer that provides a responsive web application allowing users to:
- Browse dealership branches across different states
- View and submit customer reviews
- Explore car inventory and dealer details
- Experience sentiment analysis on reviews
- Access both frontend and backend functionality

## 🛠 Technologies Used

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Python 3.11+** - Programming language

### Frontend
- **HTML5/CSS3** - Structure and styling
- **Bootstrap 5.1.3** - Responsive design
- **JavaScript (ES6+)** - Interactive functionality
- **React Components** - Dynamic UI elements

### DevOps & Deployment
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Cloud Run** - Deployment platform

## 📁 Project Structure

```
car-dealership/
├── server/                     # Django backend
│   ├── cars/                   # Cars app
│   ├── dealerships/            # Dealerships app
│   ├── reviews/                # Reviews app
│   ├── frontend/               # Frontend templates and static files
│   │   ├── static/             # HTML, CSS, JS files
│   │   └── templates/          # Django templates
│   └── manage.py               # Django management script
├── sentiment/                  # Sentiment analysis microservice
├── .github/workflows/          # CI/CD workflows
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abeiku52/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup database**
   ```bash
   cd server
   python manage.py migrate
   python manage.py loaddata fixtures/initial_data.json  # Load sample data
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API endpoints: http://127.0.0.1:8000/api/

## 🌐 API Endpoints

### Dealers
- `GET /api/dealers/` - List all dealers
- `GET /api/dealers/{id}/` - Get dealer details
- `GET /api/dealers/state/{state}/` - Get dealers by state

### Reviews
- `GET /api/reviews/{dealer_id}/` - Get reviews for a dealer
- `POST /api/reviews/{dealer_id}/submit/` - Submit a new review

### Cars
- `GET /api/cars/` - List all car makes and models

## 🎯 Key Features

### 1. Dealer Management
- Browse dealers by location
- Filter dealers by state
- View detailed dealer information
- Contact information and business hours

### 2. Review System
- Submit customer reviews with ratings
- Sentiment analysis on review text
- View aggregated dealer ratings
- Review moderation and display

### 3. User Authentication
- User registration and login
- Session management
- Protected review submission
- User profile management

### 4. Responsive Design
- Mobile-first approach
- Bootstrap-based UI
- Cross-browser compatibility
- Accessible design patterns

### 5. Sentiment Analysis
- Automatic sentiment detection
- Positive/Negative/Neutral classification
- Review quality indicators
- Dealer rating impact analysis

## 🧪 Testing

Run the test suite:
```bash
cd server
python manage.py test
```

## 🚀 Deployment

The application is configured for deployment on Google Cloud Run:

1. **Build Docker image**
   ```bash
   docker build -t car-dealership .
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy car-dealership --source .
   ```

3. **Access deployed application**
   - Live URL: https://car-dealership-abc123-uc.a.run.app

## 📊 CI/CD Pipeline

The project includes GitHub Actions workflows for:
- Automated testing on multiple Python versions
- Code quality checks with flake8
- Automated deployment to production
- Database migrations
- Security scanning

## 🎨 Screenshots & Demo

### Main Features
- **Homepage**: Browse all dealers with filtering options
- **Dealer Details**: Complete dealer information with reviews
- **Review Submission**: Interactive form with rating system
- **User Dashboard**: Personalized experience for logged-in users

### Admin Features
- **Django Admin**: Full CRUD operations for all models
- **Review Management**: Moderate and manage customer reviews
- **User Management**: Handle user accounts and permissions

## 🤝 Contributing

This is a capstone project, but contributions are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of a capstone program and is for educational purposes.

## 👨‍💻 Author

**Abeiku52**
- GitHub: [@Abeiku52](https://github.com/Abeiku52)
- Project: xrwvm-fullstack_developer_capstone
- Repository: https://github.com/Abeiku52/xrwvm-fullstack_developer_capstone

## 🙏 Acknowledgments

- Full-stack development capstone program
- Django and React communities
- Bootstrap team for the UI framework
- All contributors and reviewers

---

**Note**: This project demonstrates full-stack development skills including backend API development, frontend design, database management, user authentication, CI/CD implementation, and cloud deployment.