from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import ast

app = FastAPI()

app.get("/")
def root():
    return {"RULE": "ENGINE"}

class UserAttributes(BaseModel):
    age: int
    department: str
    income: float
    spend: float

# Example rule stored as a string that can be dynamically modified

RULES = """
(age > 25 and department == 'HR' and income > 50000) or (spend > 30000)
"""

def evaluate_rule(attributes: dict, rule: str) -> bool:
    #parse and evaluate the rule using AST
    tree = ast.parse(rule, mode='eval')
    code = compile(tree, filename="<ast>", mode="eval")
    return eval(code, {}, attributes)

@app.post("/api/check-eligibility")
def check_eligibility(user: UserAttributes):
    attributes = user.dict()
    try:
        eligible = evaluate_rule(attributes, RULES)
        return {"message": "Eligible" if eligible else "Not Eligible"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error evaluating rule: {e}")

