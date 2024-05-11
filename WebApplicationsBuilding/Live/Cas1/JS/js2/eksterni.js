//document.write("Ovo je prvi JS tekst.")
console.log("Neki tekst")
/*a = 5;
b = 8;
b = "broj" + b
document.write(b);*/
/*a = 5;
b = a++;
c = ++a;
document.write(a,b,c);
document.write("<br>");
function fakt(n)
{
    if(n==1)
        return 1;
    return n*fakt(n-1);
}
document.write(fakt(10));*/
/*alert("Hello World");
let x = confirm("da ili ne");
alert(x);*/

/*let x = confirm("dan ili noc");
if(x==true)
    alert("DAN");
else
    alert("NOC");

x==true?alert("DAN"):alert("NOC")
alert(x==true?"dan":"noc")*/

/*a = 5
b = 7
if(a<b)
   alert("Max je "+b)
else
    alert("Max je b"+a);

alert(a<b?"Max je"+b:"Max je"+a)

function maximum(a,b)
{
    return alert(a<b?"Max je"+b:"Max je"+a)
}
maximum(2,9)

var x = prompt("Unesi vrednos");
alert("Uneli ste" + x);*/

///setTimeout("alert('pozdrav')",2000);

/*for(i=0;i<100;i++)
    document.write(i+" ")
document.write("<br><br><br>")
i = 0
while(i<100)
{
    document.write(i+" ");
    i++;
}*/

niz = []
niz[0]=9
document.write(niz)
niz[3]=5
document.write(niz) //nije dobro, preskace!!!!! cudna ispis
document.write("<br>")
lst = []
for(i=0;i<100;i++)
    lst[i] =  Math.floor(Math.random() * 100);
document.write(lst)

maxi = lst[0]
for(i=1;i<lst.lenght;i++)
    if(lst[i]>maxi)
        maxi = lst[i]
document.write("<br>"+"Maximum je:"+ maxi);