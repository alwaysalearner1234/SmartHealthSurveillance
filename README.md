Overview

The Smart Health Surveillance and Early Warning System is a lightweight, AI- and IoT-enabled platform designed to detect and monitor water-borne disease outbreaks in vulnerable communities. It collects health data from local clinics, ASHA workers, and IoT sensors, predicts outbreak risks using a machine learning model, and displays insights through an interactive dashboard.

Features

📱 Mobile app skeleton for ASHA worker reporting

🤖 Basic AI/ML outbreak prediction (placeholder model)

💧 IoT data simulation for water quality monitoring

⚠️ Real-time alerts (placeholder) through dashboard

🌐 Streamlit dashboard for visualization

🗃️ Local JSON file used for storing reports

Folder Structure
SmartHealthSurveillance/
├── backend/             # Flask API and data storage
├── dashboard/           # Streamlit dashboard
├── iot_module/          # Simulated IoT sensor data script
├── mobile_app/          # Flutter app skeleton
├── ml_model/            # ML model placeholder and prediction script
└── README.md            # Project overview and instructions
Installation

Unzip the project.

Navigate to the backend folder:

cd SmartHealthSurveillance/backend

Install dependencies:

pip install -r requirements.txt

Run Flask backend:

python app.py

Run Streamlit dashboard:

streamlit run ../dashboard/dashboard_app.py
Usage

The backend API has endpoints like /submit_health_data (POST) and /get_predictions (GET).

IoT simulation sends random data to the backend.

Flutter app skeleton contains a sample form for ASHA worker input.

Dashboard reads JSON data and displays reports and risk alerts (placeholders).

Notes

This is a minimal functional version with placeholders; ML model and IoT integration are for demonstration purposes.

Data is stored in a local JSON file for simplicity.

Future Enhancements

Full AI/ML outbreak prediction with real datasets.

Multi-language Flutter app with backend integration.

Real IoT water sensor data collection.

User authentication and secure data storage.

License

MIT License
