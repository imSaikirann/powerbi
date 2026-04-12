# PARUL UNIVERSITY
## Faculty of Engineering and Technology
## Department of Computer Science and Engineering

# INTERNSHIP / PROJECT REPORT

## On
## **HR Analytics Dashboard with Predictive Attrition Analysis**

### Submitted in partial fulfillment of the requirements for the award of the degree of
### **Bachelor of Technology**
### in
### **Computer Science and Engineering**

**Submitted by:**  
`[Student Name]`  
Enrollment No.: `[Enrollment Number]`  
Semester: `[Semester]`

**Internship Company:** Self Project  
**Domain:** Data Analytics, Business Intelligence, Machine Learning, and Backend Development  
**Duration:** January 2026 - April 2026  
**Role:** Full Stack Data Analytics Developer

**Academic Year:** 2025-26

**Submitted To:**  
Department of Computer Science and Engineering  
Parul University, Vadodara, Gujarat

---

# CERTIFICATE

This is to certify that the internship/project report entitled **"HR Analytics Dashboard with Predictive Attrition Analysis"** is a bonafide work carried out by **`[Student Name]`**, Enrollment No. **`[Enrollment Number]`**, student of **B.Tech in Computer Science and Engineering**, Parul University, during the academic year **2025-26**, in partial fulfillment of the requirements for the award of the degree of **Bachelor of Technology**.

The work embodied in this report has been carried out under proper guidance and supervision. To the best of our knowledge, this work is original and has not been submitted previously, in part or in full, for the award of any degree, diploma, or certificate of this or any other university.

**Project Guide / Faculty Mentor**  
Name: `[Guide Name]`  
Designation: `[Designation]`  
Department of Computer Science and Engineering  
Parul University

**Industrial Mentor / Project Supervisor**  
Name: `[Mentor Name / Self Guided]`  
Designation: `[Designation]`  
Organisation: Self Project

**Head of Department**  
Department of Computer Science and Engineering  
Parul University

Place: Vadodara  
Date: `[Submission Date]`

---

# INTERNSHIP CERTIFICATE

**To Whomsoever It May Concern**

This is to certify that **`[Student Name]`**, a student of **B.Tech, Computer Science and Engineering, Parul University**, has successfully completed the internship/project work titled **"HR Analytics Dashboard with Predictive Attrition Analysis"** during the period from **January 2026 to April 2026**.

During this period, the student worked on the design and development of an end-to-end HR analytics system involving synthetic workforce data generation, data cleaning and standardization, KPI computation, predictive modeling for employee attrition, API development, and dashboard-oriented visual analytics.

The student demonstrated sincerity, technical competence, analytical thinking, and professional conduct throughout the internship period. The work carried out is found to be satisfactory and reflects a sound understanding of software engineering, data analytics, and reporting systems.

This certificate is issued upon request for academic submission and record purposes.

**Authorised Signatory**  
`[Company / Mentor Signature Placeholder]`  
Self Project / Internship Supervisor  
Date: `[Date]`

---

# ACKNOWLEDGEMENT

The successful completion of this internship project report is the result of consistent guidance, academic support, self-discipline, and the collective encouragement of several individuals and institutions. I express my sincere gratitude to all those who directly or indirectly contributed to the completion of this work.

First and foremost, I would like to express my heartfelt gratitude to **Parul University**, the **Faculty of Engineering and Technology**, and the **Department of Computer Science and Engineering** for providing a strong academic environment that continuously encouraged practical learning, innovation, and technical exploration. The academic structure of the program created the foundation upon which this project was conceived and executed.

I extend my respectful thanks to my **faculty guide**, **`[Guide Name]`**, for the valuable guidance, constructive feedback, and continuous motivation offered throughout the course of this internship. The suggestions provided during the planning, implementation, and documentation phases were instrumental in improving both the technical quality and presentation of the project.

I also express my sincere appreciation to the internship/project mentor **`[Mentor Name / Self Guided]`** for encouraging me to approach the project with a real-world problem-solving mindset. The practical orientation of the work helped me understand that software systems are not merely collections of code modules, but decision-support tools that can directly influence organizational efficiency and business outcomes.

I am deeply thankful to all the faculty members of the department whose lectures, discussions, and technical insights during the course of the degree program played a significant role in shaping my understanding of data processing, backend development, software architecture, and analytical reporting.

I would also like to acknowledge the contribution of the open-source ecosystem and the developer communities whose libraries, frameworks, and documentation made this project technically feasible. Tools such as Python, FastAPI, Pandas, Scikit-learn, and Power BI-related design practices offered a reliable foundation for implementing a practical and modern analytics system.

On a personal note, I am grateful to my parents, family members, and friends for their constant encouragement, patience, and emotional support throughout this academic journey. Their belief in my abilities gave me the confidence to complete this project with dedication and consistency.

Finally, I would like to thank everyone who supported me in ways both visible and unseen. This report is not only a reflection of my technical effort but also a reflection of the guidance, trust, and support I received during the internship period.

---

# ABSTRACT

Human Resource departments in modern organizations are increasingly expected to make strategic decisions using workforce data rather than intuition alone. However, many organizations, especially growing enterprises and educational project environments, lack an integrated and practical framework for understanding employee demographics, attendance behavior, departmental performance, salary distribution, hiring trends, and potential attrition risks in a single analytics pipeline. This project, titled **"HR Analytics Dashboard with Predictive Attrition Analysis,"** was undertaken to address this gap by designing and implementing an end-to-end workforce analytics solution that combines data engineering, data cleaning, exploratory analysis, predictive modeling, backend API exposure, and dashboard-ready reporting outputs.

The central objective of the project was to build a realistic, scalable, and technically structured HR analytics system that could simulate organizational employee data and transform it into meaningful business insights. Since real employee datasets are often confidential and difficult to access, the project began with synthetic dataset generation. A data generation module was designed in Python to create realistic employee records across multiple departments, roles, salary bands, attendance levels, performance scores, and location categories. In order to mimic practical industry challenges, the raw dataset intentionally included duplicate records, null values, inconsistent text formatting, and noisy labels.

The second phase of the project involved data preprocessing and data quality enhancement. A dedicated cleaning module was implemented to remove duplicates, normalize categories, fill missing values using department-level median statistics, standardize labels, derive tenure-related fields, and create additional business reporting fields such as employment status, joining year, and joining month. This stage ensured that the dataset became analytics-ready and suitable for both dashboard generation and predictive modeling.

To support advanced decision-making, a machine learning component was integrated into the project. A logistic regression model was trained using selected employee attributes such as age, department, role, salary, attendance percentage, performance rating, location, and tenure. The purpose of this model was not to replace HR decision-makers, but to provide an interpretable attrition risk estimation framework. The pipeline included feature preprocessing through imputation, scaling, and one-hot encoding, followed by performance evaluation using classification metrics and ROC-AUC.

In addition to data processing and predictive modeling, a FastAPI-based backend layer was developed to expose system outputs through structured endpoints. These endpoints support health monitoring, pipeline execution, employee data retrieval, KPI access, and visualization payload generation for browser-based frontend rendering. A built-in dashboard-style interface was also implemented to present executive overview and workforce performance insights in a user-friendly format.

The project demonstrates how software engineering principles, analytical thinking, and machine learning can be combined to create a practical HR decision-support system. The final output is not merely a technical prototype, but a complete internship-level engineering solution that reflects real-world data challenges, reporting needs, and architectural design considerations. This report documents the complete lifecycle of the project, including motivation, objectives, literature review, system methodology, implementation details, results, limitations, and future scope.

---

# TABLE OF CONTENTS

| Sr. No. | Particulars | Page No. |
|---|---|---|
| 1 | Cover Page | 1 |
| 2 | Certificate | 2 |
| 3 | Internship Certificate | 3 |
| 4 | Acknowledgement | 4-5 |
| 5 | Abstract | 6-7 |
| 6 | Table of Contents | 8 |
| 7 | List of Abbreviations | 9 |
| 8 | List of Figures | 10 |
| 9 | Chapter 1: Introduction | 11-15 |
| 10 | Chapter 2: Aim and Objectives | 16-18 |
| 11 | Chapter 3: Literature Review | 19-25 |
| 12 | Chapter 4: Methodology | 26-42 |
| 13 | Chapter 5: Results and Discussion | 43-48 |
| 14 | Chapter 6: Conclusion | 49-51 |
| 15 | References | 52 |
| 16 | Annexures | 53-62 |

---

# LIST OF ABBREVIATIONS

| Abbreviation | Full Form |
|---|---|
| HR | Human Resources |
| API | Application Programming Interface |
| BI | Business Intelligence |
| ML | Machine Learning |
| CSV | Comma-Separated Values |
| KPI | Key Performance Indicator |
| ROC-AUC | Receiver Operating Characteristic - Area Under Curve |
| UI | User Interface |
| ETL | Extract, Transform, Load |
| JSON | JavaScript Object Notation |
| REST | Representational State Transfer |
| POC | Proof of Concept |
| OHE | One-Hot Encoding |
| CPU | Central Processing Unit |
| UAT | User Acceptance Testing |
| SDLC | Software Development Life Cycle |

---

# LIST OF FIGURES

