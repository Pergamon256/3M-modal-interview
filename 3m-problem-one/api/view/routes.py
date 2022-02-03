from flask import Blueprint, request
from models.auth import User, db

import json
import flask_praetorian
import constants.errors as errors

view = Blueprint('view', __name__)


@view.route('/api/view/get_table', methods=['GET'])
@flask_praetorian.auth_required
def get_table():

    # t = request.get_data()
    # print(t)
    registered_users = list(set(db.session.query(User).all()))

    if not registered_users:
        return errors.NO_USERS_FOUND

    counts = {}
    for user in registered_users:
        if user.ageGroup in counts:
            counts[user.ageGroup] += 1
        else:
            counts[user.ageGroup] = 1

    ageGroupsArray = []
    ctr = 0
    for ageGroup in counts:
        ageGroupsArray.append(
            {
                "id": ctr,
                "ageGroup": ageGroup,
                "count": counts[ageGroup]
            }
        )

        ctr += 1

    return {
        'ageGroups': json.dumps(ageGroupsArray),
        'userAgeGroup': flask_praetorian.current_user().ageGroup}, 200