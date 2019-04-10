from ask_meagain import db

class TestQuestions(db.Model):
    __tablename__ = 'testQ'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionText = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    choices = db.relationship('TestChoices', backref='testQ')
    responces = db.relationship('TestResponses', backref='testR')
    
    def __str__(self):
        return self.questionText

class TestChoices(db.Model):
    __tablename__ = 'testC'
    qid = db.Column(db.Integer, db.ForeignKey('testQ.id'))
    choiceText = db.Column(db.Text)
    choiceId = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __str__(self):
        return self.choiceText

class TestResponses(db.Model):
    __tablename__ = 'testR'
    resId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qid = db.Column(db.Integer, db.ForeignKey('testQ.id'))
    responce = db.Column(db.Integer)
    dt = db.Column(db.DateTime)
    studentId = db.Column(db.Integer)

    def __str__(self):
        return self.responce
