// Understanding JavaScript Objects
console.log('Understanding JavaScript Objects')
let car = {
    make: "honda",
    model: "city",
    year: "2022"
}

console.log(car)

// Accessing and Modifying Object Properties
console.log('\nAccessing and Modifying Object Properties')
car.year = '2024'
console.log(car)

// Adding Methods to Objects
console.log('\nAdding Methods to Objects')
let employee = {
    firstName: "Chinmaya",
    lastName: "Rao",
    position: "Intern",
    fullName: function() {
        return `${this.firstName} ${this.lastName}`
    }
}

console.log(employee.fullName())


// Nested Objects
console.log('\nNested Objects')
let company = {
    name: "pw",
    location: {
        street: "Kapikad",
        city: "Mangalore",
        state: "Karnataka"
    },
    employees: 450,
    getLocation: function() {
        return `${this.location.street} ${this.location.city} ${this.location.state}`
    }
}

console.log(company)
console.log(company.getLocation())

// Object Constructors
console.log('\nObject Constructors')
function Car(make,model,year){
    
    this.make = make,
    this.model = model,
    this.year =  year,
    this.getInfo = function(){
        return `${this.make} ${this.model} ${this.year}`
    }    
}

let car1 = new Car("Honda pvt", "honda city", 2022)
let car2 = new Car("Maruthi Suzuki" , "WagonR", 2023)
console.log(car1.getInfo());
console.log(car2.getInfo());

// Object Prototypes and Inheritance
console.log('\nObject Prototypes and Inheritance')
function Animals(species,sound){
    this.species = species;
    this.sound = sound;
}
Animals.prototype.makeSound = function(){
    return `${this.species} makes sound ${this.sound}`
};

let a1 = new Animals("lion","roar");
let a2 = new Animals("dog","bark");

console.log(a1.makeSound() + "\n" + a2.makeSound())

// JavaScript Classes
console.log('\nJavaScript Classes')
class Cars{
    constructor(make,model,year){
    
        this.make = make,
        this.model = model,
        this.year =  year,
        this.getInfo = function(){
            return `${this.make} ${this.model} ${this.year}`
        } 
}
}

let car11 = new Cars("Morries Garage", "MG Hector", 2022)
let car22 = new Cars("Audi" , "audi q1", 2023)
console.log(car11.getInfo());
console.log(car22.getInfo());

// Inheritance in Classes
console.log('\nInheritance in Classes')

class Employee{
    constructor(firstName,lastName,position){
        this.firstName  = firstName 
        this.lastName = lastName
        this.position = position
    }

    getDetails(){
        return `Name: ${this.firstName} ${this.lastName} \nPosition: ${this.position}`
    }
}

class Manager extends Employee{
    constructor(firstName,lastName, position,department){
        super(firstName,lastName, position)
        this.department = department
    }

    getDetails(condition = false){
        if(condition){
            return super.getDetails();
        }
        else{
            return  `Name: ${this.firstName} ${this.lastName} \nPosition: ${this.position} \nDepartment: ${this.department}`
        }
        
    }

}
// let e1 = new Employee("Suresh", "Shetty", "Senior Devops");
let m1 = new Manager("Suresh", "Shetty", "Senior Devops", "Dev-Ops");

// console.log(e1.getDetails())
console.log(m1.getDetails(true))

// Getters and Setters
console.log('\nGetters and Setters')

class Rectange{
    constructor(width,height){
        this.width = width;
        this.height = height
    }
    get area(){
        return this.width*this.height
    }

    set dimensions(dimn){
        this.width = dimn[0]
        this.height = dimn[1]
    }
}

let r1 = new Rectange();
r1.dimensions = [23,4]
console.log(r1.width,r1.height,r1.area)



// Static Methods
console.log('\nStatic Methods')

class Utils{
    static avg(arr){
        return arr.reduce((accumulator, currentValue) => {
            return accumulator + currentValue
          },0) / arr.length;

        
    }

    static reverseStr(str){
        return str.split('').reverse().join('')
    }
}

let a = [1,2,3,4,5]
let avgg = Utils.avg(a)
let s = "absd"
let revS = Utils.reverseStr(s)
console.log(avgg,revS)




