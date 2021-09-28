from behave import *
from POM.statistics import *
import collections


@given("Verify the title of statistics page")
def step_impl(context):
    context.stats_page = StatisticsPage(context.driver)
    title = context.stats_page.get_stats_page_title()
    assert title == "Cyber attack completely fake statistics", "Failed to verify statistics page"


@given("Clear the filter box")
def step_impl(context):
    context.stats_page.clear_filter()


@step("Capture the table")
def step_impl(context):
    context.original_table_data = context.stats_page.get_table_data()


@step("The Table with some fake data")
def step_impl(context):
    assert context.original_table_data, "Initial table data is empty, please re-run the scripts once data is available"


@when("I sort the table by name")
def step_impl(context):
    context.stats_page.sort_by_category("Name", context.original_table_data)


@then("Verify the names in ascending order")
def step_impl(context):
    context.sorted_table = context.stats_page.get_table_data()
    original_names = context.original_table_data['NAME']
    sorted_names = context.sorted_table['NAME']
    original_names = [e.lower() for e in original_names]
    sorted_names = [e.lower() for e in sorted_names]
    assert sorted(original_names) == sorted_names, "Failed to sort the elements by name"


@step("Filter the data by {category}")
def step_impl(context, category):
    context.category = category
    context.stats_page.filter_by_text(category)


@then("Capture the filtered table and verify by name")
def step_impl(context):
    context.filtered_table = context.stats_page.get_table_data()
    for name in context.filtered_table["NAME"]:
        assert name.lower() == context.category.lower(), "Failed to verify the filtered_table"


@when("I sort the table by complexity")
def step_impl(context):
    context.stats_page.sort_by_category("Complexity", context.original_table_data)


@then("Verify the complexity in low-medium-high order")
def step_impl(context):
    context.sorted_table = context.stats_page.get_table_data()
    context.original_complexity = context.original_table_data['COMPLEXITY']
    sorted_complexity = context.sorted_table['COMPLEXITY']
    COMPLEXITY = dict(low=0, medium=1, high=2)
    context.original_complexity.sort(key=lambda x: COMPLEXITY[x])
    assert context.original_complexity == sorted_complexity, "Failed to sort the elements by Complexity"


@then("Capture the filtered table and verify by complexity and its count")
def step_impl(context):
    context.filtered_table = context.stats_page.get_table_data()
    filtered_complexity = context.filtered_table["COMPLEXITY"]

    # Taking complexity from original table data
    complexities = context.orig_table_data['COMPLEXITY']
    context.orig_com_occurs = dict(collections.Counter(complexities))
    for complexity in filtered_complexity:
        assert context.category == complexity, "Failed to verify the filter by complexity"
    assert len(filtered_complexity) == context.orig_com_occurs[context.category]
