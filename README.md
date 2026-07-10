# Python Projects Portfolio

Welcome to my collection of Python applications and data analysis tools! This repository serves as a centralized space showcasing my foundational software engineering skills and practical applications of data science libraries.



## Core Skills & Tech Stack
* **Languages:** Python 3.x

* **Libraries:** NumPy (Data Manipulation, Vectorized Operations, Random Number Generation)

* **Paradigms:** Object-Oriented Programming (OOP), Procedural Programming, Error & Exception Handling

## Projects Directory
* **1. Exploring Weather Data using NumPy** : A comprehensive data analysis module that simulates and analyzes a year's worth of meteorological data using pure vectorization techniques in NumPy.
* **2.  Interactive Python Calculator** : A clean terminal application built to demonstrate object-oriented application design combined with proactive defensive runtime error verification




### 1.  Exploring Weather Data using NumPy

This script is structured around four primary programmatic operations that handle data generation, mathematical transformations, and logical pattern matching:

* **Synthetic Dataset Generation (`generate_weather_data`):**
    * **Seed Control:** Uses `np.random.seed(42)` to ensure that every time you run the script, the exact same "random" numbers are generated. This makes your results reproducible.

    * **Data Structure:** It builds a 2D NumPy array with 365 rows and 3 columns. Column 0 represents the day of the year, Column 1 represents simulated minimum temperatures (ranging from -10°C to 15°C), and Column 2 represents simulated maximum temperatures (ranging from 5°C to 35°C).

    * **Stacking:** Uses `np.column_stack` to merge these separate 1D tracks into a single unified matrix.


* **Statistical Analysis (`basic_statistics`):**
     * **Slicing Matrix Data:** Uses NumPy slicing notation (`data[:, 1]` and `data[:, 2]`) to isolate the minimum and maximum temperature vectors across all 365 days.

     * **Mathematical Averages:** Leverages `np.mean()` to compute the overall annual averages for both temperature thresholds.

     * **Index Mapping:** Employs `np.argmax()` to locate the exact row index of the highest temperature. By reading the corresponding row entry in Column 0, it dynamically determines the specific day the peak occurred.


* **Variance Calculation (`daily_temperature_range`):**
     * **Vectorized Subtraction:** Instead of using slow `for` loops, the script subtracts the entire minimum temperature array from the maximum temperature array in a single operation (`data[:,2] - data[:,1]`) to compute the temperature variance for every single day instantly.


* **Advanced Logic: Heatwave Tracking (`identify_heatwaves`):**
     * **Boolean Masking:** Creates a True/False array identifying days exceeding 30°C (`max_temps > 30`).

     * **Edge Detection (`np.diff`):** Pads the array with zeros and calculates differences between adjacent days. A jump from `0` to `1` flags the exact day a hot streak starts, while a drop from `1` to `-1` flags when it ends.

     * **Duration Filtering:** The script calculates the length of each hot streak (`end_idx - start_idx + 1`) and saves the start and end days only if the streak lasts 3 or more consecutive days.



---

### 2. Interactive Python Calculator

This application showcases clean, professional Object-Oriented Programming (OOP) principles and robust exception management:

* **The `Calculator` Class:**
     * **Encapsulation:** The four core mathematical functions—`add`, `subtract`, `multiply`, and `divide`—are neatly encapsulated as methods inside a single `Calculator` object.

     * **Proactive Safeguards:** The `divide` method includes a custom logical gate. Before attempting an impossible mathematical operation, it checks if the divisor ($y$) is equal to $0$. If it is, it explicitly interrupts the code by raising a `ZeroDivisionError("Cannot divide by zero.")`.




* **The Execution Engine (`run_calculator`):**
     * **Object Instantiation:** Creates an active runtime instance of your calculator using `calc = Calculator()`.


     * **Defensive `try-except-finally` Blocks:** The program routes all user activity through an error-catching wrapper to ensure that common user mistakes never crash the terminal application:


          * `ValueError`: If a user types letters or symbols when asked for numbers, this block catches the input error and gently warns the user.


          * `ZeroDivisionError`: Catches the specific division-by-zero error raised by the class and prints out the clean error message.


          * `Exception`: Acts as a catch-all safety net for any other unpredicted runtime anomalies.




* **The `finally` Clause:** This block is guaranteed to execute no matter what happens during the calculation (even if errors occur). It prompts the user with a continuation check, allowing them to type `'no'` to break out of the calculator loop with a friendly closing message.





