
package heladeria;

import java.util.ArrayList;
import java.util.List;

public class Combo extends Producto{
    private List<Producto> productos;


    public Combo( int IDProducto, String Nombre, int Precio, String Tipo) {
        super(IDProducto, Nombre, Precio, Tipo);
        this.productos = productos;
    }
     
     
}
