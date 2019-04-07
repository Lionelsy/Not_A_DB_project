import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Random;

public class generate_class_and_gender {

    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("/Users/windyluan/Desktop/students_info.csv"));//换成你的文件名
            //reader.readLine();//第一行信息，为标题信息，不用，如果需要，注释掉
            String line = null;
            while((line=reader.readLine())!=null){
                String item[] = new String[3];
                item= line.split(",");//CSV格式文件为逗号分隔符文件，这里根据逗号切分
                System.out.print(item[0]);
                System.out.print(',');
                String last = item[item.length-1];//这就是你要的数据了
                System.out.print(item[1]);
                System.out.print(',');
                int value = Integer.parseInt(item[0].substring(6,8));//如果是数值，可以转化为数值
                String class_num = item[0].substring(4,8);
                String gender = "F";
                if(value<29){
                    gender = "M";
                }
                System.out.print(class_num);
                System.out.print(',');
                System.out.print(gender);
                System.out.print(',');
                System.out.print(item[0]);
                System.out.print(',');
                System.out.print(',');
                Random ran = new Random();
                double money = ran.nextInt(350)+0.1*ran.nextInt(9);
                System.out.println(money);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}