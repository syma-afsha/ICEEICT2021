from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
# import math


def all_speakers():
    data = {
        "henning-schulzrinne": {
            "name": "Henning Schulzrinne",
            "image": "henning-schulzrinne.png",
            "position": "Professor, Columbia University, NY, USA",
            "address": "",
            "email": "",
            "bio": from_template("bio/henning.html"),
            "title": "The Internet of Things that Shouldn't be on the Internet",
            "description": "The Internet of Things promises to make homes, factories, cars and cities smarter, promising better information and better outcomes. We have made significant progress in making these devices cheaper and allow them to communicate in many more places than a few years ago. But the promise of the Internet of Things faces significant obstacles: Security, usability, programmability and impact. I will discuss challenges to making the Internet of Things more secure, why using IoT services and devices remains difficult, how to effectively control thousands of devices within a single campus, factory or hospital, and how to think about possible impacts on the public.",
        },
        "frede-blaabjerg": {
            "name": "Frede Blaabjerg",
            "image": "frede-blaabjerg.png",
            "position": "Professor, Aalborg University, Denmark",
            "address": "",
            "email": "",
            "bio": from_template("bio/frede.html"),
            "title": "Power Electronics Technology - Quo Vadis",
            "description": from_template("description/frede.html"),
        },
        "anind-k-dey": {
            "name": "Anind K. Dey",
            "image": "anind-k-dey.png",
            "position": "Professor, University of Washington, USA",
            "address": "",
            "email": "",
            "bio": "Anind K. Dey is a Professor and Dean of the Information School and Adjunct Professor in the Department of Human-Centered Design and Engineering. Anind is renowned for his early work in context-aware computing, an important theme in modern computing, where computational processes are aware of the context in which they operate and can adapt appropriately to that context. His research is at the intersection of human-computer interaction, machine learning, and ubiquitous computing. For the past few years, Anind has focused on passively collecting large amounts of data about how people interact with their phones and the objects around them, to use for producing detection and classification models for human behaviors of interest. He applies a human-centered and problem-based approach through a collaboration with an amazing collection of domain experts in areas of substance abuse (alcohol, marijuana, opioids), mental health, driving and transportation needs, smart spaces, sustainability, and education. Anind was inducted into the ACM SIGCHI Academy for his significant contributions to the field of human-computer interaction in 2015.",
            "title": "Using Everyday Routines for Understanding Health Behaviors",
            "description": """We live in a world where the promise of ubiquitous computing and the Internet of Things is coming true. We have smart devices that pervade our lives, and that are constantly collecting data about us and mostly discarded as irrelevant. I will demonstrate how researchers can extract relevance from this passively collected data and use it to "image" people's behaviors. I will describe approaches for extracting behavioral routines from smart devices, and then how these routines can help us better understand individual and group human behaviors, as well as anomalies. Using examples from healthcare, I will describe how we can leverage both the routines and anomalies to improve our understanding of health-related behaviors and support behavior change.""",
        },
        "murat-tekalp": {
            "name": "Ahmet Murat Tekalp",
            "image": "murat-tekalp.jpg",
            "position": "Professor, Koç University, Turkey",
            "address": "",
            "email": "",
            "bio": "A. Murat Tekalp received BS degrees in Electrical Engineering and Mathematics from Bogazici University in 1980 with high honors, and the M.S. and Ph.D. degrees in Electrical, Computer, and Systems Engineering from Rensselaer Polytechnic Institute (RPI) respectively. Since June 2001, he has been a Professor at Koc University, Istanbul, Turkey. He was the Dean of Engineering at Koç University between 2010-2013. His research interests are in the area of digital image and video processing, including video compression and streaming, motion-compensated filtering, super-resolution, video segmentation, object tracking, content-based video analysis and summarization, 3D video processing, deep learning for image and video processing, video streaming and real-time video communications services, and software-defined networking. Prof. Tekalp is a Fellow of IEEE and a member of Turkish Academy of Sciences and Academia Europaea.",
            "title": "Recent Advances in Learned Image and Video Compression",
            "description": "Conventional video compression methods employ a linear transform and block motion model, and the steps of motion estimation, mode and quantization parameter selection, and entropy coding are optimized individually due to the combinatorial nature of the end-to-end optimization problem. Learned video compression allows end-to-end rate-distortion (R-D) optimized training of nonlinear transform, motion compensation and entropy model simultaneously. I will first review recent advances in learned image compression. Then, I will discuss the state-of-the-art in learned video compression and present recent results on learned hierarchical bi-directional video compression that combines the benefits of hierarchical bi-directional motion compensation and~end-to-end rate-distortion optimization",
        },
        "kashem-muttaqi": {
            "name": "Kashem M. Muttaqi",
            "image": "kashem-muttaqi.jpg",
            "position": "Professor, University of Wollongong, Australia",
            "address": "",
            "email": "",
            "bio": "Dr. Kashem Muttaqi received his Bachelor of Science in Electrical and Electronic Engineering degree from Bangladesh University of Engineering and Technology (BUET), Bangladesh in 1993. He then received a Masters of Engineering in Science degree from the University of Malaya (UM), Malaysia in 1997, and received his Doctor of Philosophy degree from Multimedia University (MMU), Malaysia in 2001. Currently, he is the Director of the Australian Power and Energy Research Institute (APERI) and a Professor at the School of Electrical, Computer and Telecommunications Engineering at the University of Wollongong. He is also serving as the Discipline Leader for Electrical Engineering at the School of Electrical, Computer and Telecommunications Engineering (SECTE), University of wollongong. He served as the Postgraduate Coursework Degree Coordinator at the School of Electrical, Computer and Telecommunications Engineering, University of Wollongong from 2008 to 2010, and the Cluster Head for 09 Engineering, Faculty of Engineering and Information Sciences (EIS) at the University of Wollongong from 2019 to 2021. He was associated with the University of Tasmania, Australia as a Research Fellow/Lecturer/Senior Lecturer from 2002 to 2007, and with the Queensland University of Technology, Australia as a Research Fellow from 2000 to 2002. Previously, he worked for Multimedia University, Malaysia as a Lecturer from 1997 to 2000.",
            "title": "Energy Technologies for Future Grids",
            "description": "New and modern energy technologies will make a significant change in the operation of electricity systems in future power grids. The current power grids are undergoing an unprecedented transformation, changing the way we have been producing, delivering, and consuming energy over the past century. This new energy era includes renewable sources and energy storage, integrated to power grids through power converters and transformers. In the future, these resources will be interfaced through high frequency magnetic links and solid state transformers. Electric vehicles and energy efficient technologies are also rapidly emerging and interacting with the grids. As these connections are being evolved, it is causing the engineers to rethink the current paradigms of system analysis and planning with a focus on how they can achieve the most flexible, efficient, and reliable power grid for the future.",
        },
        "syoji-kobashi": {
            "name": "Syoji Kobashi",
            "image": "syoji-kobashi.png",
            "position": "Professor, University of Hyogo, Japan",
            "address": "",
            "email": "",
            "bio": "Syoji Kobashi received BE in 1995, ME in 1997, and Doctor of Engineering in 2000, all from Himeji institute of Technology. He was an assistant professor at Himeji Institute of Technology (2000-2004), an associate professor (2005-2016), currently a professor (2016-) and the manager of advanced medical engineering research center (2016-), University of Hyogo. And, he was a guest associate professor at Osaka University, WPI immunology frontier research center (2010-2016), and was a visiting scholar at University of Pennsylvania (2011- 2012). His research interests include computer-aided diagnosis in medical images and artificial intelligence. He received 16 international awards, including Lifetime Achievement Award (WAC, 2016), Franklin V. Taylor Memorial Award (IEEE-SMCS, 2009). He has been serving on Program Chair of WAC2021, Publication Chair SMC2018, of and many others. Moreover, he is an editor-at-large of Intelligent Automation & Soft Computing journal, an editor-in-chief of International Journal of Biomedical Soft Computing and Human Sciences, etc. He is the senior member of IEEE.",
            "title": "Medical image analysis with artificial intelligence",
            "description": "Computer-aided diagnosis (CAD) in medical image analysis (MIA) is one of the expected fields that artificial intelligence (AI), especially deep learning (DL), improves the performance. However, DL alone is not enough to analyze medical images. DL process is just one processing step in the overall CAD system. Rather, the main role of researcher is to develop methods to synthesize data that are processed by the DL models, and methods that derive satisfactory results from the inferred results of the DL model. In order to discuss how to develop AI-based-CAD systems, I will introduce some CAD applications using DL models. It will include fatigue fracture detection in 3-D computer tomography (CT) images, tooth recognition in dental panorama radiograph, finger joint detection in hand radiograph. Through the applications, I am going to summarize the strategy to develop AI-based-CAD systems.",

        },

        "marco-liserre": {
            "name": "Marco Liserre",
            "image": "marco.jpg",
            "position": "Professor, University of Kiel, Germany",
            "address": "",
            "email": "",
            "bio": from_template("bio/marco.html"),
            "title": "Unlocking the hidden capacity of the electrical grid through power  electronics",
            "description": "Studies have revealed that the actual electrical grid is less utilized than 25 years ago: there is a higher utilization for a shorter time. This “greater demand variability” has been mostly caused by new loads, like air conditioning, but also by changes in the industrialization landscape. The wider integration of renewable energies and new loads(like heat pumps and electric vehicle charging stations) is expected to worsen the situation resulting in further congestion or underutilization of the electrical network, while their control(e. g. Load Demand Response) could relive the problem. The use of direct current(Hybrid grid) and the coordination among more energy carriers(Multimodal grids) together with Smart Grid technologies, is attempting to give to the electrical grid more flexibility in controlling the power flow by exchanging it with the dc-infrastructure or with other energy layers. Power Electronics is a key technology in all these solutions and offer the possibility to unlock the hidden potential of the grid without the need of a massive reinforcement of the electrical infrastructure.",


        },

        "ranjan-gangopadhyay": {
            "name": "Ranjan Gangopadhyay",
            "image": "ranjan-gangopadhyay.jpg",
            "position": "Professor, The LNM Institute of Information Technology, India",
            "address": "",
            "email": "",
            "bio": from_template("bio/ranjan.html"),
            "title": "Multi-perspectives of New and Next Generation Radio",
            "description": from_template("description/ranjan.html"),
        },

        "sample": {
            "name": "",
            "image": "",
            "position": "",
            "address": "",
            "email": "",
            "bio": "",
            "title": "",
            "description": "",
        },
    }
    return data


