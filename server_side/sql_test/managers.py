import pymysql
from . import GetInformation

config = {
    'host': 'cdb-73iebo87.gz.tencentcdb.com',
    'port': 10110,
    'user': 'root',
    "password": '1234!@#$',
    'database': 'DB',
    'charset': 'utf8mb4'
}


def add_staff(staff_id, position_id, name, phone_number, id_card_number):
    age = GetInformation(str(id_card_number)).get_age()
    print(age)
    name = "'" + name + "'"
    insert1 = 'insert into staff(staff_id, password) values (%s, %s)' % (staff_id, 000000)
    insert2 = 'insert into staff_info (staff_id, name, phone_number, id_card_number , age) values (%s, %s, %s, %s, %s)' \
              % (staff_id, name, phone_number, id_card_number, int(age))

    insert3 = 'insert into staff_and_position(staff_id, position_id) values (%s, %s)' % (staff_id, position_id)
    db = pymysql.connect(**config)

    with db.cursor() as cursor:
        try:
            cursor.execute(insert1)
            db.commit()
        except:
            db.rollback()
            print("BAD1")
        try:
            cursor.execute(insert2)
            db.commit()
        except Exception:  # 方法一：捕获所有异常
            # 如果发生异常，则回滚
            print("BAD2")
            db.rollback()
        try:
            cursor.execute(insert3)
            db.commit()
        except:
            db.rollback()
            print("BAD3")
    db.close()


def update_staff_password(staff_id, new_password):
    np = "'" + str(new_password) + "'"
    update_p = "update staff set password = %s where staff_id = %s" % (np, staff_id)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(update_p)
            # print(update_p)
            db.commit()
        except:
            print("BAD1")
            db.rollback()
    db.close()


def delete_staff(staff_id):
    delete1 = 'delete from staff_info where staff_id = %s' % (staff_id)
    delete2 = 'delete from staff_and_position where staff_id = %s ' % (staff_id)
    delete3 = 'delete from staff where staff_id = %s' % (staff_id)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(delete1)
            db.commit()
        except:
            print("BAD1")
            db.rollback()
        try:
            cursor.execute(delete2)
            db.commit()
        except:
            print("BAD2")
            db.rollback()
        try:
            cursor.execute(delete3)
            db.commit()
        except:
            print("BAD3")
            db.rollback()
    db.close()


def add_dishes(name, description, price, sale):
    n = "'" + name + "'"
    d = "'" + description + "'"
    insert1 = "insert into dishes(name, description, price, sale) " \
              "values(%s, %s, %s, %s)" % (n, d, price, sale)

    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(insert1)
            db.commit()
        except:
            print("bad1")
            db.rollback()
    db.close()


def delete_dishes(name):
    n = "'" + name + "'"
    delete1 = 'delete from dishes where name = %s' % (n)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(delete1)
            db.commit()
        except:
            print("bad1")
            db.rollback()
    db.close()


def add_window(status, sale):
    set_status = ('close', 'open')
    if status in set_status:
        s = "'" + status + "'"
        insert1 = 'insert into window(status, sale) values (%s, %s);' % \
                  (s, sale)
        db = pymysql.connect(**config)
        with db.cursor() as cursor:
            try:
                cursor.execute(insert1)
                db.commit()
            except:
                print("bad1")
                db.rollback()
        db.close()
    else:
        return False


def delete_window(id):
    delete1 = 'delete from window where id = %s;' % (id)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(delete1)
            db.commit()
        except:
            print("bad1")
            db.rollback()
    db.close()


def add_position(name, description):
    n = "'" + name + "'"
    d = "'" + description + "'"
    insert1 = "insert into position (name, description) values ( %s, %s); " % (n, d)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(insert1)
            db.commit()
        except:
            print("bad1")
            db.rollback()
    db.close()


def delete_position(name):
    name = "'" + name + "'"
    delete1 = "delete from position where name = %s;" % (name)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(delete1)
            db.commit()
        except:
            print("bad1")
            db.rollback()
    db.close()
