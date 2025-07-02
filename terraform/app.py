from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory quiz data: 10 Terraform questions, each with 4 options
quiz = [
    {
        "question": "What is Terraform primarily used for?",
        "options": [
            "Web development",
            "Infrastructure as Code",
            "Database management",
            "Machine learning"
        ],
        "answer": 1
    },
    {
        "question": "Which file extension does Terraform use for configuration files?",
        "options": [
            ".tf",
            ".terraform",
            ".config",
            ".yaml"
        ],
        "answer": 0
    },
    {
        "question": "What is a provider in Terraform?",
        "options": [
            "A type of resource",
            "A plugin to interact with APIs",
            "A variable",
            "A module"
        ],
        "answer": 1
    },
    {
        "question": "What is the default name of the Terraform state file?",
        "options": [
            "terraform.tfstate",
            "main.tf",
            "state.json",
            "terraform.state"
        ],
        "answer": 0
    },
    {
        "question": "How do you define a variable in Terraform?",
        "options": [
            "var {}",
            "variable {}",
            "input {}",
            "define {}"
        ],
        "answer": 1
    },
    {
        "question": "How do you reference a variable in Terraform?",
        "options": [
            "${var.variable_name}",
            "${variable.variable_name}",
            "${input.variable_name}",
            "${define.variable_name}"
        ],
        "answer": 0
    },
    {
        "question": "What is a module in Terraform?",
        "options": [
            "A single resource",
            "A reusable configuration",
            "A provider",
            "A variable"
        ],
        "answer": 1
    },
    {
        "question": "How do you call a module in Terraform?",
        "options": [
            "module {}",
            "call {}",
            "import {}",
            "use {}"
        ],
        "answer": 0
    },
    {
        "question": "Which command initializes a Terraform working directory?",
        "options": [
            "terraform plan",
            "terraform apply",
            "terraform init",
            "terraform destroy"
        ],
        "answer": 2
    },
    {
        "question": "Which command shows the execution plan in Terraform?",
        "options": [
            "terraform show",
            "terraform plan",
            "terraform apply",
            "terraform output"
        ],
        "answer": 1
    }
]

@app.route('/', methods=['GET'])
def dashboard():
    return render_template('single_quiz.html', quiz=quiz)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form
    results = []
    score = 0
    for idx, q in enumerate(quiz):
        user_answer = user_answers.get(f'q{idx}')
        correct = str(q['answer']) == user_answer
        results.append({
            "question": q["question"],
            "user_answer": int(user_answer) if user_answer is not None else None,
            "correct_answer": q["answer"],
            "options": q["options"],
            "is_correct": correct
        })
        if correct:
            score += 1
    return render_template('single_result.html', results=results, score=score, total=len(quiz))

if __name__ == '__main__':
    app.run(debug=True)
