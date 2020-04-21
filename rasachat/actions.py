# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import difflib
import random

from typing import Any, Text, Dict, List

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import UserUtteranceReverted

import sqlite3
import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
logger = logging.getLogger(__name__)

class ActionFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "I'm sorry. Please enter expected details."
        dispatcher.utter_message(message)

        return [UserUtteranceReverted()]








class ActionCircuit(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_submit_cir"
    def run(self, dispatcher, tracker, domain):
        opportunity_name = tracker.get_slot('opportunity_name')
        account_holder_name = tracker.get_slot('account_name')
        state_name = tracker.get_slot('state_name')
        primary_contact_name = tracker.get_slot('contact_name')
        title_name = tracker.get_slot('title_name')
        pricing_type = tracker.get_slot('pricing')
        estimate_type = tracker.get_slot('estimate_type')
        circuit_type = tracker.get_slot('circuit_type')
        product_type = tracker.get_slot('product_type')
        bandwidth = tracker.get_slot('bandwidth')
        location_a = tracker.get_slot('locationA')
        location_z = tracker.get_slot('locationZ')
        location_a_a = tracker.get_slot('location_A_a')
        location_z_z = tracker.get_slot('location_Z_z')

        print("value of opportunity name " + str(opportunity_name))
        print("value of account name " + str(account_holder_name))
        print("value of state name " + str(state_name))
        print("value of contact name " + str(primary_contact_name))
        print("value of title name " + str(title_name))
        print("value of pricing name " + str(pricing_type))
        print("value of estimate name " + str(estimate_type))
        print("value of circuit type "+str(circuit_type))
        print("value of product type "+str(product_type))
        print("value of bandwidth " + str(bandwidth))
        print("value of locationA " + str(location_a))
        print("value of locationZ " + str(location_z))
        print("value of locationA_a " + str(location_a_a))
        print("value of locationZ_z " + str(location_z_z))


        opportunity_type = "New Business"

        con = sqlite3.connect('upnchat.db')
        cursorObj = con.cursor()

        entities = (
        opportunity_name, opportunity_type, account_holder_name, state_name, primary_contact_name, title_name, pricing_type,
        estimate_type,
        circuit_type, product_type, bandwidth, location_a_a, location_z_z)
        cursorObj.execute(
            "INSERT INTO UPN_account_information (Opportunity_name, Opportunity_type,Account_holder_name, State_name,Primary_contact_name, Title_name,  Pricing_type, Estimate_type, Circuit_type, Product_type, Bandwidth,  Location_A, Location_Z) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            entities)
        con.commit()

        cursorObj.execute('SELECT MAX(id) FROM UPN_account_information')
        rows = cursorObj.fetchall()
        Id = rows[0][0]
        con.close()

        message = 'Your circuit has been added with account name "{}" and to check the details [Click here](http://127.0.0.1:8000/getUPNAccountDetails/{}).'. format(account_holder_name,Id)

        dispatcher.utter_message(message)
        return []
