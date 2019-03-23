package ca.uw.tongliu.mobihealthapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.content.Context;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONArray;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.io.File;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.TimeZone;

public class UserDataListActivity extends AppCompatActivity {

    ListView user_data_listView;
    View mProgressView;
    TextView mFetchDataView;
    JSONObject ret_data_obj;
    String ret_data_string;

    private ArrayList<HashMap<String, String>> list;
    public static final String FIRST_COLUMN="First";
    public static final String SECOND_COLUMN="Second";
    public static final String THIRD_COLUMN="Third";
    public static final String FOURTH_COLUMN="Fourth";
    public static final String FIFTH_COLUMN="Fifth";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_data_list);
        mFetchDataView = findViewById(R.id.progressView);
        mProgressView = findViewById(R.id.communication_progress);
        user_data_listView = (ListView)findViewById(R.id.dataListView);
        populateList();
        ListViewAdapter adapter=new ListViewAdapter(this, list);
        user_data_listView.setAdapter(adapter);
    }

    private void populateList() {
        // TODO Auto-generated method stub

        int char_index = 0;
        list=new ArrayList<HashMap<String,String>>();
        String user_data = ReadDataFromLocalFile("bpData");

        String tmp_data = null;
        HashMap<String,String> hashmap=new HashMap<String, String>();
        hashmap.put(FIRST_COLUMN, "Date");
        hashmap.put(SECOND_COLUMN, "Systolic");
        hashmap.put(THIRD_COLUMN, "Diastolic");
        hashmap.put(FOURTH_COLUMN, "HeartRate");
        hashmap.put(FIFTH_COLUMN, "Weight");
        list.add(hashmap);

        try {
            JSONArray jsonArray = new JSONArray (user_data);
            for (int i = 0; i < jsonArray.length ( ); i++) {
                JSONObject recordObject = jsonArray.getJSONObject (i);
                hashmap=new HashMap<String, String>();
                tmp_data = recordObject.getString ("created_on");
                //SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
                char_index = tmp_data.indexOf ("-");
                String year = tmp_data.substring (0, char_index);
                String sub_tmp = tmp_data.substring (char_index+1);
                char_index = sub_tmp.indexOf ("-");
                String mm = sub_tmp.substring (0, char_index);
                tmp_data = sub_tmp.substring (char_index+1);
                char_index = tmp_data.indexOf ("T");
                String dd = tmp_data.substring (0,char_index);
                sub_tmp = tmp_data.substring (char_index+1);
                char_index = sub_tmp.indexOf (":");
                String hh = sub_tmp.substring (0, char_index);
                tmp_data = sub_tmp.substring (char_index+1);
                char_index = tmp_data.indexOf (":");
                String min = tmp_data.substring (0, char_index);
                String ss = tmp_data.substring (char_index+1, char_index+3);



                hashmap.put(FIRST_COLUMN, (mm+"-"+dd+" "+hh+":"+min));
                tmp_data = recordObject.getString ("bp_systolic");
                hashmap.put(SECOND_COLUMN, tmp_data);
                tmp_data = recordObject.getString ("bp_diastolic");
                hashmap.put(THIRD_COLUMN, tmp_data);
                tmp_data = recordObject.getString ("heart_rate");
                hashmap.put(FOURTH_COLUMN, tmp_data);
                tmp_data = recordObject.getString ("weight");
                hashmap.put(FIFTH_COLUMN, tmp_data);
                list.add(hashmap);
            }
        } catch (JSONException e) {
            e.printStackTrace ( );
        }

    }
    private String ReadDataFromLocalFile(String filename)
    {
        StringBuffer file_contents = new StringBuffer ();
        String lineData="";
        File file = new File(getFilesDir(), filename);

        FileInputStream fileInputStream = null;

        try {
            fileInputStream = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace ( );
        }

        if ( fileInputStream != null){
            InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

            try {
                lineData = bufferedReader.readLine();
                while(lineData!=null){
                    file_contents.append (lineData);
                    lineData = bufferedReader.readLine();
                }

            } catch (IOException e) {
                e.printStackTrace ( );
            }
        }
        return file_contents.toString ();
    }


}
