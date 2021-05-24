# fraud_website_detection
This repository contain classifier model of machine learning which are trained to whether a site is phishing or not.</br>
I have extracted features from url in following ways:</br>
<b>Address-based features</b> (total no -7)</br>
<b>Domain-based features</b> (total  no -4)</br>
<b>Javascript based features</b>(total no-4)</br>
Address Based features are: 'Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', </br>
                           'https_Domain', 'TinyURL', 'Prefix/Suffix'</br>
Domain based features are:  'DNS_Record', 'Web_Traffic', 'Domain_Age', 'Domain_End'</br>
javascript based features are:'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards'</br>
Note: during training I have extracted "Domain name" as feature but this does not have  signifcance in traing  model so I have drop this feature later.</br>
Hence, in total there are about 16 features which I have used to train my model.</br>
I have selected these features by the  refernce of UCI Archive dataset.
I got the dataset for training from https://www.unb.ca/cic/datasets/url-2016.html</br>
for this project I have selected in total 10,000 data samples in which 5,000 are benign and 5,000 are phising </br>
I have created  three model on this dataset namely decision tree,random forest and support vector</br>
from which I found that random forest gives best performance among them.</br>
Modules used are:</br>
pandas</br>
numpy</br>
sklearn</br>
urllib.request</br>
bs4</br>
whois</br>
request</br>
