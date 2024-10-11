from selenium.webdriver.common.by import By


class Login:
    userNameFieldId = "user-name"
    passwordID = "password"
    loginButtonID = "login-button"
    dashboardLogoXpath = "//div[@class='app_logo']"

    def __init__(self, driver):
        self.driver = driver

    def inputUserName(self, userName):
        self.driver.find_element(By.ID, self.userNameFieldId).send_keys(userName)

    def inputPassword(self, password):
        self.driver.find_element(By.ID, self.passwordID).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.loginButtonID).click()

    def assertDashboardLogo(self):
        return self.driver.find_element(By.XPATH, self.dashboardLogoXpath).text

