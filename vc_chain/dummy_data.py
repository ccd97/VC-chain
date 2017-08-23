

def getUserDummyData():
    return {
        "name": "Cyprien Dcunha",
        "username": "CCD",
        "email": "dcunha.cyprien@gmail.com",
        "projects": 6,
        "stars": 10,
        "forks": 3,
        "followers": 1,
    }


def getTimelineDummyData():
    return [
        {
            "type": "commit",
            "time": "5 minutes ago",
            "puser": "CCD",
            "suser": "",
            "pproject": "xyz",
            "sproject": "",
            "branch": "stagging",
        },
        {
            "type": "star",
            "time": "10 hours ago",
            "puser": "imtoobose",
            "suser": "CCD",
            "pproject": "",
            "sproject": "mnop",
            "branch": "",
        },
        {
            "type": "commit",
            "time": "1 day ago",
            "puser": "CCD",
            "suser": "",
            "pproject": "mnop",
            "sproject": "",
            "branch": "master",
        },
        {
            "type": "fork",
            "time": "2 day ago",
            "puser": "CCD",
            "suser": "imtoobose",
            "pproject": "mnop",
            "sproject": "pqrs",
            "branch": "",
        },
        {
            "type": "star",
            "time": "10 day ago",
            "puser": "CCD",
            "suser": "imtoobose",
            "pproject": "",
            "sproject": "pqrs",
            "branch": "",
        },
        {
            "type": "follow",
            "time": "11 day ago",
            "puser": "CCD",
            "suser": "imtoobose",
            "pproject": "",
            "sproject": "",
            "branch": "",
        },
    ]


def getCommitStatsDummyData():
    return [
        {"y": '10 Jul', "a": "5"},
        {"y": '11 Jul', "a": "1"},
        {"y": '12 Jul', "a": "0"},
        {"y": '13 Jul', "a": "2"},
        {"y": '14 Jul', "a": "2"},
        {"y": '15 Jul', "a": "0"},
        {"y": '16 Jul', "a": "0"},
        {"y": '17 Jul', "a": "5"},
        {"y": '18 Jul', "a": "0"},
        {"y": '19 Jul', "a": "7"},
        {"y": '20 Jul', "a": "1"},
    ]


def getProjectListDummyData():
    return [
        {
            "name": "hello_nn",
            "description": "Some of my simple neural networks",
            "last_update": "Apr 30",
            "stars": "8",
            "forks": "0",
        },
        {
            "name": "AttendanceManager",
            "last_update": "Apr 25",
            "stars": "0",
            "forks": "0",
        },
        {
            "name": "mnop",
            "last_update": "Jul 20",
            "forked_user": "imtoobose",
            "forked_project": "pqrs",
            "stars": "2",
            "forks": "1",
        },
        {
            "name": "image-classify-server",
            "description": "Image classification using Tensorflow (Inception v3)",
            "last_update": "Apr 19",
            "stars": "0",
            "forks": "2",
        },
        {
            "name": "xyz",
            "last_update": "Jul 21",
            "stars": "0",
            "forks": "0",
        },
    ]
