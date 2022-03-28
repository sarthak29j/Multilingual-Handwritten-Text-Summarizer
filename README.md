# Multilingual-Handwritten-Text-Summarizer
There is a problem of searching for relevant documents from the number of documents available and absorbing relevant information from it. With ever growing media, who has the time to go through the entire book to decide how useful it is? It is particularly necessary for historical documents, archives, etc.

Recognition of images, including symbols, is one of the urgent tasks arising in various fields of human activity today. The free software products are mainly focused on the recognition of printed text, not handwritten. 
What if there is a way to reduce this data to a shorter, focused summary that captures the salient details so that we can quickly decide if the larger document contains the relevant information needed by us? 
For handwritten documents, manual summarization is not possible and automatic text summarization is the need of the hour.

#### Primary Azure Technology:
Computer Vision, Text Analytics, Translator.
#### Other Azure Technologies: 
Visual studio code, Azure portal, Static web app
#### Language Used:  
Python 3.10.2


## Description: 
The project takes a handwritten document image as an input. This is where Azure's Computer Vision service comes in play to extract text from the image. Optical character recognition (OCR) in Azure's Computer Vision service allows you to extract printed or handwritten text from images, such as photos of street signs and products, as well as from documents—invoices, bills, financial reports, articles, and more. Microsoft's OCR technologies support extracting printed text in several languages.

The extracted text is then summarized using Azure Cognitive Service for Language. Text summarization is one of the features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. There are two main approaches to summarize text documents: Extractive and Abstractive. This project uses extractive summarization. In extractive summarization we identify the important sentences or phrases from the original text and extract only those from the text. Those extracted sentences would be our summary. 

Finally, the summarized text is translated to other languages using another Cognitive service used in this project is Translator service. Translator is a cloud-based neural machine translation service that is part of the Azure Cognitive Services family of REST APIs. Test translation feature of translator executes text translation between supported source and target languages in real time.

