

const go_to_login= ()=>{
    console.log("going to login")
    window.location.href="./login.html" // for redirecting the webpage

}

function go_to_register(){
    console.log("going to register");
    window.location.href="./register.html"
    
}

// named arrow anonymous  iife 

const login_user =async function(){
    console.log("login clicked!")
    user_name=document.getElementById("login_username").value
    user_password=document.getElementById("login_password").value

    console.log(user_name,user_password);
    //make a api call for db.json
    let all_users=null
    all_user_data=await fetch("http://localhost:3000/users").then(data=>data.json()).then(data=>all_users=data).catch(err=>console.error("error occured!"))
    all_users= await all_user_data
    console.log(all_users);

    // for   for in  for of   map filter foreach reduce
    //map -> 
    //filter ->
    //for each ->
    let user_exists=false 

    all_users.forEach(element => {
       if (element.username==user_name && element.password===user_password){
        user_exists=true
        alert("user found!")
        window.sessionStorage.setItem("is_logged_in","true")
        window.location.href="./products.html"
       }        
    });

    if (user_exists==false){
        alert("user not found!")
    }


    
    
}

//CORS  -> Cross Origin Resource Sharing
const  show_products =  async()=>{
    let user_logged_in=window.sessionStorage.getItem("is_logged_in")
    console.log(user_logged_in);
    if (user_logged_in==="true"){

    
    
    console.log("products page is loaded");
    let all_products=null
    let fetch_products=fetch("https://fakestoreapi.com/products")
    .then(data=>data.json()).then(data=>all_products=data).catch(err=>console.error("failed to fetch products"))
    all_products=await fetch_products
    console.log(all_products);
    pro_div=document.getElementById("pro_div")
    pro_div.style.display="flex"
    pro_div.style.flexWrap="wrap"

    all_products.forEach(prod=>{
        single_pro=document.createElement("div")
        pro_image=document.createElement("img")
        pro_image.setAttribute("src",prod.image)
        pro_image.setAttribute("height","250px")
        pro_image.setAttribute("width","300px")
        pro_price=document.createElement("h2")
        pro_price.innerText=prod.price
        pro_category=document.createElement("p")
        pro_category.innerText=prod.category
        single_pro.append(pro_image,pro_price,pro_category)
        pro_div.append(single_pro)
    })
}
else{
    alert("pls login first to see the products")
    window.location.href="./login.html"
}
}


//await  -> 3 friends  - > movie ->ticket  ->friend ticket



//webstorages 
// -> local storage  -> data is stored permenantly key value pairs
// -> session storage --> active till the tab is open 
//cookies 


const go_to_cart=()=>{

    console.log("going to cart");
    const user_logged=window.sessionStorage.getItem("is_logged_in")
    if (user_logged==="true"){
        window.location.href="./cart.html"
    }else{
        alert("pls login first")
        window.location.href="./login.html"
    }
    
}

const register_user=()=>{
    user_name=document.getElementById("username").value 
    user_password=document.getElementById("password").value 
    user_email=document.getElementById("email").value 
    user_mobile=document.getElementById("mobile").value 
    user_id=document.getElementById("user_id").value 

    console.log(user_email,user_mobile,user_password,user_name,user_id);

    details={
        "id":user_id,
        "name":user_name,
        "password":user_password,
        "email":user_email,
        "mobile":user_mobile
    }

    let send_user=fetch("http://localhost:3000/users",{
        method:"POST",
        body:JSON.stringify(details)  //parse
    }).then(data=>data.json()).then(data=>console.log(data).catch(err=>console.log(err)
    )
    )
}

