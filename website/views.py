from flask import Blueprint, render_template

views = Blueprint('views', __name__)

drug = {
    "name":         "Odansetron",
    "desc":         "used to prevent vomiting and naseau, commonly paired with chemotherapy treatment for cancer",
    "func":         "antagonizes serotonin receptors in the brain and Vagus nerve, preventing nausea and vomiting triggers in the body from reaching the brain",
    "admin":        "Oral (capsule), intramuscular (IM), intravenous (IV)",
    "effects":      "headaches, fatigue, dry mouth, malaise, constipation",
    "clas":        "anti-emetic",
    "brands":       "Zofran",
}


@views.route('/')
def home():
    return render_template('home.html')

@views.route('/odansetron')
def odansetron():
    return render_template(
        'ae0.html', 
        **drug,
    )