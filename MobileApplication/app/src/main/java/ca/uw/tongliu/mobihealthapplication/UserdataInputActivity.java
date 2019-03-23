package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;
import android.os.AsyncTask;
import android.os.Bundle;
import androidx.fragment.app.FragmentActivity;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.File;
import java.io.InputStreamReader;
import java.util.Date;

/**
 * A User data input screen.
 */
public class UserdataInputActivity extends FragmentActivity {

    /** Reference to the TextView showing fetched data, so we can clear it with a button
     * as necessary.
     */
    private TextView mDataText;

    // UI references.
    private EditText mSystolicView;
    private EditText mDiastolicView;
    private EditText mHeartrateView;
    private EditText mHeightView;
    private EditText mWeightView;
    private String systolic;
    private String diastolic;
    private String heartrate;
    private String height;
    private String weight;

    private String httpmethod;
    private HttpComm http_comm;
    private  JSONObject jsondata;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.data_input);
        // Set up the Data input form.
        mSystolicView = (EditText) findViewById(R.id.systolic);

        mDiastolicView = (EditText) findViewById(R.id.diastolic);

        mHeartrateView = (EditText) findViewById(R.id.Heartrate);

        mHeightView = (EditText) findViewById(R.id.Height);
        mWeightView = (EditText) findViewById(R.id.Weight);

        mDiastolicView.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView textView, int id, KeyEvent keyEvent) {
                if (id == EditorInfo.IME_ACTION_DONE || id == EditorInfo.IME_NULL) {
                    //attemptLogin();
                    return true;
                }
                return false;
            }
        });

        Button mSubmitButton = this.<Button>findViewById(R.id.submit_button);
        mSubmitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {

                    systolic = mSystolicView.getText().toString();
                    diastolic = mDiastolicView.getText().toString();
                    heartrate = mHeartrateView.getText().toString();
                    height  = mHeightView.getText ().toString ();
                    weight = mWeightView.getText ().toString ();
                    httpmethod = "POST";

                    jsondata = buidJsonObject();
                    String token = ReadDataFromLocalFile("auth_token");

                    HttpComm http_comm = new HttpComm(
                            httpmethod
                            ,jsondata
                    );

                    http_comm.setUrlResource("api/");
                    http_comm.setUrlPath("patientrecords");
                    http_comm.setAuthToken (token);
                    AsyncTask<String, Void, String> execute = new ExecuteNetworkOperation(http_comm);
                    execute.execute();

                } catch (Exception ex) {
                }
            }

        });

        mDataText = (TextView) findViewById(R.id.data_text);

    }

    private JSONObject buidJsonObject() throws JSONException {

        JSONObject jsonObject = new JSONObject();
        jsonObject.accumulate("bp_systolic",systolic);
        jsonObject.accumulate("bp_diastolic",diastolic);
        jsonObject.accumulate("heart_rate",heartrate);
        jsonObject.accumulate("height",height);
        jsonObject.accumulate("weight",weight);

        return jsonObject;
    }

     /**
     * This subclass handles the network operations in a new thread.
     * It starts the progress bar, makes the API call, and ends the progress bar.
     */

    private class ExecuteNetworkOperation extends AsyncTask<String, Void, String> {
        HttpComm data_input_http_comm;
        /**
         * Overload the constructor to pass objects to this class.
         */
        public ExecuteNetworkOperation(HttpComm http_comm) {
            this.data_input_http_comm = http_comm;
        }

        @Override
        protected String doInBackground(String... urls) {
            // params comes from the execute() call: params[0] is the url.
            try {
                try {
                    return data_input_http_comm.httpAPI();
                } catch (JSONException e) {
                    return "Error!";
                }
            } catch (IOException e) {
                return "Unable to retrieve web page. URL may be invalid.";
            }
        }
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {
            mDataText.setText(result);
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

