def pdf_extract(file, i):
  print("extracting from file:", file)
  delete_ppms()
  images = pdf2image.convert_from_path(PATH + file, output_folder=PATH)
  j = 0
  for file in sorted (os.listdir(PATH)):
      if '.ppm' in file and 'image' not in file:
        os.rename(PATH + file, PATH + 'image' + str(i) + '-' + str(j) + '.ppm')
        j += 1
  j = 0
  f = open(PATH +'result{}.txt'.format(i), 'w')
  files = [f for f in os.listdir(PATH) if '.ppm' in f]

  for file in sorted(files, key=lambda x: int(x[x.index('-') + 1: x.index('.')])):
      temp = pytesseract.image_to_string(Image.open(PATH + file))
      f.write(temp)
  f.close()

  
  for i in range(len(pdf_files)):
  pdf_file = pdf_files[i]
  pdf_extract(pdf_file, i)
