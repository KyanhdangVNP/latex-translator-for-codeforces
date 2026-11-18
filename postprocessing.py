from pathlib import Path
import re


def process_latex_file(filepath):
    r"""Reads a LaTeX file, replaces \( and \) with $, and returns the processed content.

    Args:
        filepath: The path to the LaTeX file.

    Returns:
        The processed content of the LaTeX file as a string, or None if an error
        occurs.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # (comments to remind the future-self developer, ignore these)
        # Use regular expressions for more robust replacement
        # The r before 'blah blah blah' means that the string is to be treated as a raw string,
        # which means all escape codes will be ignored (IDK maybe EXCEPT \, I dunno???)

        # Replacements for Codeforces / Polygon compatibility
        content = re.sub(r"\\\(", "$", content)  # Replace \( with $
        content = re.sub(r"\\\)", "$", content)  # Replace \) with $
        content = re.sub(r"\\tightlist", "", content)  # Remove \tightlist
        content = re.sub(r"\\textless\{\}", "<", content)  # Replace \textless{} with <
        content = re.sub(r"\\textgreater\{\}", ">", content)  # Replace \textgreater{} with >
        content = re.sub(r"\{Copy\}", "", content)  # Remove {Copy}
        content = re.sub(r"\\begin\{quote\}", "", content)  # Remove \begin{quote}
        content = re.sub(r"\\end\{quote\}", "", content)  # Remove \end{quote}
        content = re.sub(r"\\emph", r"\\it", content)  # Replace \emph with \it to prevent the text being italic instead of underlined
        content = re.sub(r"\\hat\{\}", "^", content)  # Replace \hat{} with ^

        # ADD MORE HERE IF THE SYSTEM SKIPPED SOME "TRANSLATING" KEYWORDS

        # Replacing some Math symbols that are not supported on Codeforces into visible-only symbols (without Latex syntaxes):
        content = re.sub(r"\\mathbb\{\\in N\}", r"\\ ∈ \\ ℕ", content)
        content = re.sub(r"\\in", "∈", content)
        return content

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_processed_content(content, output_filepath):
    """Writes the processed content to a new file."""
    if content is None:
        return

    try:
        with open(output_filepath, "w", encoding="utf-8") as outfile:
            outfile.write(content)
        print(f"Processed content written to {output_filepath}")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    # Look for output.tex inside d:\latex-converter-test\ automatically
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir / "output.tex"
    output_file = base_dir / "output_postprocessed.tex"

    processed_content = process_latex_file(input_file)
    if processed_content:
        write_processed_content(processed_content, output_file)
