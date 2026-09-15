from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TasksPage(BasePage):
    TO_DO_TAB = (By.CSS_SELECTOR, "#list_1 .title-block")
    TEST_FIELD = (By.CSS_SELECTOR, ".mtt-taskbox #newtask_form #task")
    ADD_TASK_BTN = (By.CSS_SELECTOR, "#newtask_submit")
    ADVANCED_BTN = (By.CSS_SELECTOR, "#newtask_adv")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    TASKS_NUMBER = (By.CSS_SELECTOR, "#total")
    LIST_BTN = (By.CSS_SELECTOR, ".mtt-tabs-new-button")
    LIST_TITLE_FIELD = (By.CSS_SELECTOR, "#modalTextInput")
    OK_BTN = (By.CSS_SELECTOR, "#btnModalOk")

    TASK_TITLE = (By.CSS_SELECTOR,".task-title")
    OPTION_BTN = (By.CSS_SELECTOR, ".taskactionbtn")
    DELETE_TASK_BTN = (By.CSS_SELECTOR, "#cmenu_delete")
    TASK_BLOCK = (By.CSS_SELECTOR, ".task-row")


    def __init__(self, driver):
        super().__init__(driver)

    def press_todo_tab(self):
        self.click(self.TO_DO_TAB)

    def adding_new_task(self):
        self.click(self.ADVANCED_BTN)

    def add_simple_task(self, task_title):
        self.fill_text(self.TEST_FIELD, task_title)
        self.click(self.ADD_TASK_BTN)

    def search_task(self, task_title):
        self.fill_text(self.SEARCH_FIELD, task_title)

    def get_title_text(self):
        return self.get_text(self.TASK_TITLE)

    def get_tasks_number(self):
        return self.get_text(self.TASKS_NUMBER)

    def select_list(self, list_title):
        list_tab = (By.XPATH, f"//span[text()='{list_title}']")
        self.click(list_tab)

    def create_new_list(self, list_title):
        self.click(self.LIST_BTN)
        self.fill_text(self.LIST_TITLE_FIELD, list_title)
        self.click(self.OK_BTN)
        self.select_list(list_title)



    def delete_tasks(self):
        list_of_tasks = self.find_elements(self.TASK_BLOCK)
        while len(list_of_tasks)>0:
            first_task = list_of_tasks[0]
            ActionChains(self.driver).move_to_element(first_task).perform()
            first_task.find_element(*self.OPTION_BTN).click()
            self.click(self.DELETE_TASK_BTN)
            list_of_tasks = self.find_elements(self.TASK_BLOCK)
