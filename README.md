# Paws & Claws: System Requirements Engineering & Data Pipeline

### 🚀 Project Abstract
This repository documents the end-to-end Requirements Engineering (RE) process for **"Paws & Claws"**, a comprehensive service platform management system. 

Beyond standard specification practices, this project demonstrates a **"Docs-as-Code" approach**: combining Systems Engineering best practices (V-Model, CCC Pattern) with **Python automation** to transform raw unstructured data into 105+ verifiable technical specifications.

> **Key Competencies Demonstrated:**
> * **Systems Engineering:** System Decomposition, Goal Modeling (4EM), Variability Modeling (OVM).
> * **Data Engineering:** Building ETL pipelines to clean and structure raw requirement logs.
> * **Verification:** Defining strict Acceptance Criteria for system testing.
> * **Traceability:** Managing dependencies between Business Needs and Technical Specs.

---

### 📂 Repository Structure
The project is organized to demonstrate the transformation from "Raw Data" to "Structured Documentation":

```text
├── process_requirements.py                            # 🐍 Python ETL Script (Data Cleaning & Logic)
├── requirements_specification.csv                     # 📄 Raw Data Source (Exported from Miro)
├── docs/
│   ├── REQUIREMENTS_SORTED.md                         # ✅ Generated Structured Documentation (Markdown)
│   └── full_system_specification_document.pdf         # 📐 High-Res System Architecture (Vector PDF)
└── assets/                                            # 🖼️ Diagrams & Models
```
---

### 🛠️ The Automation Pipeline (Python)
To handle the complexity of large-scale requirement management, I engineered a Python script (process_requirements.py) to automate the documentation process.

The Pipeline Logic:

1. Ingest: Reads raw CSV exports from collaboration tools (Miro), handling encoding and delimiter issues.

2. Parse & Clean: Uses Regex to split mixed-text fields based on the CCC Pattern (Card, Conversation, Confirmation).

3. Format:

  - Extracts IDs and Titles using string manipulation logic.
  
  - Transforms unstructured text blocks into bulleted lists (based on punctuation).
  
  - Standardizes Acceptance Criteria into testable items.

4. Generate: Outputs a clean, readable Markdown table automatically.

   How to Reproduce: You can run the script locally to regenerate the documentation from the source CSV:
   ```bash
   python process_requirements.py
   ```

---

### 🏗 System Architecture & Goal Modeling
We utilized 4EM (For Enterprise Modeling) to map technical components back to business goals, ensuring strategic alignment between stakeholders and developers.

🧩 Variability & Scalability (OVM)
An Orthogonal Variability Model (OVM) was constructed to manage service variants (e.g., Medical care vs. Standard care), ensuring the system architecture is adaptable to future business changes.

---

### 📋 Detailed Requirements Specification (CCC Pattern)
Requirements were specified using the Card, Conversation, Confirmation pattern to ensure they are ready for Verification & Validation (V&V).
| Feature | Link |
|:---|:---|
| **Full List** | [📄 **View Full Requirements Table (105+ User Stories)**](./docs/REQUIREMENTS_SORTED.md) |
| **Source Data** | [📊 View Raw CSV Data](./requirements_specification.csv) |

Specification Preview:
The table below highlights the "Verification Criteria" column, generated automatically by the Python pipeline.
| ID | Title | User Story | Verification Criteria (Confirmation) |
|:---|:---|:---|:---|
| **BRD-1** | **Specify duration** | As a customer, I want to specify dates... | • **Test** booking logic with valid dates<br>• **Test** rejection if capacity exceeded |
| **GRM-1** | **Create service** | As an Admin, I want to add new services... | • **Test** creation flow<br>• **Test** visibility in catalog |

---

### ⚙️ Non-Functional Requirements (NFRs)
Rigorous constraints were defined to simulate safety-critical environments:

Safety Assurance: Automated alerts for animal health monitoring.

Compliance: GDPR data retention policies for customer PII.

Performance: <200ms latency targets for real-time booking availability.

---

### 🎓 Academic Context & Individual Contribution
This project was executed as a semester-long case study for the **Advanced Requirements Engineering of IT-systems (HT2025)** course at **Stockholm University**.

While the project was a collaborative effort by a 3-person team, my specific **individual contributions** include:

* **Lead Requirements Engineer:**
    * **Sole Author:** Personally authored all **105+ User Stories**, defining the strict **CCC Pattern** (Card, Conversation, Confirmation) and Acceptance Criteria.
    * **Variability Modeling:** Independently designed and constructed the **Orthogonal Variability Model (OVM)** to handle system scalability.
* **Automation & Tooling (Python):**
    * **Sole Developer:** Independently engineered the **Python Data Pipeline** (`process_requirements.py`) to automate the cleaning, formatting, and generation of documentation from raw Miro logs, demonstrating a "Docs-as-Code" mindset.
* **Project Leadership:**
    * Led the system decomposition strategy and coordinated the team's effort in developing Goal Models (4EM) and Non-Functional Requirements (NFRs).
