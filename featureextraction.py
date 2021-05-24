import AddressBasedFeatures as abf
import DomianBasedFeatures as dbf
import JsBasedFeatures as jbf
import requests
def featureExtraction(url):

  features = []
  #Address bar based features (10)
  domain_name=abf.getDomain(url)
  features.append(domain_name)
  features.append(abf.havingIP(url))
  features.append(abf.haveAtSign(url))
  features.append(abf.getLength(url))
  features.append(abf.getDepth(url))
  features.append(abf.redirection(url))
  features.append(abf.httpDomain(url))
  features.append(abf.tinyURL(url))
  features.append(abf.prefixSuffix(url))
  dns=dbf.ifdns(url)
  features.append(dns)
  features.append(dbf.web_traffic(url))
  features.append(1 if dns == 1 else dbf.domainAge(domain_name))
  features.append(1 if dns == 1 else dbf.domainEnd(domain_name))
  
  # HTML & Javascript based features
  try:
    response = requests.get(url)
  except:
    response = ""

  features.append(jbf.iframe(response))
  features.append(jbf.mouseOver(response))
  features.append(jbf.rightClick(response))
  features.append(jbf.forwarding(response))
  
  return features

#converting the list to dataframe
feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label']

# print(featureExtraction("https://galcoservices.com/e7a4a86c64c5dd082e999bbf890bbd8e/verify.php?country_x=-&ACCT_x=ID-PPL=PA324192.255.65.83=ScrPg=81a5203ae69723b88be3cd03cd2429066cd1fa7a7127d784d22a8f3ec6d54f09S=$1$iQJXaqXE$FHsmAio7e428hMLh7.51f0gnKVwcijFp8qYsu6M4EaTH27hvdSA1ZyQ3WfOkmRrL0oPBlC9JDItzxU5XeGbNnkj3HXGSUsJIOvzf6w8FAeKxRdbaC2Y9lMWpTmcgE5V1NDtB7hqQ4ZrPLyiou081166031421"))