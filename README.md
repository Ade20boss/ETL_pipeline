# 🛡️ Log Audit & Blacklist Cross-Referencer

## Overview
This project is a simulation of a **Security Compliance Audit** workflow. It simulates the process of ingesting raw, unstructured log data (emails and phone numbers), normalizing it, and cross-referencing it against a known "Blacklist" of compromised or spam actors.

The tool demonstrates an **ETL (Extract, Transform, Load)** pipeline approach using Python, utilizing Regular Expressions (Regex) for data scraping and Hash Sets for high-performance data matching.



<img width="3999" height="2666" alt="image" src="https://github.com/user-attachments/assets/4c841cc0-b8cb-436b-8c14-aa0134acc9f8" />



## 🚀 Features

* **Synthetic Data Generation:** Uses the `Faker` library to generate thousands of realistic (but fake) US phone numbers (with varying formats) and email addresses.
* **Advanced Pattern Matching:** Custom Regex patterns capable of extracting phone numbers with dashes, dots, spaces, and extensions, as well as complex email structures.
* **High-Performance Lookup:** Converts blacklist arrays into Python Sets to achieve **O(1)** time complexity during the cross-referencing phase, ensuring scalability even with millions of records.
* **Data Injection:** Simulates real-world "hits" by injecting known blacklist entities into the clean logs.

## 📂 Project Structure

```text
.
├── audit_script.py        # The main logic: scrapes data and runs the cross-reference
├── data.py                # Generates the 'clean' log data (Phone numbers/Emails)
├── black_list.py          # Generates the 'blacklist' data (Spam domains/Burner phones)
└── README.md              # Documentation
````

## 🛠️ Prerequisites

  * Python 3.x
  * `Faker` library (for generating synthetic data)

## 📦 Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/Ade20boss/ETL_pipeline.git](https://github.com/Ade20boss/ETL_pipeline.git)
    cd ETL_pipeline
    ```

2.  **Install dependencies:**

    ```bash
    pip install faker
    ```

## ⚡ Usage

1.  **Generate the Data:**
    Ensure `data.py` and `black_list.py` are in the same directory.
    *(Note: Ensure you include the injection logic in `data.py` to guarantee hits during the simulation).*

2.  **Run the Audit:**
    Execute the main script to parse the logs and find the threats.

    ```bash
    python audit_script.py
    ```

3.  **View Results:**
    The script will output the loading status, scraping progress, and a final count of matching hits found in the logs.

## 🔍 Technical Details

### The Regex Logic

The project uses `re.VERBOSE` to handle complex string matching:

  * **Phone Numbers:** Handles formats like `(555) 123-4567`, `555.123.4567`, and `555-123-4567 x1234`.
  * **Emails:** Validates structure including specific handling for the `@` symbol and domain extensions.

### Performance Optimization

Naive cross-referencing (checking a list against a list) results in **O(n\*m)** complexity. This project casts the blacklist to a `set()`, reducing the lookup to **O(1)** on average.

```python
# Instead of iterating through a list, we use instant lookup
if phone_no in blacklist_phones_set:
    phone_no_hits.append(phone_no)
```

## 🤝 Contributing

Contributions are welcome\! Please fork the repository and submit a pull request for any enhancements (e.g., adding multithreading for larger datasets or exporting results to CSV).

## 📄 License

This project is open-source and available under the MIT License.
