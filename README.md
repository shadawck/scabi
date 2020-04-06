# PMS SCAN

Implement vulnerability scanning on top of package management system like apt, yarn, chocolatey... in command line 

Ex : this command will analyse all dpendencies of ```make``` and the ```make``` package in itself 
```bash
pms apt-get install make 
```

### Apt 

Required : 
```bash
# list recursively all the dependencies of an apt package
sudo apt install apt-rdepends

``` 
See ```apt_scan.py```


### Composer

### Gem