| Figure No. | Title | Page No. |
|---|---|---|
| Fig. 1.1 | HR Analytics Ecosystem Overview | Not Inserted |
| Fig. 1.2 | Problem Context of Workforce Decision Making | Not Inserted |
| Fig. 3.1 | Comparative View of Existing HR Systems | Not Inserted |
| Fig. 4.1 | Overall System Architecture | 28 |
| Fig. 4.2 | Data Generation Workflow | 30 |
| Fig. 4.3 | Data Cleaning and Transformation Flow | 32 |
| Fig. 4.4 | Predictive Attrition Modeling Pipeline | 35 |
| Fig. 4.5 | API Interaction Flow | 37 |
| Fig. 4.6 | Executive Overview Page | 38 |
| Fig. 4.7 | Workforce Performance Page | 38 |
| Fig. 4.8 | Data Quality Report Page | 38 |
| Fig. 4.9 | Final Output Report Page | 39 |
| Fig. 5.1 | KPI Result Snapshot | 44 |
| Fig. 5.2 | Performance Analysis View | 46 |
| Fig. A.1 | Overview Dashboard Screenshot | 55 |
| Fig. A.2 | Performance Dashboard Screenshot | 55 |
| Fig. A.3 | Data Quality Dashboard Screenshot | 55 |
| Fig. A.4 | Final Output Dashboard Screenshot | 55 |

---

# CHAPTER 1: INTRODUCTION

## 1.1 Background of Industry

In the current digital economy, organizations across all sectors are increasingly dependent on data-driven decision-making. Human Resource Management, which was traditionally viewed as an administrative support function, has evolved into a strategic unit that directly influences organizational productivity, retention, workforce planning, employee engagement, and long-term competitiveness. With the widespread adoption of enterprise software, digital attendance systems, payroll systems, performance management platforms, and employee self-service portals, HR departments now generate large volumes of workforce-related data. However, in many organizations this data remains fragmented across files, disconnected tools, or operational systems, limiting its usefulness for strategic planning.

The rise of **HR Analytics**, also referred to as workforce analytics or people analytics, represents a major transformation in the HR domain. HR analytics seeks to use employee data systematically to understand trends, identify operational inefficiencies, predict potential risks such as attrition, and improve workforce outcomes. The demand for HR analytics has grown significantly because organizations must now respond to business pressures such as employee turnover, skill shortages, hybrid work models, employee well-being concerns, and performance optimization.

Traditional HR reporting often focuses on static summaries such as total employee count, number of new hires, or number of resignations. While such reports are useful, they do not offer deep analytical value unless they are connected to context such as tenure, salary levels, attendance behavior, departmental performance, and hiring patterns. Modern HR teams require dynamic dashboards and predictive insights that help answer business-critical questions such as:

- Which departments are experiencing high attrition?
- Are low attendance patterns associated with lower performance?
- Which workforce segments may require proactive intervention?
- Is salary distribution aligned with role hierarchy and department structure?
- Are recent hiring trends sustainable across multiple locations?

In real organizations, producing such insights is not simple because workforce data is often incomplete, inconsistent, and operationally dispersed. A practical analytics system therefore requires more than visualization alone. It must include data generation or collection, data cleaning, feature engineering, model development, API integration, and a meaningful presentation layer. This project was designed specifically to address this end-to-end requirement.

## 1.2 Overview of Technology Domain

The technology domain of this project lies at the intersection of **data analytics**, **machine learning**, **backend development**, and **dashboard engineering**. Each of these areas contributes a specific role in transforming raw data into business value.

### 1.2.1 Data Analytics

Data analytics is the process of collecting, preparing, transforming, and interpreting data in order to derive useful conclusions. In the HR context, analytics enables organizations to evaluate workforce metrics such as headcount, compensation, performance, tenure, and attrition. Data analytics workflows usually involve raw data acquisition, cleaning, exploratory analysis, metric computation, and reporting.

### 1.2.2 Business Intelligence

Business Intelligence refers to the technologies and practices used to convert data into dashboards, reports, summaries, and decision-support tools. For HR teams, BI dashboards serve as visual control panels through which stakeholders can monitor workforce health. Dashboard design is not merely a visual activity; it involves selecting relevant KPIs, defining dimensions and measures, structuring drill-down pathways, and making metrics interpretable for managerial use.

### 1.2.3 Machine Learning in HR

Machine learning contributes predictive capability to analytics systems. In HR, predictive models can be used for attrition estimation, candidate screening support, absenteeism analysis, workforce demand forecasting, and employee segmentation. In this project, machine learning was used to construct a supervised classification model to estimate the probability of employee attrition using historical and behavioral attributes.

### 1.2.4 Backend APIs and Data Services

Modern analytics systems are increasingly service-oriented. Instead of embedding all logic directly into dashboards, organizations expose data through APIs so that multiple applications can reuse the same metrics and outputs. A backend API makes the system extensible, testable, and integration-friendly. This project uses FastAPI to create lightweight REST-style endpoints for health checks, pipeline execution, KPI retrieval, and employee-level access.

### 1.2.5 Python-Based Analytical Engineering

Python has emerged as a standard technology in analytical engineering because it combines simple syntax with a mature ecosystem for data manipulation, scientific computing, web APIs, and machine learning. Libraries such as Pandas, NumPy, Scikit-learn, and FastAPI make Python especially suitable for building academic and industrial analytical systems.

## 1.3 Problem Statement

Human Resource teams frequently need actionable insights related to employee retention, department-level performance, attendance behavior, salary structures, and hiring trends. However, many organizations either do not possess integrated analytics systems or rely on manual spreadsheet-based reporting that is time-consuming, inconsistent, and incapable of predictive analysis. Furthermore, publicly available real-world HR datasets are limited due to confidentiality concerns, which creates an additional challenge for academic implementation and experimentation.

The specific problem addressed in this project can therefore be stated as follows:

**To design and implement an end-to-end HR analytics system that can generate realistic employee data, clean and transform it into reporting-ready form, compute meaningful workforce KPIs, predict attrition risk using machine learning, and present analytical outputs through a usable frontend and API layer.**

This problem contains several sub-problems:

1. Workforce data required for analytics is often unavailable or confidential.
2. Raw HR data may contain missing values, duplicate records, formatting inconsistencies, and noisy labels.
3. Decision-makers require dashboards and KPIs rather than raw tables.
4. HR managers benefit from predictive indicators, especially in attrition-sensitive departments.
5. Technical systems should be modular enough to support future integration and reuse.

The project addresses these issues by implementing a complete pipeline rather than an isolated dashboard or isolated model.

## 1.4 Objectives of the Project

The major objectives of the project are as follows:

- To create a realistic synthetic HR dataset containing employee demographic, departmental, performance, attendance, and compensation attributes.
- To simulate real-world data quality issues in order to design a meaningful cleaning pipeline.
- To build a preprocessing module that standardizes, imputes, and enriches employee data for analytics.
- To compute business-relevant KPIs such as headcount, attrition rate, average attendance, average salary, tenure metrics, and department-level distributions.
- To train and evaluate a predictive model for employee attrition.
- To develop backend APIs for structured access to analytical outputs.
- To build a browser-rendered dashboard interface for executive overview and workforce performance insights.
- To produce a reusable project architecture suitable for academic documentation and future industrial extension.

## 1.5 Scope of the Project

The scope of this project is deliberately practical and implementation-oriented. The work covers the full lifecycle of an HR analytics prototype, starting from data creation and ending with frontend display. The system has been scoped to focus on the following areas:

- Synthetic employee data generation for academic and demonstration use
- Data cleaning and quality reporting
- KPI computation from cleaned data
- Employee attrition prediction using interpretable supervised learning
- REST API development
- Browser-based dashboard representation for overview and performance analysis

At the same time, the project intentionally excludes certain enterprise-grade concerns in order to remain manageable within internship duration:

- Real employee data integration from proprietary HRMS platforms
- Production-grade authentication and authorization
- Multi-tenant deployment
- Advanced MLOps orchestration
- Payroll compliance workflows
- Deep legal and regulatory auditing features

Therefore, the project should be viewed as a robust internship-scale analytical solution that demonstrates industry-relevant design and implementation capability rather than a full enterprise HR suite.

## 1.6 Significance of the Project

The significance of the project lies in its ability to combine analytical, engineering, and reporting disciplines into a unified implementation. It demonstrates that meaningful HR intelligence does not emerge from visualization alone; it requires proper data design, preprocessing logic, predictive modeling, and accessible presentation layers. The project is academically significant because it reflects multiple computer science concepts in one system. It is also professionally significant because HR analytics is a rapidly growing area in data-driven organizations.

## 1.7 Chapter Summary

This chapter introduced the industrial context of HR analytics, explained the relevant technology domain, articulated the central problem statement, defined project objectives, and clarified the project scope. The next chapter elaborates the aim and objectives of the internship in a more structured and requirement-oriented form.

---

# CHAPTER 2: AIM AND OBJECTIVES

## 2.1 Aim of the Internship

The primary aim of this internship was to develop practical expertise in designing and implementing a real-world analytics solution that addresses a meaningful organizational problem. Specifically, the internship aimed to build an integrated HR analytics dashboard system capable of simulating workforce data, improving data quality, generating decision-support metrics, predicting employee attrition, and presenting the outputs through a modern backend-enabled reporting interface.

The internship was not limited to code implementation alone. It aimed to strengthen understanding of system thinking, modular architecture, reporting design, data engineering practices, and the translation of business questions into technical components. By working on an HR analytics project, the internship created an opportunity to connect academic concepts such as data structures, machine learning, software engineering, and API development with a practical decision-support use case.

## 2.2 Technical Objectives

The technical objectives of the internship are listed below.

### 2.2.1 Data Generation Objective

To develop a Python-based synthetic data generator that creates employee records with realistic department distributions, role hierarchies, salary variation, attendance levels, performance scores, and attrition patterns.

### 2.2.2 Data Quality Objective

