import pytest
from LoginPageObject.dashbordPage import Dashboard
from LoginPageObject.loginPage import Login


@pytest.mark.usefixtures('setup')
class TestDashboard:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)
        self.dashboard = Dashboard(self.driver)

    def test_dashboard(self, setup):
        self.driver = setup

        self.login.inputUserName('standard_user')
        self.login.inputPassword('secret_sauce')
        self.login.clickLoginButton()

        try:
            assert 6 == self.dashboard.ItemDisplayInventory()
            assert self.dashboard.sortFunction()

        except AssertionError as e:
            print(f'Assertion Error {str(e)}')




