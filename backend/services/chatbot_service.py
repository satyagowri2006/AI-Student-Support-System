def generate_response(question):

    question = question.lower()

    if "admission" in question:
        return "You can apply for admission through the Vignan University admission portal."

    elif "course" in question:
        return "Vignan University offers BTech, MBA, MCA and many other programs."

    elif "fees" in question:
        return "Fee details are available in the finance section."

    elif "hostel" in question:
        return "Hostel facilities include WiFi, mess and study rooms."

    else:
        return "Please contact the university help desk for more information."