To intentionally simulate noisy real-world conditions such as duplicate records, null values, text inconsistency, and unstandardized labels, thereby making the cleaning stage meaningful and realistic.

### 2.2.3 Data Cleaning Objective

To implement a robust preprocessing module capable of standardizing fields, removing duplicates, imputing missing values, deriving new features, and producing a data quality report.

### 2.2.4 Predictive Analytics Objective

To build a machine learning workflow for employee attrition prediction using interpretable modeling techniques and structured preprocessing steps.

### 2.2.5 Backend Development Objective

To create an API layer using FastAPI that can expose metrics, employee records, pipeline execution functions, and status information in a reusable manner.

### 2.2.6 Dashboard Objective

To present the processed outputs in a dashboard-like frontend with multiple analytical views, including executive overview and workforce performance.

### 2.2.7 Documentation Objective

To prepare complete technical documentation in the format of a formal B.Tech internship report that captures design rationale, implementation process, observations, and learning outcomes.

## 2.3 Functional Requirements

| Requirement ID | Functional Requirement | Description |
|---|---|---|
| FR-01 | Generate employee dataset | System should generate realistic synthetic HR records. |
| FR-02 | Inject quality issues | System should introduce duplicate rows, null values, and inconsistent labels. |
| FR-03 | Clean dataset | System should standardize, deduplicate, and impute missing values. |
| FR-04 | Derive analytical fields | System should compute tenure, employment status, joining year, and month. |
| FR-05 | Train attrition model | System should train a predictive classification model. |
| FR-06 | Produce model report | System should generate classification metrics and ROC-AUC summary. |
| FR-07 | Provide API endpoints | System should expose health, pipeline, employee, and KPI endpoints. |
| FR-08 | Render overview dashboard | System should show headcount, attrition, salary, and attendance insights. |
| FR-09 | Render performance dashboard | System should show department performance, scatter analysis, and role matrix. |
| FR-10 | Return visualization payload | System should provide frontend-ready JSON structures for charts and tables. |

## 2.4 Non-Functional Requirements

| Requirement ID | Non-Functional Requirement | Description |
|---|---|---|
| NFR-01 | Usability | Output should be understandable for non-technical stakeholders. |
| NFR-02 | Modularity | Code should be separated into scripts, API, and dashboard logic. |
| NFR-03 | Maintainability | New metrics and pages should be easy to add in future. |
| NFR-04 | Scalability | Pipeline should handle thousands of employee rows without redesign. |
| NFR-05 | Reproducibility | Synthetic generation should use fixed random seeds for consistent outputs. |
| NFR-06 | Accuracy | Cleaning and predictive outputs should be logically consistent and testable. |
| NFR-07 | Portability | Project should run on a standard Python environment. |
| NFR-08 | Readability | Documentation and code structure should be understandable for academic review. |

## 2.5 Expected Outcomes

The expected outcomes of the internship were clearly identified at the beginning of the work:

- A complete synthetic dataset containing workforce records
- A cleaned analytics-ready dataset and quality report
- A trained attrition model with evaluation summary
- A backend API exposing useful endpoints
- A dashboard-style browser frontend for HR insights
- A technically sound and academically presentable report

Beyond deliverables, the internship also aimed to produce conceptual outcomes:

- Improved understanding of real-world data problems
- Better command over backend and analytical programming
- Experience in translating organizational needs into system modules
- Ability to document engineering work in formal academic language

## 2.6 Constraints Considered During the Internship

The project was planned within several realistic constraints:

- Limited internship duration
- Absence of real confidential employee data
- Need to produce demonstrable results without enterprise HR software access
- Requirement to maintain academic clarity while implementing practical logic

These constraints influenced the architecture, leading to the use of synthetic data generation, modular scripts, and a lightweight API-driven frontend.

## 2.7 Chapter Summary

This chapter translated the broad project purpose into clearly defined aims, technical objectives, functional requirements, non-functional requirements, and expected outcomes. The next chapter reviews the literature and technology landscape relevant to HR analytics and predictive workforce systems.

---

# CHAPTER 3: LITERATURE REVIEW

## 3.1 Introduction to Literature Review

The purpose of the literature review is to understand the current state of HR analytics systems, identify existing tools and methods, compare relevant technologies, and recognize the research and implementation gaps that motivate this project. HR analytics is a multidisciplinary area, drawing from management science, business intelligence, data mining, statistical analysis, machine learning, and information systems engineering.

## 3.2 Existing Systems in HR Analytics

Several types of systems currently exist in the HR technology landscape. These systems vary in complexity, accessibility, and technical capability.

### 3.2.1 Traditional Spreadsheet-Based Reporting

Many small and medium organizations continue to use spreadsheets for HR reporting. In such systems, attendance, payroll, joining details, and exit records are exported manually from multiple tools and consolidated through spreadsheet formulas or pivot tables.

**Advantages**

- Low entry cost
- Easy to understand for non-technical users
- Useful for static periodic reports

**Limitations**

- High dependence on manual effort
- Prone to version control and human errors
- Weak scalability
- No predictive capability
- Poor integration with automated services

### 3.2.2 HRMS and ERP-Based Reporting Systems

Enterprise organizations often use HRMS and ERP systems such as SAP SuccessFactors, Oracle HCM, Workday, or Zoho People. These platforms provide structured employee management, attendance monitoring, leave management, payroll integration, and some analytics features.

**Advantages**

- Centralized data management
- Strong process integration
- Role-based access and enterprise controls
- Rich operational capabilities

**Limitations**

- Costly for small organizations
- Custom analytics may require specialized setup
- Limited flexibility in academic experimentation
- Real organizational data cannot be easily shared for student projects

### 3.2.3 BI Dashboard Solutions

Tools such as Power BI, Tableau, and Looker are widely used for HR dashboards. These tools excel at presenting KPIs, interactive filters, drill-downs, and visual storytelling.

**Advantages**

- Strong dashboarding capabilities
- Easy stakeholder consumption
- Rich visualization ecosystem
- Effective for presentations and decision reviews

**Limitations**

- Dependence on upstream data quality
- Usually descriptive rather than predictive unless extended
- Often require external pipelines for cleaning and feature preparation

### 3.2.4 Predictive HR Analytics Solutions

Some advanced organizations and research-oriented implementations apply machine learning to estimate attrition risk, absenteeism, or performance categories. These systems often use classification algorithms, survival analysis, decision trees, or ensemble models.

**Advantages**

- Provides proactive rather than purely descriptive insights
- Helps identify risk segments early
- Supports strategic workforce planning

**Limitations**

- Requires good historical data
- Model bias and interpretability concerns
- Difficult to implement without pipeline discipline

## 3.3 Review of Current Technologies

### 3.3.1 Python for Analytical Systems

Python is widely used in data-centric applications because it provides mature libraries for data processing, numerical computing, statistical analysis, and backend services. Pandas simplifies tabular transformation, NumPy supports vectorized operations, and Scikit-learn offers standardized model-building workflows.

### 3.3.2 FastAPI for Service Layer Development

FastAPI has become a popular framework for modern Python APIs due to its speed, clear type annotations, automatic documentation support, and developer productivity. Compared to heavier frameworks, FastAPI is highly suitable for internship-level and prototype analytics systems where quick iteration and structured JSON responses are important.

### 3.3.3 Machine Learning for Attrition Prediction

Attrition prediction is commonly framed as a binary classification problem. Logistic regression remains a valuable baseline model because it is interpretable, computationally efficient, and appropriate for structured tabular data. More complex methods such as random forests, XGBoost, or neural networks may improve predictive power but often reduce interpretability.

### 3.3.4 Dashboard-Centric Reporting

Modern reporting systems rely on dashboard patterns that balance KPI summary, trend visualization, comparative analysis, filtering, and tabular detail. The challenge is not only to produce graphs but to structure them in a way that decision-makers can quickly interpret.

## 3.4 Comparative Analysis of Existing Approaches

| Approach | Data Quality Handling | Predictive Capability | Dashboard Readiness | Cost / Accessibility | Suitability for Academic Project |
|---|---|---|---|---|---|
| Spreadsheet Reporting | Low | None | Limited | Very High Accessibility | Moderate |
| ERP / HRMS Reporting | Medium to High | Medium | High | Expensive | Low |
| Standalone BI Dashboard | Medium | Low | Very High | Medium | High |
| ML-Only Attrition Model | Low | High | Low | Medium | Moderate |
| Integrated Analytics Pipeline | High | High | High | High for custom effort | Very High |

## 3.5 Research Gaps

The literature and technology review reveal several implementation gaps that justify the present project.

### 3.5.1 Lack of End-to-End Academic HR Analytics Implementations

Many academic mini-projects focus only on visualization or only on predictive modeling. Very few demonstrate the complete sequence from data generation to cleaning, feature engineering, model training, API delivery, and frontend rendering.

### 3.5.2 Insufficient Emphasis on Data Quality

In many sample projects, datasets are assumed to be perfectly clean. This is unrealistic. Actual workforce data often contains missing values, duplicates, inconsistent department naming, and incomplete demographic fields. Ignoring data quality leads to unrealistic analytics systems.

### 3.5.3 Limited Reusable Backend Integration

Several dashboard projects are tightly bound to specific visualization tools and do not expose reusable APIs. This reduces extensibility and makes integration with other systems more difficult.

### 3.5.4 Weak Focus on Explainable Predictive Modeling

Complex models may produce predictions, but without interpretability they are harder to justify in HR contexts. There is a need for solutions that balance predictive insight with explainable modeling choices.

### 3.5.5 Limited Availability of Safe Demonstration Data

