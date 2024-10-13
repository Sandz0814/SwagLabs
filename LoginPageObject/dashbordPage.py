from selenium.webdriver.common.by import By


class Dashboard:

    countOfItemDisplayCss = ".inventory_list>div"  # 6 elements
    sortFunctionCss = ".product_sort_container"

    def __init__(self, driver):
        self.driver = driver

    def ItemDisplayInventory(self):
        x = self.driver.find_elements(By.CSS_SELECTOR, self.countOfItemDisplayCss)
        count = len(x)
        return count

    def sortFunction(self):
        self.driver.find_elements(By.CSS_SELECTOR, self.sortFunctionCss).is_displayed()


