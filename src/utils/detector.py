import cv2
import numpy as np
import logging

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        logging.error(f"Resim dosyası okunamadı: {image_path}")
        raise FileNotFoundError(f"Resim dosyası okunamadı: {image_path}")
    return image

def create_masks(hsi_image, hue_range, saturation_range, intensity_range):
    hue, saturation, intensity = cv2.split(hsi_image)

    hue_mask = cv2.inRange(hue, hue_range[0], hue_range[1])
    saturation_mask = cv2.inRange(saturation, saturation_range[0], saturation_range[1])
    intensity_mask = cv2.inRange(intensity, intensity_range[0], intensity_range[1])

    flame_mask = cv2.bitwise_and(hue_mask, saturation_mask)
    flame_mask = cv2.bitwise_and(flame_mask, intensity_mask)

    return flame_mask

def clean_mask(mask):
    kernel = np.ones((5, 5), np.uint8)
    cleaned_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_CLOSE, kernel)
    return cleaned_mask

def detect_flames(image, mask, min_contour_area):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    return image
