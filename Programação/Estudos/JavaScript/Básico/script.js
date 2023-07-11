let nome = 'Marcos'; //string literal
let idade = 25; // number literal
let estaAprovado = true; // boolean
let sobrenome = undefined; // Undefined


// Objeto
let pessoa = {
    nome:'Marcos',
    idade: 22,
    estaAprovado: true,
    sobrenome:'Raulisson',
    altura: 183,
    peso: 58
};

console.log(pessoa);

// Array
let familia = ['Marcos', 22, 'Pirenópolis']

console.log(familia);

// Funções
function alterarPessoa(nome, sobrenome) {
    pessoa.nome = 'Maria'
    pessoa.sobrenome = 'Eduarda'
};

alterarPessoa(pessoa)

console.log(pessoa);

//Realizar uma tarefa, mas não devolve nada
function dizerNome(){
    console.log('Marcos');
}
dizerNome();

// Faz um cálculo ou operação e retorna algo
function MultiplicarPorDois(valor){
    return valor * 2;
}

//console.log(MultiplicarPorDois(5));
let resultado = MultiplicarPorDois(5);

console.log(resultado)

//Operador tenário
// Tem um cliente, 100 premium, comum
let pontos = 200;
let tipo = pontos > 100 ? 'premium' : 'comum';
console.log(tipo)