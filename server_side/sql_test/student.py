import pymysql
from pypinyin import lazy_pinyin as lp

config = {
    'host': 'cdb-73iebo87.gz.tencentcdb.com',
    'port': 10110,
    'user': 'root',
    "password": '1234!@#$',
    'database': 'DB',
    'charset': 'utf8mb4'
}


def login(student_id, password):
    # if the returning value is 1,
    # which means the person is one of the members

    id = "student_id"
    p = "log_in_code"
    select = "select %s, %s  from student where %s = %s and  %s = %s " % (id, p, id,
                                                                          student_id, p, password)
    db = pymysql.connect(**config)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        rows = cursor.execute(select)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()


def add_money(student_id, money):
    # put money into acount
    # update the money
    id = "student_id"
    p = "log_in_code"
    update1 = "update student set money_left = %s where student_id = %s" % (money, student_id)
    db = pymysql.connect(**config)
    cursor = db.cursor()

    try:
        flag = cursor.execute(update1)
        db.commit()
    except:
        db.rollback()

    cursor.close()
    db.close()


def comsume(dish_id, student_id):
    # buy food from the window
    # the money of the students cannot be reduce without purchase, we need a trigger
    # the purchase cannot happen if the money is less than the price, we need another trigger
    price1 = ' select price from dishes where id = %s' % (dish_id)
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        cursor.execute(price1)
        price = cursor.fetchall()
        db.commit()
    except:
        db.rollback()

    compare_money = '''select compare_money_left(%s
                    , (select money_left from student where student_id = %s))''' % (price[0][0], student_id)
    # print(float(price[0][0]))
    row = 0
    try:
        row = cursor.execute(compare_money)
        db.commit()
    except:
        db.rollback()

    if row == 1:
        add_money(student_id, -(float(price[0][0])))
        comsume1 = 'insert into consumption_situation(student_id, dish_id) values (%s,%s)' % \
                   (student_id, dish_id)
        try:
            cursor.execute(comsume1)
            db.commit()
        except:
            db.rollback()
        print("purchase succeed")
        return True
    else:
        print("purchase fail")
        return False

    cursor.close()
    db.close()


def stringBuilder(name):
    n = lp(name)
    if len(n) == 3:
        return n[0].capitalize() + " " + (n[1] + n[2]).capitalize()
    if len(n) == 2:
        return n[0].capitalize() + " " + n[1].capitalize()


def add_students(student_id, name, money):
    # pay attention to the foreign key limit
    Ename = "'" + stringBuilder(name) + "'"
    name = "'" + name + "'"
    print(name, Ename)
    insert1 = "insert into student(student_id, log_in_code, money_left) values (%s, %s, %s)" % (
    student_id, student_id, money)
    db = pymysql.connect(**config)

    insert2 = 'insert into student_name (student_id, chinese_name, english_name)  values (%s, %s, %s) ' \
              % (student_id, name, Ename)

    insert3 = 'insert into student_info values (%s, (select define_sex(%s) ), (select define_class(%s)) )' \
              % (student_id, student_id, student_id)

    # 使用 cursor() 方法创建一个游标对象 cursor
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


def delete_student(student_id):
    delete1 = 'delete from student_info where student_id = %s' % (student_id)
    delete2 = 'delete from student_name where student_id = %s ' % (student_id)
    delete3 = 'delete from student where student_id = %s' % (student_id)
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(delete1)
            db.commit()
        except:
            db.rollback()
            print("BAD1")
        try:
            cursor.execute(delete2)
            db.commit()
        except:  # 方法一：捕获所有异常
            # 如果发生异常，则回滚
            print("BAD2")
            db.rollback()
        try:
            cursor.execute(delete3)
            db.commit()
        except:
            db.rollback()
            print("BAD3")
    db.close()

def complaint_dish(student_id, score, dishes_id, word):
    # the score will be in enum{1, 1.5, 2, 2.5}, we need another trigger
    # the problem of the length of the word
    insert = "insert into comment_dish (score, from_student, dishes_id, content) values (%s, %s, %s, %s)" % \
             (score, student_id, dishes_id, word)
    switch = (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)

    if score in switch:
        db = pymysql.connect(**config)
        with db.cursor() as cursor:
            try:
                cursor.execute(insert)
                db.commit()
            except:
                db.rollback()
        return True
    else:
        return "The score is not okay"


def complaint_window(student_id, score, window_id, word):
    insert = "insert into comment_dish (score, from_student, window_id, content) values (%s, %s, %s, %s)" % \
             (score, student_id, window_id, word)
    switch = (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)

    if score in switch:
        db = pymysql.connect(**config)
        with db.cursor() as cursor:
            try:
                cursor.execute(insert)
                db.commit()
            except:
                db.rollback()
        return True
    else:
        return "The score is not okay"
