import ascii_magic
output = ascii_magic.from_image_file("m.dzikri.jpg", columns=50,char="#")
ascii_magic.to_terminal(output)
