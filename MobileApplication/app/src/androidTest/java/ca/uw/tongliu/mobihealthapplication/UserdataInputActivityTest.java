package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import androidx.test.InstrumentationRegistry;
import androidx.test.runner.AndroidJUnit4;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.action.ViewActions.typeText;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static org.junit.Assert.*;
import android.content.Context;
import androidx.test.rule.ActivityTestRule;
import androidx.test.runner.AndroidJUnit4;

import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;


import static org.junit.Assert.assertEquals;

@RunWith(AndroidJUnit4.class)
public class UserdataInputActivityTest {

    @Rule
    public ActivityTestRule<UserdataInputActivity> mActivityRule = new ActivityTestRule<>(UserdataInputActivity.class);

    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getTargetContext();

        assertEquals("ca.uw.tongliu.mobihealthapplication", appContext.getPackageName());
    }

    @Test
    public void normal_user_data_input_test() throws InterruptedException {
        onView(withId(R.id.systolic)).perform(typeText("120"));
        onView(withId(R.id.diastolic)).perform(typeText("75"));
        onView(withId(R.id.Heartrate)).perform(typeText("65"));
        onView(withId(R.id.Height)).perform(typeText("175"));
        onView(withId(R.id.Weight)).perform(typeText("150"));
        onView(withId(R.id.submit_button)).perform(click());
    }

}

