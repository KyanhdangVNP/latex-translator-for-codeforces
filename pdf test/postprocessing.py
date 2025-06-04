import re

def process_latex_file(filepath):
    """
    Reads a LaTeX file, replaces \( and \) with $, and returns the processed content.

    Args:
        filepath: The path to the LaTeX file.

    Returns:
        The processed content of the LaTeX file as a string, or None if an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # Handle potential encoding issues
            content = f.read()

        # Use regular expressions for more robust replacement
        # The r before 'blah blah blah' means that the string is to be treated as a raw string,
        # which means all escape codes will be ignored (IDK maybe EXCEPT \, I dunno???)
        content = re.sub(r'\\\(', r'$', content)  # Replace \( with $
        content = re.sub(r"\\\)", r'$', content)  # Replace \) with $
        content = re.sub('\\tightlist', '', content) # Remove tightlist
        content = re.sub(r'\\textless{}', r'<', content) # Remove \textless{}
        content = re.sub(r'\\textgreater{}', r'>', content) # Remove \textgreater{}
        content = re.sub(r'{Copy}', r'', content) # Remove {Copy}
        content = re.sub(r'\\begin{quote}', r'', content) # Remove \begin{quote}
        content = re.sub(r'\\end{quote}', r'', content) # Remove \end{quote}
        content = re.sub(r'\\emph', r'\\it', content) # Replace \emph with \it to prevent the text being italic instead of underlined
        content = re.sub(r'\\hat{}', r'^', content) # Replace \hat{} with ^

        # ADD MORE HERE IF THE SYSTEM SKIPPED SOME "TRANSLATING" KEYWORDS

        # Replacing some Math symbols that are not supported on Codeforces into visible-only symbols (without Latex syntaxes):
        content = re.sub(r'\\mathbb{\\in N}', r'\ ∈ \ ℕ', content) # Replace \mathbb{\in N} with ∈ ℕ (with spaces in Latex syntaxes)
        content = re.sub(r'\\in', r'∈', content) # Replace \in with ∈

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
        return  # Nothing to write

    try:
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"Processed content written to {output_filepath}")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    input_file = "output.tex"  # Replace with your LaTeX file path
    output_file = "output_postprocessed.tex" # Replace with desired output file path

    processed_content = process_latex_file(input_file)

    if processed_content:
       write_processed_content(processed_content, output_file)

        # Example of printing the processed content (optional):
        #print(processed_content)