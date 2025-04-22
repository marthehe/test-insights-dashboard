# 📊 Test Coverage & Performance Insights Dashboard

This project demonstrates how to turn automated test run data into meaningful insights. The dashboard, built with **Power BI**, visualizes key quality signals like pass/fail rates, test duration trends, flaky test rates, and browser coverage — helping drive smarter testing decisions.

---

## 🎯 Purpose  
Analyze and visualize test health and performance across CI pipelines, showcasing an understanding of continuous testing, observability, and quality insights.

---

## ✅ Features  
- 📈 Pass vs fail test outcomes  
- ⏱️ Average test duration over time  
- 🔁 Flaky vs stable test rate  
- 🌐 Browser and platform coverage  
- 📋 Table of recent test runs for detailed view  

---

## 🛠️ Tech Stack

| Purpose               | Tool                  |
|-----------------------|-----------------------|
| Visualization         | Power BI              |
| Data Source           | Mock CSV (expandable to API data) |
| Optional AI Insights  | Azure OpenAI / GPT (planned) |

---

## 🚀 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/marthehe/test-insights-dashboard.git
   cd test-insights-dashboard
2. **Open `test-results.csv` in Power BI**  
   _(Get Data → Text/CSV)_

3. **Build the visuals** following the dashboard layout.

4. **Apply slicers and formatting** for easy filtering and clean presentation.

5. **Save your report** as `.pbix` or publish to Power BI Service.

---

## 📌 Roadmap

- [x] Mock data and initial dashboard  
- [x] Pass/fail, duration, flaky rate, browser coverage visuals  
- [ ] Integration with GitHub Actions or Sauce Labs data  
- [ ] Add AI-generated summaries for failure insights  

---

> 👩‍💻 Built with ☕ and 💙 by Marta.

