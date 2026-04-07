# 📊 Sales Data Analyzer

## 📌 Problem

Raw sales data often contains:

* Duplicate records
* Missing values
* Unstructured and inconsistent entries

This makes it difficult to analyze and extract meaningful insights.

---

## ✅ Solution

This project is a Python-based automation script that cleans and processes raw sales data using **pandas**, and generates a structured, analysis-ready report.

---

## ⚙️ Features

* Removes duplicate records
* Handles missing values (e.g., empty names)
* Categorizes sales into **High** and **Low**
* Identifies **VIP customers** based on business rules
* Filters relevant transactions
* Exports a clean and usable report

---

## 🛠️ Tech Stack

* Python
* Pandas

---

## 📂 Input

`sales.csv` – Raw sales dataset containing:

* Customer ID
* Name
* Purchase Amount
* Country

---

## 📤 Output

`final_report.csv` – Cleaned and processed dataset with:

* No duplicates
* No missing names
* Additional columns:

  * `Category` (High / Low)
  * `Priority` (VIP / Normal)

---

## 💡 Use Cases

* Cleaning messy CSV/Excel files
* Automating data preprocessing
* Preparing datasets for analysis
* Freelance data cleaning tasks
