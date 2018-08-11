import uuid
from datetime import datetime

from src.common.database import Database


class LoanApplication(object):
    def __init__(self, loan_category, district, caste, bank, roi, loan_reason, received_date, status, status_date,
                 no_of_demands, ann_loan_id, loan_amount, user_id, user_name, annual_income=None, age=None, gender=None,
                 address=None, applicant_name=None, n1=None, s1=None, a1=None, n2=None, s2=None, a2=None, n3=None,
                 s3=None, a3=None, n4=None, s4=None, a4=None, n5=None, s5=None, a5=None, n6=None, s6=None, a6=None,
                 n7=None, s7=None, a7=None, n8=None, s8=None, a8=None, n9=None, s9=None, a9=None, n10=None, s10=None,
                 a10=None, no_of_beneficiaries=None, _id=None, no_of_shgs=None, app1=None, app2=None, app3=None,
                 app4=None, app5=None, app6=None, app7=None, app8=None, app9=None, app10=None, cheque_number=None,
                 sub_bank=None, final_collection_amount=None, amount_yet_to_pay=None, father_name=None,
                 screening_date=None, loan_number=None):
        self.applicant_name = applicant_name
        self.father_name = father_name
        self.loan_category = loan_category
        self.age = age
        self.gender = gender
        self.address = address
        self.district = district
        self.caste = caste
        self.annual_income = annual_income
        self.bank = bank
        self.sub_bank = sub_bank
        self.loan_reason = loan_reason

        if received_date:
            self.received_date = (datetime.combine(datetime.strptime(received_date, '%Y-%m-%d').date(),
                                                   datetime.now().time()))
        else:
            self.received_date = received_date

        if screening_date:
            self.screening_date = (datetime.combine(datetime.strptime(screening_date, '%Y-%m-%d').date(),
                                                    datetime.now().time()))
        else:
            self.screening_date = screening_date

        self.status = status

        if status_date:
            self.status_date = (datetime.combine(datetime.strptime(status_date, '%Y-%m-%d').date(),
                                                 datetime.now().time()))
        else:
            self.status_date = status_date

        self.ann_loan_id = ann_loan_id
        self.loan_amount = loan_amount
        self.roi = roi
        self.no_of_demands = no_of_demands
        self.user_id = user_id
        self.user_name = user_name
        self.no_of_shgs = no_of_shgs
        self.n1 = n1
        self.s1 = s1
        self.a1 = a1
        self.n2 = n2
        self.s2 = s2
        self.a2 = a2
        self.n3 = n3
        self.s3 = s3
        self.a3 = a3
        self.n4 = n4
        self.s4 = s4
        self.a4 = a4
        self.n5 = n5
        self.s5 = s5
        self.a5 = a5
        self.n6 = n6
        self.s6 = s6
        self.a6 = a6
        self.n7 = n7
        self.s7 = s7
        self.a7 = a7
        self.n8 = n8
        self.s8 = s8
        self.a8 = a8
        self.n9 = n9
        self.s9 = s9
        self.a9 = a9
        self.n10 = n10
        self.s10 = s10
        self.a10 = a10
        self.app1 = app1
        self.app2 = app2
        self.app3 = app3
        self.app4 = app4
        self.app5 = app5
        self.app6 = app6
        self.app7 = app7
        self.app8 = app8
        self.app9 = app9
        self.app10 = app10
        self.no_of_beneficiaries = no_of_beneficiaries
        self.cheque_number = cheque_number
        self.final_collection_amount = final_collection_amount
        self.amount_yet_to_pay = int(loan_amount)
        self.loan_number = int(loan_number)
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='loans', data=self.json())

    @classmethod
    def update_loan_app(cls, applicant_name, loan_category, age, gender, address, district, annual_income, sub_bank,
                        caste, bank, loan_reason, loan_amount, received_date, status, status_date, roi, no_of_demands,
                        ann_loan_id, user_id, user_name, loan_id, n1, s1, a1, n2, s2, a2, n3, s3, a3, n4, s4, a4,
                        n5, s5, a5, n6, s6, a6, n7, s7, a7, n8, s8, a8, n9, s9, a9, n10, s10, a10, no_of_beneficiaries,
                        no_of_shgs, app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, cheque_number,
                        amount_to_pay, father_name, loan_number):
        Database.update_application(collection='loans', query={'_id': loan_id}, applicant_name=applicant_name,
                                    loan_category=loan_category, age=age, gender=gender, address=address, roi=roi,
                                    district=district, annual_income=annual_income, caste=caste, bank=bank, sb=sub_bank,
                                    no_of_demands=no_of_demands, loan_reason=loan_reason, loan_amount=loan_amount,
                                    received_date=received_date, status=status, status_date=status_date,
                                    ann_loan_id=ann_loan_id, user_id=user_id, user_name=user_name, n1=n1, s1=s1, a1=a1,
                                    n2=n2, s2=s2, a2=a2, n3=n3, s3=s3, a3=a3, n4=n4, s4=s4, a4=a4, n5=n5, s5=s5, a5=a5,
                                    n6=n6, s6=s6, a6=a6, n7=n7, s7=s7, a7=a7, n8=n8, s8=s8, a8=a8, n9=n9, s9=s9, a9=a9,
                                    n10=n10, s10=s10, a10=a10, no_of_beneficiaries=no_of_beneficiaries,
                                    no_of_shgs=no_of_shgs, app1=app1, app2=app2, app3=app3, app4=app4, app5=app5,
                                    app6=app6, app7=app7, app8=app8, app9=app9, app10=app10,
                                    cheque_number=cheque_number, amount_to_pay=amount_to_pay, father_name=father_name,
                                    loan_number=loan_number)

    @classmethod
    def update_pend_amount(cls, amount_yet_to_be_paid, loan_id):
        Database.update_pending_amount(collection='loans', query={'_id': loan_id},
                                       amount_yet_to_be_paid=amount_yet_to_be_paid)

    @classmethod
    def deletefrom_mongo(cls, _id):
        Database.delete_from_mongo(collection='loans', query={'_id': _id})

    def json(self):
        return {
            'applicant_name': self.applicant_name,
            'father_name': self.father_name,
            'loan_category': self.loan_category,
            'age': self.age,
            'gender': self.gender,
            'address': self.address,
            'district': self.district,
            'caste': self.caste,
            'annual_income': self.annual_income,
            'bank': self.bank,
            'sub_bank': self.sub_bank,
            'loan_reason': self.loan_reason,
            'received_date': self.received_date,
            'screening_date': self.screening_date,
            'status': self.status,
            'status_date': self.status_date,
            'ann_loan_id': self.ann_loan_id,
            'loan_amount': self.loan_amount,
            'loan_number': self.loan_number,
            'amount_yet_to_pay': self.amount_yet_to_pay,
            'final_collection_amount': self.final_collection_amount,
            'roi': self.roi,
            'no_of_demands': self.no_of_demands,
            'user_name': self.user_name,
            'user_id': self.user_id,
            'no_of_shgs': self.no_of_shgs,
            'shg1': {'name': self.n1, 'strength': self.s1, 'amount': self.a1, 'applicants': self.app1},
            'shg2': {'name': self.n2, 'strength': self.s2, 'amount': self.a2, 'applicants': self.app2},
            'shg3': {'name': self.n3, 'strength': self.s3, 'amount': self.a3, 'applicants': self.app3},
            'shg4': {'name': self.n4, 'strength': self.s4, 'amount': self.a4, 'applicants': self.app4},
            'shg5': {'name': self.n5, 'strength': self.s5, 'amount': self.a5, 'applicants': self.app5},
            'shg6': {'name': self.n6, 'strength': self.s6, 'amount': self.a6, 'applicants': self.app6},
            'shg7': {'name': self.n7, 'strength': self.s7, 'amount': self.a7, 'applicants': self.app7},
            'shg8': {'name': self.n8, 'strength': self.s8, 'amount': self.a8, 'applicants': self.app8},
            'shg9': {'name': self.n9, 'strength': self.s9, 'amount': self.a9, 'applicants': self.app9},
            'shg10': {'name': self.n10, 'strength': self.s10, 'amount': self.a10, 'applicants': self.app10},
            'no_of_beneficiaries': self.no_of_beneficiaries,
            'cheque_number': self.cheque_number,
            '_id': self._id,
        }

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find('loans', {'_id': _id})
        return [cls(**data) for data in data]
