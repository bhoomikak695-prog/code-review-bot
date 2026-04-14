def review_code(code: str, language: str = "Python") -> str:
    try:
        lines = code.strip().split("\n")
        feedback = []

        for i, line in enumerate(lines, 1):

            # ---------------- PYTHON RULES ----------------
            if language == "Python":
                if "except:" in line:
                    feedback.append(f"Line {i}: Bare `except:` clause — catch a specific exception instead.")
                if "==" in line and "None" in line:
                    feedback.append(f"Line {i}: Use `is None` instead of `== None`.")
                if len(line) > 79:
                    feedback.append(f"Line {i}: Line too long ({len(line)} chars) — PEP8 recommends max 79.")
                if "print(" in line:
                    feedback.append(f"Line {i}: Consider using logging instead of print().")
                if "global " in line:
                    feedback.append(f"Line {i}: Avoid global variables if possible.")

            # ---------------- JAVASCRIPT RULES ----------------
            elif language == "JavaScript":
                if "==" in line:
                    feedback.append(f"Line {i}: Use '===' instead of '==' for strict comparison.")
                if "var " in line:
                    feedback.append(f"Line {i}: Avoid 'var', use 'let' or 'const'.")
                if "console.log" in line:
                    feedback.append(f"Line {i}: Avoid console.log in production code.")
                if len(line) > 80:
                    feedback.append(f"Line {i}: Line too long ({len(line)} chars).")

            # ---------------- JAVA RULES ----------------
            elif language == "Java":
                if "==" in line and "String" in line:
                    feedback.append(f"Line {i}: Use `.equals()` instead of '==' for String comparison.")
                if "System.out.println" in line:
                    feedback.append(f"Line {i}: Avoid System.out.println in production, use logging frameworks.")
                if "catch(Exception" in line:
                    feedback.append(f"Line {i}: Avoid catching generic Exception.")
                if len(line) > 100:
                    feedback.append(f"Line {i}: Line too long ({len(line)} chars).")
                if "public static" in line and "main" not in line:
                    feedback.append(f"Line {i}: Check unnecessary static usage.")

            # ---------------- C++ RULES ----------------
            elif language == "C++":
                if "using namespace std" in line:
                    feedback.append(f"Line {i}: Avoid 'using namespace std;' in header/global scope.")
                if "cout" in line:
                    feedback.append(f"Line {i}: Consider using proper logging instead of cout.")
                if "NULL" in line:
                    feedback.append(f"Line {i}: Use 'nullptr' instead of NULL (modern C++).")
                if "printf" in line:
                    feedback.append(f"Line {i}: Avoid printf, use cout or modern C++ streams.")
                if len(line) > 100:
                    feedback.append(f"Line {i}: Line too long ({len(line)} chars).")

        # ---------------- FINAL OUTPUT ----------------
        if not feedback:
            return "No major issues found! Code looks clean."

        return "\n".join(feedback)

    except Exception as e:
        return f"Error during review: {str(e)}"