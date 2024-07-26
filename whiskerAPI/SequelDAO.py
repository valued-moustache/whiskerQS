from . import SequelSupport


def get_item_count(item: str):
    cnxn = SequelSupport.get_sql_connector()
    cursor = cnxn.cursor()

    selectByPkeyQuery = "SELECT ITEM,QUANTITY FROM inventory.PARTS WHERE ITEM = ?"

    cursor.execute(selectByPkeyQuery, item)

    response = cursor.fetchone()

    return response
