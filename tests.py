from FaceRecognition import *


face = FaceRecognition()

cur = face.conn.cursor()

model = FaceRecognition()

model.data_to_db('./Tom_Hanks/Tom_Hanks_mask.jpg')


# Query

cur.execute('SELECT * FROM face_features;')
rows = cur.fetchall()
face.conn.commit()

for row in rows:
    print(row[2])

cur.execute('DELETE FROM face_features *;')
face.conn.commit()

# Closing the Database Access
cur.close()
face.conn.close()