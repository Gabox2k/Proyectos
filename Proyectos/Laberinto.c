//Bloque 1
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//variables
#define filas 15
#define columnas 15

//tablero vacio
char tablero[filas][columnas];

typedef struct {
    int x, y;
}nodo;

nodo cola[filas * columnas];
int frente = 0, final = 0;
nodo padre[filas][columnas];

//Movimientos
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

//bloque 2
//imprimir tablero
void mostrarTablero(){
    for(int i = 0; i < filas; i++){
        for (int j = 0; j < columnas; j++){
            printf("%c ", tablero[i][j]);
        }
        printf("\n");
    }

}
//queue(FIFO)
void agregarcola(int x, int y){
    cola[final ++] = (nodo){x, y};
}

nodo quitarcola(){
    return cola[frente++];
}
 
//validacion dentro del tablero
int valido (int x, int y){
    return ( x >= 0 && x < filas  && y >= 0 && y < columnas);
}

//bloque 3
//Mezclar dirrecciones
void direcciones_mezcladas(int dir[4]){
    for (int i = 3; i > 0; i--){
        int j = rand() % (i + 1);
        int temp = dir[i];
        dir[i] = dir[j];
        dir[j] = temp;
    }
}

//Generar laberinto
void laberinto(int x , int y){
    int direcciones[] = {0,1,2,3};
    direcciones_mezcladas(direcciones);

    for(int i=0; i < 4; i++){
        int direc = direcciones[i];
        int npX= x + dx[direc] * 2;
        int npY = y + dy[direc] * 2;

        if (valido(npX, npY) && tablero[npX][npY] == '#'){
            tablero[x + dx[direc]][y + dy[direc]] = ' ';
            tablero[npX][npY] = ' ';
            laberinto(npX, npY);
        }
    }
}

//Funcion bfs (busqueda de anchura)
int bfs (int inicX, int inicY, int finalX, int finalY){
    agregarcola(inicX, inicY);
    int visitar[filas][columnas] = {0};
    visitar[inicX][inicY] = 1;

    while (frente < final) {
        nodo actual = quitarcola();

        if (actual.x == finalX && actual.y == finalY){
            return 1;
        }

        int direcciones[] = {0,1,2,3};
        direcciones_mezcladas(direcciones);

        for(int i = 0; i < 4; i++ ){
            int dir = direcciones[i];
            int npX = actual.x + dx[dir];
            int npY = actual.y + dy[dir];

            if (valido(npX,npY) && !visitar[npX][npY] && (tablero[npX][npY] == ' ' || tablero[npX][npY] == 'S')) {
                visitar[npX][npY] = 1;
                padre[npX][npY] = actual;
                agregarcola(npX,npY);
            }
        }
    }

    return 0;
    
}

//bloque 4
//Marcar el  camino desde la S
void marcacamino(nodo fin){
    nodo actual = fin;
    while (tablero[actual.x][actual.y] != 'E'){
        if (tablero[actual.x][actual.y] != 'S')
            tablero[actual.x][actual.y] = '+';
        actual = padre[actual.x][actual.y];

    }
}

//Llenar los muros, el punto de inicio y final, marcar el camino correcto 
int main () {
    srand(time(NULL));

    for (int i = 0; i < filas; i++)
        for (int j = 0; j < columnas; j++)
            tablero[i][j] = '#';
    
    int inicX = 1, inciY = 1;
    int finX = filas - 2, finY = columnas - 2;

    tablero[inicX][inciY] = ' ';
    laberinto(inicX,inciY);


    tablero[inicX][inciY] = 'E';
    tablero[finX][finY] = 'S';

    printf("Generando laberinto \n");
    mostrarTablero();

    frente = final = 0;
    if(bfs (inicX,inciY, finX,finY)){
        marcacamino((nodo){finX, finY});
        printf("laberinto resuelto\n");
        mostrarTablero();
    } else{
        printf("\n no se encontro camino");
    }

    return 0;
}


