from sql_alchemy import banco


class FileModel(banco.Model):
    __tablename__ = 'files'

    file_id = banco.Column(banco.String(200), primary_key=True)
    file_name = banco.Column(banco.String(200))

    def __init__(self, file_id, file_name):
        self.file_id = file_id
        self.file_name = file_name

    def json(self):
        return {
            'file_id': self.file_id,
            'file_name': self.file_name,
        }

    @classmethod
    def find_file(cls, file_id):
        file = cls.query.filter_by(file_id=file_id).first()
        if file:
            return file
        return None

    def save_file(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_file(self):
        banco.session.delete(self)
        banco.session.commit()
