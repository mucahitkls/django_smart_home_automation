# Smart Home Automation System

This project is a Django-based web application designed to manage a smart home automation system. It allows users to create and manage their houses, rooms within those houses, and various smart devices within each room. The project is currently under active development.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles. User authentication ensures data privacy and security.
- **House Management**: Users can add, update, and delete houses.
- **Room Management**: Within each house, users can add, update, and delete rooms.
- **Device Management**: Users can add smart devices to rooms, update their attributes, and remove them. Supported devices include lights, TVs, thermostats, and doors.
- **Dynamic Device Forms**: The application dynamically displays relevant form fields based on the selected device type for streamlined user experience.

## Technologies Used

- **Django**: The project is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django's powerful features like ORM, authentication, and template engine are extensively utilized.
- **Bootstrap 4**: For frontend design, Bootstrap 4 is used to create responsive and visually appealing layouts.
- **SQLite**: As the default database for Django, SQLite is used for development purposes.
- **JavaScript**: Enhances interactivity, particularly in dynamic forms and user interactions.

## APP Design

## Development Setup

To set up the project for development:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd smart-home-automation
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations to create database schema:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Access the application in a web browser at `localhost:8000`.

## Contribution

As the project is under active development, contributions in the form of feedback, bug reports, or pull requests are welcome.

---