def styles():
    css = {
        "styles": "styles/styles1.css",
    }
    return css


def conf_logo():
    return "finalised_logo2.png"


def from_template(x):
    val = get_template(str(x))
    val = val.render({"foo": "foo", "bar": "baz"})
    return val


def nav_items():

    val = {
        "ABOUT": {
            "ICEEICT": "/about-iceeict",
            # "MIST": "https://mist.ac.bd/",
            "MIST": "/about-mist",
            "Dept of EECE": "https://mist.ac.bd/department/eece",
            # "Keynote Speaker": "/speakers",
            # "Invited Speaker": "/speakers",
        },
        "COMMITTEE": {
            "International Advisory Committee": "/international-advisory-committee",
            # "Chief Patron": "/chief-patron",
            "Local Advisory Committee": "/local-advisory-committee",
            "Organizing Committee": "/organizing-committee",
            "Technical Program Committee": "/technical-program-committee",
            # "Publications Management": "/publications-mang",
            # "Website & ICT Support": "/web&ict-support",
            # "Admin Support": "/admin-support",
        },
        "PROGRAM": {
            "Program Schedule": "/program-summary",
            # "Program Timeline": "/program-timeline",
            # "General Technical Sessions": "/program-summary-gts",
            "Keynote Sessions": "/keynotespeaker",
            "Industrial and Academia Session": "/industrial_session",
            "Special Technical Sessions": "/program-summary-sts",
            "Tutorials": "/program-summary-tutorials",
            "IEEE BD Section Event": "/program-summary-ieee-bd",
        },
        "AUTHORS": {
            "Scope & Call For Paper": "/authors-call-for-paper",
            "Important Dates": "/authors-important-dates",
            "Initial Paper Submission": "/authors-ips",
            "Camera Ready Submission": "/authors-crs",
            "Certificate": "/authors-certificate",
        },
        "REGISTRATION": [],
        "AWARDS": [],
        "SPONSORS": [], }
    return val


