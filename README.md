# Animal Shelter CRUD Dashboard

## Overview
This project was developed as part of the CS-340: Client/Server Development course and later enhanced for my CS-499 ePortfolio. It demonstrates full CRUD (Create, Read, Update, Delete) functionality using **Python**, **MongoDB**, and **Dash**. The project was completely reconstructed to restore all database operations and includes a dynamic web dashboard that allows users to visualize, search, and filter data on different animal types and breeds stored in the database.

---

## Key Features
- **CRUD Operations:** Full create, read, update, and delete functionality using MongoDB.
- **Dash Web Dashboard:** Interactive visualization for exploring data such as animal type, breed, and adoption details.
- **Filtering and Search:** Users can filter animals by type and breed through dropdown menus.
- **Sample Data:** Includes 20 preloaded dog and cat breeds with age, sex, and outcome type details.
- **Data Persistence:** MongoDB ensures that data remains consistent and accessible between sessions.
- **Modular Design:** Separated functionality into clean modules (`animalshelter.py`, `dash_app.py`, `seed_animals.py`).

---

## Files
| File Name | Description |
|------------|--------------|
| `animalshelter.py` | Handles MongoDB operations and defines the CRUD methods. |
| `dash_app.py` | Runs the Dash dashboard for data visualization and filtering. |
| `seed_animals.py` | Populates the MongoDB collection with 20 sample records of cats and dogs. |
| `__init__.py` | Initializes the project as a Python package. |
| `README.md` | Provides project documentation and usage instructions. |

---

## Technologies Used
- **Programming Language:** Python 3  
- **Database:** MongoDB  
- **Framework:** Dash (for visualization)  
- **Libraries:** pandas, pymongo  

---

## Skills Demonstrated
- Database design and CRUD operations  
- Backend development using Python  
- Data handling and visualization with Dash  
- Integration of Python applications with MongoDB  
- Secure and maintainable software structure  

---

## How to Run
1. **Install dependencies:**
   ```bash
   pip install dash pandas pymongo
   mongod
   python dashboard/dash_app.py
