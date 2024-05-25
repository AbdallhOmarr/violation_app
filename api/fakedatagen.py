# # # import requests
# # # import json 

# # # def create_department(base_url, endpoint, data):
# # #     """
# # #     Function to create a department via HTTP POST request.

# # #     Args:
# # #         base_url (str): The base URL of the API.
# # #         endpoint (str): The endpoint for creating departments.
# # #         data (list): A list of dictionaries containing department data.

# # #     Returns:
# # #         list: A list of response objects for each department created.
# # #     """
# # #     responses = []

# # #     for department_data in data:
# # #         response = requests.post(base_url + endpoint, json=department_data)
# # #         try:
# # #             response_json = response.json()
# # #             responses.append(response_json)
# # #         except json.JSONDecodeError:
# # #             print(f"Raw Response status code: {response.status_code}")
# # #             responses.append({'error': 'Failed to decode JSON response'})

# # #     return responses

# # # # Example data for multiple departments
# # # departments_data = [
# # #     {"department_name": "Department of Engineering"},
# # #     {"department_name": "Department of Computer Science"},
# # #     {"department_name": "Department of Mathematics"}
# # # ]

# # # # Define the base URL of your API
# # # base_url = 'http://localhost:8000/api/'

# # # # Create departments in bulk
# # # responses = create_department(base_url, 'departments/', departments_data)

# # # # Print the responses
# # # for idx, response in enumerate(responses):
# # #     print(f"Department {idx+1} - Response: {response}")




# # from faker import Faker
# # import requests

# # fake = Faker()

# # def generate_trainer_data():
# #     """
# #     Function to generate random trainer data.

# #     Returns:
# #         dict: A dictionary containing randomly generated trainer data.
# #     """
# #     return {
# #         "account_number": fake.random_number(digits=9),
# #         "full_name": fake.name(),
# #         "mobile_number": fake.phone_number(),
# #         "status": fake.random_element(elements=("Active", "Inactive")),
# #         "password": fake.password()
# #     }

# # def create_trainer(base_url, endpoint, data):
# #     """
# #     Function to create a trainer via HTTP POST request.

# #     Args:
# #         base_url (str): The base URL of the API.
# #         endpoint (str): The endpoint for creating trainers.
# #         data (dict): A dictionary containing trainer data.

# #     Returns:
# #         dict: The response object for the trainer created.
# #     """
# #     response = requests.post(base_url + endpoint, json=data)
# #     try:
# #         response_json = response.json()
# #     except ValueError:
# #         response_json = {'error': 'Failed to decode JSON response'}
# #     return response_json

# # # Define the base URL of your API
# # base_url = 'http://localhost:8000/api/'

# # # Generate and create multiple trainers
# # num_trainers = 50
# # for _ in range(num_trainers):
# #     trainer_data = generate_trainer_data()
# #     response = create_trainer(base_url, 'trainers/', trainer_data)
# #     print("Trainer - Response:", response)



# from faker import Faker
# import random
# import requests

# fake = Faker()

# # Sample departments to choose from
# departments = [x for x in range(2,7)]

# def generate_trainee_data():
#     """
#     Function to generate random trainee data.

#     Returns:
#         dict: A dictionary containing randomly generated trainee data.
#     """
#     return {
#         "academic_number": fake.random_number(digits=11),
#         "full_name": fake.name(),
#         "mobile_number": fake.phone_number(),
#         "department": random.choice(departments)
#     }

# def create_trainee(base_url, endpoint, data):
#     """
#     Function to create a trainee via HTTP POST request.

#     Args:
#         base_url (str): The base URL of the API.
#         endpoint (str): The endpoint for creating trainees.
#         data (dict): A dictionary containing trainee data.

#     Returns:
#         dict: The response object for the trainee created.
#     """
#     response = requests.post(base_url + endpoint, json=data)
#     try:
#         response_json = response.json()
#     except ValueError:
#         response_json = {'error': 'Failed to decode JSON response'}
#     return response_json

# # Define the base URL of your API
# base_url = 'http://localhost:8000/api/'

# # Generate and create multiple trainees
# num_trainees = 50
# for _ in range(num_trainees):
#     trainee_data = generate_trainee_data()
#     response = create_trainee(base_url, 'trainees/', trainee_data)
#     print("Trainee - Response:", response)



import requests
import random
from faker import Faker

fake = Faker()

# Define the base URL of your API
base_url = 'http://localhost:8000/api/'

# Function to get all trainer IDs
def get_trainer_ids():
    response = requests.get(base_url + 'trainers/')
    trainers = response.json()
    return [trainer['id'] for trainer in trainers]

# Function to get all trainee IDs
def get_trainee_ids():
    response = requests.get(base_url + 'trainees/')
    trainees = response.json()
    return [trainee['id'] for trainee in trainees]

# Function to generate random violation data
def generate_violation_data(trainee_ids, trainer_ids):
    violation_types = ["Plagiarism", "Cheating", "Misconduct", "Late Submission", "Absenteeism"]
    return {
        "trainee": random.choice(trainee_ids),
        "trainer": random.choice(trainer_ids),
        "date": "2024-04-25T12:00:00Z",  # Example date (modify as needed)
        "violation_type": random.choice(violation_types),
        "violation_details": fake.paragraph(nb_sentences=2),  # Random text for violation details
        "taken_procedure": fake.paragraph(nb_sentences=1),  # Random text for taken procedure
        "degree": random.randint(1, 5)  # Example degree (modify as needed)
    }

# Function to create a violation via HTTP POST request
def create_violation(base_url, endpoint, data):
    response = requests.post(base_url + endpoint, json=data)
    try:
        response_json = response.json()
    except ValueError:
        response_json = {'error': 'Failed to decode JSON response'}
    return response_json

# Get all trainer and trainee IDs
trainer_ids = get_trainer_ids()
trainee_ids = get_trainee_ids()

# Generate and create multiple violations
num_violations = 50
for _ in range(num_violations):
    violation_data = generate_violation_data(trainee_ids, trainer_ids)
    response = create_violation(base_url, 'violations/', violation_data)
    print("Violation - Response:", response)
