from sklearn.model_selection import train_test_split
from src.training.select_data.select_data_dependencies import SelectDataDependencies
from options.prepro_options import PreproOptions

def run_select_data(opts: PreproOptions):
    deps = SelectDataDependencies(opts)

    # Fetch messages of specified users and folders
    messages = deps.message_fetcher.fetch(
        opts.selected_folders,
        opts.user_id_int_dict
    )

    # Filter based on the filtering options
    messages = deps.message_filterer.filter(messages, opts)
    
    # Print messages
    deps.printer.print_message_summary(messages)

    # Split into train and test data
    labels = [x.user_int_id for x in messages]
    train_messages, test_messages, _, _ = train_test_split(messages, labels, test_size=opts.test_size, stratify=labels)

    return train_messages, test_messages