def footer():
    return from_template("misc/footer.html")


def index(request):

    speaker = [
        {
            "name": "Henning Schulzrinne",
            "url": "henning-schulzrinne",
            "image": "henning-schulzrinne.png",
            "position": "Professor, Columbia University, NY, USA",
            "scholar": "https://tinyurl.com/erphwm9r",
            "home": "https://www.cs.columbia.edu/~hgs/",
        },
        {
            "name": "Frede Blaabjerg",
            "url": "frede-blaabjerg",
            "image": "frede-blaabjerg.png",
            "position": "Professor, Aalborg University, Denmark",
            "scholar": "https://tinyurl.com/4kdzt2fw",
            "home": "https://vbn.aau.dk/en/persons/101000",
        },
        {
            "name": "Anind K. Dey",
            "url": "anind-k-dey",
            "image": "anind-k-dey.png",
            "position": "Professor, University of Washington, USA",
            "scholar": "https://tinyurl.com/h4v6y8xp",
            "home": "https://ischool.uw.edu/people/faculty/profile/anind",
        },
        {
            "name": "Ahmet Murat Tekalp",
            "url": "murat-tekalp",
            "image": "murat-tekalp.jpg",
            "position": "Professor, Koç University, Turkey",
            "scholar": "https://scholar.google.com.tr/citations?user=GzwcDjUAAAAJ&hl=en",
            "home": "http://home.ku.edu.tr/~mtekalp/index.htm",
        },

        {
            "name": "Marco Liserre",
            "url": "marco-liserre",
            "image": "marco.jpg",
            "position": "Professor, University of Kiel, Germany",
            "scholar": "https://scholar.google.it/citations?user=v-SeUGkAAAAJ&hl=it",
            "home": "https://www.pe.tf.uni-kiel.de/en/staff/professors/prof.-dr.-ing.-marco-liserre",
        },

        {
            "name": "Kashem M. Muttaqi",
            "url": "kashem-muttaqi",
            "image": "kashem-muttaqi.jpg",
            "position": "Professor, University of Wollongong, Australia",
            "scholar": "https://scholar.google.com/citations?user=00oG-SgAAAAJ&hl=en&oi=ao",
            "home": "https://scholars.uow.edu.au/display/kashem_muttaqi",
        },
        {
            "name": "Syoji Kobashi",
            "url": "syoji-kobashi",
            "image": "syoji-kobashi.png",
            "position": "Professor, University of Hyogo, Japan",
            "scholar": "https://tinyurl.com/yp3p2hzj",
            "home": "https://sites.google.com/site/syojikobashi/",
        },
        {
            "name": "Ranjan Gangopadhyay",
            "url": "ranjan-gangopadhyay",
            "image": "ranjan-gangopadhyay.jpg",
            "position": "Professor, LNM Institute of Information Technology",
            "scholar": "https://scholar.google.co.in/citations?user=rIbPZvQAAAAJ&hl=en",
            "home": "https://www.lnmiit.ac.in/Employee_ProfileNew.aspx?nDeptID=oo",
        },

    ]

    # total_speakers = len(speaker)

    messages = {


        "Camera ready submission deadline is extended": "/authors-crs",
        "Program Schedule is now available": "/program-summary",
        "Camera ready submission guideline is updated": "/authors-crs",
        # "Acceptance notifications deadline is rescheduled to 5 October 2021": "/authors-important-dates",
        "Submission System is closed now": "/authors-important-dates",
        "Special session and special issue journals/book chapters": "/program-summary-sts",
        # "Registration fee has been reviewed and published": "/registration",
        # "Call for papers is now available": "/authors-call-for-paper"

    }

    context = {
        "nav_items": nav_items(),
        "footer": footer(),
        "messages": messages,
        "conf_logo": conf_logo(),
        "styles": styles(),
        "speaker": speaker,
        # "total_speakers": total_speakers,
    }
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def shotoborsho(request):
    context = {}
    return render(request, "shotoborsho.html", context)


