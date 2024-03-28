from db_operations import DBOperations

db_operations = DBOperations('weather_data.sqlite')
db_operations.initialize_db()
db_operations.insert_sample_data()
