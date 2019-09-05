import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_btn_add_tobasket_exists(browser):
    browser.get(link)
    time.sleep(30)
    if browser.find_element_by_class_name('btn-add-to-basket'):
        print("Element exists")
