from selenium.webdriver.support.select import Select


class StatisticsPage:

    def __init__(self, driver):
        self.title = "//div[@id='app']/h1"
        self.table = "//div[@class='table']"
        self.column_names = "div[1]/div"
        self.rows = "//div[@class='table']/div[2]/div"
        self.filter_box = 'filter-input'
        self.drop_down = 'sort-select'
        self.driver = driver

    def get_stats_page_title(self):
        title = self.driver.find_element_by_xpath(self.title).text
        return title

    def sort_by_category(self, category, table_data):
        if category in table_data:
            drop_down_obj = self.driver.find_element_by_id(self.drop_down)
            drop = Select(drop_down_obj)
            drop.select_by_visible_text(category)

    def filter_by_text(self, text):
        filter = self.driver.find_element_by_id(self.filter_box)
        filter.clear()
        filter.send_keys(text)

    def clear_filter(self):
        self.driver.find_element_by_id(self.filter_box).clear()

    def get_table_data(self):
        table = self.driver.find_element_by_xpath(self.table)
        columns_titles = table.find_elements_by_xpath(self.column_names)
        row_objects = table.find_elements_by_xpath(self.rows)

        columns_title_list = [col.text for col in columns_titles]
        rows_list = [row.text.split("\n") for row in row_objects]

        formatted_rows_list = [[] for _ in range(len(columns_title_list))]

        for i in range(len(columns_title_list)):
            formatted_rows_list[i] = [item[i] for item in rows_list]
        print(formatted_rows_list)
        table_data = {}

        for col in range(len(columns_title_list)):
            table_data[columns_title_list[col]] = formatted_rows_list[col]

        return table_data
