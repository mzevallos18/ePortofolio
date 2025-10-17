# Android Inventory Management App

## Overview
This project was originally developed in the **CS-360: Mobile Architecture and Programming** course and later enhanced for my **CS-499 ePortfolio**.  
It demonstrates my ability to design secure, user-friendly mobile applications with persistent data storage and role-based access control.  
The enhanced version implements key upgrades including **login functionality**, **role-based permissions**, **session management**, and **data persistence**, transforming the app into a complete inventory management solution for mobile devices.

---

## Key Features
- **User Authentication:** Secure login and logout features using credential validation.  
- **Role-Based Access Control:** Admin users have full permissions to add, update, and delete items; standard users have view-only access.  
- **Inventory Management:** Grid-based dashboard that displays current inventory with plus/minus buttons for adjusting quantities.  
- **Session Handling:** Maintains login sessions between app uses to improve user experience.  
- **Data Persistence:** Local storage helper that preserves data even after the app is closed.  
- **Clean UI/UX:** Responsive interface with a structured layout for usability and clarity.  

---

## Files

| File Name | Description |
|------------|-------------|
| `LoginActivity.java` | Handles user authentication and login/logout logic. |
| `DashboardActivity.java` | Displays the inventory grid and manages item updates. |
| `InventoryAdapter.java` | Connects inventory data to the grid layout for display. |
| `StorageHelper.java` | Manages local data storage and session persistence. |
| `User.java` | Defines user roles and permissions. |
| `AndroidManifest.xml` | Declares activities and required permissions. |
| `activity_login.xml`, `activity_dashboard.xml` | Layout files defining the app’s UI. |
| `README.md` | Project documentation and usage instructions. |

---

## Technologies Used
- **Language:** Java  
- **Platform:** Android Studio  
- **Database:** Local data storage (SharedPreferences / internal storage)  
- **Architecture:** MVC (Model-View-Controller) pattern for organized design  
- **Development Tools:** Android Emulator, Gradle build system  

---

## Skills Demonstrated
- Mobile app development using Android Studio  
- Secure software design and role-based access implementation  
- Persistent data management and session handling  
- UI/UX optimization for usability and accessibility  
- Modular and maintainable code structure following object-oriented design  

---

## How to Run
1. **Open the project in Android Studio.**  
   - Navigate to **File → Open** and select the project folder.  

2. **Build the project.**  
   - Gradle will automatically install all required dependencies.  

3. **Run the app on an emulator or a connected Android device.**  
   - Use Android 11 (API 30) or higher for best compatibility.  

4. **Login credentials (sample):**  
   - **Admin user:** username: `admin` / password: `1234`  
   - **Standard user:** username: `user` / password: `5678`  

5. **Explore features:**  
   - Add, edit, and delete items as an Admin.  
   - View and adjust quantities with plus/minus buttons.  
   - Logout and re-login to test session persistence.

---

## Future Enhancements
While the project now meets all planned goals and course outcomes, future versions could include:  
- Integration with a cloud-based backend (Firebase or AWS).  
- Real-time synchronization across multiple devices.  
- Enhanced encryption for stored user data.  
- Push notifications for low-stock alerts.

---

## Project Reflection
This enhanced version fulfills all planned improvements established at the beginning of the course.  
It demonstrates strong progress in mobile development, secure design, and software engineering best practices.  
Through this project, I strengthened my understanding of Android architecture, persistent storage, and user-role management—key skills applicable to professional software development.
