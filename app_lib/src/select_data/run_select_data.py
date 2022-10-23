from app_lib.src.select_data.select_data_dependencies import SelectDataDependencies
from app_lib.options.prepro_options import PreproOptions
from app_lib.src.select_data.select_data_printer import SelectDataPrinter

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

    # TODO: May add a split here for test data

    return messages

