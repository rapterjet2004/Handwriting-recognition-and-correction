# Handwriting detector and Corrector 
A python gui app, it uses a pretrained model to perform optical character recognition on handwritten words. 
Then, it attempts analyzes these words by searching through the entire english dictionary using binary search, and if not found feeds it through <a href="https://github.com/filyp/autocorrect">Autocorrect</a>, 
a open source tool for performing spelling checks using ML. Although it's not very accurate in it's current form.

<img width="653" alt="image" src="https://user-images.githubusercontent.com/69230048/178080816-64daa8d4-f33f-4b4a-bbba-ec614ed97afc.png">
