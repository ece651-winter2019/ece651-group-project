package ca.uw.ece.mobileapplication;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

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
    private String systolic;
    private String diastolic;
    private String heartrate;
    private String httpmethod;
    private HttpComm http_comm;
    private  JSONObject jsondata;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.data_input);
        // Set up the Data input form.
        mSystolicView = (EditText) findViewById(R.id.systolic);
        populateAutoComplete();

        mDiastolicView = (EditText) findViewById(R.id.diastolic);

        mHeartrateView = (EditText) findViewById(R.id.Heartrate);
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
                    //baseUrl = "http://192.168.92.210:6543/";
                    httpmethod = "POST";

                    jsondata = buidJsonObject();
                    HttpComm http_comm = new HttpComm(
                            httpmethod
                            ,jsondata
                    );

                    http_comm.setUrlResource("records");
                    //http_comm.setUrlPath("tliu");
                    AsyncTask<String, Void, String> execute = new ExecuteNetworkOperation(http_comm);
                    execute.execute();

                } catch (Exception ex) {
                }
            }
/*
            attemptLogin();
                //mNetworkFragment.startDownload();

                if (!mDownloading && mNetworkFragment != null) {
                        // Execute the async download.
                        mNetworkFragment.startDownload();
                        mDownloading = true;
                }
            }
*/
        });

        mDataText = (TextView) findViewById(R.id.data_text);

    }

    private JSONObject buidJsonObject() throws JSONException {

        JSONObject jsonObject = new JSONObject();
        jsonObject.accumulate("systolic",systolic);
        jsonObject.accumulate("diastolic",diastolic);
        jsonObject.accumulate("heartrate",heartrate);

        return jsonObject;
    }

    private void populateAutoComplete() {
        return;
    }

    /**
     * This subclass handles the network operations in a new thread.
     * It starts the progress bar, makes the API call, and ends the progress bar.
     */

    private class ExecuteNetworkOperation extends AsyncTask<String, Void, String> {
        HttpComm signup_http_comm;
        /**
         * Overload the constructor to pass objects to this class.
         */
        public ExecuteNetworkOperation(HttpComm http_comm) {
            this.signup_http_comm = http_comm;
        }

        @Override
        protected String doInBackground(String... urls) {
            // params comes from the execute() call: params[0] is the url.
            try {
                try {
                    return signup_http_comm.httpAPI();
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


}

