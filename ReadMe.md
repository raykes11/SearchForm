# Search Form

**Search Form** is a Python project built on the **FastAPI** framework. Its main functionality is to dynamically generate unlimited Pydantic models from JSON input, validate incoming data, and output either the matching model name or the data type if no match is found.  

## Supported Data Types

1. **`str`** - Regular Python string.  
2. **`email`** - Pydantic's standard `EmailStr` class for email validation.  
3. **`phone`** - A custom Pydantic class `PhoneNumber`, recognizing phone numbers in formats:  
   - `+7 xxx xxx xx xx`  
   - `8 xxx xxx xx xx`  
4. **`date`** - A custom Pydantic class `Date`, validating dates in the formats:  
   - `"%d.%m.%Y"`  
   - `"%Y-%m-%d"`  

---

## Installation

The project was developed using **Python 3.12**.  

To work with Search Form, install the following dependencies:  

1. **FastAPI[all]**  
2. **tinydb**  
3. **pytest**  

### Steps to Set Up  

1. Clone the repository:  
   ```bash
   git clone https://github.com/raykes11/SearchForm.git
   ```

2. Navigate to the `SearchForm` directory:  
   ```bash
   cd SearchForm
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
4. Running the test:  
   ```bash
   pytest
   ```

---

## Project Features

This project implements custom extensions for variable validation. These extensions allow for the creation of complex validation logic tailored to specific needs.

---  

Feel free to explore and contribute! 🎉