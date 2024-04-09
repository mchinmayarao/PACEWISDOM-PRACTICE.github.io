document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuToggle = document.getElementById("mobile-menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");


    mobileMenuToggle.addEventListener("click", function (event) {
        event.stopPropagation();
        mobileMenu.classList.toggle("hidden");
    });


    document.body.addEventListener("click", function (event) {

        if (!mobileMenu.contains(event.target) && !mobileMenuToggle.contains(event.target)) {
            mobileMenu.classList.add("hidden");
        }
    });
});

var projectDetails = [
    {
        projectTitle: "AgriKart",
        projectInfo : "This project entails the development of a static e-commerce website tailored for the agricultural sector, facilitating the purchase of various products such as seeds, fertilizers, and equipment. The website incorporates essential features including user authentication, product search, filtering options, cart management, and a streamlined checkout process. By integrating these functionalities, the website offers users a seamless and efficient shopping experience while catering to the specific needs of the agricultural community.",
        technologies : "HTML, CSS, JavaScript",
        type : "Static Website",
        gitHub : "https://github.com/mchinmayarao/PACEWISDOM-PRACTICE.github.io/tree/main/AgriKart",
        img : "./images/agrikart.jpeg"

    },
    {
        projectTitle: "Heart Disease Prediction",
        projectInfo : "This project aims to predict the probability of heart disease based on various clinical parameters. It includes a graphical user interface (GUI) application, data preprocessing steps, model training, and evaluation.",
        technologies : "python, tkinter",
        type : "Machine Learning",
        gitHub : "https://github.com/mchinmayarao/HeartDiseasePrediction",
        img : "./images/heart.jpeg"
    },
    {
        projectTitle: "Malaria Detection",
        projectInfo : "This project aims to detect malaria cells in microscopic images using MATLAB. It provides both a MATLAB app and a standalone script for malaria detection.",
        technologies : "MatLab",
        type : "Image Processing",
        gitHub : "https://github.com/mchinmayarao/MalariaDetector",
        img : "./images/malaria.jpeg"
    },
    {
        projectTitle: "Arecanut Price Prdiction",
        projectInfo : "This project implements a Long Short-Term Memory (LSTM) model for predicting the modal price of a commodity based on the historical data provided in the dataset",
        technologies : "Python 3.x, pandas, numpy, scikit-learn, matplotlib, seaborn, tensorflow",
        type : "Machine Learning(LSTM model)",
        gitHub : "https://github.com/mchinmayarao/ArecanutPricePrediction",
        img : "./images/lstm.jpeg"
    },
    {
        projectTitle: "MetaMind",
        projectInfo : "This project aims to develop a mobile application called \"MetaMind\" that provides a collection of AI tools and functionalities to users. The application allows users to sign up or log in with their credentials to access the main dashboard. From the dashboard, users can explore various AI tools and their functionalities. The tools are categorized into different categories for easy navigation.",
        technologies : "Android Studio",
        type : "Android app",
        gitHub : "https://github.com/mchinmayarao/MetaMind",
        img : "./images/metamind.jpeg"
    },
    {
        projectTitle: "Sudoko Solver",
        projectInfo : "This project is a Sudoku solver application that uses image processing techniques and machine learning to solve Sudoku puzzles from input images. It provides a user-friendly interface to select an image file containing a Sudoku puzzle and generates the solved puzzle as an output.",
        technologies : "Python 3.x, OpenCV, NumPy, TensorFlow",
        type : "Image Processing",
        gitHub : "https://github.com/mchinmayarao/Smart-Sudoku-Solver",
        img : "./images/sudoko.jpg"
    }
]
function closeProjectDetails() {
    let project_info = document.getElementById('project-info');
    project_info.classList.add('hidden')
}

function showProjectDetails(id) {
    let project_info = document.getElementById('project-info');
    project_info.classList.remove('hidden');
    
    document.getElementById('project-image').setAttribute('src',projectDetails[id-1].img)
    document.getElementById('project-title').innerHTML = projectDetails[id-1].projectTitle;
    document.getElementById('project-desc').innerHTML = projectDetails[id-1].projectInfo;
    document.getElementById('project-type').innerHTML = projectDetails[id-1].type;
    document.getElementById('project-tech').innerHTML = projectDetails[id-1].technologies;
    document.getElementById('project-repo').innerHTML = projectDetails[id-1].gitHub;
    document.getElementById('project-repo').setAttribute('href' , projectDetails[id-1].gitHub);

}