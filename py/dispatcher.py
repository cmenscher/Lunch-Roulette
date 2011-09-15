import string
import MySQLdb
import datetime
import re
import sys, getopt

import util
import settings

class Dispatcher:

    def __init__(self, appsettings, email_type="initial"):
        self.appsettings = appsettings
        self.email_type = email_type
        self.email_header_filename = "email_header.html"
        self.email_footer_filename = "email_footer.html"
        self.email_form_filename = "email_form.html"
        self.email_group_filename = "email_group.html"

    def send_initial_email(self, name, email):
        print "sending Initial email..."
        subject = "Betaworks Lunch Roulette TODAY!"
        header_file = "%s/%s" % (self.appsettings.email_template_path, self.email_header_filename)
        footer_file = "%s/%s" % (self.appsettings.email_template_path, self.email_footer_filename)
        form_file = "%s/%s" % (self.appsettings.email_template_path, self.email_form_filename)
        
        header_html = open(header_file, 'r').read()
        footer_html = open(footer_file, 'r').read()
        form_templ = open(form_file, 'r').read()
        

        #replace {{ name }} with name
        form_html = re.sub("\{\{\s*name\s*\}\}", name, form_templ)

        #replace {{ email }} with email
        form_html = re.sub("\{\{\s*email\s*\}\}", email, form_html)
        
        body = "%s%s%s" % (header_html, form_html, footer_html)

        result = None
        if self.appsettings.debug:
            print body
        else:
            result = util.sendMail("smtp.gmail.com", self.appsettings.email, self.appsettings.password, self.appsettings.smtp_port, [email], self.appsettings.email, subject, html=body)
        return result


    def send_group_email(self):
        print "sending Group email..."
        name = "Corey Menscher"
        email = "corey@findings.com"

        subject = "Your Lunch Roulette Group"
        #sendMail("smtp.gmail.com", "lunchroul@gmail.com", "betawork$", 587, ["lunchroul@gmail.com"], lunchroul@gmail.com, subj, body,["/path/to/file/include"])
    
    def run(self):
        #loop through the People table
        name = "Corey Menscher"
        email = "corey@findings.com"
        
        if self.email_type == "initial":
            self.send_initial_email(name, email)
        elif self.email_type == "group":
            self.send_group_email()
        else:
            x=1
            #do nothing


def main():
    # parse command line options
    
    commandline_example = 'python dispatcher.py --type=[initial|group]'
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["type="])
    except getopt.error, msg:
        #python dispatcher.py --user=lunchroul@gmail.com --pw=betawork$
        print commandline_example
        sys.exit(2)
    
    email_type = ''
    # Process options
    for o, a in opts:
        if o == "--type":
            email_type = a
    
    if email_type == '':
        print commandline_example
        sys.exit(2)
    
    appsettings = settings.Settings()

    dispatch = Dispatcher(appsettings, email_type=email_type)
    dispatch.run()


if __name__ == '__main__':
  main()
