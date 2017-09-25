import requests
import unittest


class TestServices(unittest.TestCase):

    # booglak@gmail.com

    adminWs = "Basic Ym9vZ2xha0BnbWFpbC5jb206MjIyMjIy"
    host = "https://worldskillsacademy.ru:8080"

    def test_authentication_service(self):
        request = requests.post(self.host + '/AuthenticationService/',
                                headers={"content-type": "application/json"},
                                json={"Login": "booglak@gmail.com", "Password": "222222"})
        assert request.status_code == 200

    def test_competence_service(self):
        request = requests.get(self.host + '/CompetenceService/1',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_file_service(self):
        request = requests.get(self.host + '/FileService/Report/Competence/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_group_participant_service(self):
        request = requests.get(self.host + '/GroupParticipantService/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_group_service(self):
        request = requests.get(self.host + '/GroupService/1',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_organization_service(self):
        request = requests.get(self.host + '/OrganizationService/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_place_service(self):
        request = requests.get(self.host + '/PlaceService/Region/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_program_service(self):
        request = requests.get(self.host + '/ProgramService/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_report_service(self):
        request = requests.get(self.host + '/ReportService/Competence/',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200

    def test_user_service(self):
        request = requests.get(self.host + '/UserService/1234',
                               headers={"Authorization": self.adminWs})
        assert request.status_code == 200
        assert '"IsReserve":fale' in str(request.text)


if __name__ == "__main__":
    unittest.main()













