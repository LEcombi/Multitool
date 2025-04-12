import os
import os
import time
from barcode import Code128
from barcode.writer import ImageWriter
import dependencies.clear_screen as clear_screen
import dependencies.pause as pause

def generate_barcode(data, output_folder="barcodes", file_name="barcode.png"):
    clear_screen.clear_screen()

    os.system('cls' if os.name == 'nt' else 'clear')
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Generate the barcode
    barcode = Code128(data, writer=ImageWriter())
    
    # Save the barcode image to the specified folder
    file_path = os.path.join(output_folder, file_name)
    barcode.save(file_path)
    print(f"Barcode saved to {file_path}")
    input("Press Enter to continue...")
    pause.pause()