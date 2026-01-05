import pdfminer.high_level

import os
dirname = os.path.dirname(__file__)
os.chdir(dirname)

def pdf_to_tex(pdf_path, tex_path):
    try:
        # Extract text from PDF
        text = pdfminer.high_level.extract_text(pdf_path)

        # Format as LaTeX document
        tex_content = """
        \documentclass{article}
        \usepackage{geometry}
        \geometry{a4paper, margin=1in}
        \begin{document}
        """
        tex_content += text
        tex_content += """
        \end{document}
        """

        # Save as .tex file
        with open(tex_path, "w", encoding="utf-8") as tex_file:
            tex_file.write(tex_content)
        
        print(f"Conversion successful: {tex_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
pdf_to_tex("input.pdf", "output.tex")