def page(request, key):

    context = {
        "styles": styles(),
        "nav_items": nav_items(),
        "footer": footer(),
        "conf_logo": conf_logo(),
        "local_adv": sorted(
            [
                "Satya Prasad Majumder, EEE, BUET",
                "Mohammad Rezwan Khan, EEE, UIU",
                "Quazi Deen Mohd Khosru, EEE, BUET",
                "Anisul Haque, EEE, EWU",
                "M. Sohel Rahman, CSE, BUET",
                "Md. Liakot Ali, IICT, BUET",
                "Md. Saiful Islam, IICT, BUET",
                "Shahidul Islam Khan, EEE, BRACU",
                "M. M. Shahidul Hassan, EEE, EWU",
                "Enamul Basher, EEE, UAP",
                "Pran Kanai Saha, EEE, BUET",
                "Md. Kamrul Hasan, EEE, BUET",
                "Sharif Mohammad Mominuzzaman, EEE, BUET",
                "Md. Shah Alam, EEE, BUET",
                "Md. Shahid Ullah, EEE, DIU",
                "Md. Nurunnabi Mollah, EEE, KUET",
                "Md. Mostafizur Rahman, ECE, KUET",
                "Md. Sheikh Sadi, CSE, KUET",
                "Md. Rafiqul Islam, EEE, KUET",
                "Mohammad Shaifur Islam, EEE, KUET",
                "Kaushik Deb, CSE, CUET",
                "S M Abdur Razzak, EEE, RUET",
                "Subrata Kumar Aditya, EEE, DU",
                "Mohammad Shahidul Islam, SUST",
                "Mohammad Shahadat Hossain, CSE, CU",
                "A Z M Touhidul Islam, ICE, RU",
                "Mohammad Zahidur Rahman, CSE, BRACU",
                "M. Shamim Kaiser, IIT, JU",
                "Shamim Al Mamun, IIT, JU",
                "A K M Baki, EEE, AUST",
                "Shahriar Khan, EEE, IUB",
                "Mohammad Rakibul Islam, EEE, IUT",
                "Abdur Rahman, EEE, AIUB",
                "Munshi Mahbubur Rahman, EEE, PrimeU",
                "Kazi Abu Taher, ICT, BUP",
            ]
        ),
    }
    valid = [
        # "international-advisory-committee",
        # "local-advisory-committee",
        "speakers",
        # "authors-crs",
        "chief-patron",
        # "admin-support",
        #     "organizing-committee",
        #     "technical-program-committee",
    ]
    invalid = [
        "footer",
        "admin-support",
        "web&ict-support",
        "publications-mang",
        # "about-mist",
    ]
    if key in valid:
        return render(request, "under_construction.html", context)
    elif key in invalid:
        return render(request, "does_not_exist.html", context)
    else:
        try:
            print(str(key) + ".html")
            return render(request, str(key) + ".html", context)
        except:
            return render(request, "does_not_exist.html", context)
