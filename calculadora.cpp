#include <iostream>

int main(){


    // calculadora basica

    char operador;
    double NM1;
    double NM2;
    double resultado;

    std::cout<<"###########calculadora basica###########\n";

 
     std::cout<<"ingrese un operador (+, -, *, /): ";
     std::cin>>operador;

    if (operador != '+' && operador != '-' && operador != '*' && operador != '/') { 
        std::cout << "operador invalido\n";

        std::cout << "Presione Enter para continuar...";
        std::cin.ignore(); // Limpia el buffer
        std::cin.get();    // Espera por Enter // razonamiento de porque se usa esto, es para que no se cierre la consola al instante, y se pueda ver el resultado.
        return 1;

    } // aqui lo que estamos diciendo es que si no se implementan ninguno de estos simbolos, da un error. "! es para indicar que si no es = que"


     std::cout << "ingrese un numero: ";
     std::cin >> NM1;

     std::cout << "ingrese otro numero: ";
     std::cin >> NM2;

 switch (operador){

    case '+':
        resultado = NM1 + NM2;
        std::cout << " el resultado es " << resultado << std::endl;
        break;

    case '-':
        resultado = NM1 - NM2;
        std::cout << " el resultado es " << resultado << std::endl;
        break;

    case '*':
        resultado = NM1 * NM2;
        std::cout << " el resultado es " << resultado << std::endl;
        break;

        case '/':
        if (NM2 == 0) {
            std::cout << " no se puede dividir entre 0 " << std::endl;
        } 
         else {
            resultado = NM1 / NM2;
            std::cout << " el resultado es " << resultado << std::endl;
        }
        break;
        // como sabemos que no se puede dividir por 0.
        // para arreglar esto implementamos un if, tambien se puede hacer con un "?"         
        

    default:
        std::cout << "operador no valido" << std::endl;
        break;

 }

    std::cout<<"########################################"<<std::endl;

    std::cout << "Presione Enter para continuar...";
    std::cin.ignore(); // Limpia el buffer
    std::cin.get();    // Espera por Enter
 // el ignore se usa para limpiar el buffer, y el get se usa para esperar a que el usuario presione enter, para que no se cierre la consola al instante, y se pueda ver el resultado.
    return 0;
}