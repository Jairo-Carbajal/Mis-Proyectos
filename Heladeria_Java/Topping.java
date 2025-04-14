
package heladeria;


public class Topping extends Producto{
    private String Tipo_topping;

    public Topping(String Tipo_topping, int IDProducto, String Nombre, int Precio, String Tipo) {
        super(IDProducto, Nombre, Precio, Tipo);
        this.Tipo_topping = Tipo_topping;
    }
    
    
    
    
}
