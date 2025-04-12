import os
import qrcode
import dependencies.clear_screen as clear_screen
import dependencies.pause as pause

def generate_qr_code(data, output_folder="qr_codes", file_name="qr_code.png"):
    clear_screen.clear_screen()
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to the specified folder
    file_path = os.path.join(output_folder, file_name)
    img.save(file_path)
    print(f"QR code saved to {file_path}")
    pause.pause()
    