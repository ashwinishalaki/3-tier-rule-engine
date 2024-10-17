# 3-tier-rule-engine
Developed a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend.


1.User Interface (UI)
Purpose: Provide a simple interface for users to input their attributes (age, department, income, etc.) and view eligibility results. Also allow admins to create or modify rules.
Tech Stack: simple HTML/CSS.
Features:
Form to capture user attributes.
View results of eligibility.
Admin interface to define or modify rules.

2. API (Middle Layer)
Purpose: Handle requests from the UI and communicate with the backend. Also handle the rule parsing and execution via the AST.
Tech Stack: Flask/FastAPIFramework.
Features:
Endpoints for submitting user attributes.
Endpoint for admins to add/modify rules dynamically.
AST-based rule engine to evaluate user eligibility.
Endpoints:
POST /evaluate: Takes user attributes as input and returns eligibility based on the defined rules.
POST /rules: Allows admin to define or modify rules dynamically using AST.

3. Backend (Data Tier)
Purpose: Store user attributes, rules, and evaluation history.
Tech Stack: SQLite.
Features:
Store user attribute data and their evaluation results.
Store rules in a structured format for easy retrieval and modification.

5. Abstract Syntax Tree (AST) for Rule Representation
Purpose: Represent the conditional logic (rules) in a tree structure where each node is a condition, and nodes combine to form more complex rules.
Python Example for AST:
Use Python’s built-in ast library to dynamically create or modify rules.
High-Level Workflow:
User Submission: Users submit their attributes via the UI.
API Processing: The API receives the submission and uses the AST-based rule engine to evaluate the eligibility based on the current rules.
AST-Based Rule Engine:
Parse rules into an AST structure.
Traverse the AST to evaluate conditions like age > 18 and income > 50000.
Store Results: The results of eligibility evaluation are stored in the backend.
Admin Rules: Admins can define or modify rules dynamically, and these changes reflect immediately in the evaluation process.

Conclusion
The UI will allow users to input data and view results.
The API will handle requests and leverage an AST-based engine to evaluate dynamic rules.
The backend will store user data, rules, and evaluation results.
