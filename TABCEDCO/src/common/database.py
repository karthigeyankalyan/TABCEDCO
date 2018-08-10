import os

import pymongo


class Database(object):
    URI = os.environ['MONGODB_URI']
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['heroku_xwlzxcmr']

    # URI = "mongodb://127.0.0.1:27017"
    # DATABASE = None
    #
    # @staticmethod
    # def initialize():
    #     client = pymongo.MongoClient(Database.URI)
    #     Database.DATABASE = client['TABCEDCO']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_receipt(collection, query, invoice_date, nature_of_transaction, account_head, bank_account, amount,
                       user_id, user_name, doc_account_head, cheque_number, payment_voucher, depositing_bank,
                       adjustment_voucher, voucher_date, ledger, cleared, cheque_date, narration):

        return Database.DATABASE[collection].update_one(query, {'$set': {'invoice_date': invoice_date,
                                                                         'cheque_date': cheque_date,
                                                                         'nature_of_transaction': nature_of_transaction,
                                                                         'account_head': account_head,
                                                                         'doc_account_head': doc_account_head,
                                                                         'bank_account': bank_account,
                                                                         'depositing_bank': depositing_bank,
                                                                         'adjustment_voucher': adjustment_voucher,
                                                                         'payment_voucher': payment_voucher,
                                                                         'voucher_date': voucher_date,
                                                                         'ledger': ledger,
                                                                         'cleared': cleared,
                                                                         'amount': amount,
                                                                         'narration': narration,
                                                                         'cheque_number': cheque_number,
                                                                         'user_id': user_id,
                                                                         'user_name': user_name}}, True)

    @staticmethod
    def update_balance(collection, query, amount, changed_on_date):
        return Database.DATABASE[collection].update_one(query, {'$set': {'amount': amount,
                                                                         'changed_on_date': changed_on_date}}, True)

    @staticmethod
    def update_application(collection, query, applicant_name, loan_category, age, gender, address, district, roi,
                           annual_income, caste, bank, loan_reason, loan_amount, received_date, status, status_date,
                           ann_loan_id, user_id, user_name, n1, s1, a1, n2, s2, a2, n3, s3, a3, n4, s4, a4, n5, s5, a5,
                           n6, s6, a6, n7, s7, a7, n8, s8, a8, n9, s9, a9, n10, s10, a10, no_of_beneficiaries,
                           no_of_shgs, app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, cheque_number,
                           no_of_demands, sb, amount_to_pay, father_name):
        return Database.DATABASE[collection].update_one(query, {'$set': {'applicant_name': applicant_name,
                                                                         'father_name': father_name,
                                                                         'loan_category': loan_category,
                                                                         'age': age,
                                                                         'gender': gender,
                                                                         'address': address,
                                                                         'district': district,
                                                                         'caste': caste,
                                                                         'annual_income': annual_income,
                                                                         'bank': bank,
                                                                         'sub_bank': sb,
                                                                         'loan_reason': loan_reason,
                                                                         'received_date': received_date,
                                                                         'status': status,
                                                                         'status_date': status_date,
                                                                         'ann_loan_id': ann_loan_id,
                                                                         'loan_amount': loan_amount,
                                                                         'roi': roi,
                                                                         'no_of_demands': no_of_demands,
                                                                         'user_name': user_name,
                                                                         'user_id': user_id,
                                                                         'no_of_shgs': no_of_shgs,
                                                                         'shg1': {'name': n1, 'strength': s1,
                                                                                  'amount': a1, 'applicants': app1},
                                                                         'shg2': {'name': n2, 'strength': s2,
                                                                                  'amount': a2, 'applicants': app2},
                                                                         'shg3': {'name': n3, 'strength': s3,
                                                                                  'amount': a3, 'applicants': app3},
                                                                         'shg4': {'name': n4, 'strength': s4,
                                                                                  'amount': a4, 'applicants': app4},
                                                                         'shg5': {'name': n5, 'strength': s5,
                                                                                  'amount': a5, 'applicants': app5},
                                                                         'shg6': {'name': n6, 'strength': s6,
                                                                                  'amount': a6, 'applicants': app6},
                                                                         'shg7': {'name': n7, 'strength': s7,
                                                                                  'amount': a7, 'applicants': app7},
                                                                         'shg8': {'name': n8, 'strength': s8,
                                                                                  'amount': a8, 'applicants': app8},
                                                                         'shg9': {'name': n9, 'strength': s9,
                                                                                  'amount': a9, 'applicants': app9},
                                                                         'shg10': {'name': n10, 'strength': s10,
                                                                                   'amount': a10, 'applicants': app10},
                                                                         'no_of_beneficiaries': no_of_beneficiaries,
                                                                         'cheque_number': cheque_number,
                                                                         "amount_yet_to_pay":
                                                                             amount_to_pay}}, True)

    @staticmethod
    def update_demand(collection, query, demand_number, demand_date, cheque_number, cheque_date, principal_collected,
                      interest_collected, penal_interest, belated_interest, service_charge, no_of_demands,
                      closing_balance_principal_due, closing_balance_principal_ndue, closing_balance_interest_due):
        return Database.DATABASE[collection].update_one(query, {'$set': {'demand_number': demand_number,
                                                                         "demand_date": demand_date,
                                                                         "cheque_date": cheque_date,
                                                                         "cheque_number": cheque_number,
                                                                         "principal_collected": principal_collected,
                                                                         "interest_collected": interest_collected,
                                                                         "penal_interest": penal_interest,
                                                                         "belated_interest": belated_interest,
                                                                         "service_charge": service_charge,
                                                                         "no_of_demands": no_of_demands,
                                                                         "closing_balance_principal_due":
                                                                             closing_balance_principal_due,
                                                                         "closing_balance_principal_ndue":
                                                                             closing_balance_principal_ndue,
                                                                         "closing_balance_interest_due":
                                                                             closing_balance_interest_due}}, True)

    @staticmethod
    def update_pending_amount(collection, query, amount_yet_to_be_paid):
        return Database.DATABASE[collection].update_one(query, {'$set':
                                                                {"amount_yet_to_pay": amount_yet_to_be_paid}}, True)

    @staticmethod
    def delete_from_mongo(collection, query):
        print(query)
        Database.DATABASE[collection].remove(query)
