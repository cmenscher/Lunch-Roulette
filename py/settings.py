
#sendMail("smtp.gmail.com", "lunchroul@gmail.com", "betawork$", 587, ["lunchroul@gmail.com"], lunchroul@gmail.com, subj, body,["/path/to/file/include"])
class Settings:
    def __init__(self):
        self.email = "lunchroul@gmail.com"
        self.password = "betawork$"
        self.smtp_port = 587
        self.email_template_path = "/home/www/Lunch-Roulette/email-templates"
        self.debug = False
