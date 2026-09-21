import streamlit as st

# पेज कॉन्फ़िगरेशन - ABIC रेणुकूट
st.set_page_config(
    page_title="कौशल शिक्षा पोर्टल - ABIC रेणुकूट",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------------------
# पाठ्यक्रम डेटा: कक्षा-वार, विषय-वार और 5-5 हिंदी वीडियो मॉड्यूल्स
# -------------------------------------------------------------
PATHYAKRAM_DATA = {
    "कक्षा 6 से 8 (मिडिल स्तर)": {
        "आर्टिफिशियल इंटेलिजेंस (AI)": [
            {
                "title": "मॉड्यूल 1: AI क्या है और स्मार्ट मशीनें कैसे काम करती हैं?",
                "url": "https://www.youtube.com/watch?v=62XAt60Lv-4",
                "task": "दैनिक जीवन में उपयोग होने वाले किन्हीं 3 AI टूल्स या स्मार्ट डिवाइसेस के नाम और उनके कार्य लिखें।"
            },
            {
                "title": "मॉड्यूल 2: मानव बुद्धिमत्ता बनाम कृत्रिम बुद्धिमत्ता (Human vs AI)",
                "url": "https://www.youtube.com/watch?v=3x3Cdty1nxk",
                "task": "मनुष्य के सोचने की प्रक्रिया और कंप्यूटर के निर्णय लेने के नियमों की तुलना तालिका बनाएं।"
            },
            {
                "title": "मॉड्यूल 3: कंप्यूटर विज़न की मूल बातें (मशीन कैसे देखती है)",
                "url": "https://www.youtube.com/watch?v=OcycT1JwsYo",
                "task": "Google Teachable Machine या Quick Draw का उपयोग करके इमेज पहचान का परीक्षण करें।"
            },
            {
                "title": "मॉड्यूल 4: नेचुरल लैंग्वेज प्रोसेसिंग (AI से बातचीत)",
                "url": "https://www.youtube.com/watch?v=fOvTtapxa9c",
                "task": "एक साधारण चैटबॉट के लिए 'नमस्ते' और 'समय क्या हुआ है?' के उत्तरों का नियम-चार्ट बनाएं।"
            },
            {
                "title": "मॉड्यूल 5: AI नैतिकता और डिजिटल जिम्मेदारी",
                "url": "https://www.youtube.com/watch?v=GboOXRhFzWA",
                "task": "केस स्टडी: स्कूल में बायोमेट्रिक या फेस रिकग्निशन से उपस्थिति लगाने के फायदे और सावधानियां लिखें।"
            }
        ],
        "मार्केटिंग (Marketing)": [
            {
                "title": "मॉड्यूल 1: वस्तु और सेवा (Goods & Services) का परिचय",
                "url": "https://www.youtube.com/watch?v=q6P30mODNyo",
                "task": "रेणुकूट बाजार से 5 वस्तुओं (Goods) और 5 सेवाओं (Services) की सूची तैयार करें।"
            },
            {
                "title": "मॉड्यूल 2: मार्केटिंग के 4 'P' (Product, Price, Place, Promotion)",
                "url": "https://www.youtube.com/watch?v=Mco8vBAwOmA",
                "task": "पर्यावरण-अनुकूल स्कूल बैग के लिए 4P मॉडल (उत्पाद, मूल्य, स्थान, प्रचार) तैयार करें।"
            },
            {
                "title": "मॉड्यूल 3: ग्राहक की पहचान और आवश्यकता को समझना",
                "url": "https://www.youtube.com/watch?v=x7E26gY3Oac",
                "task": "अपने सहपाठियों से स्कूल कैंटीन के बारे में 3 प्रश्नों का एक छोटा सर्वे करें।"
            },
            {
                "title": "मॉड्यूल 4: रचनात्मक विज्ञापन और पोस्टर डिजाइन करना",
                "url": "https://www.youtube.com/watch?v=0kEeVb1_XjA",
                "task": "हस्तनिर्मित पेन या स्टेशनरी के लिए एक आकर्षक नारा (स्लोगन) और पोस्टर बनाएं।"
            },
            {
                "title": "मॉड्यूल 5: डिजिटल बिक्री और सुरक्षित ऑनलाइन लेनदेन",
                "url": "https://www.youtube.com/watch?v=y2X7CeD-2L4",
                "task": "ऑनलाइन खरीदारी करते समय ध्यान रखने योग्य 5 सुरक्षा नियम लिखें।"
            }
        ],
        "कोडिंग (Coding)": [
            {
                "title": "मॉड्यूल 1: एल्गोरिदम और फ्लोचार्ट की समझ",
                "url": "https://www.youtube.com/watch?v=eSYeHlwDCNA",
                "task": "स्कूल यूनिफॉर्म पहनने या पेंसिल छीलने की प्रक्रिया का स्टेप-बाय-स्टेप फ्लोचार्ट बनाएं।"
            },
            {
                "title": "मॉड्यूल 2: ब्लॉक-आधारित कोडिंग (स्क्रैच बेसिक्स)",
                "url": "https://www.youtube.com/watch?v=Z1KKzN_fG0U",
                "task": "स्क्रैच में एक कैरेक्टर (स्प्राइट) को आगे-पीछे घुमाने के ब्लॉक्स जोड़ें।"
            },
            {
                "title": "मॉड्यूल 3: लूप्स (Loops) और पुनरावृत्ति की शक्ति",
                "url": "https://www.youtube.com/watch?v=QvyTEx1JOUQ",
                "task": "1 से 10 तक सम संख्याएं (Even Numbers) प्रिंट करने का लॉजिक लिखें।"
            },
            {
                "title": "मॉड्यूल 4: कंडीशनल स्टेटमेंट (If-Else लॉजिक)",
                "url": "https://www.youtube.com/watch?v=1oEQqHj3Y-s",
                "task": "शर्त बनाएं: 'यदि छात्र के अंक 33 से अधिक हैं तो उत्तीर्ण, अन्यथा पुनः प्रयास करें'।"
            },
            {
                "title": "मॉड्यूल 5: मिनी प्रोजेक्ट: साधारण गेम बनाना",
                "url": "https://www.youtube.com/watch?v=hK8N2bT-3qM",
                "task": "एक गिरती हुई गेंद को पकड़ने और स्कोर बढ़ाने वाला साधारण गेम डिजाइन करें।"
            }
        ]
    },
    "कक्षा 9 एवं 10 (माध्यमिक स्तर)": {
        "सूचना प्रौद्योगिकी (IT - कोड 402)": [
            {
                "title": "मॉड्यूल 1: संचार कौशल (मौखिक और गैर-मौखिक संचार)",
                "url": "https://www.youtube.com/watch?v=0xdiYdRqY1g",
                "task": "कक्षा शिक्षक को बीमारी के अवकाश हेतु एक औपचारिक ईमेल का प्रारूप तैयार करें।"
            },
            {
                "title": "मॉड्यूल 2: आईसीटी कौशल और फाइल प्रबंधन",
                "url": "https://www.youtube.com/watch?v=AsbmcPrC1Fs",
                "task": "कंप्यूटर में विभिन्न विषयों (Physics, Chemistry, IT) के लिए अलग-अलग फोल्डर बनाएं और फाइलों को व्यवस्थित करें।"
            },
            {
                "title": "मॉड्यूल 3: डिजिटल दस्तावेज़ीकरण (Word Processing)",
                "url": "https://www.youtube.com/watch?v=4q48bWJ6GgU",
                "task": "हेडर, फुटर और विषय-सूची (Table of Contents) का उपयोग करके 2 पेज की एक रिपोर्ट बनाएं।"
            },
            {
                "title": "मॉड्यूल 4: इलेक्ट्रॉनिक स्प्रेडशीट (Excel / Calc फॉर्मूले)",
                "url": "https://www.youtube.com/watch?v=8VnZ6U-yWqI",
                "task": "स्प्रेडशीट में 5 विद्यार्थियों के कुल प्राप्तांक और औसत निकालने के लिए SUM और AVERAGE फॉर्मूला लगाएं।"
            },
            {
                "title": "मॉड्यूल 5: डिजिटल प्रेजेंटेशन और स्लाइड डिजाइन",
                "url": "https://www.youtube.com/watch?v=1hNlZtW5zEQ",
                "task": "'साइबर सुरक्षा' विषय पर 5 स्लाइड्स की प्रेजेंटेशन तैयार करें जिसमें ट्रांजिशन और एनिमेशन लगा हो।"
            }
        ],
        "खाद्य उत्पादन (Food Production - कोड 409)": [
            {
                "title": "मॉड्यूल 1: रसोई स्वच्छता और खाद्य सुरक्षा मानक",
                "url": "https://www.youtube.com/watch?v=aG_jZ2wYm_Q",
                "task": "रसोई में काम करते समय व्यक्तिगत स्वच्छता और बर्तनों के रख-रखाव के 5 नियम लिखें।"
            },
            {
                "title": "मॉड्यूल 2: रसोई उपकरण और चाकू के प्रकार",
                "url": "https://www.youtube.com/watch?v=cM3uYfQ3PjA",
                "task": "किचन के 8 प्रमुख उपकरणों के नाम और उनके सुरक्षित उपयोग का विवरण लिखें।"
            },
            {
                "title": "मॉड्यूल 3: पकाने की मुख्य विधियां (उबालना, भूनना, भाप से पकाना)",
                "url": "https://www.youtube.com/watch?v=8gXGv9yXyM8",
                "task": "भाप में पकाने (Steaming) और तलने (Frying) में पौष्टिक तत्वों के अंतर की तुलना करें।"
            },
            {
                "title": "मॉड्यूल 4: सब्जियों की कटाई के तरीके (Julienne, Dicing आदि)",
                "url": "https://www.youtube.com/watch?v=Ydc_SaQ_eCE",
                "task": "आलू या गाजर को जूलियन (लंबे टुकड़े) और डाइसिंग (छोटे चौकोर टुकड़े) में काटकर फोटो संलग्न करें।"
            },
            {
                "title": "मॉड्यूल 5: संतुलित आहार और मेनू प्लानिंग",
                "url": "https://www.youtube.com/watch?v=5rLzW8yVvB8",
                "task": "विद्यालय के विद्यार्थियों के दोपहर के भोजन के लिए 3-कोर्स का संतुलित मेनू चार्ट बनाएं।"
            }
        ],
        "आर्टिफिशियल इंटेलिजेंस (AI - कोड 417)": [
            {
                "title": "मॉड्यूल 1: AI प्रोजेक्ट साइकिल (समस्या पहचान और डेटा संग्रह)",
                "url": "https://www.youtube.com/watch?v=62XAt60Lv-4",
                "task": "अपने विद्यालय में कचरा प्रबंधन समस्या के लिए 4Ws कैनवास (Who, What, Where, Why) भरें।"
            },
            {
                "title": "मॉड्यूल 2: डेटा एक्सप्लोरेशन और विज़ुअलाइज़ेशन",
                "url": "https://www.youtube.com/watch?v=jW94Fv_gX88",
                "task": "कक्षा के विद्यार्थियों की लंबाई और वजन के डेटा का एक साधारण बार ग्राफ बनाएं।"
            },
            {
                "title": "मॉड्यूल 3: AI के लिए पाइथन प्रोग्रामिंग बेसिक्स",
                "url": "https://www.youtube.com/watch?v=rfscVS0vtbw",
                "task": "पाइथन में लिस्ट (List) और लूप (For Loop) का उपयोग करके संख्याओं का योग निकालें।"
            },
            {
                "title": "मॉड्यूल 4: कंप्यूटर विज़न और पिक्सेल की समझ",
                "url": "https://www.youtube.com/watch?v=2-Ol7ZB0GmU",
                "task": "पाइथन (OpenCV/PIL) से एक इमेज लोड करें और उसके पिक्सेल व आकार (Dimensions) प्रिंट करें।"
            },
            {
                "title": "मॉड्यूल 5: AI मॉडल मूल्यांकन (कंफ्यूजन मैट्रिक्स)",
                "url": "https://www.youtube.com/watch?v=Kdsp6soqA7g",
                "task": "दिए गए 2x2 कंफ्यूजन मैट्रिक्स से एक्यूरेसी (Accuracy) और प्रिसिजन (Precision) की गणना करें।"
            }
        ]
    },
    "कक्षा 11 एवं 12 (उच्चतर माध्यमिक स्तर)": {
        "सूचना प्रौद्योगिकी (IT - कोड 802)": [
            {
                "title": "मॉड्यूल 1: कंप्यूटर आर्किटेक्चर और ऑपरेटिंग सिस्टम",
                "url": "https://www.youtube.com/watch?v=vBURTt97EkA",
                "task": "कमांड प्रॉम्प्ट (CLI) का उपयोग करके सिस्टम की डायरेक्टरी और आईपी एड्रेस चेक करें।"
            },
            {
                "title": "मॉड्यूल 2: रिलेशनल डेटाबेस और SQL कमांड्स",
                "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                "task": "विद्यार्थियों के रिकॉर्ड के लिए SQL क्वेरी: CREATE TABLE और INSERT INTO लिखें।"
            },
            {
                "title": "मॉड्यूल 3: ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग (Java / Python)",
                "url": "https://www.youtube.com/watch?v=grEKMHGYyns",
                "task": "'Student' नाम की क्लास बनाएं जिसमें रोल नंबर, नाम और अंक के मेथड्स शामिल हों।"
            },
            {
                "title": "मॉड्यूल 4: वेब एप्लिकेशन और फॉर्म वेलिडेशन",
                "url": "https://www.youtube.com/watch?v=2JYT5f2S74k",
                "task": "HTML और JavaScript का उपयोग करके एक प्रवेश फॉर्म (Registration Form) तैयार करें।"
            },
            {
                "title": "मॉड्यूल 5: नेटवर्क प्रोटोकॉल और साइबर सुरक्षा उपाय",
                "url": "https://www.youtube.com/watch?v=1V_4-45wZvg",
                "task": "नेटवर्क में TCP/IP और HTTP/HTTPS के कार्य करने के तरीके का आरेख बनाएं।"
            }
        ],
        "वित्तीय बाजार प्रबंधन (Financial Markets - कोड 805)": [
            {
                "title": "मॉड्यूल 1: भारतीय वित्तीय प्रणाली, RBI और SEBI का परिचय",
                "url": "https://www.youtube.com/watch?v=4A83jfGuiAQ",
                "task": "SEBI और RBI की मुख्य भूमिकाओं और कार्यप्रणाली का तुलनात्मक विवरण लिखें।"
            },
            {
                "title": "मॉड्यूल 2: प्राथमिक बाजार (IPO) और द्वितीयक बाजार (Stock Exchange)",
                "url": "https://www.youtube.com/watch?v=BfgEm17KEKM",
                "task": "किसी कंपनी के IPO जारी करने से लेकर शेयर बाजार में लिस्टिंग तक की प्रक्रिया लिखें।"
            },
            {
                "title": "मॉड्यूल 3: डीमैट खाता और शेयर ट्रेडिंग की प्रक्रिया",
                "url": "https://www.youtube.com/watch?v=QTV1_kRQm3s",
                "task": "मार्केट ऑर्डर और लिमिट ऑर्डर में क्या अंतर है? उदाहरण सहित समझाएं।"
            },
            {
                "title": "मॉड्यूल 4: म्यूचुअल फंड और एसआईपी (SIP) की कार्यप्रणाली",
                "url": "https://www.youtube.com/watch?v=5rCbg6kS0jA",
                "task": "₹1500 प्रति माह के 5 वर्षीय SIP निवेश पर चक्रवृद्धि ब्याज की गणना का चार्ट बनाएं।"
            },
            {
                "title": "मॉड्यूल 5: वित्तीय जोखिम प्रबंधन और डेरिवेटिव्स बेसिक्स",
                "url": "https://www.youtube.com/watch?v=7uV89w0_xKw",
                "task": "फ्यूचर्स और ऑप्शंस (Call/Put) के मूल सिद्धांतों को संक्षेप में स्पष्ट करें।"
            }
        ],
        "योग (Yoga - कोड 841)": [
            {
                "title": "मॉड्यूल 1: यौगिक विज्ञान का इतिहास और अष्टांग योग",
                "url": "https://www.youtube.com/watch?v=v7AYKMP6rOE",
                "task": "महर्षि पतंजलि के अष्टांग योग के 8 अंगों (यम, नियम, आसन आदि) का चार्ट बनाएं।"
            },
            {
                "title": "मॉड्यूल 2: षट्कर्म और शरीर शुद्धि की विधियां",
                "url": "https://www.youtube.com/watch?v=m756Gz8kI9Y",
                "task": "कपालभाति और जलनेति के अभ्यास की सावधानियां और शारीरिक लाभ लिखें।"
            },
            {
                "title": "मॉड्यूल 3: प्रमुख योगासन और शारीरिक संरेखण (सूर्य नमस्कार)",
                "url": "https://www.youtube.com/watch?v=sTANio_2E0Q",
                "task": "सूर्य नमस्कार के 12 चरणों के नाम और उनसे संबंधित श्वसन प्रक्रिया का विवरण लिखें।"
            },
            {
                "title": "मॉड्यूल 4: प्राणायाम और श्वास नियंत्रण तकनीक",
                "url": "https://www.youtube.com/watch?v=1xRX1MuoqSc",
                "task": "अनुलोम-विलोम और भ्रामरी प्राणायाम का 5 मिनट अभ्यास कर एकाग्रता पर प्रभाव दर्ज करें।"
            },
            {
                "title": "मॉड्यूल 5: मिताहार (योगिक आहार) और मानसिक तनाव प्रबंधन",
                "url": "https://www.youtube.com/watch?v=txkZzT2n6m4",
                "task": "विद्यार्थियों के मानसिक संतुलन और स्मरण शक्ति हेतु एक सात्विक भोजन तालिका बनाएं।"
            }
        ],
        "आर्टिफिशियल इंटेलिजेंस (AI - कोड 843)": [
            {
                "title": "मॉड्यूल 1: मशीन लर्निंग तकनीक और लीनियर रिग्रेशन",
                "url": "https://www.youtube.com/watch?v=3x3Cdty1nxk",
                "task": "पाइथन Scikit-Learn लाइब्रेरी से डेटा पर साधारण रिग्रेशन मॉडल का कोड लिखें।"
            },
            {
                "title": "मॉड्यूल 2: डेटा प्री-प्रोसेसिंग और मिसिंग वैल्यूज संभालना",
                "url": "https://www.youtube.com/watch?v=bDhvCp3_lYw",
                "task": "Pandas का उपयोग करके CSV फाइल में खाली (Null) डेटा को एवरेज से बदलें।"
            },
            {
                "title": "मॉड्यूल 3: क्लासिफिकेशन मॉडल (Decision Tree व KNN)",
                "url": "https://www.youtube.com/watch?v=Rmajwe65u70",
                "task": "आयरिस (Iris) डेटासेट पर डिसिजन ट्री ट्रेन करें और आउटपुट की सटीकता जांचें।"
            },
            {
                "title": "मॉड्यूल 4: न्यूरल नेटवर्क और डीप लर्निंग की नींव",
                "url": "https://www.youtube.com/watch?v=aircAruvnKk",
                "task": "परसेप्ट्रॉन मॉडल का आरेख बनाएं जिसमें इनपुट, वेट्स और एक्टिवेशन फंक्शन दर्शाएं।"
            },
            {
                "title": "मॉड्यूल 5: AI मॉडल को वेब पोर्टल से जोड़ना (डिप्लॉयमेंट)",
                "url": "https://www.youtube.com/watch?v=62XAt60Lv-4",
                "task": "अपने बनाए मॉडल को Streamlit वेब इंटरफेस के साथ जोड़कर टेस्ट रन करें।"
            }
        ]
    }
}

# -------------------------------------------------------------
# साइडबार: विद्यालय शीर्षक एवं चयन
# -------------------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/Aditya_Birla_Group_Logo.svg", width=160)
st.sidebar.title("ABIC रेणुकूट")
st.sidebar.markdown("**आदित्य बिड़ला इंटर कॉलेज, रेणुकूट**")
st.sidebar.markdown("*कौशल विकास एवं डिजिटल प्रशिक्षण केंद्र*")
st.sidebar.markdown("---")

# 1. कक्षा समूह का चयन
chuni_gayee_kaksha = st.sidebar.selectbox(
    "1. अपनी कक्षा श्रेणी चुनें:",
    list(PATHYAKRAM_DATA.keys())
)

# 2. विषय का चयन
vishey_soochi = list(PATHYAKRAM_DATA[chuni_gayee_kaksha].keys())
chuna_gaya_vishey = st.sidebar.selectbox(
    "2. कौशल विषय (Skill Subject) चुनें:",
    vishey_soochi
)

# 3. मॉड्यूल (5 में से 1) का चयन
module_list = PATHYAKRAM_DATA[chuni_gayee_kaksha][chuna_gaya_vishey]
module_titles = [m["title"] for m in module_list]
chuna_gaya_module_title = st.sidebar.radio(
    "3. अध्याय / वीडियो मॉड्यूल चुनें:",
    module_titles
)

# चयनित मॉड्यूल का विवरण प्राप्त करना
vartaman_module = next(m for m in module_list if m["title"] == chuna_gaya_module_title)

# -------------------------------------------------------------
# मुख्य स्क्रीन सामग्री
# -------------------------------------------------------------
st.title("🏫 आदित्य बिड़ला इंटर कॉलेज (ABIC), रेणुकूट")
st.subheader(f"📖 {chuna_gaya_vishey}")
st.caption(f"स्तर: {chuni_gayee_kaksha} | केंद्रीय माध्यमिक शिक्षा बोर्ड (CBSE) कौशल पाठ्यक्रम")
st.markdown("---")

col_video, col_task = st.columns([3, 2])

with col_video:
    st.markdown(f"### 🎥 {vartaman_module['title']}")
    # हिंदी व्याख्यान वीडियो
    st.video(vartaman_module["url"])
    st.info("💡 **सुझाव:** वीडियो को पूरा ध्यान से देखें और उसमें बताए गए मुख्य बिंदुओं को अपनी अभ्यास पुस्तिका में नोट करें।")

with col_task:
    st.markdown("### 🧪 प्रायोगिक कार्य (Practical Lab Task)")
    st.warning(vartaman_module["task"])
    
    st.markdown("#### ✍️ छात्र उत्तर एवं प्रोजेक्ट सबमिशन")
    uttar_text = st.text_area(
        "विद्यार्थी अपना प्रायोगिक उत्तर, कोड या निष्कर्ष यहाँ टाइप करें:",
        height=140,
        placeholder="यहाँ अपना उत्तर लिखें..."
    )
    
    file_upload = st.file_uploader(
        "प्रैक्टिकल स्क्रीनशॉट या प्रोजेक्ट फाइल अपलोड करें (PNG/JPG/PDF/PY):",
        type=["png", "jpg", "pdf", "py", "ipynb"]
    )
    
    if st.button("📤 प्रायोगिक कार्य सबमिट करें"):
        if uttar_text.strip() or file_upload is not None:
            st.success("✅ आपका कार्य सफलतापूर्वक सबमिट हो गया है! शिक्षक द्वारा शीघ्र ही इसका मूल्यांकन किया जाएगा।")
        else:
            st.error("⚠️ कृपया सबमिट करने से पहले टेक्स्ट बॉक्स में कुछ लिखें या फाइल अपलोड करें।")

# -------------------------------------------------------------
# पाठ्यक्रम प्रगति ट्रैकर (Progress Bar)
# -------------------------------------------------------------
st.markdown("---")
vartaman_kram = module_titles.index(chuna_gaya_module_title) + 1
pragati_pratishat = vartaman_kram / len(module_titles)

st.write(f"**पाठ्यक्रम प्रगति (Progress):** 5 में से {vartaman_kram} मॉड्यूल पूर्ण ({int(pragati_pratishat * 100)}%)")
st.progress(pragati_pratishat)
