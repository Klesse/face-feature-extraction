import psycopg2
import json
from FaceRecognition import *

face = FaceRecognition()

cur = face.conn.cursor()

model = FaceRecognition()

features_np = model.extract_features('./Tom_Hanks/Tom_Hanks_mask.jpg')

print(features_np.shape)

json_feature = json.dumps(features_np.tolist())

# print(json_feature)

sql_query = "INSERT INTO face_features(name, feature) VALUES (%s, %s);"

cur.execute(sql_query, ('Tom Hanks', json_feature))
face.conn.commit()

# Query

cur.execute('SELECT * FROM face_features;')
rows = cur.fetchall()
face.conn.commit()

for row in rows:
    print(row)

# cur.execute('DELETE FROM face_features *;')
# conn.commit()

# Closing the Database Access
cur.close()
face.conn.close()