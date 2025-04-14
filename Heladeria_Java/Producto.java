
package heladeria;

import java.sql.*;

public class Producto {
    private int IDProducto;
    private String Nombre;
    private int Precio;
    private String Tipo;

    public Producto(int IDProducto, String Nombre, int Precio, String Tipo) {
        this.IDProducto = IDProducto;
        this.Nombre = Nombre;
        this.Precio = Precio;
        this.Tipo = Tipo;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public void setPrecio(int Precio) {
        this.Precio = Precio;
    }

    public int getPrecio() {
        return Precio;
    }

    @Override
    public String toString() {
        return "Productos{" + "IDProducto=" + IDProducto + ", Nombre=" + Nombre + ", Precio=" + Precio + ", Tipo=" + Tipo + '}';
    }



    

    
    
}
