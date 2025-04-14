package heladeria;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int op;
        do {
            System.out.println("selecciona tu Rol(Elegir N°): \n"
                    + "1. Vendedor \n"
                    + "2. Repartidor \n"
                    + "3. Salir \n");
            op = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer
            
            switch (op) {
                case 1:
                    System.out.println("----------------------------------");                        
                    System.out.println("Menu Vendedor(Elegir N°): ");
                    System.out.println("---------------------------------- \n");
                    
                    break;
                case 2:
                    System.out.println("----------------------------------");                        
                    System.out.println("Menu Repartidor(Elegir N°): ");
                    System.out.println("---------------------------------- \n");                        
                    break;

                case 3:
                    System.out.println("---------------------------------- ");                        
                    System.out.println("Se salió del Sistema");
                    System.out.println("---------------------------------- \n");                        
                    break;
                default:
                    System.out.println("Opción no válida. Intente nuevamente.");
                    break;
                }
        } while (op != 3);
        
        sc.close(); // Cerrar el scanner
    }
}
