from flask import render_template

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/register/candidate")
    def register_candidate():
        return render_template("register_candidate.html")

    @app.route("/register/company")
    def register_company():
        return render_template("register_company.html")

    @app.route("/jobs")
    def jobs():
        return render_template("jobs.html")

    @app.route("/candidate/dashboard")
    def candidate_dashboard():
        return render_template("candidate_dashboard.html")

    @app.route("/company/dashboard")
    def company_dashboard():
        return render_template("company_dashboard.html")

    @app.route("/company/jobs/new")
    def new_job():
        return render_template("new_job.html")
