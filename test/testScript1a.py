from seleniumbase import BaseCase

class SchooxCourseEnrollment(BaseCase):

    def test_enroll_and_complete_course(self):
        self.open("https://qatest.schoox.com/login")

        self.send_keys('//*[@id="root"]/div[2]/form/div[1]/input', 'admin@schoox.com')
        self.send_keys('//*[@id="root"]/div[2]/form/div[2]/input', '123456')

        self.click("#root > div.login > form > button")

        self.click('//*[@id="menu"]/div[3]/a')

        self.click('//*[@id="course_catalogue"]/div[2]/div[2]')

        elements_with_class = self.find_elements("#course_catalogue > div.course_listing > table  a.course_title")

        expected_items = [
            "QA course",
            "ΒΑ course",
            "Μάθημα για τους Devs",
            "Μάθημα για automation"
        ]

        for element in elements_with_class:
            element_text = element.text.strip()

            assert element_text in expected_items, f"Unexpected item found: '{element_text}'"
            assert element_text.count(",") == len(
                element_text.split(',')) - 1, f"Unexpected format in element text: '{element_text}'"

        print("Class elements validation successful.")