Because actual employee records are sensitive, many students lack access to realistic datasets. Synthetic data generation is therefore an important contribution in educational implementations.

## 3.6 Relevance of the Present Project

The present project addresses the identified gaps in a structured manner:

- It builds an end-to-end workflow rather than a single isolated module.
- It begins with synthetic yet realistic data generation.
- It models real-world data quality problems and solves them through preprocessing.
- It combines KPI reporting with predictive analytics.
- It exposes outputs via APIs and displays them in a dashboard interface.
- It remains interpretable, modular, and appropriate for internship-level demonstration.

## 3.7 Summary of Tools and Methods Considered

| Category | Tool / Method | Reason for Consideration |
|---|---|---|
| Programming Language | Python | Strong ecosystem for analytics and APIs |
| Data Handling | Pandas | Effective tabular transformation |
| Numerical Support | NumPy | Efficient sampling and numeric operations |
| Synthetic Data | Faker | Realistic record generation |
| ML Pipeline | Scikit-learn | Standard preprocessing and modeling |
| Backend API | FastAPI | Lightweight and structured service development |
| Environment | Virtual Environment | Reproducible setup |
| Frontend Rendering | HTML/CSS/JavaScript in FastAPI response | Simple deployment and quick demonstration |

## 3.8 Critical Observations from Literature

The literature suggests that successful HR analytics solutions must satisfy four conditions:

1. Data must be reliable enough to support analysis.
2. Metrics must align with organizational decision needs.
3. Predictive outputs must be explainable and responsibly interpreted.
4. Insights must be consumable by decision-makers through visual interfaces.

Projects that ignore any one of these conditions often remain incomplete or impractical. This observation directly informed the architecture of the present system.

## 3.9 Chapter Summary

This chapter reviewed existing HR reporting practices, current technologies, comparative approaches, and implementation gaps. The analysis established the need for an integrated HR analytics pipeline with cleaning, prediction, API exposure, and dashboard support. The next chapter explains how this project was actually designed and implemented.

---

# CHAPTER 4: METHODOLOGY

## 4.1 Introduction

This chapter is the core of the project report because it explains the technical methodology followed to convert an abstract problem statement into a functioning HR analytics system. The methodology was designed according to modular software engineering principles. Instead of building a single monolithic script, the project was divided into separate components for data generation, data cleaning, predictive modeling, API services, and frontend visualization. This modular structure improved maintainability, testability, and conceptual clarity.

The project followed a practical mini-SDLC approach consisting of:

1. Problem understanding and scope definition
2. Dataset design
3. Synthetic data generation
4. Data quality issue injection
5. Cleaning and transformation
6. Feature engineering
7. Predictive model training
8. API exposure
9. Frontend dashboard rendering
10. Result validation and documentation

## 4.2 Overall System Architecture

The architecture of the system can be described as a linear-yet-modular analytics pipeline. Each stage produces an output that becomes the input to the next stage.

**Generated figure files for this report section:**

- `docs/figures/system_architecture.svg`
- `docs/figures/data_flow_pipeline.svg`

### 4.2.1 Architectural Layers

| Layer | Description | Main Components |
|---|---|---|
| Data Creation Layer | Generates synthetic HR records with realistic distributions | `generate_hr_data.py` |
| Data Quality Layer | Injects duplicates, nulls, and inconsistencies | Quality injection logic in generator |
| Preprocessing Layer | Cleans, standardizes, imputes, and enriches data | `clean_hr_data.py` |
| Analytics Layer | Computes KPI-oriented aggregations | API visual payload builder |
| Predictive Layer | Trains attrition prediction model | `train_attrition_model.py` |
| Service Layer | Exposes pipeline and metrics through API | `api/main.py` |
| Presentation Layer | Displays dashboard pages in browser | HTML/CSS/JS embedded in FastAPI |

### 4.2.2 Architecture Narrative

The first module creates a dataset of 6,000 employee records. These records contain demographic attributes, department assignments, role labels, salary values, joining dates, attrition labels, attendance percentages, performance ratings, and locations. Once the base dataset is created, realistic quality issues are intentionally introduced. This allows the second module to operate on data that resembles real-world conditions rather than idealized tables.

The cleaning module removes duplicate rows, standardizes categorical text, fills missing values using departmental statistics, clips numeric ranges, and derives new fields such as tenure, employment status, joining year, and joining month. The cleaned file then becomes the central analytical dataset.

After cleaning, a machine learning pipeline trains a logistic regression model to predict attrition. The model uses both numerical and categorical features after suitable preprocessing. Performance metrics are generated and saved as a report.

The API layer then loads the cleaned data and generated reports, computes chart-friendly structures, and exposes them through endpoints. The root route provides a browser interface from which the user can run the entire pipeline and view the outputs interactively.

### 4.2.3 Architecture Figure Note

The generated architecture image `system_architecture.svg` visually summarizes the layered structure of the project. It shows how the data creation layer, data quality layer, preprocessing layer, predictive layer, service layer, and presentation layer are connected in sequence. This figure should be used in the final Word submission where the report refers to the overall system architecture.

### 4.2.4 Data Flow Figure Note

The generated data flow image `data_flow_pipeline.svg` explains how information moves through the system from raw data generation to cleaned outputs, model training, API payload preparation, dashboard rendering, and final report review. This figure is particularly useful for methodology explanation because it reflects the operational order of the pipeline.

## 4.3 Module-Wise Methodology

## 4.3.1 Data Generation Module

The data generation module was designed to simulate a realistic workforce distribution rather than random disconnected values. This design choice was important because meaningful analytics depends on believable relationships between variables.

### Inputs Considered in Data Generation

- Department composition
- Role composition inside each department
- Salary ranges by department
- Age distribution
- Gender distribution
- Location distribution
- Joining date range
- Performance tendencies by department
- Attendance variation
- Attrition risk dependency on multiple factors

### Department Specification Logic

The project defines departmental structures with explicit headcount shares, salary bands, and role distributions. Example departments include Engineering, Sales, Human Resources, Finance, Marketing, Operations, and Customer Support. Each department contains a weighted distribution of relevant job roles.

This approach ensures that:

- Engineering has higher salary ranges than support functions
- Sales and support departments show different attrition pressures
- Leadership-oriented roles receive higher salary multipliers
- Dataset composition resembles a plausible medium-to-large organization

### Performance Rating Generation

Performance ratings are not assigned uniformly. Instead, each department has a probability distribution over ratings from 1 to 5. This creates realistic differences across departments and avoids artificial balance.

### Attendance Generation Logic

Attendance percentage is derived from a baseline formula influenced by performance rating, tenure, and attrition bias. Better-performing employees and long-tenure employees tend to have higher attendance, while employees with attrition tendency receive a downward adjustment. A normal distribution adds controlled variability. Values are clipped within realistic bounds.

### Salary Generation Logic

Salary generation uses:

- Department salary range
- Role-based multipliers
- Experience factor from tenure
- Age effect
- Performance factor

As a result, salary is not random but structurally linked to role seniority and employee characteristics.

### Attrition Generation Logic

Attrition is generated probabilistically. The probability combines multiple components:

- Lower salary relative to department midpoint increases risk
- Early tenure increases risk
- Lower performance strongly increases risk
- Lower attendance increases risk
- Some departments inherently carry higher churn pressure

This logic makes the later prediction problem meaningful because the target variable is driven by understandable relationships.

### Simplified Pseudocode for Data Generation

```text
For each employee from 1 to N:
    Choose department using weighted probabilities
    Choose role based on department-specific role weights
    Generate age, gender, and location
    Assign joining date within the last 10 years
    Compute tenure from joining date
    Derive performance rating using department distribution
    Derive attendance using performance, tenure, and bias
    Derive salary using department range, role, age, performance, tenure
    Compute attrition probability using performance, attendance, salary, tenure, department
    If attrition = Yes:
        generate exit date
    Save employee row
Inject duplicates, nulls, and inconsistent category formatting
Export raw CSV
```

## 4.3.2 Data Cleaning Module

The cleaning module is responsible for transforming raw employee data into a trustworthy analytical dataset.

### Cleaning Operations Performed

| Operation | Purpose |
|---|---|
| Duplicate removal | Eliminate repeated employee rows |
| Date parsing | Convert joining and exit fields into datetime format |
| Department normalization | Standardize naming variations |
| Gender normalization | Replace missing values and enforce title case |
| Location cleaning | Remove formatting inconsistencies |
| Attrition normalization | Convert all labels to Yes / No |
| Salary imputation | Fill missing salary using department median |
| Attendance imputation | Fill missing attendance using department median |
| Range clipping | Keep age, performance, and attendance within valid limits |
| Feature derivation | Create tenure, employment status, join year, and join month |

### Why Median Imputation Was Used

Median imputation was preferred over mean imputation for salary and attendance because it is less sensitive to extreme values. Departments may contain high-salary senior roles and low-salary entry roles; the median provides a more stable fallback estimate than the arithmetic mean.

### Derived Features

The following derived features were added:

- `tenure_years`
- `employment_status`
- `join_year`
- `join_month`

These fields improve both analytics and model readiness. For example, `employment_status` supports dashboard filters, while `tenure_years` is useful for attrition prediction.

### Data Quality Report

The cleaning script generates a structured quality report in JSON form containing:

- Input row count
- Output row count
- Number of duplicates removed
- Missing values after cleaning
- Attrition rate percentage
- Average attendance percentage

This report improves auditability and makes the cleaning stage measurable rather than opaque.

## 4.3.3 Predictive Modeling Module

