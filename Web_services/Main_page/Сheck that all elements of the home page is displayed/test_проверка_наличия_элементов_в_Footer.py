from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod
from Interneturok.web_services.Main_page.Elements.Footer import Checks_all_elements_the_page_in_footer


class Footer(StartInterneturokClassMethod):
    def test_check_footer(self):
        Checks_all_elements_the_page_in_footer()
        return