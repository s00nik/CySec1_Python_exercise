def password_check(username: str, password: str) -> str:
    score = 0
    if len(password) >= 12:
        score += 1
    else:
        score -= 1
    if not password.isalnum():
        score += 1
    else:
        score -= 1
    weak_patterns = [username.lower(), "12345", "qwert", "password"]
    if any(pattern in password.lower() for pattern in weak_patterns):
        score -= 1
    if score >= 2:
        return "good"
    elif score == 1:
        return "Ok"
    elif score == 0:
        return "weak"
    else:
        return "bad"


def main() -> None:
    # Tests only for student side debugging
    assert password_check("Hans", "asdhf2324#fq1sa") == "good"
    assert password_check("Dieter", "securepassword!") == "Ok"
    assert password_check("Kevin", "Kevin2002!") == "weak"
    assert password_check("Bob", "qwertz") == "bad"


if __name__ == '__main__':
    main()
