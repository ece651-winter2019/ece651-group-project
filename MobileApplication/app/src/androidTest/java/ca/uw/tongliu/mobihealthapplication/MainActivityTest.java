package ca.uw.tongliu.mobihealthapplication;

import android.content.res.Resources;
import android.view.Menu;

import com.google.android.material.navigation.NavigationView;

import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.HashMap;
import java.util.Map;

import androidx.drawerlayout.widget.DrawerLayout;
import androidx.test.rule.ActivityTestRule;
import androidx.test.runner.AndroidJUnit4;

import static androidx.test.InstrumentationRegistry.getInstrumentation;
import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.Espresso.openActionBarOverflowOrOptionsMenu;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;

@RunWith(AndroidJUnit4.class)
public class MainActivityTest {
    private static final int[] MENU_CONTENT_ITEM_IDS = { R.id.nav_login,
            R.id.nav_data_sync, R.id.nav_manual_input, R.id.nav_data_list, R.id.nav_show_graph };
    private Map<Integer, String> mMenuStringContent;

    @Rule
    public ActivityTestRule<MainActivity> mActivityRule = new ActivityTestRule<>(MainActivity.class);

    private DrawerLayout mDrawerLayout;
    private NavigationView mNavigationView;
    private Menu mOptionMenu;

    @Before
    public void setUp() throws Exception {
        final MainActivity activity = mActivityRule.getActivity();
        mDrawerLayout = (DrawerLayout) activity.findViewById(R.id.drawer_layout);
        mNavigationView = (NavigationView) mDrawerLayout.findViewById(R.id.nav_view);
        // Close the drawer to reset the state for the next test
//        onView(withId(R.id.drawer_layout)).perform(closeDrawer(GravityCompat.START));
        final Resources res = activity.getResources();
        mMenuStringContent = new HashMap<>(MENU_CONTENT_ITEM_IDS.length);
        mMenuStringContent.put(R.id.nav_login, res.getString(R.string.menu_login));
        mMenuStringContent.put(R.id.nav_data_sync, res.getString(R.string.menu_data_sync));
        mMenuStringContent.put(R.id.nav_manual_input, res.getString(R.string.menu_data_input));
        mMenuStringContent.put(R.id.nav_data_list, res.getString(R.string.menu_data_list));
        mMenuStringContent.put(R.id.nav_show_graph, res.getString(R.string.menu_data_graph));
    }
    @Test
    public void TestDrawerMenu0() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        onView(withId(R.id.drawer_layout)).perform(click());
        // Check the contents of the Menu object
        final Menu menu = mNavigationView.getMenu();
        // Check that we have the expected menu items in our NavigationView
        activity.onNavigationItemSelected(menu.getItem(0));
    }
    @Test
    public void TestDrawerMenu1() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        onView(withId(R.id.drawer_layout)).perform(click());
        // Check the contents of the Menu object
        final Menu menu = mNavigationView.getMenu();
        // Check that we have the expected menu items in our NavigationView
        activity.onNavigationItemSelected(menu.getItem(1));
    }
    @Test
    public void TestDrawerMenu2() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        onView(withId(R.id.drawer_layout)).perform(click());
        // Check the contents of the Menu object
        final Menu menu = mNavigationView.getMenu();
        // Check that we have the expected menu items in our NavigationView
        activity.onNavigationItemSelected(menu.getItem(2));
    }
    @Test
    public void TestDrawerMenu3() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        onView(withId(R.id.drawer_layout)).perform(click());
        // Check the contents of the Menu object
        final Menu menu = mNavigationView.getMenu();
        // Check that we have the expected menu items in our NavigationView
        activity.onNavigationItemSelected(menu.getItem(3));
    }
    @Test
    public void TestDrawerMenu4() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        onView(withId(R.id.drawer_layout)).perform(click());
        // Check the contents of the Menu object
        final Menu menu = mNavigationView.getMenu();
        // Check that we have the expected menu items in our NavigationView
        activity.onNavigationItemSelected(menu.getItem(4));
    }

    @Test
    public void TestOptionMenu() {
        final MainActivity activity = mActivityRule.getActivity();
        // Open our drawer
        //onView(withId(R.id.action_exit)).perform(click());
        openActionBarOverflowOrOptionsMenu(getInstrumentation().getTargetContext());
        onView(withText("Exit")).perform(click());
    }

}