
def populate_calculated_fields(objective_summary_data):
    if type(objective_summary_data) is list:
        for data in objective_summary_data:
            calculate_and_add_additional_fields(data)
    else:
        calculate_and_add_additional_fields(objective_summary_data)

    return objective_summary_data


def calculate_and_add_additional_fields(summary_data):
    total_count = summary_data['total_count']
    not_on_track_count = summary_data['not_on_track_count']
    on_track_count = total_count - not_on_track_count
    summary_data['on_track_count'] = on_track_count
    summary_data['on_track_percentage'] = format(on_track_count / total_count, '%')
    summary_data['not_on_track_percentage'] = format(not_on_track_count / total_count, '%')
    return summary_data
