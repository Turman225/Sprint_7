import helper


create_courier_point = '/api/v1/courier'
login_courier_point = '/api/v1/courier/login'
create_order_point = '/api/v1/orders'
order_list_point = '/api/v1/orders'

create_user_payload = {
    "login": helper.generate_random_string(12),
    "password": helper.generate_random_string(12),
    "firstName": helper.generate_random_string(12)
}