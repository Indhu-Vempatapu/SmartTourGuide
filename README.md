# Tourist Recommendation Expert System
This is an **AI-based rule-driven web application** that provides **personalized travel recommendations** to users based on their interests and preferences. It is powered by a **forward chaining expert system** built using Python's *experta* library and served via a **Flask web interface**.

# Project Functionality
- Collects tourist preferences via a simple web form.

- Uses forward chaining (data-driven inference) to match inputs with a rich set of tourism-related rules.

- Generates destination recommendations across multiple categories like:

  - Historical places

  - Adventure sports

  - Festivals and culture

  - Art and architecture

  - Nature and wildlife

  - Food, music, and more

- Eliminates duplicate suggestions with a clean result view.

# 🔗 How Forward Chaining Works Here
The system uses the *experta* library (a Python port of CLIPS) to define a knowledge base and rules. When a user selects preferences, **facts** are declared and matched with **rules** using forward chaining:

  - Inputs → Facts (TouristInterests)

  - Rules fire if conditions match

  - Matching rules append specific recommendations

  - Final list of destinations is presented to the user

This approach makes the system scalable and modular—just add new rules for new features.

# 🛠️ Tools & Technologies Used
- Python – Core programming

- Flask – Web framework for UI routing

- HTML/CSS – Front-end for form and results display

- Experta – Rule engine for AI-based inference

- Jinja2 – Template rendering for web pages

# 🧠 Concepts Involved
- Artificial Intelligence

  - Expert Systems

  - Rule-based reasoning

- Forward Chaining Inference

- Modular Rule Design

- Web Development (Flask)

- Fact Declarations & Rule Matching

# Key Features
- Forward chaining logic using declarative rules

- Custom rule-based recommendation logic

- Clear separation of logic (rules_engine.py) and interface (app.py)

- Realistic travel destinations across budget ranges, interests, and geography

- Scalable design for future rule additions (e.g., climate, group size)

