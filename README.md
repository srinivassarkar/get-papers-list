# Get Papers List

A Python tool to fetch research papers from PubMed and filter those with authors affiliated with pharmaceutical or biotech companies. Results are saved in a CSV file.

---

## 🚀 Features

- Fetch papers using the **PubMed API**.
- Filter papers with **non-academic authors**.
- Save results in **CSV format**.
- Supports **PubMed’s full query syntax**.

---

## 🛠️ Installation

1. Install **Poetry**:

   ```bash
   pip install poetry
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/get-papers-list.git
   ```

   ```
   cd get-papers-list
   ```

3. Install dependencies::
   ```bash
   pip install poetry
   ```

---

### 🧰 Dependencies

- **requests**: HTTP requests to PubMed API.
- **lxml**: Parse XML responses.
- **pandas**: CSV handling (optional).

## Output CSV Format

| Column                      | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| **PubmedID**                 | Unique identifier for the paper.                          |
| **Title**                    | Title of the paper.                                       |
| **Publication Date**         | Date the paper was published.                             |
| **Non-academic Author(s)**   | Authors affiliated with non-academic institutions.        |
| **Company Affiliation(s)**   | Names of pharmaceutical/biotech companies.                |
| **Corresponding Author Email** | Email of the corresponding author.                        |


## **🖥️ Usage**

**Run the tool with a PubMed query:**

```
poetry run get-papers-list "cancer treatment" -f output.csv
```

**Note**: If you omit the file name, the results will be displayed directly in the terminal instead of being saved to a file.

```
poetry run get-papers-list "cancer treatment"
```

## **more examples:**

- Search for "diabetes AND treatment" with debug mode enabled:

```
poetry run get-papers-list "diabetes AND treatment" -f diabetes_papers.csv -d
```

- Search for "COVID-19 vaccine" and print results to the console:

```
poetry run get-papers-list "COVID-19 vaccine"
```

- Search for "machine learning in medicine" and save results to ml_medicine.csv:

```
poetry run get-papers-list "machine learning in medicine" -f ml_medicine.csv
```

## **Command-Line Options**

- **Query**: The PubMed search query (e.g., "cancer treatment").

- **-f or --file**: Save results to a CSV file (e.g., output.csv).

- **-d or --debug**: Enable debug mode for additional logging.

---


## **Why This Works**

- **Simple and Clean**: Easy to read and understand.
- **Actionable**: Includes installation and usage instructions with example commands.
- **Structured**: Uses tables and code blocks for better readability.
- **Minimalist**: Focuses on essential information without unnecessary details.

Thanks to chatGPT to help me finish this assessment.

---
