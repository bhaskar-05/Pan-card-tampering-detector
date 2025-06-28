# app.py
import streamlit as st
from PIL import Image
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import tempfile

st.set_page_config(page_title="PAN Card Tampering Detector")

st.title("🕵️‍♂️ PAN Card Tampering Detector")

# Upload images
original_file = st.file_uploader("Upload Original PAN Card", type=["jpg", "png", "jpeg"])
tampered_file = st.file_uploader("Upload Suspected PAN Card", type=["jpg", "png", "jpeg"])

if original_file and tampered_file:
    original = Image.open(original_file).convert('RGB')
    tampered = Image.open(tampered_file).convert('RGB')

    # Resize for uniformity
    original = original.resize((600, 400))
    tampered = tampered.resize((600, 400))

    # Convert to grayscale
    gray_original = cv2.cvtColor(np.array(original), cv2.COLOR_RGB2GRAY)
    gray_tampered = cv2.cvtColor(np.array(tampered), cv2.COLOR_RGB2GRAY)

    # Compute SSIM
    score, diff = ssim(gray_original, gray_tampered, full=True)
    diff = (diff * 255).astype("uint8")

    st.subheader(f"🔍 SSIM Score: {score:.4f}")
    if score < 0.98:
        st.error("⚠️ Possible tampering detected!")
    else:
        st.success("✅ No significant differences found.")

    # Threshold + contours
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.array(tampered).copy()

    for c in contours:
        if cv2.contourArea(c) > 40:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 0), 2)

    st.image(mask, caption="Differences Highlighted", use_column_width=True)
