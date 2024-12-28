import cv2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from src.utils.loggin import setup_logging, load_config
from src.utils.detector import load_image, create_masks, clean_mask, detect_flames
from src.utils.visualizer import visualize_results

def main():
    setup_logging()
    
    try:
        config = load_config()
    except FileNotFoundError:
        return
    
    Tk().withdraw()  
    file_path = askopenfilename(title="Bir resim dosyası seçin", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if not file_path:
        print("Dosya seçilmedi, program sonlandırılıyor.")
        return

    try:
        image = load_image(file_path)
    except FileNotFoundError:
        return

    hsi_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    flame_mask = create_masks(hsi_image, config["hue_range"], config["saturation_range"], config["intensity_range"])

    cleaned_mask = clean_mask(flame_mask)

    result_image = detect_flames(image, cleaned_mask, config["min_contour_area"])

    visualize_results(result_image, cleaned_mask)

if __name__ == "__main__":
    main()
