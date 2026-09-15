from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewTaskPage(BasePage):
    SELECT_PRIORITY = (By.CSS_SELECTOR, "[name='prio']")
    CALENDER_FIELD = (By.CSS_SELECTOR, "#duedate")

    TASK_FIELD = (By.CSS_SELECTOR, ".form-row>[name='task']")
    NOTE_FIELD = (By.CSS_SELECTOR, "[name='note']")
    TAGS_FIELD = (By.CSS_SELECTOR, "#edittags")

    SAVE_BTN = (By.CSS_SELECTOR, ".form-row.form-bottom-buttons [type='submit']")
    CANCEL_BTN = (By.CSS_SELECTOR, ".form-row.form-bottom-buttons  .mtt-back-button")

    def __init__(self, driver):
        super(). __init__(driver)


    def choose_priority(self, priority):
        self.select_by_text(self.SELECT_PRIORITY,priority)

    def fill_info(self, due, Task, Note, Tags):
        self.fill_text(self.CALENDER_FIELD, due)
        self.fill_text(self.TASK_FIELD, Task)
        self.fill_text(self.NOTE_FIELD, Note)
        self.fill_text(self.TAGS_FIELD, Tags)

    def click_save_btn(self):
        self.click(self.SAVE_BTN)