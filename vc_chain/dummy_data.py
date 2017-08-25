

def getUserDummyData():
    return {
        "name": "Cyprien Dcunha",
        "username": "CCD",
        "email": "dcunha.cyprien@gmail.com",
        "img": "images/users/ccd-avatar.jpg",
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


def getProjectExplorerDummyData():
    return {
        "name": "helloCL",
        "branch": "master",
        "description": "Some of my simple neural networks",
        "latest_commit": "Add opencl helper functions",
        "stars": "2",
        "forks": "0",
        "commits": "32",
        "branches": ["master", "stagging", "testing"],
        "files": [
            {
                "name": "image-grayscale.cpp",
                "last_commit": "Add Graysscaling",
                "last_commit_age": "8 months"
            },
            {
                "name": "image-blur.cpp",
                "last_commit": "Add Gaussian Filter",
                "last_commit_age": "8 months"
            },
            {
                "name": "main.cpp",
                "last_commit": "Add opencl helper functions",
                "last_commit_age": "8 months"
            },
        ]
    }


def getCommitListDummyData():
    return {
        "project": "helloCL",
        "branch": "master",
        "commits_by_date": [
            {
                "date": "Dec 5, 2016",
                "commits": [
                    {
                        "author": "CCD-1997",
                        "author_img": "images/users/ccd-avatar.jpg",
                        "message": "Add Graysscaling",
                        "id": "4",
                    },
                ]
            },
            {
                "date": "Dec 1, 2016",
                "commits": [
                    {
                        "author": "CCD-1997",
                        "author_img": "images/users/ccd-avatar.jpg",
                        "message": "A minor change to logging",
                        "id": "3",
                    },
                ]
            },
            {
                "date": "Nov 28, 2016",
                "commits": [
                    {
                        "author": "CCD-1997",
                        "author_img": "images/users/ccd-avatar.jpg",
                        "message": "Add OpenCV to cmake and Add Readme",
                        "id": "2",
                    },
                    {
                        "author": "CCD-1997",
                        "author_img": "images/users/ccd-avatar.jpg",
                        "message": "Add opencl helper functions",
                        "id": "1",
                    },
                ]
            }
        ]
    }


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


def getPeopleDummyData():
    return [
        {
            "name": "Cyprien Dcunha",
            "username": "CCD",
            "email": "dcunha.cyprien@gmail.com",
            "img": "images/users/ccd-avatar.jpg",
        },
        {
            "name": "Saumitra Bose",
            "username": "imtoobose",
            "email": "imtoobose@gmail.com",
            "img": "images/users/ccd-avatar.jpg",
        },
        {
            "name": "Anand G",
            "username": "AnandGH5",
            "email": "anandganeshgx97@gmail.com",
            "img": "images/users/ccd-avatar.jpg",
        },
        {
            "name": "YinYang021997",
            "username": "YinYang021997",
            "email": "anmolb97@gmail.com",
            "img": "images/users/ccd-avatar.jpg",
        },
        {
            "name": "Gargee Bhase",
            "username": "Gargeebhase",
            "email": "gbhase2@gmail.com",
            "img": "images/users/ccd-avatar.jpg",
        },
    ]


def getFileCodeDummyData():
    return {
        "name": "Image-grayscale.cpp",
        "project": "helloCL",
        "branch": "master",
        "size": "2.04 kB",
        "code": """#include "image-grayscale.h"

extern "C"{
    #include "utils/cl_utils.h"
    #include "utils/file_utils.h"
}

void image_grayscale(char *input_image_path, char *output_image_path){
    //check if input image paths is valid
    check_if_proper_image_path(&input_image_path);

    //Image variables
    size_t rows, cols, ARRAY_SIZE, ARRAY_BYTES, NO_OF_CHANNELS;

    //Output data array
    unsigned char *h_output_data;

    //Memory pointer for image
    cl_mem d_input, d_output;

    //Get and convert image to matrix with proper color channels
    cv::Mat img_mat = cv::imread(input_image_path);
    cv::cvtColor(img_mat, img_mat, CV_RGB2RGBA);

    rows = (size_t) img_mat.rows;
    cols = (size_t) img_mat.cols;

    NO_OF_CHANNELS = 4;
    ARRAY_SIZE = rows * cols;
    ARRAY_BYTES = ARRAY_SIZE * sizeof(unsigned char);

    //Copy kernel from file
    const char* grayscale = read_kernel_from_file((char *) "image-grayscale/grayscale.cl");

    //Setup opencl and allocate memory
    cl_setup();
    cl_malloc(d_input, ARRAY_BYTES * NO_OF_CHANNELS);
    cl_malloc(d_output, ARRAY_BYTES);

    //Copy input image data and filter to opencl-device
    cl_memcpy(d_input, img_mat.data, ARRAY_BYTES * NO_OF_CHANNELS, host_to_device);

    //Setup global and local work size
    //TODO: set proper global and local work size
    size_t global_work_size[] = { rows, cols };
    size_t local_work_size[] = { 8,cols };

    //Execute kernel
    cl_run((char *) "grayscale", grayscale, 2, global_work_size, NULL, 2,
    sizeof(cl_mem), d_input, sizeof(cl_mem), d_output);

    //Copy resultant image back to host
    h_output_data = new unsigned char[ARRAY_BYTES];
    cl_memcpy(d_output, h_output_data, ARRAY_BYTES, device_to_host);

    //Save the image
    cv::Mat output((int) rows, (int) cols, CV_8UC1, h_output_data);
    cv::imwrite(output_image_path, output);

    //Clear all allocated memory
    cl_free(d_input);
    cl_free(d_output);

    delete grayscale;
    delete h_output_data;

} """,

    }


def getCommitDiffDummyData():
    return {
        "project": "helloCL",
        "branch": "master",
        "author": "CCD-1997",
        "author_img": "images/users/ccd-avatar.jpg",
        "message": "fix bugs",
        "commit_id": "10",
        "date": "Mar 19, 2017",
        "diff": """commit 6a854bf12bd3a71dff09847d529dd556b0222aed
Author: CCD-1997 <dcunha.cyprien@gmail.com>
Date:   Sun Mar 19 18:04:49 2017 +0530

    fix bugs

diff --git a/app/src/main/java/api/feedback/FeedBackForm.java b/app/src/main/java/api/feedback/FeedBackForm.java
index 869b689..f5dc209 100644
--- a/app/src/main/java/api/feedback/FeedBackForm.java
+++ b/app/src/main/java/api/feedback/FeedBackForm.java
@@ -1,11 +1,11 @@
 package api.feedback;

+import android.content.Context;
 import android.content.DialogInterface;
 import android.content.Intent;
 import android.content.SharedPreferences;
 import android.os.AsyncTask;
 import android.os.Bundle;
-import android.preference.PreferenceManager;
 import android.support.design.widget.FloatingActionButton;
 import android.support.v7.app.AlertDialog;
 import android.support.v7.app.AppCompatActivity;
@@ -29,6 +29,8 @@ import java.net.HttpURLConnection;
 import java.net.URL;
 import java.util.ArrayList;

+import static api.feedback.LoginActivity.SP_LOGIN_ID;
+
 public class FeedBackForm extends AppCompatActivity {

     public static final int FORM_TYPE_THEORY = 1;
@@ -142,10 +144,10 @@ public class FeedBackForm extends AppCompatActivity {
             e.printStackTrace();
         }

-        SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
+        SharedPreferences prefs = getSharedPreferences(SP_LOGIN_ID, Context.MODE_PRIVATE);
         uploadToServer("http://10.120.110.161:8000/save-feedback/", String.valueOf(json));
-        preferences.edit().putBoolean(subject + teacherName, true).apply();
-
+        prefs.edit().putBoolean(subject + teacherName, true).apply();
+        finish();
     }

     public boolean onCreateOptionsMenu(Menu menu) {
diff --git a/app/src/main/java/api/feedback/MainActivity.java b/app/src/main/java/api/feedback/MainActivity.java
index 9f34cf8..1a57ccd 100644
--- a/app/src/main/java/api/feedback/MainActivity.java
+++ b/app/src/main/java/api/feedback/MainActivity.java
@@ -7,7 +7,6 @@ import android.content.SharedPreferences;
 import android.graphics.Rect;
 import android.os.AsyncTask;
 import android.os.Bundle;
-import android.preference.PreferenceManager;
 import android.support.v7.app.AppCompatActivity;
 import android.support.v7.widget.LinearLayoutManager;
 import android.support.v7.widget.RecyclerView;
@@ -54,11 +53,10 @@ public class MainActivity extends AppCompatActivity {
             }
         }.execute();

-        SharedPreferences pref = PreferenceManager.getDefaultSharedPreferences(this);
-
+        SharedPreferences prefs = getSharedPreferences(SP_LOGIN_ID, Context.MODE_PRIVATE);
         RecyclerView rv = (RecyclerView) findViewById(R.id.subject_rv);
         rv.setLayoutManager(new LinearLayoutManager(this));
-        String div = pref.getString(LoginActivity.SP_LOGIN_CLASS, "");
+        String div = prefs.getString(LoginActivity.SP_LOGIN_CLASS, "");
         rv.addItemDecoration(new SpacingDecoration(4));
         rv.setAdapter(new SubjectAdapter(this, getData(div)));
     }
@@ -66,31 +64,32 @@ public class MainActivity extends AppCompatActivity {
     private ArrayList<Subject> getData(String div){
         ArrayList<Subject> subjects = new ArrayList<>();
         if(Objects.equals(div, "SE-A")){
-            subjects.add(new Subject("Ruhina", "DBMS", "SE-A", false));
-            subjects.add(new Subject("Chirag", "CG", "SE-A", false));
-            subjects.add(new Subject("Chirage", "CG", "SE-A", true));
-            subjects.add(new Subject("Priya", "COA", "SE-A", false));
-            subjects.add(new Subject("Harish", "DBMS", "SE-A", true));
-            subjects.add(new Subject("Sonali", "Maths", "SE-A", true));
-            subjects.add(new Subject("Pranjali", "AOA", "SE-A", false));
+            subjects.add(new Subject("Saumitra Bose", "DBMS", "SE-A", false));
+            subjects.add(new Subject("Cyprien Dcunha", "CG", "SE-A", false));
+            subjects.add(new Subject("Cyprien Dcunha", "CG", "SE-A", true));
+            subjects.add(new Subject("Jitendra Kumhar", "COA", "SE-A", false));
+            subjects.add(new Subject("Saumitra Bose", "DBMS", "SE-A", true));
+            subjects.add(new Subject("Ketav Bhatt", "Maths", "SE-A", true));
+            subjects.add(new Subject("Jitendra Kumhar", "AOA", "SE-A", false));
         }
-        else if(Objects.equals(div, "SE-A")){
-            subjects.add(new Subject("ABCD", "DBMS", "SE-B", false));
+        else if(Objects.equals(div, "SE-B")){
+            subjects.add(new Subject("Saumitra Bose", "DBMS", "SE-B", false));
             subjects.add(new Subject("Chirag", "CG", "SE-B", false));
-            subjects.add(new Subject("Chirage", "CG", "SE-B", true));
-            subjects.add(new Subject("Priya", "COA", "SE-B", false));
-            subjects.add(new Subject("Priya", "DBMS", "SE-B", true));
-            subjects.add(new Subject("XYZ", "Maths", "SE-B", true));
-            subjects.add(new Subject("Pranjali", "AOA", "SE-B", false));
+            subjects.add(new Subject("Miloni", "CG", "SE-B", true));
+            subjects.add(new Subject("Maitri", "COA", "SE-B", false));
+            subjects.add(new Subject("Saumitra", "DBMS", "SE-B", true));
+            subjects.add(new Subject("Ramesh", "Maths", "SE-B", true));
+            subjects.add(new Subject("Cyprien Dcunha", "AOA", "SE-B", false));
         }
         else {
-            subjects.add(new Subject("ABCD", "DBMS", "SE-A", false));
-            subjects.add(new Subject("JHDSH", "COA", "SE-A", false));
-            subjects.add(new Subject("SDKNH", "CG", "SE-A", true));
-            subjects.add(new Subject("DSKJS", "CG", "SE-A", false));
-            subjects.add(new Subject("DSKNS", "DBMS", "SE-A", true));
-            subjects.add(new Subject("XYZ", "Maths", "SE-A", true));
-            subjects.add(new Subject("SDFSD", "Maths", "SE-A", false));
+
+            subjects.add(new Subject("Saumitra Bose", "DBMS", "SE-A", false));
+            subjects.add(new Subject("Jitendra Kumhar", "COA", "SE-A", false));
+            subjects.add(new Subject("Ankit", "CG", "SE-A", true));
+            subjects.add(new Subject("Jigar", "CG", "SE-A", false));
+            subjects.add(new Subject("Saumitra Bose", "DBMS", "SE-A", true));
+            subjects.add(new Subject("Anand", "Maths", "SE-A", true));
+            subjects.add(new Subject("Zahan", "Maths", "SE-A", false));
         }
         return subjects;
   }"""
    }
