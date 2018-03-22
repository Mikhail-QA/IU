from Web_services.SetUp import StartInterneturokClassMethod
from Web_services.Main_page.Elements.Footer import ChecksAllElementsThePageInFooter


class Footer(StartInterneturokClassMethod):
    def test_check_footer(self):
        ChecksAllElementsThePageInFooter()
        return
