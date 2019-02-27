package ca.uw.ece.mobileapplication;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.net.NetworkInfo;
import android.support.v4.app.FragmentActivity;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.content.Context;

import android.os.AsyncTask;

import android.os.Build;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.text.TextUtils;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.inputmethod.EditorInfo;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;

import java.util.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;



/**
 * A login screen that offers login via Username/password.
 */
//public class LoginActivity extends AppCompatActivity implements LoaderCallbacks<Cursor> {
public class LoginActivity extends FragmentActivity {

    /** Reference to the TextView showing fetched data, so we can clear it with a button
    * as necessary.
    */
    private TextView mDataText;

    /**
     *Boolean telling us whether a download is in progress, so we don't trigger overlapping
     *downloads with consecutive button clicks.
     */

    private boolean mDownloading = false;

    /**
     * A dummy authentication store containing known user names and passwords.
     * TODO: remove after connecting to a real authentication system.
     */
    private static final String[] DUMMY_CREDENTIALS = new String[]{
            "uwaterloo.ca:hello", "uwaterloo.ca:world"
    };
    /**
     * Keep track of the login task to ensure we can cancel it if requested.
     */
 //   private UserLoginTask mAuthTask = null;

    // UI references.
    private AutoCompleteTextView mUsernameView;
    private EditText mPasswordView;
    private View mProgressView;
    private View mLoginFormView;
    private String username;
    private String password;
    private String baseUrl;
    private String httpmethod;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        // Set up the login form.
        mUsernameView = (AutoCompleteTextView) findViewById(R.id.userName);
        populateAutoComplete();

        mPasswordView = (EditText) findViewById(R.id.password);
        mPasswordView.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView textView, int id, KeyEvent keyEvent) {
                if (id == EditorInfo.IME_ACTION_DONE || id == EditorInfo.IME_NULL) {
                    //attemptLogin();
                    return true;
                }
                return false;
            }
        });

        Button mSignInButton = this.<Button>findViewById(R.id.sign_in_button);
        mSignInButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View view) {
                try {

                    username = mUsernameView.getText().toString();
                    password = mPasswordView.getText().toString();
                    baseUrl = "http://192.168.92.52:6543/records/tliu";
                    httpmethod = "GET";
                    HttpApiClient httpApiClient = new HttpApiClient(
                            baseUrl
                            , username
                            , password
                            , httpmethod
                    );

                    httpApiClient.setUrlResource("records");
                    httpApiClient.setUrlPath("tliu");
                    AsyncTask<String, Void, String> execute = new ExecuteNetworkOperation();
                    execute.execute(baseUrl.toString());

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

        mLoginFormView = findViewById(R.id.login_form);
        mProgressView = findViewById(R.id.login_progress);

        mDataText = (TextView) findViewById(R.id.data_text);

    }

    private void populateAutoComplete() {
        return;
    }

    private JSONObject buidJsonObject() throws JSONException {

        JSONObject jsonObject = new JSONObject();
        jsonObject.accumulate("patient","1");
        jsonObject.accumulate("systolic","120");
        jsonObject.accumulate("diastolic","80");
        jsonObject.accumulate("heartRate","90");

        return jsonObject;
    }

    private void setPostRequestContent(HttpURLConnection conn, JSONObject jsonObject) throws IOException {

        OutputStream os = conn.getOutputStream();
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
        writer.write(jsonObject.toString());
        writer.flush();
        writer.close();
        os.close();
    }

    private String httpAPI(String myUrl, String method) throws IOException, JSONException {
        String result = "";

        URL url = new URL(myUrl);

        // 1. create HttpURLConnection
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod(method);
        conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");

        if ( method.equals("POST")) {
            // 2. build JSON object
            JSONObject jsonObject = buidJsonObject();

            // 3. add JSON content to POST request body
            setPostRequestContent(conn, jsonObject);
        }
        // 4. make request to the given URL
        conn.connect();

        // 5. return response message
        return conn.getResponseMessage()+ "";

    }
    /**
     * This subclass handles the network operations in a new thread.
     * It starts the progress bar, makes the API call, and ends the progress bar.
     */

    private class ExecuteNetworkOperation extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... urls) {
            // params comes from the execute() call: params[0] is the url.
            try {
                try {
                    return httpAPI(urls[0], "GET");
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
//    public class ExecuteNetworkOperation extends AsyncTask<Void, Void, String> {
//
//        private HttpApiClient apiAuthenticationClient;
//        private String isValidCredentials;
//
//        /**
//         * Overload the constructor to pass objects to this class.
//         */
//        public ExecuteNetworkOperation(HttpApiClient apiAuthenticationClient) {
//            this.apiAuthenticationClient = apiAuthenticationClient;
//        }
//
//        @Override
//        protected void onPreExecute() {
//            super.onPreExecute();
//
//            // Display the progress bar.
//            findViewById(R.id.loadingPanel).setVisibility(View.VISIBLE);
//        }
//
//        @Override
//        protected String doInBackground(Void... params) {
//            try {
//                isValidCredentials = apiAuthenticationClient.execute();
//            } catch (Exception e) {
//                e.printStackTrace();
//            }
//
//            return null;
//        }
//
//        @Override
//        protected void onPostExecute(String result) {
//            super.onPostExecute(result);
//
//            // Hide the progress bar.
//            findViewById(R.id.loadingPanel).setVisibility(View.GONE);
//
//            // Login Success
//            if (isValidCredentials.equals("true")) {
//                //goToSecondActivity();
//            }
//            // Login Failure
//            else {
//                Toast.makeText(getApplicationContext(), "Login Failed", Toast.LENGTH_LONG).show();
//            }
//        }
//    }


}

