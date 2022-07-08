# Handwriting detector and Corrector 
A Python GUI app, it uses a pretrained model to perform optical character recognition on handwritten words. 
Then, it attempts analyzes these words by searching through the entire English dictionary using binary search, and if not found, feeds it through <a href="https://github.com/filyp/autocorrect">Autocorrect</a>, 
a open source tool for performing spelling checks using ML. 

In theory at least, practically the model isn't very accurate in it's current form. At least 4 now. ¯\\_(ツ)_/¯

<img width="653" alt="image" src="https://user-images.githubusercontent.com/69230048/178080816-64daa8d4-f33f-4b4a-bbba-ec614ed97afc.png">
