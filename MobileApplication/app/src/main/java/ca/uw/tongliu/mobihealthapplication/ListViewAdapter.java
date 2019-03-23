package ca.uw.tongliu.mobihealthapplication;


import java.util.ArrayList;
import java.util.HashMap;
import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class ListViewAdapter extends BaseAdapter{

    public ArrayList<HashMap<String, String>> list;
    Activity activity;
    public static final String FIRST_COLUMN="First";
    public static final String SECOND_COLUMN="Second";
    public static final String THIRD_COLUMN="Third";
    public static final String FOURTH_COLUMN="Fourth";
    private static final String FIFTH_COLUMN = "Fifth";

    public ListViewAdapter(Activity activity,ArrayList<HashMap<String, String>> list){
        super();
        this.activity=activity;
        this.list=list;
    }

    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return list.size();
    }

    @Override
    public Object getItem(int position) {
        // TODO Auto-generated method stub
        return list.get(position);
    }

    @Override
    public long getItemId(int position) {
        // TODO Auto-generated method stub
        return 0;
    }

    private class ViewHolder{
        TextView txtFirst;
        TextView txtSecond;
        TextView txtThird;
        TextView txtFourth;
        TextView txtFifth;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // TODO Auto-generated method stub

        ViewHolder holder;

        LayoutInflater inflater=activity.getLayoutInflater();

        if(convertView == null){

            convertView=inflater.inflate(R.layout.multi_column_layout, null);
            holder=new ViewHolder();

            holder.txtFirst=(TextView) convertView.findViewById(R.id.TextFirst);
            holder.txtSecond=(TextView) convertView.findViewById(R.id.TextSecond);
            holder.txtThird=(TextView) convertView.findViewById(R.id.TextThird);
            holder.txtFourth=(TextView) convertView.findViewById(R.id.TextFourth);
            holder.txtFifth=(TextView) convertView.findViewById(R.id.TextFifth);

            convertView.setTag(holder);
        }else{

            holder=(ViewHolder) convertView.getTag();
        }

        HashMap<String, String> map=list.get(position);
        holder.txtFirst.setText (map.get (FIRST_COLUMN));
        if ( position > 0) {
            String str_systolic = map.get (SECOND_COLUMN).toString ( );
            int systolic = Integer.parseInt (str_systolic);
            if (systolic > 140 || systolic < 90) {
                holder.txtSecond.setTextColor (0xFFFF0000);
            }
            else{
                holder.txtSecond.setTextColor (0xFF007F00);
            }
            String str_diastolic = map.get (THIRD_COLUMN).toString ( );
            int diastolic = Integer.parseInt (str_diastolic);
            if (diastolic > 90 || systolic < 60) {
                holder.txtThird.setTextColor (0xFFFF0000);
            }
            else{
                holder.txtThird.setTextColor (0xFF007F00);
            }
            String heart_rate = map.get (FOURTH_COLUMN).toString ( );
            int heartRate = Integer.parseInt (heart_rate);
            if (heartRate > 120 || systolic < 50) {
                holder.txtFourth.setTextColor (0xFFFF0000);
            }
            else{
                holder.txtFourth.setTextColor (0xFF007F00);
            }
        }
        holder.txtSecond.setText(map.get(SECOND_COLUMN));
        holder.txtThird.setText(map.get(THIRD_COLUMN));
        holder.txtFourth.setText(map.get(FOURTH_COLUMN));
        holder.txtFifth.setText(map.get(FIFTH_COLUMN));

        return convertView;
    }

}
