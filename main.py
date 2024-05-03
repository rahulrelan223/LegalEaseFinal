import streamlit as st
from extraction import extract_text_from_image, extract_text_from_pdf
from preprocessing import preprocess_text
from simplification import simplify_jargon
from simplification import preprocess_simplify_paraphrase
import re

def main():
    # Set page configuration
    st.set_page_config(page_title="LegalEase", page_icon=":scales:", layout="wide")

    # Custom CSS styling
    st.markdown(
        """
        <style>
        .css-17eq0hr {
            width: 100%;
            padding: 20px;
            border-radius: 10px;
        }
        .btn-primary {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .btn-primary:hover {
            background-color: #0056b3;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("LegalEase - Simplify Your Document")

    st.header("Extract Text from Image or PDF")

    # Single button for choosing file type
    file_type = st.radio("Choose file type:", ("Image", "PDF"))

    if file_type == "Image":
        st.write("Upload an image file:")
        image_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

        if image_file is not None:
            st.write("Extracted text from image:")
            extracted_text = extract_text_from_image(image_file)
            if extracted_text is not None:
                st.text_area("Extracted Text:", extracted_text, height=300)  # Increased height
                preprocessed_text = preprocess_text(extracted_text)
                if st.button("Simplify and Summarize", key="pdf_btn"):
                    simplified_and_summarized_text = preprocess_simplify_paraphrase(preprocessed_text)
                    simplify_jargon_text=simplify_jargon(preprocessed_text)
                    if simplified_and_summarized_text:
                        st.write("Simplified and Summarized Text:")
                        bullet_points = format_as_bullet_points(simplified_and_summarized_text)
                        st.markdown(bullet_points, unsafe_allow_html=True)  # Render as HTML
                    else:
                        st.error("Error: Unable to simplify and summarize the text.")
    elif file_type == "PDF":
        st.write("Upload a PDF file:")
        pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])

        if pdf_file is not None:
            st.write("Extracted text from PDF:")
            extracted_text = extract_text_from_pdf(pdf_file)
            if extracted_text is not None:
                st.text_area("Extracted Text:", extracted_text, height=300)  # Increased height
                preprocessed_text = preprocess_text(extracted_text)
                if st.button("Simplify and Summarize", key="pdf_btn"):
                    simplified_and_summarized_text = preprocess_simplify_paraphrase(preprocessed_text)
                    simplify_jargon_text=simplify_jargon(preprocessed_text)
                    if simplified_and_summarized_text:
                        st.write("Simplified and Summarized Text:")
                        bullet_points = format_as_bullet_points(simplified_and_summarized_text)
                        st.markdown(bullet_points, unsafe_allow_html=True)  # Render as HTML
                    else:
                        st.error("Error: Unable to simplify and summarize the text.")

def format_as_bullet_points(text):
    # Capitalize first letter of each sentence
    formatted_text = re.sub(r"(^|\. *)(\w)", lambda m: m.group(0).capitalize(), text)

    # Split text into sentences and format as bullet points
    sentences = formatted_text.split(". ")
    bullet_points = "<ul>" + "".join([f"<li>{sentence}</li>" for sentence in sentences]) + "</ul>"

    return bullet_points

if __name__ == "__main__":
    main()
