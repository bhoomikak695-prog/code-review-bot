def review_code(code: str, language: str = "Python") -> str:
    try:
        lines = code.strip().split("\n")
        feedback = []

        for i, line in enumerate(lines, 1):
            if "except:" in line:
                feedback.append(f"Line {i}: Bare `except:` clause — catch a specific exception instead.")

            if "== None" in line:
                feedback.append(f"Line {i}: Use `is None` instead of `== None`.")

            if len(line) > 79:
                feedback.append(f"Line {i}: Line too long ({len(line)} chars) — keep under 79.")

            if "print(" in line:
                feedback.append(f"Line {i}: Consider using logging instead of print().")

            if "global " in line:
                feedback.append(f"Line {i}: Avoid global variables if possible.")

        if not feedback:
            return "✅ No major issues found! Code looks clean."

        return "\n".join(feedback)

    except Exception as e:
        return f"❌ Error during review: {str(e)}"