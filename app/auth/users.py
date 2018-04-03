from flask import request, jsonify
from app.models.users import User
from app.auth import auth
from app import db


@auth.route('/apidemo', methods=['GET', 'POST'])
def apidemo():
    """一个返回JSON数据接口的设计示例"""
    if request.method == "POST":
        
        user = User("www", "123", "baiyang", '2')
        db.session.add(user)
        db.session.commit()
        db.session.close()
        
        response = jsonify(dict(errCode="0", errMsg="操作成功！"))
        return response
    elif request.method == "GET":
        contactsArr = []
        users = User.query.order_by(User.id)
        for usr in users:
            contactsArr.append(usr.to_dict())
        jsonResponse = dict(errCode="1", errMsg="操作成功！", users=contactsArr)
        response = jsonify(jsonResponse)
        return response