The predictive module was designed to estimate employee attrition using an interpretable supervised learning pipeline.

### Problem Framing

Attrition prediction is formulated as a binary classification problem where:

- `Yes` indicates an employee left the organization
- `No` indicates an employee remained active

### Features Used

| Feature Category | Features |
|---|---|
| Demographic | age, gender |
| Organizational | department, job_role, location |
| Economic | salary |
| Behavioral | attendance_percentage |
| Assessment | performance_rating |
| Career | tenure_years |

### Target Variable

`attrition_flag`, derived by mapping:

- `Yes -> 1`
- `No -> 0`

### Preprocessing Pipeline

The machine learning pipeline uses separate transformations for numeric and categorical features.

**Numeric pipeline**

- Median imputation
- Standard scaling

**Categorical pipeline**

- Most frequent imputation
- One-hot encoding with unknown-category handling

### Model Selection

Logistic Regression was selected because:

- It is computationally efficient
- It works well for structured tabular data
- It is easier to interpret than many complex models
- It provides class probabilities
- It is appropriate for internship-level explainable analytics

### Training Strategy

The cleaned dataset is split into training and testing data using stratified sampling. Stratification ensures that the proportion of attrition cases is preserved in both sets. The test size is 25%, and a fixed random state is used for reproducibility.

### Evaluation Metrics

The model report includes:

- ROC-AUC
- Precision
- Recall
- F1-score
- Support counts
- Positive target rate

These metrics together provide a balanced picture of predictive performance.

### Simplified Pseudocode for Model Training

```text
Load cleaned dataset
Map attrition labels to binary target
Select feature columns
Split data into train and test sets using stratification
Create numeric preprocessing pipeline
Create categorical preprocessing pipeline
Combine pipelines in a column transformer
Build logistic regression classifier pipeline
Fit model on training data
Predict labels and probabilities on test data
Compute ROC-AUC and classification metrics
Save model report to JSON
```

### Detailed Explanation of Logistic Regression Usage in This Project

Logistic Regression was used in this project as the core supervised learning model for employee attrition prediction. The purpose of the model was not to make final HR decisions automatically, but to estimate the likelihood that an employee may leave the organization based on structured workforce attributes. This made the model suitable for decision support rather than direct action. The project intentionally selected Logistic Regression because it is interpretable, computationally efficient, and academically appropriate for tabular business data.

The model was trained on the cleaned employee dataset generated by the preprocessing pipeline. Before training, the target field `attrition` was transformed into a binary variable named `attrition_flag`, where employees marked as `Yes` were encoded as `1` and employees marked as `No` were encoded as `0`. This conversion allowed the classification algorithm to learn a probability boundary between two business outcomes: likely to stay and likely to leave.

The feature set combined several types of employee information. Numeric variables such as age, salary, attendance percentage, performance rating, and tenure years represented continuous behavioral and economic signals. Categorical variables such as department, job role, gender, and location represented organizational context. This combination was important because attrition is not driven by a single factor. In the project design, attrition tendencies were influenced by attendance, performance, compensation level, department pressure, and employee tenure, so the model needed to observe these variables together.

To prepare these features correctly, the project used a preprocessing pipeline before the Logistic Regression estimator. Numeric columns passed through median imputation and standard scaling. Median imputation helped preserve records even when some values were missing, while scaling kept large-value columns such as salary from dominating smaller-scale variables. Categorical columns passed through most-frequent imputation and one-hot encoding. One-hot encoding transformed text-based categories into machine-readable indicator columns and allowed the model to work with departments and roles without imposing an incorrect numeric order on them.

The dataset was then divided into training and testing subsets using stratified sampling. Stratification was necessary because attrition classes can be imbalanced. By preserving the class ratio in both subsets, the evaluation remained more reliable. The model was trained on the training subset and evaluated on the testing subset, which helped measure generalization instead of memorization.

After fitting the pipeline, the Logistic Regression model produced both predicted labels and predicted probabilities. The probability output was especially useful for this project because HR analytics often needs risk scoring rather than only yes-or-no classification. A probability such as `0.72` is more informative than a hard class label because it allows the dashboard or report to interpret risk as a spectrum. This matches the project goal of building a decision-support system rather than a rigid automation tool.

Model performance was evaluated using ROC-AUC, precision, recall, F1-score, support counts, and positive class rate. ROC-AUC was included because it measures how well the model separates attrition and non-attrition cases across thresholds. Precision and recall were useful because an attrition model must balance false alarms with missed high-risk employees. F1-score summarized that tradeoff in a single value. These metrics were saved into a JSON report so that the API and dashboard layer could expose them as part of the project output.

In practical terms, Logistic Regression supported the project in three ways. First, it demonstrated how cleaned HR data can be transformed into predictive insight. Second, it provided interpretable probabilities that fit well into dashboard reporting. Third, it allowed the internship project to connect data engineering, machine learning, API design, and business reporting into one coherent workflow. For these reasons, Logistic Regression was an appropriate and effective modeling choice for the HR Analytics Dashboard with Predictive Attrition Analysis.

## 4.3.4 API Module

The API module was built using FastAPI and serves as the communication bridge between processing logic and frontend consumption.

### API Responsibilities

- Load cleaned data and generated reports
- Run the full pipeline on demand
- Return health status
- Return employee records
- Return KPI summary
- Return visual payloads for frontend charts

### Endpoints Implemented

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Serves browser-based dashboard interface |
| `/health` | GET | Returns service health status |
| `/pipeline/status` | GET | Returns processed output if available |
| `/pipeline/run` | POST | Executes generation, cleaning, and modeling pipeline |
| `/employees` | GET | Returns employee records from analytical source |
| `/kpis` | GET | Returns KPI summary structure |

### Visualization Payload Design

Instead of forcing the frontend to compute all charts, the backend prepares structured payloads such as:

- department counts
- attrition split
- hiring trend
- average attendance by department
- average salary by department
- average performance by department
- performance scatter points
- role matrix rows

This design reduces frontend complexity and keeps business logic centralized.

## 4.3.5 Frontend Visualization Module

The presentation layer is rendered within the browser through HTML, CSS, and JavaScript embedded in the FastAPI root response. This design was selected to keep deployment simple while still providing an interactive dashboard experience.

### Pages Implemented

#### Executive Overview Page

This page focuses on high-level metrics and organizational summaries:

- Raw rows
- Clean rows
- Duplicates removed
- Attrition rate
- Average attendance
- ROC-AUC
- Department headcount
- Attrition split
- Hiring trend
- Salary and attendance summaries

#### Workforce Performance Page

This page focuses on behavior and performance relationships:

- Average performance KPI cards
- Top-performing department
- Department-wise performance bar chart
- Attendance vs performance scatter chart
- Department and role matrix table

#### Data Quality Report Page

This page focuses on the measurable results of the cleaning pipeline and makes preprocessing outcomes visible to the user:

- Input row count
- Clean row count
- Duplicates removed
- Missing value summary
- Field-level data quality table
- Department-wise quality impact summary

#### Final Output Report Page

This page focuses on the final processed output in a report-friendly structure for review and presentation:

- Final employee summary table
- Department-wise employee count
- Attrition count
- High performer count
- Attendance and performance summary cards

### Frontend Design Logic

The dashboard uses:

- card-based layout for KPIs
- responsive grid structure
- SVG-based line and scatter charts
- dynamically generated tables
- page switching between overview, performance, data quality, and final output views

This design offers a report-like dashboard while remaining lightweight.

## 4.4 Workflow of the Complete System

The following step-by-step workflow summarizes the methodology:

1. User initiates or triggers the pipeline.
2. System generates synthetic raw HR data.
3. Raw data is exported to the raw data folder.
4. Cleaning module removes duplicates and normalizes values.
5. Missing fields are imputed using department-level medians.
6. Derived columns are created for tenure and reporting.
7. Clean data and quality report are saved.
8. Predictive model training begins using cleaned data.
9. Model metrics are generated and saved as JSON.
10. API loads cleaned data and reports.
11. Backend computes chart-friendly analytical structures.
12. Frontend requests and displays results interactively.

## 4.5 Data Flow Explanation

The system follows a controlled data flow.

### Stage 1: Raw Data Flow

Synthetic employee records are produced and written as a CSV file in the raw data directory. At this stage, data still contains duplicates, missing values, and inconsistencies.

### Stage 2: Clean Data Flow

The raw CSV is read into a Pandas DataFrame. Cleaning transforms are applied, and the cleaned output is written to a cleaned data directory. A separate JSON report stores quality metrics.

### Stage 3: Model Data Flow

The cleaned CSV becomes the model input. Feature columns and target labels are extracted, transformed, and passed through the classification pipeline. The model report is saved to a processed-data directory.

### Stage 4: API Data Flow

The API reads the cleaned CSV and the JSON reports, generates aggregate structures, and serves them to consumers.

### Stage 5: Presentation Data Flow

The frontend triggers the pipeline, receives a JSON payload, and renders KPIs, charts, and tables for the user.

## 4.6 Algorithmic Logic and Design Decisions

### 4.6.1 Use of Random Seed

Random seed control was used to make synthetic data generation reproducible. Reproducibility is important for academic validation because it ensures that repeated executions produce comparable results.

### 4.6.2 Weighted Sampling

Simple random sampling would not create realistic workforce composition. Weighted sampling was therefore used for departments, roles, genders, and locations.

### 4.6.3 Department-Specific Behavior Modeling

Different departments naturally behave differently in real organizations. For example, Sales and Customer Support often experience different attrition pressures compared to Finance. The project reflects this through department-specific performance and attrition logic.

