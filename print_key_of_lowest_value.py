sample_dict={
    "C":92,
    "Jawa":66,
    "Python":95
}
#using min()+dict comphrehension
a=min(sample_dict.values())
d1={key:value for key,value in sample_dict.items() if sample_dict[key]==a}
print(d1)






    

    
    