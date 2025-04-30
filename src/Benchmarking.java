public class Benchmarking {
    private MetodosOrdenamiento mOrdenamiento;
    public Benchmarking() {
        
        long currentMills = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println(currentMills);
        System.out.println(currentNano);
        mOrdenamiento = new MetodosOrdenamiento();

        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea =()-> mOrdenamiento.burbujaTradicional(arreglo) ;

        double tiempoDuracionMills = medirContCurrent(tarea);
        double tiempoDuracionNanos = medirContNanoTime(tarea);

        System.out.println("tiempo en milisegundos: " + tiempoDuracionMills);
        System.out.println("tiempo en nanosegundos: " + tiempoDuracionNanos);    
    }

    private int[] generarArregloAleatorio(int tamano) {
        int[] array = new int[tamano];
        for (int i = 0; i < tamano; i++) {
            array[i] = (int) (Math.random() * 100000);
        }
        return array;
    }

    public double medirContCurrent(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
    double tiempoSegundos = (fin - inicio)/ 1000.0;
        return tiempoSegundos;
    }

    public double medirContNanoTime(Runnable tarea) {
       long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0; 
    }

}