### 4.6.4 Model Interpretability

Although more advanced algorithms could have been considered, logistic regression was selected due to interpretability and educational appropriateness. In HR-related decisions, simpler and explainable models are often preferable to opaque black-box methods.

### 4.6.5 Dashboard-Oriented Backend Aggregation

Preparing aggregations in the backend improves code organization and separates metric logic from rendering logic. This makes the frontend simpler and keeps analytical definitions consistent across pages.

## 4.7 Tech Stack Justification

| Technology | Role in Project | Justification |
|---|---|---|
| Python | Core development language | Rich support for analytics, scripting, and APIs |
| Pandas | Data cleaning and transformation | Best suited for tabular preprocessing |
| NumPy | Probability and numerical operations | Efficient mathematical support |
| Faker | Synthetic data generation | Creates realistic names and dates |
| Scikit-learn | Machine learning pipeline | Standardized ML workflow and evaluation |
| FastAPI | API and frontend delivery | Fast, structured, and easy to maintain |
| HTML/CSS/JavaScript | Frontend rendering | Lightweight browser-side visualization |
| JSON | Structured report storage | Human-readable and integration-friendly |

## 4.8 Methodological Strengths

The implemented methodology has several strengths:

- End-to-end coverage from data creation to visualization
- Clear modular separation
- Inclusion of real-world data quality challenges
- Interpretable predictive modeling
- Dashboard-oriented service design
- Strong academic demonstrability

## 4.9 Methodological Limitations

Even though the methodology is strong for an internship project, certain limitations remain:

- The data is synthetic, not real organizational data.
- Model validation is limited to generated data patterns.
- Authentication and production deployment concerns are not central to the current implementation.
- The frontend is optimized for demonstration rather than enterprise UX depth.

## 4.10 Chapter Summary

This chapter presented the complete methodology of the project, including architecture, modules, workflows, algorithms, data flow, API design, and technology justification. The methodology reflects a practical engineering approach aligned with the project objectives. The next chapter discusses implementation results, observations, challenges, and performance analysis.

---

# CHAPTER 5: RESULTS AND DISCUSSION

## 5.1 Introduction

This chapter presents the outcomes of the implemented system and evaluates how effectively the project objectives were achieved. The discussion is based on the outputs produced by the synthetic data pipeline, cleaned dataset, model report, and frontend views.

## 5.2 Testing Methods

The project was validated using a combination of functional testing, output verification, and logic consistency checks.

### 5.2.1 Functional Testing

Functional testing focused on whether each module performed its intended task correctly:

- data generation script created raw CSV output
- cleaning script produced cleaned CSV and quality report
- model script generated model report JSON
- API served responses correctly
- frontend rendered overview and performance pages

### 5.2.2 Data Validation Testing

Data validation checks included:

- duplicate row removal confirmation
- missing value handling verification
- category normalization checks
- valid numeric range enforcement
- correct derivation of tenure and employment status

### 5.2.3 Model Validation Testing

Model evaluation was performed through standard classification metrics, especially ROC-AUC and class-wise precision and recall.

### 5.2.4 UI Testing

Browser-side testing checked:

- page switching behavior
- chart rendering
- table rendering
- pipeline trigger response
- readability on standard screen layouts

## 5.3 Results Obtained

The implemented system produced the following major outputs:

| Output | Result |
|---|---|
| Raw employee dataset | Generated successfully with synthetic quality issues |
| Cleaned dataset | Produced successfully with standardized fields |
| Data quality report | Generated with row counts and quality indicators |
| Attrition model report | Generated with ROC-AUC and classification metrics |
| API endpoints | Implemented and structured |
| Overview dashboard page | Implemented and rendered |
| Performance dashboard page | Implemented and rendered |
| Data quality report page | Added to reporting design |
| Final output report page | Added to reporting design |

### 5.3.1 Dataset Result

The raw dataset generation stage successfully created thousands of employee records across multiple departments and locations. The records included realistic attributes such as role, salary, performance, attendance, joining date, and attrition status. The intentional addition of null values and duplicates made the cleaning stage non-trivial.

### 5.3.2 Cleaning Result

The cleaning module successfully:

- removed duplicate records
- standardized department names
- normalized attrition labels to Yes and No
- filled missing salary values
- filled missing attendance values
- replaced missing gender with a neutral category
- derived useful reporting fields

The quality report provided measurable confirmation that the transformed dataset was suitable for downstream analysis.

### 5.3.3 Predictive Result

The attrition model successfully generated probabilities and evaluation metrics. Since the target variable was created from meaningful synthetic relationships, the model was able to detect useful patterns. The ROC-AUC metric reflected reasonable separability between attrition and non-attrition cases for an internship-scale analytical system.

### 5.3.4 Frontend Result

The frontend successfully displayed:

- KPI cards for executive summary
- trend and comparison visuals
- performance-focused analytical page
- data preview and role-wise matrix structures

The browser interface improved the demonstrability of the project significantly because it allowed results to be viewed immediately after running the pipeline.

## 5.4 Performance Analysis

Performance analysis in this context refers not only to computational performance but also to analytical usefulness.

### 5.4.1 Computational Performance

The system was designed for moderate dataset volumes such as thousands of employee records. Under this scope, the scripts are expected to run efficiently on a standard student development system. The use of vectorized Pandas operations and Scikit-learn pipelines helps maintain acceptable performance.

### 5.4.2 Analytical Performance

The system supports useful business insights such as:

- identifying departments with higher attrition pressure
- comparing attendance across departments
- examining relationship between performance and attendance
- finding top-performing departments
- observing salary and workforce distribution differences

### 5.4.3 Frontend Utility Performance

The value of the frontend lies in how quickly a decision-maker can interpret results. The card layout, chart grouping, and separate page logic improved clarity by preventing overcrowding of information.

## 5.5 Challenges Faced

Several technical and conceptual challenges were encountered during the project.

### 5.5.1 Realistic Data Design

Creating synthetic data that feels realistic is harder than generating random rows. The challenge was to ensure that salary, performance, tenure, and attrition interacted in believable ways.

### 5.5.2 Balancing Simplicity and Realism

An internship project must remain implementable in limited time, yet it should not be oversimplified. Balancing these two demands required careful decisions about scope.

### 5.5.3 Data Cleaning Logic

Cleaning should be strong enough to improve data quality without destroying useful variation. Choosing appropriate imputation and normalization logic was therefore important.

### 5.5.4 Model Choice

Using a simple model supports interpretability, but may not produce the highest possible predictive accuracy. This required balancing educational clarity with analytical ambition.

### 5.5.5 Frontend Integration

The frontend had to remain lightweight while still presenting multiple analytical views. Designing chart payloads in the backend reduced complexity but required thoughtful data shaping.

## 5.6 Limitations of the Project

The project has the following limitations:

- It uses synthetic rather than real enterprise HR data.
- Model findings should not be treated as production HR decisions.
- The system does not include role-based user authentication.
- The frontend is demonstration-oriented and not a full BI platform.
- Long-term deployment, CI/CD, and production monitoring are outside current scope.

## 5.7 Improvements That Can Be Made

The following improvements can enhance the project:

- integration with real HRMS exports
- richer predictive models and feature importance analysis
- department-level drill-down filtering in frontend
- export to PDF / Excel reports
- authentication and user roles
- containerized deployment
- scheduled automated pipeline execution
- alerting for high-risk attrition segments

## 5.8 Discussion

The project successfully demonstrates that useful HR analytics systems require engineering discipline, not only charting tools. The strongest aspect of the project is its end-to-end integration. The combination of synthetic data generation, preprocessing, predictive modeling, API delivery, and frontend rendering makes the system academically rich and technically coherent.

The project also highlights an important lesson: data quality directly shapes analytical reliability. Without cleaning and derived fields, both dashboards and models would be less meaningful. Similarly, predictive analytics becomes more useful when coupled with a reporting layer that enables interpretation by users.

## 5.9 Chapter Summary

This chapter evaluated the outputs and practical effectiveness of the project. The results confirm that the system met the main project objectives and produced demonstrable analytical value. The next chapter concludes the report with summary observations, achievements, learning outcomes, and future scope.

---

# CHAPTER 6: CONCLUSION

## 6.1 Summary of the Work

This internship project focused on the design and development of a complete HR analytics solution titled **"HR Analytics Dashboard with Predictive Attrition Analysis."** The project addressed a relevant organizational problem: the need for structured workforce insights and attrition-aware decision support. The work began with synthetic data generation, progressed through data cleaning and transformation, incorporated machine learning for attrition prediction, exposed metrics through APIs, and presented outputs through a browser-based dashboard interface.

The project was successful in demonstrating how software engineering, analytics, and machine learning can be combined within a single coherent application. Rather than treating analytics as a visualization-only task, the project approached it as an end-to-end system problem requiring robust data preparation, logical modeling, and accessible reporting.

## 6.2 Achievements

The major achievements of the project are summarized below:

- Developed a realistic synthetic HR dataset generator
- Incorporated real-world data quality issues intentionally
- Built a preprocessing pipeline with measurable cleaning outputs
- Implemented an attrition prediction workflow using logistic regression
- Created structured backend endpoints using FastAPI
- Designed and rendered overview and performance dashboard pages
- Extended the reporting design with data quality and final output pages
- Produced a project architecture that is modular and extensible
- Documented the complete work in formal academic format

## 6.3 Learning Outcomes

The internship contributed significantly to technical and professional learning.

### Technical Learning

