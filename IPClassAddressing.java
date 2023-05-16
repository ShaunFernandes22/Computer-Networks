import java.util.*;

class ipaddress {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int f, ind;
        char ipclass=' ';
        String ip, first, subnet=" ", subnet_address=" ";
        System.out.println("Enter the IP address : ");
        ip = sc.nextLine();
        ind = ip.indexOf('.');
        String ipAdd[] = ip.split("\\.");
        if (ipAdd.length == 4)
        {
           first = ip.substring(0, ind);
           f = Integer.parseInt(first);
           if (f >=0 && f<=127)
           {
               ipclass = 'A';
               subnet = "255.0.0.0";
           }
           else if (f >=128 && f<=191)
           {
               ipclass = 'B';
               subnet = "255.255.0.0";
           }
           else if (f>=192 && f<=223)
           {
               ipclass = 'C';
               subnet = "255.255.255.0";
           }
           else if (f>=224 && f<= 239)
               ipclass = 'D';
           else if (f >= 240 && f<=255)
               ipclass = 'E';
           else 
                System.out.println("Invalid Ip address");
            
            if (ipclass == 'A' || ipclass == 'B' || ipclass == 'C')
            {
                System.out.println("Class : "+ ipclass);
                System.out.println("Subnet mask : "+ subnet);
            }
            else if (ipclass == 'D')
            {
                System.out.println("Class : "+ ipclass);
                System.out.println("Reserved for Multicast");
            }    
            else if (ipclass == 'E')
            {
                System.out.println("Class : "+ ipclass);
                System.out.println("Experimental purposes ");
            }
            
            if (subnet != " ")
            {
                int i, x, y, z;
                String maskArr[] = subnet.split("\\.");
                for (i=0; i<4; i++)
                {
                    x = Integer.parseInt(ipAdd[i]);
                    y = Integer.parseInt(maskArr[i]);
                    z = x&y;
                    subnet_address += z + ".";
                }
                System.out.println("Subnet address is "+subnet_address);
            }
        }
        else
            System.out.println("Invalid Ip address");
    }
}
