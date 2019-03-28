package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;

import org.junit.Rule;
import org.junit.Test;

import androidx.test.InstrumentationRegistry;
import androidx.test.rule.ActivityTestRule;

import static org.junit.Assert.*;

public class DataQueryActivityTest {
    @Rule
    public ActivityTestRule<UserDataQueryActivity> mActivityRule = new ActivityTestRule<>(UserDataQueryActivity.class);

    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getTargetContext();

        assertEquals("ca.uw.tongliu.mobihealthapplication", appContext.getPackageName());
    }

    @Test
    public void fetchDataTest(){
        boolean fetch_succeed = mActivityRule.getActivity().FetchUserData();
    }

}