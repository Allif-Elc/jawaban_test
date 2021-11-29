const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({extended:true}));

app.get('/',(req,res)=>{
    res.render('/index');
});

app.post('/add',(req,res)=>{
    
});

app.put('/edit',(req,res)=>{

});

app.delete('/delete',(req,res)=>{

});


app.listen(port,()=>{
    console.log('Server is running');
})