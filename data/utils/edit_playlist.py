def convert_to_lower_and_underscore(string):
    """
    Gets "Project name"
    :return: "project_name"
    """

    return "_".join([word for word in string.lower().split()])