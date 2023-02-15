<div align="center">
 <img src="https://readme-typing-svg.herokuapp.com/?lines=Shell+command+execution+using+51+single-chip+microcomputer.;---@Мартин.&font=Roboto" />
 <p align="center">
 <img title="Regulator" src='https://img.shields.io/badge/Regulator-1.0.0-brightgreen.svg' />
 <img title="Regulator" src='https://img.shields.io/badge/Hawrdware-Tool'/>
 <img title="Regulator" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="Regulator" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="Regulator" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 </p>
   
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>Leave the automatic screen</th>
  </tr>
  <tr>
    <th>Inductively execute shell commands</th>
 </table>
</div>

## usage method
  * View help information

      ```#python3 Regulator.py -h```

![图片名称](./PT/help.png)  

## Demo
[ps]The project document drawing v2.0.0 will use Bluetooth communication protocol, and the serial port will be used for testing this time

![图片名称](./PT/schematic_diagram.png)  

1.Burn hex file to 51 single-chip ne

![图片名称](./PT/Download.png)  

2.Configuration circuit

![图片名称](./PT/Config.png)  

3.Operation monitoring program

_You can use the - b parameter to set the baud rate, which is 9600 by default_
 ```#python3 Regulator.py -c COM13```

![图片名称](./PT/Run.png)  

4.After the human body is seated, it will automatically enter the combat readiness state

![图片名称](./PT/run1.jpg)  

5.Auto lock screen

![图片名称](./PT/run2.jpg)  

6.results of enforcement

![图片名称](./PT/result2.jpg)  
![图片名称](./PT/result3.png)  

## You can not only lock the screen, but also specify commands

   ```#python3 Regulator.py -c xxx -cmd "xxxx"```

![图片名称](./PT/cmd.png)  