- deeper understanding of data preprocessing workflows
- practical use of Pandas and NumPy for tabular engineering
- experience with Scikit-learn pipelines for classification
- backend API design using FastAPI
- frontend data rendering using browser-based components
- improved software modularization and project structuring

### Analytical Learning

- importance of feature relationships in synthetic data generation
- impact of data quality on downstream insights
- value of interpretable models in sensitive domains like HR
- need to align technical outputs with business questions

### Documentation Learning

- formal academic report structuring
- technical writing in professional style
- presenting implementation logic and results coherently

## 6.4 Future Scope

The project offers substantial future scope for academic extension and industrial enhancement.

### 6.4.1 Real Data Integration

The system can be adapted to consume actual HR exports from attendance systems, payroll records, or employee management platforms after applying privacy controls.

### 6.4.2 Advanced Predictive Analytics

Future versions can include ensemble learning, explainability dashboards, survival analysis, or role-specific attrition models.

### 6.4.3 Interactive Dashboard Expansion

Additional pages can be introduced for compensation analytics, attendance heatmaps, location-level trends, and hiring funnel analysis.

### 6.4.4 Deployment and Automation

The project can be containerized and deployed on cloud infrastructure. Scheduled batch processing and alert systems can also be integrated.

### 6.4.5 Responsible AI Features

Bias analysis, fairness monitoring, and human-in-the-loop review mechanisms can be added before any real-world HR decision support use.

## 6.5 Final Conclusion

In conclusion, the internship project successfully fulfilled its academic and technical objectives by delivering a practical HR analytics platform that combines synthetic data engineering, preprocessing, machine learning, API services, and visualization. The project reflects not only coding ability, but also an understanding of system design, domain relevance, and analytical thinking. It serves as a strong demonstration of internship learning and as a solid foundation for future work in analytics engineering, data science, and intelligent enterprise systems.

---

# REFERENCES

1. Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, O'Reilly Media, 3rd Edition, 2022.
2. Wes McKinney, *Python for Data Analysis*, O'Reilly Media, 3rd Edition, 2022.
3. Scikit-learn Developers, "Scikit-learn User Guide," official documentation.
4. Pandas Development Team, "Pandas Documentation," official documentation.
5. FastAPI Documentation, "FastAPI Framework Reference," official documentation.
6. NumPy Developers, "NumPy Reference Guide," official documentation.
7. Faker Documentation, "Faker Python Package Documentation," official documentation.
8. Bernard Marr, *Data-Driven HR: How to Use Analytics and Metrics to Drive Performance*, Kogan Page.
9. Cole Nussbaumer Knaflic, *Storytelling with Data*, Wiley.
10. Jason Brownlee, *Machine Learning Mastery with Python*, Machine Learning Mastery resources.
11. Tom Mitchell, *Machine Learning*, McGraw-Hill.
12. Research and product literature on people analytics, employee retention, and dashboard-oriented decision systems from publicly accessible academic and technical sources.

---

# ANNEXURES

## Annexure A: Organisation Profile

### A.1 Organisation Name

Self Project / Academic Internship Project

### A.2 Nature of Work

The project was undertaken as a self-driven academic internship exercise to simulate industry-relevant software development and analytical implementation. The work environment emphasized problem identification, modular engineering, documentation quality, and practical output generation.

### A.3 Domain of Work

- HR Analytics
- Data Processing
- Machine Learning
- Backend API Development
- Dashboard-Oriented Reporting

### A.4 Purpose of the Organisation Profile in This Report

Since the project was self-executed rather than hosted in a commercial company, the organisation profile represents the technical environment and project scope rather than a traditional corporate structure.

## Annexure B: Internship Details

| Item | Details |
|---|---|
| Internship Title | HR Analytics Dashboard with Predictive Attrition Analysis |
| Internship Type | Academic / Self Project |
| Duration | January 2026 - April 2026 |
| Role | Full Stack Data Analytics Developer |
| Area of Work | Data generation, preprocessing, machine learning, API development, frontend dashboard |
| Major Deliverables | Dataset pipeline, model report, API layer, dashboard frontend, documentation |

## Annexure C: Weekly Work Log

| Week | Work Carried Out | Outcome |
|---|---|---|
| Week 1 | Problem identification, requirement analysis, project planning | Defined scope and selected HR analytics use case |
| Week 2 | Studied HR analytics workflows and dashboard requirements | Finalized architecture and project modules |
| Week 3 | Designed synthetic workforce schema and variable relationships | Prepared generation logic structure |
| Week 4 | Implemented employee data generation module | Raw dataset generation achieved |
| Week 5 | Added realistic noise, duplicates, and missing values | Raw data quality simulation completed |
| Week 6 | Developed cleaning and preprocessing logic | Clean dataset and quality report generated |
| Week 7 | Created feature engineering and derived fields | Analytics-ready dataset finalized |
| Week 8 | Implemented logistic regression attrition modeling pipeline | Model training and evaluation report completed |
| Week 9 | Developed FastAPI endpoints and payload generation | API service layer completed |
| Week 10 | Designed overview dashboard frontend | Executive metrics page displayed successfully |
| Week 11 | Added workforce performance dashboard page and testing | Comparative and scatter-based view completed |
| Week 12 | Prepared technical documentation and final report | Internship report completed |

## Annexure D: Technical Implementation Details

### D.1 Key Project Files

| File / Module | Purpose |
|---|---|
| `scripts/generate_hr_data.py` | Creates synthetic employee dataset with realistic distributions |
| `scripts/clean_hr_data.py` | Cleans and standardizes raw data |
| `scripts/train_attrition_model.py` | Trains attrition prediction model and stores report |
| `api/main.py` | Provides API endpoints and dashboard frontend |
| `dashboard/powerbi_dashboard_guide.md` | Documents the dashboard design logic |

### D.2 Important Data Fields

| Field | Description |
|---|---|
| employee_id | Unique employee identifier |
| name | Employee name |
| age | Employee age |
| gender | Gender category |
| department | Department name |
| job_role | Role designation |
| salary | Employee compensation |
| date_of_joining | Joining date |
| exit_date | Exit date if attrited |
| attrition | Whether employee left or not |
| performance_rating | Rating from 1 to 5 |
| attendance_percentage | Attendance level |
| location | Work location |
| tenure_years | Derived duration of employment |
| employment_status | Active or inactive status |

### D.3 Simplified Execution Steps

```powershell
python scripts\generate_hr_data.py
python scripts\clean_hr_data.py
python scripts\train_attrition_model.py
uvicorn api.main:app --reload
```

## Annexure E: API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Loads dashboard homepage |
| `/health` | GET | Returns service health |
| `/pipeline/status` | GET | Returns latest processed dashboard payload |
| `/pipeline/run` | POST | Runs generation, cleaning, and model workflow |
| `/employees` | GET | Returns employee record data |
| `/kpis` | GET | Returns KPI summary |

### E.1 Sample API Response for `/health`

```json
{
  "status": "ok"
}
```

### E.2 Sample API Response for `/kpis`

```json
{
  "raw_rows": 6035,
  "clean_rows": 6000,
  "duplicates_removed": 35,
  "attrition_rate": 18.42,
  "average_attendance": 88.71,
  "roc_auc": 0.8124,
  "average_performance": 3.27,
  "top_performing_department": "Finance"
}
```

### E.3 Sample API Response for `/pipeline/status`

```json
{
  "kpis": {
    "raw_rows": 6035,
    "clean_rows": 6000,
    "duplicates_removed": 35,
    "attrition_rate": 18.42
  },
  "charts": {
    "department_counts": [
      {"department": "Engineering", "count": 1440},
      {"department": "Sales", "count": 1080}
    ],
    "performance_by_department": [
      {"department": "Finance", "average_performance": 3.56},
      {"department": "Engineering", "average_performance": 3.41}
    ]
  }
}
```

## Annexure F: Screenshots Description

### F.1 Overview Dashboard Screenshot Placeholder

**File Name:** `overview-page.png`  
**Description:** This screenshot represents the executive overview page of the dashboard showing KPI cards, department headcount, attrition split, hiring trend, attendance summary, salary summary, and sample output records.

**Image Placement Note:** Insert the actual screenshot here in the final Word file and keep the caption below the image as:  
`Fig. A.1 Executive Overview Dashboard`

### F.2 Performance Dashboard Screenshot Placeholder

**File Name:** `performance-page.png`  
**Description:** This screenshot represents the workforce performance page showing average performance indicators, department-wise performance chart, attendance versus performance scatter visualization, and department-role matrix table.

**Image Placement Note:** Insert the actual screenshot here in the final Word file and keep the caption below the image as:  
`Fig. A.2 Workforce Performance Dashboard`

### F.3 Data Quality Dashboard Screenshot Placeholder

**File Name:** `data-quality-page.png`  
**Description:** This screenshot represents the data quality report page showing input rows, clean rows, duplicates removed, missing value counts, and field-level quality summary.

**Image Placement Note:** Insert the actual screenshot here in the final Word file and keep the caption below the image as:  
`Fig. A.3 Data Quality Report Dashboard`

### F.4 Final Output Dashboard Screenshot Placeholder

**File Name:** `final-output-page.png`  
**Description:** This screenshot represents the final output report page showing the processed employee data summary, department totals, attrition count, and output-ready report view.

**Image Placement Note:** Insert the actual screenshot here in the final Word file and keep the caption below the image as:  
`Fig. A.4 Final Output Report Dashboard`

### F.5 Additional Screenshot Placeholders for Final Report

