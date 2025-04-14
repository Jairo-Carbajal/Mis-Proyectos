
package heladeria;

import java.sql.*;
import java.util.*;

public class Helado extends Producto{
    private String Sabor;
    
    
    public Helado(String Sabor, int IDProducto, String Nombre, int Precio, String Tipo) {
        super(IDProducto, Nombre, Precio, Tipo);
        this.Sabor = Sabor;
    }
    
    Scanner sc = new Scanner(System.in);

    
    
    public void Datos(){
        System.out.println("Ingrese los datos del Producto: ");
        System.out.println("Nombre: ");
        setNombre(sc.nextLine());
        System.out.println("Precio: ");
        setPrecio(sc.nextInt());
        System.out.println("Sabor: ");
        Sabor = sc.nextLine();

    }
    
    
    public void VerBatidos() {
        String url = "jdbc:mysql://localhost:3306/Heladeria";
       
        try {
            Connection conexion = DriverManager.getConnection(url, "root", "");
            Statement instruccion = conexion.createStatement();
            String sql = "select Sabor_Batido, Tamaño_batido, Precio, Nombre_Batido from batido";
            ResultSet resultado = instruccion.executeQuery(sql);
            System.out.println("----------------------------------");
            while(resultado.next()){
                System.out.print("Sabor Batido: " + resultado.getString(1));
                System.out.print("Tamanio batido: " + resultado.getString(2) + "\n");
                System.out.print("Precio: " + resultado.getInt(3)+ "\n");
                System.out.print("Nombre Batido :" + resultado.getString(4)+ "\n");
                System.out.println("----------------------------------");

            }
            resultado.close();
            instruccion.close();
            conexion.close();
               
        } catch (SQLException ex) {
            ex.printStackTrace(System.out);
        }
    }

    public String getSabor() {
        return Sabor;
    }
    
    public void AñadirBatido(){
        Connection connection = ConexionDB.conectar();
        
        if (connection != null) {
            try {
                String insertQuery = "INSERT INTO batido (Sabor_Batido, Tamaño_batido, Precio, Nombre_Batido) VALUES (?, ?, ?, ?)";
                PreparedStatement preparedStatement = connection.prepareStatement(insertQuery);
                preparedStatement.setString(1, "limon");
                preparedStatement.setString(2, "mediano");
                preparedStatement.setInt(3, 3000);
                preparedStatement.setString(4, "Limonaso");

                int filasAfectadas = preparedStatement.executeUpdate();
                if (filasAfectadas > 0) {
                    System.out.println("Datos insertados correctamente en la base de datos.");
                } else {
                    System.out.println("No se pudieron insertar los datos.");
                }

                preparedStatement.close();
                connection.close();
            } catch (SQLException e) {
                System.err.println("Error al insertar datos en la base de datos: " + e.getMessage());
            }
        } else {
            System.err.println("No se pudo establecer la conexión a la base de datos.");
        }
    }
}
