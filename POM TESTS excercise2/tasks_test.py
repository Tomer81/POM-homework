import time
from selenium import webdriver
from pages.tasks_page1 import TasksPage
from pages.tasks_page2 import NewTaskPage

class TasksTest():

    def add_task(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.mytinytodo.net/demo/")
        p1 = TasksPage(driver)
        p1.delete_tasks()
        p1.create_new_list("ToDo")
        p1.press_todo_tab()
        p1.add_simple_task("make the laundry")

class TasksTest2():
    def add_second_task(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.mytinytodo.net/demo/")
        p1 = TasksPage(driver)
        p1.delete_tasks()
        p1.press_todo_tab()
        p1.adding_new_task()
        p2 = NewTaskPage(driver)
        p2.choose_priority("+2")
        p2.fill_info("15.10.26", "play the guitar", "practice on the new song", "automation")
        p2.click_save_btn()

    def add_third_task(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.mytinytodo.net/demo/")
        p1 =TasksPage(driver)
        p1.delete_tasks()
        p1.press_todo_tab()
        p1.adding_new_task()
        p3 = NewTaskPage(driver)
        p3.choose_priority("+1")
        p3.fill_info("20.10.26", "order a hotel room", "only for 1 night", "automation")
        p3.click_save_btn()

class TasksTest3():
    def searching_task_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.mytinytodo.net/demo/")
        p4 = TasksPage(driver)
        p4.delete_tasks()
        p4.search_task("laundry")
        time.sleep(3)
        print(p4.get_tasks_number())

class TaskTest4():
    def adding_list(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.mytinytodo.net/demo/")
        p5 = TasksPage(driver)
        p5.delete_tasks()
        p5.press_todo_tab()
        time.sleep(3)
        p5.create_new_list("homework")
        p5.add_simple_task("go over manuals testings")
        p5.add_simple_task("go over sql")
        time.sleep(5)
        tasks_number = p5.get_tasks_number()
        if tasks_number == "2":
            print("correct number of tasks")
        else:
            print("wrong number of tasks")



test1 = TasksTest()
test1.add_task()
test2 = TasksTest2()
test2.add_second_task()
test3 = TasksTest2()
test3.add_third_task()
test4 = TasksTest3()
test4.searching_task_title()
test5 = TaskTest4()
test5.adding_list()
input("end")