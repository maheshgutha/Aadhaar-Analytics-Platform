# 🧠 AadhaarPulse — Unlocking Societal Trends in Aadhaar Data

> **An AI-powered governance intelligence platform for the UIDAI Data Innovation Hackathon 2026**

---

## 🚀 Overview

**AadhaarPulse** transforms raw Aadhaar enrolment, demographic and biometric update datasets into **actionable governance intelligence** using advanced data analytics, machine learning and interactive visual dashboards.

The platform uncovers:
- Regional enrolment trends  
- Service stress patterns  
- Demographic behaviour  
- Update anomalies  
- Predictive indicators for administrative planning  

All insights are delivered through a **web-based dashboard** supported by a **production-grade AI backend**.

---

## 🎯 Problem Statement

> *Unlocking Societal Trends in Aadhaar Enrolment and Updates*

Government agencies face challenges in understanding enrolment behaviour, update demand, demographic pressure and infrastructure stress across India.  
This project builds an analytical and decision-support system that converts raw Aadhaar data into policy-ready intelligence.

---

## 🧩 Solution Architecture

UIDAI/
    │   .hintrc
    │   api_service.py
    │   app.py
    │   README.md
    │   requirements.txt
    │   root.py
    │
    ├───ai_engine
    │   │   ai.py
    │   │   build_intelligence.py
    │   │   forecast_models.pkl
    │   │   knowledge.json
    │   │   new.py
    │   │   policy_ai.py
    │   │   train.py
    │   │
    │   └───__pycache__
    │           ai.cpython-310.pyc
    │           ai.cpython-313.pyc
    │           guna.cpython-310.pyc
    │           guna.cpython-313.pyc
    │           policy_ai.cpython-310.pyc
    │           policy_ai.cpython-313.pyc
    │           __init__.cpython-310.pyc
    │           __init__.cpython-313.pyc
    │
    ├───analysis_engine
    │   │   age_analyzer.py
    │   │   ai_explainer.py
    │   │   ai_models.py
    │   │   anomaly_detector.py
    │   │   biometric_analyzer.py
    │   │   data_integrator.py
    │   │   data_loader_utils.py
    │   │   demographic_analyzer.py
    │   │   enrollment_analyzer.py
    │   │   feature_builder.py
    │   │   growth_trend_analyzer.py
    │   │   inclusion_analyzer.py
    │   │   insights_engine.py
    │   │   insight_generator.py
    │   │   loader.py
    │   │   migration_analyzer.py
    │   │   national_analyzer.py
    │   │   operations_analyzer.py
    │   │   policy_engine.py
    │   │   population_analyzer.py
    │   │   state_analyzer.py
    │   │   trends_analyzer.py
    │   │   visualization_engine.py
    │   │
    │   └───__pycache__
    │           age_analyzer.cpython-310.pyc
    │           anomaly_detector.cpython-310.pyc
    │           biometric_analyzer.cpython-310.pyc
    │           demographic_analyzer.cpython-310.pyc
    │           enrollment_analyzer.cpython-310.pyc
    │           growth_trend_analyzer.cpython-310.pyc
    │           inclusion_analyzer.cpython-310.pyc
    │           insights_engine.cpython-310.pyc
    │           migration_analyzer.cpython-310.pyc
    │           operations_analyzer.cpython-310.pyc
    │           population_analyzer.cpython-310.pyc
    │
    ├───api
    │   │   ai_api.py
    │   │   analytics_api.py
    │   │   dashboard_api.py
    │   │   kpi_api.py
    │   │
    │   └───__pycache__
    │           ai_api.cpython-310.pyc
    │           ai_api.cpython-313.pyc
    │           analytics_api.cpython-310.pyc
    │           analytics_api.cpython-313.pyc
    │           dashboard_api.cpython-313.pyc
    │           kpi_api.cpython-310.pyc
    │           kpi_api.cpython-313.pyc
    │           __init__.cpython-310.pyc
    │           __init__.cpython-313.pyc
    │
    ├───data
    │   ├───processed
    │   │       integrated_master.csv
    │   │       monthly_intelligence.csv
    │   │
    │   └───raw
    │       ├───biometric
    │       │       api_data_aadhar_biometric_0_500000.csv
    │       │       api_data_aadhar_biometric_1000000_1500000.csv
    │       │       api_data_aadhar_biometric_1500000_1861108.csv
    │       │       api_data_aadhar_biometric_500000_1000000.csv
    │       │
    │       ├───demographic
    │       │       api_data_aadhar_demographic_0_500000.csv
    │       │       api_data_aadhar_demographic_1000000_1500000.csv
    │       │       api_data_aadhar_demographic_1500000_2000000.csv
    │       │       api_data_aadhar_demographic_2000000_2071700.csv
    │       │       api_data_aadhar_demographic_500000_1000000.csv
    │       │
    │       └───enrolment
    │               api_data_aadhar_enrolment_0_500000.csv
    │               api_data_aadhar_enrolment_1000000_1006029.csv
    │               api_data_aadhar_enrolment_500000_1000000.csv
    │
    ├───pipeline
    │   │   execution_controller.py
    │   │
    │   └───__pycache__
    │           execution_controller.cpython-313.pyc
    │
    ├───static
    │   │   ai.css
    │   │   ai.js
    │   │   app.js
    │   │   dashboard.css
    │   │   front.jpeg
    │   │   styles.css
    │   │
    │   └───components
    │           anomalies.js
    │           demographics.js
    │           migration.js
    │           operations.js
    │           population.js
    │           trends.js
    │
    ├───templates
    │       ai.html
    │           dashboard.html
    │       index.html
    │
    └───__pycache__
            root.cpython-310.pyc

