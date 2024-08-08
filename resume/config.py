import datetime

class Config:
    """
    Configuration class for global settings such as user details and file paths.
    """
    first_name = "Gulger"
    last_name = "Mallik"
    full_name = f'{first_name} {last_name}'
    phone = '07767924720'
    email = 'gulgermallik@gmail.com'
    website = 'mrmallik.com'
    linkedin = 'linkedin.com/in/mrmallik'
    github = 'github.com/mr-mallik'

    resume_style = 'css/resume-style.css'
    cover_letter_style = 'css/cover-style.css'

    saveHtml = True

    @staticmethod
    def get_header_html():
        """
        Returns the HTML content for the fixed header.
        """
        return f"""
        <div class="header">
            <strong>{Config.full_name}</strong><br>
            Phone: {Config.phone} | Email: {Config.email}<br>
            Portfolio: {Config.website} | LinkedIn: {Config.linkedin} | GitHub: {Config.github}
        </div>
        """

    @staticmethod
    def get_footer_html():
        """
        Returns the HTML content for the fixed footer.
        """
        return f"""
        <div class="footer">
            <em>*References available on request and more detail available on <a href='{Config.linkedin}'>LinkedIn</a> and <a href='{Config.website} '>Portfolio</a>.</em>
        </div>
        """

    @staticmethod
    def get_addressee_html():
        """
        Returns the HTML content for the addressee.
        """
        return f"""
        {Config.full_name}<br>
        {Config.email}<br>
        {Config.phone}<br>
        {datetime.date.today()}
        """
    
    @staticmethod
    def get_signature_html():
        """
        Returns the HTML content for the signature.
        """
        return f"""
        Sincerely,<br>
        {Config.full_name}
        """

    @staticmethod
    def get_css_link(css_file):
        """
        Returns the HTML link tag to include the specified CSS file.
        """
        return f'<link rel="stylesheet" type="text/css" href="{css_file}">'
