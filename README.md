# receptaPrzezSMS
send e-prescription to Seniors via SMS / rozsyłanie kodów e-recept przez SMS

prerequisites:
a working Python environment, eg. miniconda

create a new conda environment named 'workdesk':
`conda create -n workdesk Python=3`

activate the 'workdesk' environment:
`conda activate workdesk`

install 'twilio'
`pip install twilio`

sing up / or login with twilo and obtain your:
`account_sid`
`auth_token`
`your-trial-number`
replace placholders in the source code file (lines 87, 88 and 96)

save and run:
`python receptaPrzezSMS_0.0.2.py`

An executable file entitled 'receptaPrzezSMS_0.0.1.exe' is provided for demo purposes. It can be run under Microsoft Windows.

Try it out!

Download the file, dobule-click it and fill the data for:

Patient Name
Patient Surname
Telephone number (9 digits)
(this works only with Polish nubmers, but DO NOT prefix it with '+48')
Code for e-prescription (4 digits)
Click 'Wyślij SMS' button.

Compare: 01. wpisz dane pacjenta.png

A pop-up window should appear indicating SMS has been sent.

Compare: 02. wyślij wiadomość.png

Check out your tefephone.

Compare: 03. wiadomość odebrana.png

Click OK to dismiss the confirmation window.

You can now send another code to e-prescription to another patient.