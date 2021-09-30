# SingleLayerPerceptron

Simple single-layer neural network, built to differenciate cats from humans.

----



Usage:

   (Optional) Use `downloader.py [amount]` to download and resize _amount_ images for each class.
  


  - `perceptron.py` , a small set of images and a trained model are included.
  - `perceptron.py [[-f] --model=EPxSAMP] [--img1=path1 --img=path2]`
  
with:
  - `[-f]`force/override training (when updating/changing images). Model must be specified.
  - `[--model=EPxSAMP]` : Specify a training model, EP: number of epochs, SAMP: number of samples.
  - The default used model is 25x39.
  - `[--img1=path1 --img=path2]` You can change the test images by providing a path to them (150x150 8-bit grayscale JPG.) 
  
    
