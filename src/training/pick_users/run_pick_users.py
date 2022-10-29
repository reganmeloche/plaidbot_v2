from src.training.pick_users.pick_user_dependencies import PickUserDependencies
from src.options.prepro_options import PreproOptions

def run_pick_users(opts: PreproOptions):
    deps = PickUserDependencies(opts)

    # Fetch all users from the users.json file
    all_users = deps.user_fetcher.fetch(opts.user_filename)

    # Print out all users
    deps.printer.mprint('List of all users:')
    for u in all_users:
        deps.printer.mprint(u.to_string())

    # Request user input for users to include
    deps.printer.mprint('\nAlter the following list to contain the desired users, and copy it in.')
    user_set = str([(x.id, x.name) for x in all_users])
    deps.printer.mprint(user_set)
    
    # Gather and format user input
    selected_user_ids = input("\n\nEnter the user list: ")
    user_tuple_list = list(eval(selected_user_ids))
    selected_user_ids = [x[0] for x in user_tuple_list]
    selected_users = [x for x in all_users if x.id in selected_user_ids]
    deps.printer.mprint(f'\nSelected {len(selected_users)} users...\n')

    # Generate dictionaries
    user_id_int_dict =  { x.id : i for i,x in enumerate(selected_users) }
    user_int_name_dict = { i: x.name for i,x in enumerate(selected_users) }

    deps.printer.mprint('\nSave the following to \'user_int_name_dict\' in the ModelOptions file before deploying.')
    deps.printer.mprint(user_int_name_dict)
    
    return user_id_int_dict, user_int_name_dict
