import pyAesCrypt
import os

# Create function encryption
def encryption(file, password):
    
    # Create buffer
    budder_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        budder_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    os.remove(file)

# Create function all directory
def walking_by_dir(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):

            # True
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        # False
        else:
            walking_by_dir(dir, password)

password = input("Введите пароль для шифрования: >> ")
walking_by_dir("/home/egn13/Python/encryption/files", password)