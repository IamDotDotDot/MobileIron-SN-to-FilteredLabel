# MobileIron-SN-to-FilteredLabel
Takes text with serial numbers and syntax and removes the unwanted syntax and then formats the serial numbers for a new filtered label.

Input:
6VWG6KE8UEUDYPPRWCO4U3990IMIT850JOKZ =  "GG7C3183MF3M"  OR"common.SerialNumber" =  "GG7C316BMF3M"  OR"common.SerialNumber" =  "GG7C31VPMF3M"

Output:
("common.SerialNumber" =  "GG7C3183MF3M"  OR"common.SerialNumber" =  "GG7C316BMF3M"  OR"common.SerialNumber" =  "GG7C31VPMF3M"  OR"common.SerialNumber" =  "6VWG6KE8UEUD"  OR"common.SerialNumber" =  "YPPRWCO4U399"  OR"common.SerialNumber" =  "0IMIT850JOKZ") AND "common.retired" = false


Preview of using the script:

**Program Start**

This program will extract any iOS serial numbers from unwanted characters and format it for filtered labels.
For the most accurate results, do not insert Serial Numbers next to non-serial number
characters without a space or separating dilemeter.

Paste jumbled text here: ("common.SerialNumber" =  "GG7C2RQXMF3M"  OR"common.SerialNumber" =  "GG7C30DEMF3M"  OR"common.SerialNumber" =  "GG7C31PFMF3M"  OR"common.SerialNumber" =  "GG7C42DYMF3M"  OR"common.SerialNumber" =  "GG7ZX0L2MF3M"  OR"common.SerialNumber" =  "GG7C30MUMF3M"  OR"common.SerialNumber" =  "GG7C295JMF3M"  OR"common.SerialNumber" =  "GG7ZX2R3MF3M"  OR"common.SerialNumber" =  "GG7C30LTMF3M"  OR"common.SerialNumber" =  "GG7C3183MF3M"  OR"common.SerialNumber" =  "GG7C316BMF3M"  OR"common.SerialNumber" =  "GG7C31VPMF3M"  OR"common.SerialNumber" =  "GG7C315MMF3M"  OR"common.SerialN X1IZDSNZZFAD6ZPM980MSGRBJSU2VUBTOFFANMNFZPE7X1Q11QJEWRJSIPW3PJX06J4NC6LUA3GJP2OUZI6HL9FBPJWG7AY4LF68LHQRVL682P00RAUNLNJZHC5A44JZYDAPP4HVNPHI4E6PY3WDQIXQMSTZUV5TUYVXUO9K4BBCBEUD1ERLYEVSEFOJRRGP5ZJAANB3I8I74GU5PTQTEAP7   "GG7C20TGMF3M"  OR"common.SerialNumber" =  "GG7C32RLMF3M"  OR"common.SerialNum

------------------------RESULTS BELOW--------------------------------

("common.SerialNumber" =  "GG7C2RQXMF3M"  OR"common.SerialNumber" =  "GG7C30DEMF3M"  OR"common.SerialNumber" =  "GG7C31PFMF3M"  OR"common.SerialNumber" =  "GG7C42DYMF3M"  OR"common.SerialNumber" =  "GG7ZX0L2MF3M"  OR"common.SerialNumber" =  "GG7C30MUMF3M"  OR"common.SerialNumber" =  "GG7C295JMF3M"  OR"common.SerialNumber" =  "GG7ZX2R3MF3M"  OR"common.SerialNumber" =  "GG7C30LTMF3M"  OR"common.SerialNumber" =  "GG7C3183MF3M"  OR"common.SerialNumber" =  "GG7C316BMF3M"  OR"common.SerialNumber" =  "GG7C31VPMF3M"  OR"common.SerialNumber" =  "GG7C315MMF3M"  OR"common.SerialNumber" =  "GG7C20TGMF3M"  OR"common.SerialNumber" =  "GG7C32RLMF3M"  OR"common.SerialNumber" =  "X1IZDSNZZFAD"  OR"common.SerialNumber" =  "6ZPM980MSGRB"  OR"common.SerialNumber" =  "JSU2VUBTOFFA"  OR"common.SerialNumber" =  "NMNFZPE7X1Q1"  OR"common.SerialNumber" =  "1QJEWRJSIPW3"  OR"common.SerialNumber" =  "PJX06J4NC6LU"  OR"common.SerialNumber" =  "A3GJP2OUZI6H"  OR"common.SerialNumber" =  "L9FBPJWG7AY4"  OR"common.SerialNumber" =  "LF68LHQRVL68"  OR"common.SerialNumber" =  "2P00RAUNLNJZ"  OR"common.SerialNumber" =  "HC5A44JZYDAP"  OR"common.SerialNumber" =  "P4HVNPHI4E6P"  OR"common.SerialNumber" =  "Y3WDQIXQMSTZ"  OR"common.SerialNumber" =  "UV5TUYVXUO9K"  OR"common.SerialNumber" =  "4BBCBEUD1ERL"  OR"common.SerialNumber" =  "YEVSEFOJRRGP"  OR"common.SerialNumber" =  "5ZJAANB3I8I7"  OR"common.SerialNumber" =  "4GU5PTQTEAP7") AND "common.retired" = false

Hit "Enter" to close:

**Program End**
