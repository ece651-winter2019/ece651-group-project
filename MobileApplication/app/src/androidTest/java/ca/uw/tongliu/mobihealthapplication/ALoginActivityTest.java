package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import androidx.test.InstrumentationRegistry;
import androidx.test.rule.ActivityTestRule;
import androidx.test.runner.AndroidJUnit4;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.action.ViewActions.typeText;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static org.junit.Assert.assertEquals;

@RunWith(AndroidJUnit4.class)
public class ALoginActivityTest {

    @Rule
    public ActivityTestRule<LoginActivity> mActivityRule = new ActivityTestRule<>(LoginActivity.class);

    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getTargetContext();

        assertEquals("ca.uw.tongliu.mobihealthapplication", appContext.getPackageName());
    }

    @Test
    public void user_signup() throws InterruptedException {
        onView(withId(R.id.username)).perform(typeText("testpatient1"));
        onView(withId(R.id.password)).perform(typeText("genericpassword"));
        onView(withId(R.id.sign_in_button)).perform(click());
    }


}