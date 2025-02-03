import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body) #aca esta recibiendo la respuesta del sender
    return response.json()["authToken"] #me regresa el token

def positive_assert(kit_body):
    user_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body,user_token)
    assert response.status_code == 201
    assert  response.jason()["name"] ==kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test1_create_kit_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)



