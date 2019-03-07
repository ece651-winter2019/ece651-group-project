package ca.uw.ece.mobileapplication;

import android.support.v4.app.FragmentActivity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.inputmethod.EditorInfo;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;


/**
 * A Signup screen that offers Signup via Username/password.
 */
//public class SignupActivity extends AppCompatActivity implements LoaderCallbacks<Cursor> {
public class SignupActivity extends FragmentActivity {

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
     * Keep track of the Signup task to ensure we can cancel it if requested.
     */
 //   private UserSignupTask mAuthTask = null;

    // UI references.
    private AutoCompleteTextView mUsernameView;
    private EditText mPasswordView;
    private View mProgressView;
    private View mLoginFormView;
    private String username;
    private String password;
    private String baseUrl;
    private String httpmethod;
    private HttpComm http_comm;
    private JSONObject jsondata;

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
                    //baseUrl = "http://192.168.92.210:6543/signup";
                    httpmethod = "POST";
                    jsondata = buidJsonObject();
                    HttpComm http_comm = new HttpComm(
                        httpmethod, jsondata
                    );

                    http_comm.setUrlResource("signup");
                    AsyncTask<String, Void, String> execute = new ExecuteNetworkOperation(http_comm);
                    execute.execute();

                } catch (Exception ex) {
                }
            }
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
        jsonObject.accumulate("username",username);
        jsonObject.accumulate("password",password);

        return jsonObject;
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

