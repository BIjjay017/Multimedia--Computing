import cv2

def convert_to_grayscale("D:\OneDrive\तस्विरहरू\Bijay Photoes\AGZC5989.JPG", D:\OneDrive\तस्विरहरू):
#   """Converts a JPEG image to grayscale and saves it.

#   Args:
#     image_path: Path to the input JPEG image.
#     output_path: Path to save the grayscale image.
#   """
  img = cv2.imread("D:\OneDrive\तस्विरहरू\Bijay Photoes\AGZC5989.JPG)
  grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR to grayscale
  cv2.imwrite( D:\OneDrive\तस्विरहरू, grayscale_img)

# Example usage
image_path = "image.jpg"
output_path = "grayscale_image_cv-A.jpg"
convert_to_grayscale(D:\OneDrive\तस्विरहरू\Bijay Photoes\AGZC5989.JPG,  D:\OneDrive\तस्विरहरू)

