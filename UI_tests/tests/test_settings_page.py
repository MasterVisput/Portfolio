import logging

from UI_tests.pages.selectors import DashboardPageSelectors

logger = logging.getLogger(__name__)


class TestProductsPage:
    def test_add_new_pruduct(self, admin_product_page):
        logger.info('====================Start "test_add_new_pruduct"====================')
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продкт не добавлен'
        logger.info('====================End "test_add_new_pruduct"====================')

    def test_delete_product_by_name(self, admin_product_page, setup_product_page):
        logger.info('====================Start "test_delete_product_by_name"====================')
        admin_product_page.delete_product_from_tab(p_name='Mouse')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не удалён'
        logger.info('====================End "test_delete_product_by_name"====================')

    def test_edit_product_by_name(self, admin_product_page, setup_product_page):
        logger.info('====================Start "test_edit_product_by_name"====================')
        admin_product_page.edit_product_from_tab(p_name='Mouse', new_p_name='Mouse+21')
        assert admin_product_page.is_element_present(
            DashboardPageSelectors.SUCCESS_ALERT), 'Продукт не отредактирован'
        logger.info('====================End "test_edit_product_by_name"====================')

    def test_product_filter(self, admin_product_page, setup_product_page):
        logger.info('====================Start "test_product_filter"====================')
        assert admin_product_page.is_product_in_tab(p_name='Mouse'), 'Продукта нет в таблице'
        logger.info('====================End "test_delete_product_by_name"====================')


class TestCategoriesPage:
    def test_rebuild_tab(self, admin_categories_page):
        logger.info('====================Start "test_rebuild_tab"====================')
        admin_categories_page.rebuild_page()
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)
        logger.info('====================End "test_rebuild_tab"====================')

    def test_categories_tab_is_present(self, admin_categories_page):
        logger.info('====================Start "test_categories_tab_is_present"====================')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.CATEGORIES_TAB)
        logger.info('====================End "test_categories_tab_is_present"====================')

    def test_add_category(self, admin_categories_page):
        logger.info('====================Start "test_add_category"====================')
        admin_categories_page.add_new_categoriy(c_name='Lamp', m_tag='Lamps')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)
        logger.info('====================End "test_add_category"====================')

    def test_edit_category_by_name(self, admin_categories_page):
        logger.info('====================Start "test_edit_category_by_name"====================')
        admin_categories_page.edit_category(c_name='Lamp', new_c_name='Lamp mini')
        assert admin_categories_page.is_element_present(DashboardPageSelectors.SUCCESS_ALERT)
        logger.info('====================End "test_edit_category_by_name"====================')
