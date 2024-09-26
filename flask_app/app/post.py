#!/usr/bin/env python
from app import sqlsession
from app.user_stories import UserStoryVN

def add_data_to_db(us_instances, output_ontobj, output_prologobj, m, form_data):
    # get the starting position for the new userstory IDs, based on the presence/absence of
    # user stories already in the database
    starting_id = sqlsession.query(UserStoryVN).order_by(UserStoryVN.id.desc()).first()
    if starting_id is None:
        starting_id = 0
    else:
        starting_id = starting_id.id
    print('FIRST STARTING_ID', starting_id)