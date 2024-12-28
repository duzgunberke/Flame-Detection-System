import matplotlib.pyplot as plt
import cv2

def visualize_results(image, mask):
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Orijinal Görüntü")
    
    plt.subplot(1, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title("Tespit Edilen Alevler")
    
    plt.show()
