from app_lib.src.pick_users.pick_user_dependencies import PickUserDependencies
from app_lib.options.prepro_options import PreproOptions

def run_pick_users(opts: PreproOptions):
    # Deps
    deps = PickUserDependencies(opts)

    # Fetch all users from the users.json file
    all_users = deps.user_fetcher.fetch(opts.user_filename)

    # Print out all users
    print('List of all users:')
    for u in all_users:
        u.print_me()

    # Request user input for users to include
    print('\nAlter the following list to contain the desired users, and copy it in.')
    user_set = str([(x.id, x.name) for x in all_users])
    print(user_set)
    
    # Gather and format user input
    selected_user_ids = input("\n\nEnter the user list: ")
    user_tuple_list = list(eval(selected_user_ids))
    selected_user_ids = [x[0] for x in user_tuple_list]
    selected_users = [x for x in all_users if x.id in selected_user_ids]
    print(f'\nSelected {len(selected_users)} users...\n')

    # Generate dictionaries
    user_id_int_dict =  { x.id : i for i,x in enumerate(selected_users) }
    user_int_name_dict = { i: x.name for i,x in enumerate(selected_users) }

    # print('\n\nSave the following to \'user_id_int_dict\' in the PreProOptions file')
    # print(user_id_int_dict)

    print('\nSave the following to \'user_int_name_dict\' in the ModelOptions file before deploying.')
    print(user_int_name_dict)
    
    return user_id_int_dict, user_int_name_dict
