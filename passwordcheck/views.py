from django.shortcuts import render


def check_password(request):

    result = None

    if request.method == "POST":

        password = request.POST.get("password", "")

        length_ok = len(password) >= 8
        uppercase_ok = any(char.isupper() for char in password)
        lowercase_ok = any(char.islower() for char in password)
        number_ok = any(char.isdigit() for char in password)
        special_ok = any(not char.isalnum() for char in password)

        score = sum([
            length_ok,
            uppercase_ok,
            lowercase_ok,
            number_ok,
            special_ok
        ])

        if score == 5:
            strength = "STRONG"
            message = "Great! Your password satisfies all the basic requirements."

        elif score >= 3:
            strength = "MEDIUM"
            message = "Your password is almost strong. Add the missing requirements."

        else:
            strength = "WEAK"
            message = "Your password is weak. Improve it using the suggestions below."

        result = {
            "password": password,
            "length": length_ok,
            "uppercase": uppercase_ok,
            "lowercase": lowercase_ok,
            "number": number_ok,
            "special": special_ok,
            "strength": strength,
            "message": message
        }

    return render(request, "passwordcheck/index.html", {
        "result": result
    })