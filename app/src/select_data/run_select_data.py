from app.lib.select_data.select_data_dependencies import SelectDataDependencies
from app.options.prepro_options import PreproOptions

def run_select_data(opts: PreproOptions):
    deps = SelectDataDependencies(opts)

    # Fetch messages of specified users and folders
    messages = deps.message_fetcher.fetch(
        opts.selected_folders,
        opts.user_id_int_dict
    )

    # Filter based on the filtering options
    messages = deps.message_filterer.filter(messages, opts)
    

    return messages

