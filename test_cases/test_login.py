from selenium.common import NoSuchElementException, TimeoutException
import pytest
from LoginPageObject.loginPage import Login


@pytest.mark.usefixtures('setup')
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)

    def test_login(self, setup):
        self.driver = setup
        try:
            self.login.inputUserName('standard_user')
            self.login.inputPassword('secret_sauce')
            self.login.clickLoginButton()
        except (NoSuchElementException, TimeoutException) as e:
            print(f'Error: {str(e)}')

        finally:
            logo = self.login.assertDashboardLogo()
            assert 'Swag Labs' == logo, f'Expected "Swag Labs" but got {logo}'