| Screenshot Title | File Name Suggestion | Placement Purpose |
|---|---|---|
| Home / Pipeline Runner | `home-runner-page.png` | Shows the one-click pipeline interface |
| KPI Summary Cards | `kpi-summary-cards.png` | Shows summary metrics clearly |
| Hiring Trend View | `hiring-trend-view.png` | Shows monthly workforce movement |
| Attrition Distribution | `attrition-distribution.png` | Shows attrition split chart |
| Department Salary Analysis | `salary-analysis-page.png` | Shows average salary by department |
| Attendance Analysis | `attendance-analysis-page.png` | Shows attendance summary view |

### F.6 Recommended Screenshot Insertion Format

For each screenshot in the final major project report, use the following sequence:

1. Keep one descriptive paragraph introducing the figure.
2. Insert the image in centered alignment.
3. Add a caption below it in the format `Fig. X.Y Figure Title`.
4. Add 3 to 5 lines explaining what insight the figure provides.

## Annexure G: Important Code Listings

### G.1 Employee Data Generation Logic

```python
def generate_employee_row(employee_number: int) -> dict:
    department_spec = sample_department()
    age = int(np.clip(np.random.normal(loc=34, scale=7.5), 21, 60))
    gender = weighted_choice(GENDERS)
    location = weighted_choice(LOCATIONS)
    job_role = weighted_choice(department_spec.roles)
    join_date = faker.date_between(start_date="-10y", end_date="today")
    tenure_years = (pd.Timestamp.today().normalize() - pd.Timestamp(join_date)).days / 365.25
    performance_rating = derive_performance(department_spec.name)
    attrition_bias = max(0, 0.24 - (performance_rating * 0.035))
    attendance_percentage = derive_attendance(performance_rating, tenure_years, attrition_bias)
    salary = derive_salary(department_spec, job_role, age, performance_rating, tenure_years)
    attrition = derive_attrition(performance_rating, attendance_percentage, tenure_years, salary, department_spec)
```

### G.2 Data Cleaning Logic

```python
def clean_dataset(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    initial_rows = len(frame)
    frame = frame.drop_duplicates().copy()
    frame["department"] = frame["department"].astype(str).map(title_case_department)
    frame["gender"] = frame["gender"].fillna("Undisclosed").astype(str).str.strip().str.title()
    frame["attrition"] = frame["attrition"].astype(str).map(normalize_attrition)
    department_salary_medians = frame.groupby("department")["salary"].transform("median")
    frame["salary"] = frame["salary"].fillna(department_salary_medians)
    department_attendance_medians = frame.groupby("department")["attendance_percentage"].transform("median")
    frame["attendance_percentage"] = frame["attendance_percentage"].fillna(department_attendance_medians)
    frame["tenure_years"] = (
        ((frame["exit_date"].fillna(pd.Timestamp.today().normalize()) - frame["date_of_joining"]).dt.days) / 365.25
    ).round(2)
```

### G.3 Attrition Model Training Logic

```python
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]
```

### G.4 API Endpoint Logic

```python
@app.post("/pipeline/run")
def run_pipeline() -> dict[str, Any]:
    try:
        return _run_pipeline()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {exc}") from exc
```

## Annexure H: Power BI DAX Measures

The following DAX measures are relevant for the Power BI implementation of the project and should be included in the final project report because they reflect the analytics logic used in dashboard design.

### H.1 DAX Functions Explained One by One

The following DAX functions are useful for Power BI dashboard development, especially for executive overview and workforce performance analysis.

#### 1. `SUM()`

This function adds all values from a numeric column.

```DAX
Total Salary Paid = SUM('hr_employee_data_clean'[salary])
```

#### 2. `COUNT()`

This function counts numeric values in a column.

```DAX
Employee ID Count = COUNT('hr_employee_data_clean'[employee_id])
```

#### 3. `COUNTA()`

This function counts all non-empty values.

```DAX
Filled Job Roles = COUNTA('hr_employee_data_clean'[job_role])
```

#### 4. `DISTINCTCOUNT()`

This function counts unique values in a column.

```DAX
Unique Departments = DISTINCTCOUNT('hr_employee_data_clean'[department])
```

#### 5. `AVERAGE()`

This function returns the average of a numeric column.

```DAX
Average Salary = AVERAGE('hr_employee_data_clean'[salary])
```

#### 6. `MAX()` and `MIN()`

These functions return the highest and lowest values from a numeric column.

```DAX
Highest Salary = MAX('hr_employee_data_clean'[salary])
Lowest Salary = MIN('hr_employee_data_clean'[salary])
```

#### 7. `CALCULATE()`

This is one of the most important DAX functions because it changes filter context.

```DAX
Attrition Count = CALCULATE(
    [Total Employees],
    'hr_employee_data_clean'[attrition] = "Yes"
)
```

#### 8. `FILTER()`

This function is used when a calculation requires a custom condition.

```DAX
High Performers = CALCULATE(
    [Total Employees],
    FILTER('hr_employee_data_clean', 'hr_employee_data_clean'[performance_rating] >= 4)
)
```

#### 9. `IF()`

This function applies simple conditional logic.

```DAX
Performance Status = IF([Average Performance] >= 4, "Strong", "Needs Attention")
```

#### 10. `DIVIDE()`

This function safely divides one value by another and handles divide-by-zero cases.

```DAX
Attrition Rate % = DIVIDE([Attrition Count], [Total Employees], 0)
```

#### 11. `RELATED()`

This function retrieves a value from a related table in the data model.

```DAX
Department Name = RELATED('department_lookup'[department_name])
```

#### 12. `DATEADD()`

This function helps compare values across different time periods.

```DAX
Previous Month Hires = CALCULATE(
    [Total Employees],
    DATEADD('Date'[Date], -1, MONTH)
)
```

#### 13. `TOTALYTD()`

This function gives the year-to-date value of a measure.

```DAX
YTD Hires = TOTALYTD([Total Employees], 'Date'[Date])
```

#### 14. `SAMEPERIODLASTYEAR()`

This function compares a measure with the same period in the previous year.

```DAX
Last Year Hires = CALCULATE(
    [Total Employees],
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

#### 15. `SWITCH()`

This function is useful when multiple conditions must be checked in a single expression.

```DAX
Attendance Band = SWITCH(
    TRUE(),
    [Average Attendance] >= 90, "Excellent",
    [Average Attendance] >= 75, "Good",
    "Low"
)
```

### H.2 KPI Measures for Overview Dashboard

```DAX
Total Employees = COUNTROWS('hr_employee_data_clean')

Attrition Count = CALCULATE(
    [Total Employees],
    'hr_employee_data_clean'[attrition] = "Yes"
)

Attrition Rate % = DIVIDE([Attrition Count], [Total Employees], 0)

Average Salary = AVERAGE('hr_employee_data_clean'[salary])

Average Tenure = AVERAGE('hr_employee_data_clean'[tenure_years])

Average Performance = AVERAGE('hr_employee_data_clean'[performance_rating])

Average Attendance = AVERAGE('hr_employee_data_clean'[attendance_percentage])
```

### H.3 Department-Level Analytical Measures

```DAX
Employees by Department = COUNT('hr_employee_data_clean'[employee_id])

Average Department Salary = AVERAGE('hr_employee_data_clean'[salary])

Average Department Performance = AVERAGE('hr_employee_data_clean'[performance_rating])

Average Department Attendance = AVERAGE('hr_employee_data_clean'[attendance_percentage])
```

### H.4 Suggested Calculated Column for Salary Band

```DAX
Salary Band =
SWITCH(
    TRUE(),
    'hr_employee_data_clean'[salary] < 40000, "Below 40K",
    'hr_employee_data_clean'[salary] < 70000, "40K - 70K",
    'hr_employee_data_clean'[salary] < 100000, "70K - 100K",
    'hr_employee_data_clean'[salary] < 150000, "100K - 150K",
    "150K+"
)
```

### H.5 Growth Comparison Measure

The following measure can be used to compare current values with a previous period.

```DAX
Growth % = DIVIDE([Total Employees] - [Last Year Hires], [Last Year Hires], 0)
```

### H.6 Power BI Visual Mapping Notes

| Visual | Axis / Legend | Value / Measure |
|---|---|---|
| KPI Card | Not Applicable | Total Employees, Attrition Rate %, Average Salary |
| Line Chart | `date_of_joining` by month | Total Employees |
| Donut Chart | `attrition` | Total Employees |
| Clustered Bar Chart | `department` | Average Department Performance |
| Scatter Plot | Attendance Percentage, Performance Rating | Salary as size, Department as legend |
| Matrix | Department, Job Role | Average Performance, Average Attendance |
| Data Quality KPI Card | Not Applicable | Input Rows, Clean Rows, Duplicates Removed |
| Data Quality Table | Field Name | Null Count, Null Percentage |
| Final Output Table | Employee, Department, Job Role | Salary, Attendance, Performance, Attrition |

## Annexure I: Feature Summary

| Feature | Description |
|---|---|
| Synthetic HR Dataset Generator | Produces realistic academic workforce data |
| Data Cleaning Pipeline | Standardizes and enriches records |
| Attrition Prediction | Uses logistic regression for binary risk estimation |
| API Delivery | Makes analytical outputs reusable |
| Frontend Dashboard | Displays overview and performance insights |

## Annexure J: Suggested Formatting for Final Word Conversion

For final submission in university format, the following formatting may be applied while converting this report into Word:

- Font for body text: Times New Roman, 12 pt
- Line spacing: 1.5
- Heading style: Bold, uppercase for chapter titles
- Margins: As per university guidelines
- Page numbering: Roman for preliminary pages, Arabic for chapters
- Alignment: Justified
- Tables: Centered caption and consistent borders

---

# END OF REPORT
